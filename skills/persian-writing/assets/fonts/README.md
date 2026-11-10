# Bundled fonts

Persian font shipped with this skill (SIL Open Font License 1.1, see
`Sahel-OFL.txt` — free for commercial use and embedding):

- **Sahel** v3.4.0 by Saber Rastikerdar (github.com/rastikerdar/sahel-font),
  five static weights: `Sahel-Light.ttf` (300), `Sahel.ttf` (400),
  `Sahel-SemiBold.ttf` (600), `Sahel-Bold.ttf` (700), `Sahel-Black.ttf` (900).
  Light–Bold for body and documents; Black is the display/headline weight.

Before converting any document to PDF, install them into the environment:

```bash
bash ../../scripts/install_fonts.sh
```

More families (Shabnam, Samim, Parastoo, Tanha, Gandom):
`python3 ../../scripts/download_fonts.py --all` — needs GitHub access;
in sandboxed environments ask the user to add TTFs here manually.
