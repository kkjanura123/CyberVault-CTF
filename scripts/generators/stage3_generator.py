VIGENERE_KEY = "CASHIER"
RAILS = 3
PLAINTEXT = "CTF{the_ledger_cipher}"


def vigenere_encrypt(text, key):
    result = []
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord("A")
            base = ord("A") if char.isupper() else ord("a")

            encrypted = chr((ord(char) - base + shift) % 26 + base)
            result.append(encrypted)

            key_index += 1
        else:
            result.append(char)

    return "".join(result)


def rail_fence_encrypt(text, rails):
    if rails == 1:
        return text

    fence = [[] for _ in range(rails)]
    row = 0
    direction = 1

    for char in text:
        fence[row].append(char)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return "".join("".join(line) for line in fence)


vigenere_result = vigenere_encrypt(PLAINTEXT, VIGENERE_KEY)
ciphertext = rail_fence_encrypt(vigenere_result, RAILS)

output = f"""LEDGER ENTRY #204

Two locks guard what lies beneath.

"My key is what I was called
when I handled every customer's money."


Encrypted record:

{ciphertext}
"""

with open("challenges/stage3/challenge/ledger.txt", "w") as file:
    file.write(output)

print("[+] Vigenere key:", VIGENERE_KEY)
print("[+] Rail Fence rails:", RAILS)
print("[+] Encrypted flag:", ciphertext)
print("[+] Stage 3 ledger generated successfully.")
