#!/usr/bin/env bash
# Put Sahel Regular + Bold (Western digits) into a fonts/ directory for
# @font-face embedding. Never the FD / Farsi-digits cut, which draws ۳٫۱۴.
#
#   fetch-sahel.sh [dest-dir]
#
# Reuses an installed system face or a previous download before hitting the
# network, so an offline machine with the font already present still works.
# Sahel is SIL Open Font License 1.1; keep the licence file beside the
# TTFs when you ship the HTML.
set -uo pipefail

dest=${1:-fonts}
cache="${XDG_CACHE_HOME:-$HOME/.cache}/fa-fonts"
ver=${SAHEL_VERSION:-3.4.0}
base="https://cdn.jsdelivr.net/gh/rastikerdar/sahel-font@v${ver}/dist"

mkdir -p "$dest" "$cache"

want=(Sahel.ttf Sahel-Bold.ttf)

have_all() {
  local dir=$1 f
  for f in "${want[@]}"; do
    [[ -s "$dir/$f" ]] || return 1
  done
  return 0
}

report() {
  local f
  for f in "${want[@]}"; do printf '%s\n' "$dest/$f"; done
}

if have_all "$dest"; then
  echo "fetch-sahel: already present in $dest" >&2
  report
  exit 0
fi

# 1. A previous download.
if have_all "$cache"; then
  echo "fetch-sahel: using cache $cache" >&2
  cp -f "$cache"/Sahel.ttf "$cache"/Sahel-Bold.ttf "$dest/"
  report
  exit 0
fi

# 2. An installed system copy — no network needed.
if command -v fc-match >/dev/null 2>&1; then
  reg=$(fc-match -f '%{file}' 'Sahel:style=Regular' 2>/dev/null || true)
  reg_fam=$(fc-match -f '%{family[0]}' 'Sahel:style=Regular' 2>/dev/null || true)
  bold=$(fc-match -f '%{file}' 'Sahel:style=Bold' 2>/dev/null || true)
  bold_fam=$(fc-match -f '%{family[0]}' 'Sahel:style=Bold' 2>/dev/null || true)
  if [[ ${reg_fam:-} == Sahel && -f ${reg:-} ]]; then
    echo "fetch-sahel: copying the installed face" >&2
    cp -f "$reg" "$dest/Sahel.ttf"
    if [[ ${bold_fam:-} == Sahel && -f ${bold:-} ]]; then
      cp -f "$bold" "$dest/Sahel-Bold.ttf"
    else
      cp -f "$reg" "$dest/Sahel-Bold.ttf"
    fi
    cp -f "$dest/Sahel.ttf" "$cache/" 2>/dev/null || true
    cp -f "$dest/Sahel-Bold.ttf" "$cache/" 2>/dev/null || true
    report
    exit 0
  fi
fi

# 3. Download.
command -v curl >/dev/null 2>&1 || {
  echo "fetch-sahel: need curl to download the font" >&2
  echo "fetch-sahel: or install any fa face and re-run" >&2
  exit 1
}

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

echo "fetch-sahel: downloading v${ver}" >&2
for f in "${want[@]}"; do
  if ! curl -fsSL --retry 2 --connect-timeout 15 -o "$tmp/$f" "$base/$f"; then
    echo "fetch-sahel: download failed: $base/$f" >&2
    echo "fetch-sahel: fall back to any installed fa face, e.g." >&2
    echo "  fc-list :lang=fa family | sort -u" >&2
    exit 1
  fi
done

for f in "${want[@]}"; do
  src="$tmp/$f"
  [[ -s $src ]] || { echo "fetch-sahel: empty download $f" >&2; exit 1; }
  cp -f "$src" "$dest/$f"
  cp -f "$src" "$cache/$f" 2>/dev/null || true
done

if command -v sha256sum >/dev/null 2>&1; then
  echo "fetch-sahel: sha256" >&2
  ( cd "$dest" && sha256sum "${want[@]}" >&2 )
fi

report
