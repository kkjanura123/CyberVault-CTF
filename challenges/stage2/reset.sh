#!/bin/bash

set -e

echo "[+] Resetting Stage 2..."

sudo docker rm -f cybervault-stage2 2>/dev/null || true

cd app

sudo docker build -t cybervault-stage2 .

sudo docker run -d \
    --name cybervault-stage2 \
    -p 127.0.0.1:5000:5000 \
    cybervault-stage2

echo "[+] Stage 2 has been reset successfully."
echo "[+] Access: http://127.0.0.1:5000"
