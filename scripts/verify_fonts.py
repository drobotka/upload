#!/usr/bin/env python3
"""HARD font gate (R1 integrity · R11 license) — pure stdlib, no runtime deps.

Verifies fonts/poppins/: every woff2 has the `wOF2` magic, its sha256 + byte size
match fonts/poppins/MANIFEST.json (generated from the bytes), every manifest entry
exists, and the OFL license file is present (R11 third-party notice for the font).
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "fonts" / "poppins"


def main() -> int:
    man_path = FONTS / "MANIFEST.json"
    if not man_path.is_file():
        print("  FAIL: fonts/poppins/MANIFEST.json missing")
        return 1
    man = json.loads(man_path.read_text())
    files = man["files"]
    # R11: license notice present
    lic = FONTS / man["_meta"].get("license_file", "OFL.txt")
    if not lic.is_file():
        print(f"  FAIL: license file {lic.name} missing (R11)")
        return 1
    # every manifest entry: exists, magic, sha256+size match
    for name, meta in files.items():
        f = FONTS / name
        if not f.is_file():
            print(f"  FAIL: {name} in manifest but missing on disk")
            return 1
        b = f.read_bytes()
        if b[:4] != b"wOF2":
            print(f"  FAIL: {name} is not a woff2 (magic {b[:4]!r})")
            return 1
        sha = hashlib.sha256(b).hexdigest()
        if sha != meta["sha256"] or len(b) != meta["bytes"]:
            print(f"  FAIL: {name} sha256/size != manifest (regenerate)")
            return 1
    # no stray woff2 outside the manifest
    stray = [p.name for p in FONTS.glob("*.woff2") if p.name not in files]
    if stray:
        print(f"  FAIL: woff2 not in manifest: {stray}")
        return 1
    total = sum(m["bytes"] for m in files.values())
    print(f"  ok: {len(files)} Poppins woff2 valid · sha256==manifest · {total} bytes · {man['_meta']['license']} ({lic.name})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
