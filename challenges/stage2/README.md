# Stage 2 – The Forgotten Login

## Category
Web Security

## Difficulty
Easy

## Scenario
An old internal teller login system was left accessible after a system migration.
Developer information was unintentionally exposed through the application's source
and static resources.

## Objective
Investigate the web application and recover the hidden login credentials to obtain
the flag.

## Tools
- Web Browser
- Developer Tools / View Source
- curl (optional)
- Burp Suite (optional)

## Expected Solve Path

1. Access the teller portal.
2. Inspect the homepage source.
3. Discover the `/login` route.
4. Inspect the login page source.
5. Identify the referenced `script.js` resource.
6. Inspect `script.js` and recover the exposed credentials.
7. Use the credentials to log in.
8. Recover the CTF flag.

## Intended Credentials

Username:
`teller`

Password:
`ledger2026`

## Flag

`CTF{the_forgotten_login}`

## Docker

Build the challenge:

```bash
cd app
sudo docker build -t cybervault-stage2 .
