# Stage 1 – The Teller's Photo

## Category
Steganography

## Difficulty
Easy

## Scenario
A suspicious photograph was recovered from the teller's workstation.
Something important may be hidden inside the image.

## Objective
Investigate the image and recover the hidden flag.

## Tools
- ExifTool
- Steghide

## Expected Solve Path
1. Inspect the image metadata using ExifTool.
2. Identify the clue contained in the metadata.
3. Use the discovered clue as the Steghide passphrase.
4. Extract the hidden file from the JPEG.
5. Read the CTF flag.

## Flag Format
CTF{...}
