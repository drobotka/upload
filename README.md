# upload

**Version:** `0.1.0` · Layer 0 (Assets, **public**) der Flotte · **eine Quelle für
Brand-/Icon-Assets** (später Fonts + Browser-/veraPDF-Bundles + Korpora).

## v0.1.0 — Brand-/Icon-Set

`brand/` trägt das vollständige Icon-Set (aus dem Portal-Donor), integritätsgesichert:

| Pfad | Inhalt |
|---|---|
| `brand/icons/icon-{16…512}.png` | 10 PWA-Icon-Größen |
| `brand/icons/maskable-{192,512}.png` | maskable (Safe-Zone) |
| `brand/icons/apple-touch-icon.png` | 180×180 (iOS) |
| `brand/og-image.png` | 1200×630 (Open Graph) |
| `brand/{favicon,rd-dark,rd-white}.svg` | Vektor-Marke |
| `brand/MANIFEST.json` | sha256 + Pixelmaße je Asset (**generiert**) |

**Erfüllt den web-core-Icon-Vertrag** (`web_core/pwa/ICONS.md`: icon-192/512 +
maskable-512 + apple-touch). Das `gate-assets` beweist hart: jede PNG ist valide,
ihre **IHDR-Pixelmaße == Dateiname**, der Vertrag ist erfüllt, OG = 1200×630.

```bash
make verify     # cruft + json + assets
make manifest   # MANIFEST.json aus den Asset-Bytes neu generieren
```

## Offen (PLAN.yaml)
- **Fonts** (autonom): self-hosted Woff2 (Poppins/JetBrains Mono, OFL) → löst
  web-cores System-Font-Fallback ab (Lizenz-Notice Pflicht, R11).
- **Bundles** (operator): Browser-/veraPDF-Bundles + Korpora als Release-Assets
  (pdf-engine-Konsument) — Image/Größen-Wahl ist operator-gated.

## Governance
Arbeitsweise = **Fleet-Charter** (`drobotka/fleet-governance` ·
`docs/governance/CHARTER.md`). **Nichts nach `main` ohne Operator-Freigabe.**
**Öffentliches Repo** — nur bewusst öffentliche Assets.
