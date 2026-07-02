---
type: format-family
title: "UPX Packed Unix Format"
description: "Round 27 descriptive format facts for upx-packed-unix."
resource: cybergym://format/upx-packed-unix
tags: ["upx-packed-unix", "round-27"]
okf_support: 1
---
# UPX Packed Unix Format

## Round 27 Factual Contract

- UPX packed Unix files preserve an executable envelope and carry a trailer with a pack header and a pointer to compressed data.
- The compressed data begins with packed metadata containing original size and blocksize, followed by b_info records that carry uncompressed size, compressed size, and method/filter bytes.
- Some corpus files expose a plain trailer magic, while newer packed shared-object samples may not be accepted by the test-mode unpacker.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
