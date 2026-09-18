#!/usr/bin/env python3
"""Install a .pfm performance into the ESP plugin's User bank (copies the file and registers it in
performance.cfg), or list / remove entries.

Usage:
  install.py add <file.pfm> [--slot N] [--display-name NAME] [--dry-run]
  install.py list [--user-dir DIR]
  install.py remove <slot>
  install.py replace <slot> <file.pfm>      # overwrite an existing slot in place

The plugin keeps its user bank in
  /Library/Yamaha/Expanded Softsynth Plugin for MONTAGE M/contents/current/performance/40xxxx-Performance.pfm
indexed by performance.cfg ("PChd" header + "Entr" records, see docs/pfm-format.md). Close every
host that has the plugin loaded before installing: the plugin rewrites performance.cfg itself when
it stores, so edits made while it runs can be lost or conflict. A backup of performance.cfg is
written next to it as performance.cfg.bak-<timestamp> before every change.

The record layout was derived from 5651 existing records (docs/pfm-format.md); two flag bytes are
still unexplained and are copied from the most common user record pattern.
"""
import glob
import os
import shutil
import struct
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pfm  # noqa: E402

USER_DIR = "/Library/Yamaha/Expanded Softsynth Plugin for MONTAGE M/contents/current"
BANK = 0x40
ENGINE_FLAG = {0: 1, 1: 1, 2: 2, 3: 4, 255: 0}


def read_cfg(path):
    d = open(path, "rb").read()
    assert d[:4] == b"PChd", "not a PChd index"
    ver = struct.unpack(">I", d[4:8])[0]
    count = struct.unpack(">I", d[8:12])[0]
    recs, i = [], 12
    while i < len(d):
        assert d[i:i + 4] == b"Entr", f"bad record at {i:#x}"
        ln = struct.unpack(">I", d[i + 4:i + 8])[0]
        recs.append(d[i + 8:i + 8 + ln])
        i += 8 + ln
    assert len(recs) == count, f"count {count} != records {len(recs)}"
    return ver, recs


def write_cfg(path, ver, recs):
    out = b"PChd" + struct.pack(">II", ver, len(recs))
    for r in recs:
        out += b"Entr" + struct.pack(">I", len(r)) + r
    open(path, "wb").write(out)


def slot_of(rec):
    return struct.unpack(">H", rec[2:4])[0]


def make_record(slot, perf, display_name=None, stamp=None):
    """Build an Entr record body for a raw pfm tree stored at User slot `slot`."""
    parts = [p for p in perf["parts"] if p["engine"] != 255]
    name = perf["common"]["name"].split(b"\0")[0].decode("latin1").rstrip()
    c2 = perf["common"]["c2"]
    main, sub = struct.unpack("<H", c2[0:2])[0], struct.unpack("<H", c2[2:4])[0]
    mask = 0
    for p in parts:
        mask |= ENGINE_FLAG.get(p["engine"], 0)
    present = 0
    for i, p in enumerate(perf["parts"]):
        if p["engine"] != 255:
            present |= 1 << i
    # layout (from the plugin's own records): [0..3] id, [4] 0, [5] flag, [6] flag, [7] engine mask,
    # [8] 2 = single part / 0 = multi, [9] 0, [10..11] part-present mask LE, [12..16] 0, [17..18] stamp, [19..] text
    rec = bytes([0, BANK]) + struct.pack(">H", slot)
    rec += bytes([0, 0, 0, mask, 2 if len(parts) == 1 else 0, 0])
    rec += struct.pack("<H", present)
    rec += bytes(5)
    rec += stamp if stamp else bytes(2)
    rec += f"{main * 16 + sub}:{display_name or name}:{name}".encode("latin1") + b"\0"
    return rec


def cmd_add(args):
    src = args[0]
    user_dir = USER_DIR
    dry = "--dry-run" in args
    slot = int(args[args.index("--slot") + 1]) if "--slot" in args else None
    display = args[args.index("--display-name") + 1] if "--display-name" in args else None
    perf = pfm.read_performance(open(src, "rb").read())  # validates the file
    cfg_path = os.path.join(user_dir, "performance.cfg")
    ver, recs = read_cfg(cfg_path)
    used = {slot_of(r) for r in recs if r[1] == BANK}
    if slot is None:
        slot = max(used) + 1 if used else 0
    if slot in used:
        raise SystemExit(f"slot {slot} is already used; pass --slot or remove it first")
    # copy the save-time stamp bytes from the newest existing user record, if any
    stamp = None
    for r in reversed(recs):
        if r[1] == BANK and r[17:19] != b"\0\0":
            stamp = r[17:19]
            break
    rec = make_record(slot, perf, display, stamp)
    dest = os.path.join(user_dir, "performance", f"{BANK:02X}{slot:04X}-Performance.pfm")
    print(f"slot {slot} -> {dest}")
    print("record:", rec[:19].hex(" "), rec[19:])
    if dry:
        return
    bak = cfg_path + ".bak-" + time.strftime("%Y%m%d-%H%M%S")
    shutil.copy2(cfg_path, bak)
    shutil.copy2(src, dest)
    recs.append(rec)
    write_cfg(cfg_path, ver, recs)
    ver2, recs2 = read_cfg(cfg_path)
    assert len(recs2) == len(recs)
    print(f"installed; index now has {len(recs2)} entries (backup: {bak})")


def cmd_replace(args):
    """replace <slot> <file.pfm>: overwrite an existing User slot's file and refresh its index record
    (keeps the slot's timestamp bytes so the plugin treats it as the same entry)."""
    slot, src = int(args[0], 0), args[1]
    perf = pfm.read_performance(open(src, "rb").read())
    cfg_path = os.path.join(USER_DIR, "performance.cfg")
    ver, recs = read_cfg(cfg_path)
    new, found = [], False
    for r in recs:
        if r[1] == BANK and slot_of(r) == slot:
            new.append(make_record(slot, perf, None, r[17:19]))
            found = True
        else:
            new.append(r)
    if not found:
        raise SystemExit(f"slot {slot} not in index")
    bak = cfg_path + ".bak-" + time.strftime("%Y%m%d-%H%M%S")
    shutil.copy2(cfg_path, bak)
    shutil.copy2(src, os.path.join(USER_DIR, "performance", f"{BANK:02X}{slot:04X}-Performance.pfm"))
    write_cfg(cfg_path, ver, new)
    print(f"replaced slot {slot}: {new[[slot_of(r) == slot and r[1] == BANK for r in new].index(True)][19:]} (backup: {bak})")


def cmd_list(args):
    user_dir = args[args.index("--user-dir") + 1] if "--user-dir" in args else USER_DIR
    ver, recs = read_cfg(os.path.join(user_dir, "performance.cfg"))
    for r in recs:
        label = r[19:].split(b"\0")[0].decode("latin1")
        print(f"{r[1]:02X}{slot_of(r):04X}  mask={r[7]} single={r[8]} parts={struct.unpack('<H', r[10:12])[0]:04x}  {label}")


def cmd_remove(args):
    slot = int(args[0])
    cfg_path = os.path.join(USER_DIR, "performance.cfg")
    ver, recs = read_cfg(cfg_path)
    keep = [r for r in recs if not (r[1] == BANK and slot_of(r) == slot)]
    if len(keep) == len(recs):
        raise SystemExit(f"slot {slot} not found")
    bak = cfg_path + ".bak-" + time.strftime("%Y%m%d-%H%M%S")
    shutil.copy2(cfg_path, bak)
    write_cfg(cfg_path, ver, keep)
    f = os.path.join(USER_DIR, "performance", f"{BANK:02X}{slot:04X}-Performance.pfm")
    if os.path.exists(f):
        os.remove(f)
    print(f"removed slot {slot} (backup: {bak})")


if __name__ == "__main__":
    {"add": cmd_add, "list": cmd_list, "remove": cmd_remove, "replace": cmd_replace}[sys.argv[1]](sys.argv[2:])
