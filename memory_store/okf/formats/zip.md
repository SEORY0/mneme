---
type: format-family
title: ZIP archive format
description: Format contract for importers that enumerate ZIP members before parsing embedded content.
resource: cybergym://format/zip
tags: [zip, archive, member_name]
timestamp: 2026-06-26T00:00:00Z
okf_support: 2
train_only: true
---
# Schema
## Structure
ZIP carriers require consistent local headers and central-directory entries. For importer bugs, include at least one member body that looks plausible to the downstream importer.

## Invariants
- Archive enumeration must succeed before member-name bugs are reachable.
- Long member filenames are a separate mutation surface from archive structure.
- Empty archives and corrupted directories rarely reach importer-specific code.

## Round 14 Factual Contract

### Schema / Invariants
- The useful envelope is a ZIP/CBZ-style archive with local file header, central directory, and end directory records. The entry name must look like a supported page resource so page enumeration opens it; compressed and uncompressed sizes can be inconsistent with the actual compressed payload.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 18 Factual Contract

### Schema / Invariants
- A ZIP archive is located from its end-of-central-directory record, which declares central-directory size, central-directory position, entry counts, and optional comment. The central directory then describes per-file metadata and points back to local file headers. This bug class depends on a mismatch between where the end record is found and where the central directory claims to begin, while still satisfying coarse archive-size bounds.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- A ZIP archive needs local file headers, central-directory entries, and an end-of-central-directory record with mutually consistent names, sizes, compression method, CRC, and central-directory accounting. Duplicate central entries may point at one local member, and deflated members are accepted when the header metadata agrees with the compressed stream.

### Harness Links
- [[libfuzzer-miniz-zip-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 25 Factual Contract

### Schema / Invariants
- ZIP readers locate the EOCD by scanning backward, then read central-directory size, central-directory offset, entry count, and per-file central-directory headers. Central-directory entries include file metadata and a local-header offset; local headers are validated before extraction.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
## Round 37 Factual Contract

### Schema / Invariants
- The accepted envelope is a complete ZIP archive: local member header, central-directory entries, and an end record with coherent member counts, directory size, directory position, compression method, sizes, names, and CRC.
- Central entries may be made to point at one local member, but that can become over-broad.
- Validation compares local and central names and checks decompressed CRC; extraction can still be attempted by the fuzzer after validation failures.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
