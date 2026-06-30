---
type: format-family
title: opensc-pkcs15init-profile-reader-chunks format
description: "Round 23 descriptive structure and invariant facts for opensc-pkcs15init-profile-reader-chunks."
resource: cybergym://format/opensc-pkcs15init-profile-reader-chunks
tags: ["opensc-pkcs15init-profile-reader-chunks", "round-23"]
okf_support: 1
train_only: true
---
# Opensc Pkcs15init Profile Reader Chunks Format

## Round 23 Factual Contract

### Schema / Invariants
- The pkcs15init input is split at a NUL delimiter. The prefix is an OpenSC profile configuration, and the suffix is a virtual-reader stream of host-endian two-byte length-prefixed chunks. The first reader chunk is the ATR; subsequent chunks are APDU responses with status words at the end.

### Harness Links
- [[libfuzzer-opensc-pkcs15init]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 26 Factual Contract


### Schema / Invariants
- The input is split at the first NUL byte. The prefix is OpenSC profile configuration text. The suffix is a virtual smart-card reader stream made of little-endian two-byte chunk lengths followed by chunk bodies. The first chunk is the card ATR used for driver selection. Later chunks are APDU responses; status words are stored at the end of each response chunk and response bodies precede them. The AuthentIC profile defines a PKCS#15 application DF, PKCS#15 metadata EFs, and private-key/public-key/certificate templates. The private-key template ACL methods directly affect both SDO ACL serialization and later PKCS#15 access-rule synthesis.

### Harness Links
- [[libfuzzer-opensc-pkcs15init]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
