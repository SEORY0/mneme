---
type: format-family
title: "Raw Pkcs11 Fuzzer Record Format"
description: "Round 27 descriptive format facts for raw-pkcs11-fuzzer-record."
resource: cybergym://format/raw-pkcs11-fuzzer-record
tags: ["raw-pkcs11-fuzzer-record", "round-27"]
okf_support: 1
---
# Raw Pkcs11 Fuzzer Record Format

## Round 27 Factual Contract

- The fuzz record is a raw byte stream with a leading operation selector.
- The verify operation consumes a native-width mechanism value, a login-type byte, a NUL-terminated PIN string, then several little-endian length-prefixed buffers for object id, verify data, and signature.
- The remaining bytes are consumed by the virtual smart-card reader as length-prefixed APDU response chunks.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
