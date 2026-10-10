#!/usr/bin/env python3

import os
import re
import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: python3 stage4_solver.py <disk_image>")
    sys.exit(1)

image = sys.argv[1]

print("[*] Searching for deleted files...")

result = subprocess.run(
    ["fls", "-rd", "-m", "/", image],
    capture_output=True,
    text=True,
    check=True
)

deleted_files = []

for line in result.stdout.splitlines():
    match = re.search(r"\|(.+?) \(deleted-realloc\)\|(\d+)\|", line)

    if match:
        path = match.group(1)
        inode = match.group(2)
        deleted_files.append((path, inode))

if not deleted_files:
    print("[-] No deleted files found.")
    sys.exit(1)

print(f"[+] Found {len(deleted_files)} deleted files.")

target_inode = None

for path, inode in deleted_files:

    result = subprocess.run(
        ["istat", image, inode],
        capture_output=True,
        text=True,
        check=True
    )

    match = re.search(r"Deleted:\s+(.+)", result.stdout)

    if match:
        deleted_time = match.group(1).strip()

        print(f"[+] {path} (inode {inode})")
        print(f"    Deleted: {deleted_time}")

        if "transaction_confirmation.pdf" in path:
            target_inode = inode

if target_inode is None:
    print("[-] Transaction confirmation PDF not found.")
    sys.exit(1)

print(f"\n[+] Target identified: transaction_confirmation.pdf")
print(f"[+] Inode: {target_inode}")

output_file = "/tmp/stage4_recovered.pdf"

print("[*] Recovering PDF...")

with open(output_file, "wb") as f:
    subprocess.run(
        ["icat", image, target_inode],
        stdout=f,
        check=True
    )

print(f"[+] Recovered: {output_file}")

print("[*] Inspecting PDF metadata...")

result = subprocess.run(
    ["exiftool", "-s3", "-Comments", output_file],
    capture_output=True,
    text=True,
    check=True
)

flag = result.stdout.strip()

if re.fullmatch(r"CTF\{[^}]+\}", flag):
    print(f"[+] Flag: {flag}")
else:
    print("[-] Flag not found in PDF metadata.")
    sys.exit(1)
