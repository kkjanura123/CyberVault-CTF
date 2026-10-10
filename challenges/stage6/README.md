
# Stage 6 — The Vault Backdoor

**Project:** CyberVault — The Insider Incident  
**Category:** Web Security / JWT Authentication  
**Difficulty:** Moderate–Hard

## Scenario

CyberVault investigators discovered a legacy transfer authorization portal associated with suspicious financial activity.

The portal uses JWT-based authentication. Investigators suspect that a forgotten development endpoint may expose sensitive authentication configuration.

Your task is to investigate the application, identify the weakness, and retrieve the protected transaction evidence.

## Objective

Gain access to the administrator-only transaction record and recover the hidden CTF flag.

## Participant Access

The organizer will provide the URL of the running CyberVault portal.

Begin by exploring the application as an ordinary investigator.

## Challenge Files

- `app.py` — Flask application (organizer deployment source)
- `Dockerfile` — Container build instructions
- `requirements.txt` — Python dependencies

## Organizer Deployment

Build:

```bash
docker build -t cybervault-stage6 .
```

Run locally:

```bash
docker run --rm -p 127.0.0.1:5000:5000 -e HOST=0.0.0.0 cybervault-stage6
```

Open:

`http://127.0.0.1:5000`

## Security Note

This application is deliberately vulnerable and intended only for an isolated educational CTF environment.

Do not expose the application directly to the public internet without an appropriate isolated deployment environment.
