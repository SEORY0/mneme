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

## Round 23 Factual Contract

### Schema / Invariants
- The target transform fuzzer expects a valid JPEG stream, reads image dimensions and subsampling from the header, and performs several lossless transform operations including progressive/copy-none, transpose/crop/gray, rotation with arithmetic coding, and an optimized variant.

### Harness Links
- [[libfuzzer-libjpeg-turbo-transform]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 28 Factual Contract

### Schema / Invariants
- JPEG inputs require SOI marker framing, length-delimited metadata/table segments, a start-of-frame marker with precision, dimensions, and component descriptors, a start-of-scan marker with a scan component count, per-scan component selectors and table ids, spectral-selection bytes, and entropy-coded data ending at a marker. Multi-component baseline scans must use scan component descriptors consistent with the frame header order.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- JPEG reachability required SOI marker framing, length-delimited quantization and Huffman table segments, a baseline start-of-frame segment with precision, dimensions, and component descriptors, a start-of-scan segment listing the same components with table selectors, baseline spectral-selection bytes, and entropy-coded data terminated by an image marker. The decoder accepts one or three components; for color JPEGs the frame component order and scan component order are expected to agree.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 35 Factual Contract

### Schema / Invariants
- JPEG decoding gates include SOI marker framing, length-delimited table segments, a baseline SOF segment with precision, dimensions, component ids, sampling nibbles, and quantization table selectors, then an SOS segment that maps the frame components to entropy tables. Component sampling factors are stored as horizontal and vertical nibbles; stb_image computes maximum sampling factors and integer resampling ratios from those descriptors before color conversion. Coherent entropy-coded scan data is still required for the load path to reach resampling.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
