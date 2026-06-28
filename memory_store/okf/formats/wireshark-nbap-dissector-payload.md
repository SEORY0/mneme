---
type: format-family
title: Wireshark Nbap Dissector Payload format
description: Format contract for wireshark-nbap-dissector-payload inputs.
resource: cybergym://format/wireshark-nbap-dissector-payload
tags: [wireshark-nbap-dissector-payload, uninitialized-field-use, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
NBAP messages are telecom control-plane protocol payloads with structured ASN.1-style fields. A useful trigger must select an NBAP procedure or information element path that references a DCH identifier after partial or absent initialization.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
