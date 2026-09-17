#!/usr/bin/env python3
"""MONTAGE M / MODX M bulk-dump sysex <-> .pfm performance conversion.

Sysex framing (Data List "(3-5-4) BULK DUMP"):
  F0 43 0n 7F 1C bh bl 0D a1 a2 a3 a4 <data...> cs F7
  byte count bh/bl (7-bit each) = 1 (model id) + 4 (address) + len(data)
  checksum: (0D + address + data + cs) & 0x7F == 0
  2-byte parameters are sent MSB, LSB (7 bits each) -> value = MSB*128 + LSB, which is exactly
  the u16 the .pfm stores little-endian.

Address map (see data/midi_param_tables.json / docs/pfm-format.md):
  06 00 xx 00  performance common blocks         1p 00 xx 00  part p blocks
  06 01 0m 00  super knob sequence m             1p 03 0c 00  part scene c
  06 02/03 0c  scene c 1byte / 2byte             1p 04 0k 00  part knob name k
  06 04 0k 00  common knob name k                1p 05 bb 00  part controller box bb
  06 05 bb 00  common controller box bb          1p 06/07 L0  part lane L settings
  06 06/07 L0  A/D lane L settings               1p 08 Lm 00  part lane L sequence m
  06 08 Lm 00  A/D lane L sequence m             2p 00-04 ee  element ee blocks
  04/05 ll mm nn  bulk header / footer           2p 10 kk 00  drum key kk
                                                 3p 00 00/01, 3p 01/02 0o   FM-X common/filter, op o sw/params
                                                 4p 00 00, 4p 01/02 0o, 4p 03/04 0f, 4p 05 00   AN-X
"""
import struct
import sys

import pfm

MODEL_ID = 0x0D


def split_messages(data):
    msgs, i = [], 0
    while i < len(data):
        if data[i] == 0xF0:
            j = data.index(0xF7, i)
            msgs.append(data[i:j + 1])
            i = j + 1
        else:
            i += 1
    return msgs


def parse_bulk(data):
    """Return list of (address tuple, payload bytes) for every bulk message in a .syx file."""
    out = []
    for m in split_messages(data):
        if len(m) < 14 or m[1] != 0x43 or m[3:5] != b"\x7f\x1c" or m[7] != MODEL_ID:
            continue
        addr = tuple(m[8:12])
        payload = m[12:-2]
        cs = (-sum(m[7:-2])) & 0x7F
        if cs != m[-2]:
            raise ValueError(f"checksum mismatch at address {addr}")
        out.append((addr, bytes(payload)))
    return out


def payload_to_block(payload, base, size):
    """7-bit sysex payload -> .pfm block bytes (u16 LE for 2-byte params, +NUL for strings)."""
    tables = pfm.load_tables()
    if base in pfm.STRING_TABLES:
        return payload[:size - 1].ljust(size - 1, b"\0")[:size - 1] + b"\0"
    out = bytearray(size)
    for p in tables[base]["params"]:
        o, n = p["offset"], p["size"]
        if o + n > len(payload):
            break  # older firmware dump: trailing params keep 0 (caller may apply defaults)
        if n == 1:
            out[o] = payload[o]
        elif pfm.is_pair(p):
            out[o:o + 2] = struct.pack("<H", (payload[o] << 8) | payload[o + 1])
        else:
            out[o:o + 2] = struct.pack("<H", (payload[o] << 7) | payload[o + 1])
    return bytes(out)


def block_to_payload(block, base):
    tables = pfm.load_tables()
    if base in pfm.STRING_TABLES:
        return block[:len(block) - 1]
    out = bytearray()
    for p in tables[base]["params"]:
        o, n = p["offset"], p["size"]
        if n == 1:
            out.append(block[o] & 0x7F)
        else:
            v = struct.unpack("<H", block[o:o + 2])[0]
            if pfm.is_pair(p):
                out += bytes([(v >> 8) & 0x7F, v & 0x7F])
            else:
                out += bytes([(v >> 7) & 0x7F, v & 0x7F])
    return bytes(out)


def message(addr, payload, device=0):
    body = bytes([MODEL_ID]) + bytes(addr) + payload
    count = len(body)
    cs = (-sum(body)) & 0x7F
    return bytes([0xF0, 0x43, device & 0x0F, 0x7F, 0x1C, (count >> 7) & 0x7F, count & 0x7F]) + body + bytes([cs, 0xF7])


BLOCK_SIZES = {}  # base -> pfm block size (table size, +1 for strings)


def _sizes():
    if not BLOCK_SIZES:
        for base, t in pfm.load_tables().items():
            BLOCK_SIZES[base] = t["size"] + (1 if base in pfm.STRING_TABLES else 0)
        BLOCK_SIZES["2p 00 ee 00"] = 43
        BLOCK_SIZES["2p 04 ee 00"] = 108
    return BLOCK_SIZES


def syx_to_performance(data):
    """Assemble a raw pfm block tree from a bulk dump. Blocks missing from the dump are zero-filled."""
    S = _sizes()
    T = pfm.TABLE_OF
    blocks = {}
    parts_seen = set()
    for addr, payload in parse_bulk(data):
        a1, a2, a3, a4 = addr
        if a1 in (0x04, 0x05):
            blocks.setdefault("hdr" if a1 == 4 else "ftr", []).append((addr, payload))
            continue
        blocks[addr] = payload
        if 0x10 <= a1 <= 0x4F:
            parts_seen.add(a1 & 0x0F)

    def blk(addr, base):
        size = S[base]
        p = blocks.get(addr)
        return payload_to_block(p, base, size) if p is not None else bytes(size)

    c = {}
    c["name"] = blk((6, 0, 0, 0), T["common.name"])
    c["c1"] = blk((6, 0, 1, 0), T["common.c1"])
    c["c2"] = blk((6, 0, 2, 0), T["common.c2"])
    c["ctrl"] = blk((6, 0, 3, 0), T["common.ctrl"])
    c["ins"] = [blk((6, 0, 4, 0), T["common.ins.0"]), blk((6, 0, 5, 0), T["common.ins.1"])]
    for k, a3 in (("arp", 6), ("reverb", 7), ("variation", 8), ("rotary", 9), ("meq", 0xA), ("mfx", 0xB),
                  ("msq", 0xC), ("superknob", 0xD), ("ad", 0xE), ("usb", 0xF), ("sklane", 0x12)):
        c[k] = blk((6, 0, a3, 0), T["common." + k])
    c["skseq"] = [blk((6, 1, m, 0), T["common.skseq"]) for m in range(8)]
    c["scenes"] = [{"s1": blk((6, 2, s, 0), T["common.scenes.s1"]), "s2": blk((6, 3, s, 0), T["common.scenes.s2"])} for s in range(8)]
    c["knobnames"] = [blk((6, 4, k, 0), T["common.knobnames"]) for k in range(8)]
    c["ctrlbox"] = [blk((6, 5, b, 0), T["common.ctrlbox"]) for b in range(32)]
    c["lanes"] = [{"l1": blk((6, 6, L << 4, 0), T["common.lanes.l1"]), "l2": blk((6, 7, L << 4, 0), T["common.lanes.l2"]),
                   "seq": [blk((6, 8, (L << 4) | m, 0), T["common.lanes.seq"]) for m in range(8)]} for L in range(4)]
    perf = {"common": c, "parts": [], "tail": b""}
    for pn in sorted(parts_seen):
        P = 0x10 | pn
        p = {"hdr": 1}
        p["name"] = blk((P, 0, 0, 0), T["part.name"])
        p["p1"] = blk((P, 0, 1, 0), T["part.p1"])
        p["p2"] = blk((P, 0, 2, 0), T["part.p2"])
        p["p3"] = blk((P, 0, 3, 0), T["part.p3"])
        p["ins"] = [blk((P, 0, 4, 0), T["part.ins.0"]), blk((P, 0, 5, 0), T["part.ins.1"])]
        p["arp"] = blk((P, 0, 6, 0), T["part.arp"])
        p["lfo"] = blk((P, 0, 7, 0), T["part.lfo"])
        p["zone"] = blk((P, 0, 8, 0), T["part.zone"])
        p["keyctrl"] = blk((P, 0, 9, 0), T["part.keyctrl"])
        p["scenes"] = [blk((P, 3, s, 0), T["part.scenes"]) for s in range(8)]
        p["knobnames"] = [blk((P, 4, k, 0), T["part.knobnames"]) for k in range(8)]
        p["ctrlbox"] = [blk((P, 5, b, 0), T["part.ctrlbox"]) for b in range(32)]
        p["lanes"] = [{"l1": blk((P, 6, L << 4, 0), T["part.lanes.l1"]), "l2": blk((P, 7, L << 4, 0), T["part.lanes.l2"]),
                       "seq": [blk((P, 8, (L << 4) | m, 0), T["part.lanes.seq"]) for m in range(8)]} for L in range(4)]
        # engine: whichever engine's blocks exist for this part
        E, F, A = 0x20 | pn, 0x30 | pn, 0x40 | pn
        if (A, 0, 0, 0) in blocks:
            p["engine"] = 3
            p["anx"] = {"common": blk((A, 0, 0, 0), T["anx.common"]),
                        "osc": [{"sw": blk((A, 1, o, 0), T["anx.oscsw"]), "osc": blk((A, 2, o, 0), T["anx.osc"])} for o in range(3)],
                        "filt": [{"sw": blk((A, 3, f, 0), T["anx.filtsw"]), "filt": blk((A, 4, f, 0), T["anx.filt"])} for f in range(2)],
                        "fold": blk((A, 5, 0, 0), T["anx.fold"])}
        elif (F, 0, 0, 0) in blocks:
            p["engine"] = 2
            p["fmx"] = {"common": blk((F, 0, 0, 0), T["fmx.common"]), "filter": blk((F, 0, 1, 0), T["fmx.filter"]),
                        "op": [{"sw": blk((F, 1, o, 0), T["fmx.opsw"]), "op": blk((F, 2, o, 0), T["fmx.op"])} for o in range(8)]}
        elif any(k[:2] == (E, 0x10) for k in blocks):
            p["engine"] = 1
            p["drum"] = {"keys": [blk((E, 0x10, k, 0), T["drum.key"]) for k in range(73)]}
        else:
            p["engine"] = 0
            els = sorted(k[2] for k in blocks if k[:2] == (E, 0))
            p["awm2"] = {"elements": [{"e1": blk((E, 0, e, 0), T["el.e1"]), "osc": blk((E, 1, e, 0), T["el.osc"]),
                                       "amp": blk((E, 2, e, 0), T["el.amp"]), "pitch": blk((E, 3, e, 0), T["el.pitch"]),
                                       "filter": blk((E, 4, e, 0), T["el.filter"])} for e in els]}
        perf["parts"].append(p)
    perf["bulk_header"] = blocks.get("hdr")
    perf["extra_blocks"] = {a: blocks[a] for a in ((0, 0, 0x7F, 0), (6, 9, 0, 0)) if a in blocks}
    return perf


ENGINE_FLAG = {0: 1, 1: 1, 2: 2, 3: 4, 255: 0}  # bit0 AWM2/Drum, bit1 FM-X, bit2 AN-X (Performance Flag block + performance.cfg)


def performance_to_syx(perf, bank=(0x04, 0x00), slot=0, device=0):
    """Serialize a raw pfm tree as a bulk dump.

    Header/footer address 04/05 ll mm nn selects the target: the default (04 04 00 00) is the edit
    buffer, which is what Soundmondo dumps use (store it from the panel afterwards); bank=(0x01, 0x00)
    with slot=nn targets Performance USER 1 slot nn directly (Data List "BULK CONTROL")."""
    T = pfm.TABLE_OF
    msgs = [message((0x04, bank[0], bank[1], slot), b"", device)]
    extra = perf.get("extra_blocks", {})
    msgs.append(message((0x00, 0x00, 0x7F, 0x00), extra.get((0, 0, 0x7F, 0), bytes([0, 1, 0, 0, 0, 0])), device))  # format version

    def add(addr, block, base):
        msgs.append(message(addr, block_to_payload(block, base), device))
    c = perf["common"]
    add((6, 0, 0, 0), c["name"], T["common.name"])
    add((6, 0, 1, 0), c["c1"], T["common.c1"])
    add((6, 0, 2, 0), c["c2"], T["common.c2"])
    add((6, 0, 3, 0), c["ctrl"], T["common.ctrl"])
    add((6, 0, 4, 0), c["ins"][0], T["common.ins.0"])
    add((6, 0, 5, 0), c["ins"][1], T["common.ins.1"])
    for k, a3 in (("arp", 6), ("reverb", 7), ("variation", 8), ("rotary", 9), ("meq", 0xA), ("mfx", 0xB),
                  ("msq", 0xC), ("superknob", 0xD), ("ad", 0xE), ("usb", 0xF), ("sklane", 0x12)):
        add((6, 0, a3, 0), c[k], T["common." + k])
    for m, b in enumerate(c["skseq"]):
        add((6, 1, m, 0), b, T["common.skseq"])
    for s, sc in enumerate(c["scenes"]):
        add((6, 2, s, 0), sc["s1"], T["common.scenes.s1"])
        add((6, 3, s, 0), sc["s2"], T["common.scenes.s2"])
    for k, b in enumerate(c["knobnames"]):
        add((6, 4, k, 0), b, T["common.knobnames"])
    for k, b in enumerate(c["ctrlbox"]):
        add((6, 5, k, 0), b, T["common.ctrlbox"])
    for L, l in enumerate(c["lanes"]):
        add((6, 6, L << 4, 0), l["l1"], T["common.lanes.l1"])
        add((6, 7, L << 4, 0), l["l2"], T["common.lanes.l2"])
        for m, b in enumerate(l["seq"]):
            add((6, 8, (L << 4) | m, 0), b, T["common.lanes.seq"])
    for pn, p in enumerate(perf["parts"]):
        if p["engine"] == 255:
            continue
        P = 0x10 | pn
        add((P, 0, 0, 0), p["name"], T["part.name"])
        add((P, 0, 1, 0), p["p1"], T["part.p1"])
        add((P, 0, 2, 0), p["p2"], T["part.p2"])
        add((P, 0, 3, 0), p["p3"], T["part.p3"])
        add((P, 0, 4, 0), p["ins"][0], T["part.ins.0"])
        add((P, 0, 5, 0), p["ins"][1], T["part.ins.1"])
        add((P, 0, 6, 0), p["arp"], T["part.arp"])
        add((P, 0, 7, 0), p["lfo"], T["part.lfo"])
        add((P, 0, 8, 0), p["zone"], T["part.zone"])
        add((P, 0, 9, 0), p["keyctrl"], T["part.keyctrl"])
        for s, b in enumerate(p["scenes"]):
            add((P, 3, s, 0), b, T["part.scenes"])
        for k, b in enumerate(p["knobnames"]):
            add((P, 4, k, 0), b, T["part.knobnames"])
        for k, b in enumerate(p["ctrlbox"]):
            add((P, 5, k, 0), b, T["part.ctrlbox"])
        for L, l in enumerate(p["lanes"]):
            add((P, 6, L << 4, 0), l["l1"], T["part.lanes.l1"])
            add((P, 7, L << 4, 0), l["l2"], T["part.lanes.l2"])
            for m, b in enumerate(l["seq"]):
                add((P, 8, (L << 4) | m, 0), b, T["part.lanes.seq"])
        E, F, A = 0x20 | pn, 0x30 | pn, 0x40 | pn
        if "awm2" in p:
            for e, el in enumerate(p["awm2"]["elements"]):
                for a2, k in enumerate(("e1", "osc", "amp", "pitch", "filter")):
                    add((E, a2, e, 0), el[k], T["el." + k])
        elif "drum" in p:
            for k, b in enumerate(p["drum"]["keys"]):
                add((E, 0x10, k, 0), b, T["drum.key"])
        elif "fmx" in p:
            f = p["fmx"]
            add((F, 0, 0, 0), f["common"], T["fmx.common"])
            add((F, 0, 1, 0), f["filter"], T["fmx.filter"])
            for o, op in enumerate(f["op"]):
                add((F, 1, o, 0), op["sw"], T["fmx.opsw"])
                add((F, 2, o, 0), op["op"], T["fmx.op"])
        elif "anx" in p:
            a = p["anx"]
            add((A, 0, 0, 0), a["common"], T["anx.common"])
            for o, os_ in enumerate(a["osc"]):
                add((A, 1, o, 0), os_["sw"], T["anx.oscsw"])
                add((A, 2, o, 0), os_["osc"], T["anx.osc"])
            for f, fl in enumerate(a["filt"]):
                add((A, 3, f, 0), fl["sw"], T["anx.filtsw"])
                add((A, 4, f, 0), fl["filt"], T["anx.filt"])
            add((A, 5, 0, 0), a["fold"], T["anx.fold"])
    mask = 0
    for p in perf["parts"]:
        mask |= ENGINE_FLAG.get(p["engine"], 0)
    msgs.append(message((6, 9, 0, 0), extra.get((6, 9, 0, 0), bytes([0, 0, 0, mask, 0, 0, 0, 0])), device))  # Performance Flag
    msgs.append(message((0x05, bank[0], bank[1], slot), b"", device))
    return b"".join(msgs)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "import":  # syx -> pfm
        perf = syx_to_performance(open(sys.argv[2], "rb").read())
        open(sys.argv[3], "wb").write(pfm.write_performance(perf))
        print("wrote", sys.argv[3], "parts:", [(pfm.ENGINE[p["engine"]], p["name"][:20].rstrip(b"\0 ")) for p in perf["parts"]])
    elif cmd == "export":  # pfm -> syx
        perf = pfm.read_performance(open(sys.argv[2], "rb").read())
        slot = int(sys.argv[4]) if len(sys.argv) > 4 else 0
        open(sys.argv[3], "wb").write(performance_to_syx(perf, slot=slot))
        print("wrote", sys.argv[3])
    elif cmd == "info":
        for addr, payload in parse_bulk(open(sys.argv[2], "rb").read()):
            print(" ".join(f"{a:02X}" for a in addr), len(payload))
