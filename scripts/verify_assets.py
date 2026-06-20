#!/usr/bin/env python3
"""HARD asset gate (Form->Wahrheit). The brand assets are the fleet's single
source for icons/OG — this gate proves they are valid and satisfy the consumers'
contracts:
  1. every PNG is a real PNG whose IHDR pixel size matches its filename
     (icon-<N>.png is <N>x<N>; apple-touch-icon is 180; maskable-<N> is <N>),
  2. MANIFEST.json is not stale (sha256/size/px regenerate identically),
  3. the web-core PWA icon contract is satisfied (192 + 512 + maskable-512 +
     apple-touch-icon present),
  4. og-image.png is 1200x630 (Open Graph spec).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build_manifest as bm  # noqa: E402

BRAND = ROOT / "brand"
# web-core ICONS.md contract:
CONTRACT = {"icons/icon-192.png": "192x192", "icons/icon-512.png": "512x512",
            "icons/maskable-512.png": "512x512", "icons/apple-touch-icon.png": "180x180"}
fail: list[str] = []


def expected_px(name: str) -> str | None:
    if name == "apple-touch-icon":
        return "180x180"
    m = re.match(r"(?:icon|maskable)-(\d+)$", name)
    return f"{m.group(1)}x{m.group(1)}" if m else None


def main() -> int:
    manifest = json.loads((BRAND / "MANIFEST.json").read_text(encoding="utf-8"))
    files = manifest["files"]
    print(f"[assets] {manifest['asset_count']} assets")

    # 1) PNG IHDR size matches filename
    for rel, entry in files.items():
        p = Path(rel)
        if p.suffix != ".png":
            continue
        want = expected_px(p.stem)
        if rel == "og-image.png":
            want = "1200x630"
        if want and entry.get("px") != want:
            fail.append(f"{rel}: px {entry.get('px')} != expected {want}")

    # 2) manifest not stale
    if bm.render() != (BRAND / "MANIFEST.json").read_text(encoding="utf-8"):
        fail.append("MANIFEST.json stale vs assets — run: make manifest")

    # 3) web-core icon contract
    for rel, px in CONTRACT.items():
        if rel not in files:
            fail.append(f"web-core contract: missing {rel}")
        elif files[rel].get("px") != px:
            fail.append(f"web-core contract: {rel} is {files[rel].get('px')}, need {px}")

    # 4) og-image
    if "og-image.png" not in files:
        fail.append("missing og-image.png")

    print()
    if fail:
        print(f"[assets] FAIL — {len(fail)} problem(s):")
        for f in fail:
            print(f"  - {f}")
        return 1
    print("[assets] GREEN — PNGs valid, sizes match names, web-core contract + OG image satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
