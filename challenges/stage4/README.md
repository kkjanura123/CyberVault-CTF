# Stage 4 – The Wiped Workstation

## Category

Digital Forensics

## Difficulty

Moderate

## Scenario

Investigators know that a fraudulent transfer was authorized at **23:47**.

A manager deleted several files shortly before the incident, and a weekly
backup may contain recoverable deleted artifacts.

## Challenge File

`workstation_backup.dd`

## Objective

Recover the deleted files, inspect their deletion timestamps, compare them
with the 23:47 transfer time, identify the relevant transaction artifact,
and inspect its metadata to recover the flag.

## Tools

- Autopsy
- Sleuth Kit (`fls`, `istat`, `icat`)
- ExifTool or `pdfinfo`

## Expected Solve Path

1. Open `workstation_backup.dd` in Autopsy.
2. Locate the deleted/reallocated files.
3. Note the inode numbers.
4. Use `istat` to inspect the deletion times.
5. Compare the deletion times with the 23:47 transfer time.
6. Identify `transaction_confirmation.pdf`.
7. Recover the PDF.
8. Inspect the PDF metadata.
9. Recover the CTF flag.

## Flag Format

`CTF{...}`

## Hints

### Hint 1

Not every recovered file matters — check when each one was actually deleted.

### Hint 2

Compare deletion times to the transfer time from the case timeline.

## Reset

To restore the challenge to its clean state:

```bash
./reset.sh
