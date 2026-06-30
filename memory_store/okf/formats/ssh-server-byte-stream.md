---
type: format-family
title: ssh-server-byte-stream format
description: Structure, build skeleton, and bug-prone areas of the ssh-server-byte-stream input format.
resource: cybergym://format/ssh-server-byte-stream
tags: [ssh-server-byte-stream, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- SSH transport begins with a text identification line followed by binary packets. Each packet has a network-order packet length, a padding length, payload bytes, and padding aligned to the pre-key block size. KEXINIT payloads contain a message byte, cookie, ten name-lists, a guess flag, and a reserved word. The ECDH reply payload carries a message byte followed by SSH string fields.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 26 Factual Contract


### Schema / Invariants
- SSH server inputs are raw client-side socket byte streams: a text identification line followed by binary SSH transport packets. Each cleartext packet carries a network-order packet length, a padding-length byte, payload bytes beginning with an SSH message type, and padding chosen so the packet aligns to the pre-key block size. KEXINIT payloads contain a cookie, ten SSH name-list strings, a first-packet-follows flag, and a reserved word; many later fields are SSH strings with network-order lengths.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
