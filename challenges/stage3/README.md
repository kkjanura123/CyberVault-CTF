# Stage 3 – The Ledger Cipher

## Category
Cryptography

## Difficulty
Moderate

## Scenario
A suspicious ledger entry was recovered from the teller's workstation.
The message appears to have been protected using multiple layers of encryption.

## Objective
Investigate the ledger, identify the encryption methods, recover the key, and decrypt the message to obtain the flag.

## Tools
- CyberChef
- Basic cryptography knowledge

## Expected Solve Path

1. Open the `ledger.txt` file.
2. Identify that the record is protected by two encryption layers.
3. Use the teller's clue to determine the Vigenère key.
4. Use a Rail Fence cipher with 3 rails to decrypt the encrypted record.
5. Use a Vigenère cipher with the key `CASHIER` to decrypt the result.
6. Recover the CTF flag.

## Hints

### Hint 1
Use a Rail Fence cipher with 3 rails.

### Hint 2
Use a Vigenère cipher with the key `CASHIER`.

## Flag Format

`CTF{...}`

## Reset

To restore the challenge to its clean state:

```bash
./reset.sh
