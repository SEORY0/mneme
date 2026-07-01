---
type: format-family
title: Bfd Archive Or Tekhex format
description: Format contract for bfd-archive-or-tekhex.
resource: cybergym://format/bfd-archive-or-tekhex
tags: [bfd-archive-or-tekhex]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The fuzz target writes raw bytes to a temporary file and opens it through BFD with automatic target detection, then checks for archive format. TekHex records are percent-led text records carrying a length/type/integrity field prefix followed by line data. A complete BFD archive begins with the ar global marker and fixed-width member headers before member bytes.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 35 Factual Contract

### Schema / Invariants
- BFD archive inputs start with a global archive marker, followed by fixed-width member headers and member payloads; an archive symbol table member can make generic archive recognition inspect the first real member as a BFD object. TekHex object recognition is text-record based: records are percent-led, carry a hex length, record type, checksum field, and type-specific body. Termination and data records can be structurally tiny and still be accepted by object-mode BFD tools.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
