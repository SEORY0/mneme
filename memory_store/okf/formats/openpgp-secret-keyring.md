---
type: format-family
title: "OPENPGP Secret Keyring Format"
description: "Round 26 descriptive structure and invariant facts for openpgp secret keyring."
tags: ["openpgp-secret-keyring", "round-26"]
okf_support: 1
train_only: true
---
# OPENPGP Secret Keyring Format

## Round 26 Factual Contract

### Schema / Invariants
- The relevant OpenPGP carrier is a GPG-format secret keyring. Secret-key packets contain public-key material followed by secret protection metadata. GnuPG experimental smartcard S2K metadata is encoded as an experimental specifier, a GnuPG marker and extension selector, a declared serial length, and serial bytes. The parser caps the actual serial bytes copied into fixed storage but preserves the declared length for later serialization.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
