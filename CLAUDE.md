# CLAUDE.md — `upload` (slim) · verbindliche Arbeitsweise

> **Sprache: Deutsch. Status: bindend.** Schlanker Einstieg; die **kanonische**
> Arbeitsweise lebt in der Flotten-Charter: `drobotka/fleet-governance` ·
> `docs/governance/CHARTER.md` (R1–R11, Mutations-Reihenfolge, Gate-Standard,
> Autonomie-Vertrag). Bei Konflikt gewinnt die explizite Operator-Anweisung;
> Widerspruch zu Repo-HEAD **melden**, nicht still übernehmen.

## Pflicht-Pre-Read vor JEDEM Tool-Use
`VERSION` → `PLAN.yaml` (SSoT) → `README.md` → diese Datei → Charter bei
Detailfragen. **Erst lesen/grounden (R1/R8/R9), dann handeln.**

## Was dieses Repo ist
**Layer-0 · öffentliches Asset-Repo** der Flotte: Brand-/Icon-Sets, OG-Bilder,
(später) self-hosted Fonts + Browser-/veraPDF-Bundles + Korpora — als Repo-Assets
bzw. **Release-Assets**. Konsumenten: `web-core` (PWA-Icon-Vertrag `ICONS.md`,
Fonts), `pdf-engine` (Browser/veraPDF). **Eine Quelle**, integritätsgesichert
(`brand/MANIFEST.json`: sha256 + Pixelmaße).

## Harte Regeln (Kurzform — Volltext: Charter §1)
- **R1** keine Behauptung ohne Quelle (Maße/Hashes aus den Bytes, generiert)
- **R6** NIE Secrets in git · **R10** Hygiene-Gate (keine `*.bak/*.orig/*~/*.log`)
- **R11** nur permissive Lizenzen; **eigene** Brand-Assets (keine Fremd-Marken);
  Fonts/Bundles brauchen Third-Party-Notice (OFL/Apache).

## Gate / Autonomie
- **`make verify`** = die eine Gate-Suite. Truth-Gate = **`gate-assets`** (PNG
  valide · IHDR-Maße == Dateiname · web-core-Vertrag · OG 1200×630).
- **Autonom** nur: eigene Assets · `make verify` grün · keine Lizenz-/Image-Wahl.
- **Operator-Gate** bei: Browser-/veraPDF-Image-/Bundle-Wahl · Release-Asset-Größe ·
  allem `approval: operator` in `PLAN.yaml`. **Öffentliches Repo** — nur bewusst
  öffentliche Assets.

## Quick-Start
```bash
make help · make verify · make manifest
```

➡ **Kanonische Regeln/Roadmap:** `fleet-governance/docs/governance/CHARTER.md`.
