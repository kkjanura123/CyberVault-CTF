#!/bin/bash

set -e

echo "[+] Resetting Stage 3..."

python3 scripts/generators/stage3_generator.py

echo "[+] Stage 3 has been reset successfully."
