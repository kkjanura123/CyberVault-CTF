#!/usr/bin/env python3

import re

VIGENERE_KEY = "CASHIER"
RAILS = 3


def rail_fence_decrypt(ciphertext, rails):
    if rails == 1:
        return ciphertext

    pattern = []
    row = 0
    direction = 1

    for _ in ciphertext:
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    counts = [pattern.count(i) for i in range(rails)]

    fence = []
    index = 0

    for count in counts:
        fence.append(list(ciphertext[index:index + count]))
        index += count

    result = []
    positions = [0] * rails

    for rail in pattern:
        result.append(fence[rail][positions[rail]])
        positions[rail] += 1

    return "".join(result)


def vigenere_decrypt(text, key):
    result = []
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord("A")
            base = ord("A") if char.isupper() else ord("a")

            decrypted = chr((ord(char) - base - shift) % 26 + base)
            result.append(decrypted)

            key_index += 1
        else:
            result.append(char)

    return "".join(result)


with open("challenges/stage3/challenge/ledger.txt", "r") as file:
    content = file.read()

marker = "Encrypted record:\n\n"
ciphertext = content.split(marker, 1)[1]

print("[*] Reading encrypted ledger...")
print("[*] Applying Rail Fence decryption...")
rail_fence_result = rail_fence_decrypt(ciphertext, RAILS)

print("[*] Applying Vigenere decryption...")
plaintext = vigenere_decrypt(rail_fence_result, VIGENERE_KEY)

print("\n[+] Decrypted message:\n")
print(plaintext)

flag = re.search(r"CTF\{[^}]+\}", plaintext)

if flag:
    print(f"\n[+] Flag: {flag.group(0)}")
else:
    print("\n[-] Flag not found.")
