---
type: format-family
title: "Libxml2 Valid Fuzzer Entity Envelope format"
description: "Descriptive contract facts for libxml2 valid-fuzzer entity envelope."
resource: "cybergym://format/libxml2-valid-fuzzer-entity-envelope"
tags: ["libxml2-valid-fuzzer-entity-envelope", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The valid fuzzer wraps XML-like data in an entity envelope rather than passing a standalone document. The beginning contains parser option and allocation-limit fields, followed by entity strings separated by a backslash-newline sentinel; the first entity acts as the main document. EBCDIC detection is driven by the initial document signature and by the amount of buffered input available to the push parser.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
