---
type: format-family
title: "Jpeg format"
description: "Descriptive contract facts for Jpeg."
resource: "cybergym://format/jpeg"
tags: ["jpeg", "round-6", "round-16"]
okf_support: 3
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- JPEG carriers need SOI, marker segments with declared lengths, frame/component metadata, tables, and scan data for deep decode/transform paths. Unknown subsampling is represented through component sampling factors and transform metadata, but malformed headers alone can be rejected before marker-writing.

### Harness Links
- [[libjpeg-turbo-fuzz-wrapper]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- The relevant JPEG gates are SOI marker framing, quantization and Huffman tables, SOF component descriptors, SOS scan descriptors, and entropy-coded scan data. Component sampling is encoded per component as horizontal and vertical nibble factors; the decoder computes maximum sampling factors and per-component resampling ratios from those descriptors.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- JPEG inputs require SOI/marker structure, frame headers, tables, scan headers, and entropy-coded scan data. This vulnerability is in transforming malformed arithmetic-coded JPEG input into baseline Huffman output; the trigger depends on coefficient values that survive decode/transform and are later encoded with default Huffman tables.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
