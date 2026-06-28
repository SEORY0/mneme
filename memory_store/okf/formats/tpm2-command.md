---
type: format-family
title: tpm2-command format
description: Structure, build skeleton, and bug-prone areas of the tpm2-command input format.
resource: cybergym://format/tpm2-command
tags: ["tpm2-command", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The fuzz input is a TPM2 command buffer processed after a fixed startup command. Reaching RSA prime adjustment requires a semantically valid TPM command path for RSA key generation or key creation, with size and algorithm fields accepted by libtpms.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
