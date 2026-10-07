#!/usr/bin/env python3

import subprocess
import sys
import re
import os

if len(sys.argv) != 2:
    print("Usage: python3 stage1_solver.py <image>")
    sys.exit(1)

image = sys.argv[1]

print("[*] Reading image metadata...")

result = subprocess.run(
    ["exiftool", "-Comment", image],
    capture_output=True,
    text=True
)

comment = result.stdout.strip()

print(f"[+] Metadata: {comment}")

match = re.search(r":\s*(?:.*surface:\s*)?(\w+)\s*$", comment)

if not match:
    print("[-] Could not find the Steghide password.")
    sys.exit(1)

password = match.group(1)

print(f"[+] Password discovered: {password}")
print("[*] Extracting hidden file...")

subprocess.run(
    ["steghide", "extract", "-sf", image, "-p", password, "-f"],
    check=True
)

if os.path.exists("secret.txt"):
    with open("secret.txt", "r") as f:
        flag = f.read().strip()

    print(f"[+] Flag: {flag}")
else:
    print("[-] secret.txt was not extracted.")
