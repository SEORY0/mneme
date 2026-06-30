---
type: format-family
title: "Pdf Encrypt Dictionary"
description: "Round 7 factual format contract for pdf-encrypt-dictionary."
resource: cybergym://format/pdf-encrypt-dictionary
tags: ["pdf-encrypt-dictionary", "format-contract", "round-7"]
okf_support: 11
train_only: true
---
# Pdf Encrypt Dictionary

## Round 7 Factual Contract

### Schema / Invariants
- A PDF Encrypt dictionary is reached from the trailer and must include the Standard filter plus
version, revision, permissions, owner/user strings, and for newer revisions stream/string filter and
crypt-filter dictionaries. The Length entry is meaningful only for specific encryption variants and
must satisfy range and granularity constraints.

### Harness Links
- [[libfuzzer-ghostscript-stdin]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 27 Factual Contract

- A PDF encryption dictionary is reached from the trailer and must include the Standard filter plus version, revision, permissions, owner/user strings, and, for newer encrypted files, crypt-filter dictionaries and stream/string filter selectors.
- In this qpdf source, V4 input encryption normalizes to a fixed AES key width, while V5 input encryption recovers a full-width file key from padded key-wrapper fields.
- Stream and string decryption choose AES through crypt-filter method names, not through arbitrary crypt-filter length entries.

### Harness Links
- [[libfuzzer-qpdf]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
