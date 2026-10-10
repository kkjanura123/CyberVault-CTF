# Stage 5 — The Wire Tap

**Category:** Network Forensics  
**Difficulty:** Moderate–Hard  
**Project:** CyberVault — The Insider Incident

## Scenario

CyberVault's security team detected unusual network activity on the night of a suspicious financial transaction. A packet capture was collected for further investigation.

The capture contains ordinary network activity, a large HTTP file transfer, and several unusual DNS requests.

Your task is to determine which traffic is relevant and recover the information hidden within the suspicious network activity.

## Challenge Objectives

- Analyze network traffic using Wireshark.
- Identify unusual DNS queries.
- Distinguish misleading traffic from relevant evidence.
- Investigate encoded information in DNS subdomains.
- Reconstruct and decode the hidden message.

## Challenge File

`wiretap_capture.pcapng`

A SHA256 checksum is included for integrity verification.

## Recommended Tools

- Wireshark
- tshark
- CyberChef or Python

## Hints

**Hint 1:** The most obvious file transfer may not be the most important activity.

**Hint 2:** DNS queries can contain more information than ordinary domain names.

## Flag Format

`CYBERVAULT{...}`

## Submission

Submit the recovered flag to the CyberVault CTF platform.
