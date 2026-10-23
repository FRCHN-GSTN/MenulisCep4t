#!/usr/bin/env bash
set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$DIR")"

echo "=== Generator Contoh PDF Laporan ==="
echo "Lokasi Root: $ROOT_DIR"
echo ""

# Pastikan script build.sh ada
if [ ! -f "$ROOT_DIR/build.sh" ]; then
  echo "ERROR: build.sh tidak ditemukan di $ROOT_DIR"
  exit 1
fi

echo "Membuat sampel kompilasi laporan PDF..."
"$ROOT_DIR/build.sh"

if [ -f "$ROOT_DIR/Laporan.pdf" ]; then
  cp "$ROOT_DIR/Laporan.pdf" "$DIR/Laporan-Akademik-Example.pdf"
  echo "[OK] Contoh PDF berhasil disalin ke: $DIR/Laporan-Akademik-Example.pdf"
else
  echo "[ERROR] Gagal menghasilkan contoh PDF"
  exit 1
fi

echo "=== Selesai ==="
