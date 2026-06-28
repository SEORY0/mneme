---
type: format-family
title: "Libxml2 Valid Fuzzer Envelope format"
description: "Descriptive contract facts for Libxml2 Valid Fuzzer Envelope."
resource: "cybergym://format/libxml2-valid-fuzzer-envelope"
tags: ["libxml2-valid-fuzzer-envelope", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The libxml2 valid fuzzer uses a front-carved envelope: parser options, an allocation-failure limit, then escaped URL/entity string pairs. The first entity pair is the main document; additional pairs are resolved by the fuzzer entity loader for DTDs or external entities.

### Harness Links
- [[libfuzzer-libxml2-valid]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The valid fuzzer input begins with parser options and an allocator-failure limit, followed by escaped URL/content string pairs. Backslash-newline terminates each string and doubled backslashes encode literal backslashes. The first URL/content pair is the main XML entity, with later pairs available to the external entity loader.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 25 Factual Contract

### Schema / Invariants
- The libxml2 valid fuzzer envelope starts with parser options and an allocation-failure limit, then escaped URL/content string pairs terminated by a backslash-newline sentinel. The first pair is the main document and later pairs can satisfy external entity or DTD requests.

### Harness Links
- [[libfuzzer-or-wrapper-selected-libxml2-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
