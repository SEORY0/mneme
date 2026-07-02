---
type: format-family
title: "Rar Format"
description: "Round 26 descriptive structure and invariant facts for rar."
tags: ["rar", "round-26"]
okf_support: 2
train_only: true
---
# Rar Format

## Round 26 Factual Contract

### Schema / Invariants
- Old RAR archives begin with the RAR marker, a main header, then file headers whose header CRC is checked before data decoding. File headers carry dictionary flags, compressed and uncompressed sizes, method, name length, and filename before the compressed stream. RAR VM filters are encoded inside compressed data; the reader decodes filter flags, block start, block length, optional registers, bytecode, and optional global data, queues filters, and later executes queued filters over the LZSS window.

### Harness Links
- [[libfuzzer-libarchive-reader]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 33 Factual Contract

### Schema / Invariants
- Old RAR archives begin with the marker and main header, then CRC-checked block headers. File headers carry split-before/split-after flags, packed and unpacked sizes, compression method, name length/name, and then the packed stream. PPMd compressed blocks are selected inside the packed bitstream; a PPMd table can be allocated by flags in a new-code table, and later blocks may reuse that state if the stream marks a PPMd block without a dictionary allocation flag.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
