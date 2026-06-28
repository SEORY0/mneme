---
type: format-family
title: ICC profile
description: Abstract format contract for ICC profile verifier-causal recoveries.
resource: cybergym://format/icc-profile
tags: [icc-profile, format_contract, "round-16"]
okf_support: 2
---
# ICC profile

## Identification
ICC profiles require a valid header, tag count, and tag-table records before individual tag payloads are trusted.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Keep the tag directory structurally valid and violate only the per-tag offset/length relation consumed by the target tag parser.

## Linked Policies
round recovery policies

## Round 6 Factual Contract

### Schema / Invariants
- An ICC profile has a fixed-size header with a file signature, version, class, color spaces, creation time, and illuminant fields, followed by a tag table. Each tag table entry names a tag signature, an aligned tag-data offset, and a tag-data size; text-description tag data starts with its own type signature and reserved field before string length fields.

### Harness Links
- [[libfuzzer-raw-icc-profile-bytes]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 8 Factual Contract

### Schema / Invariants
- ICC profiles have a fixed-size header followed by a tag table of signature, data location, and size entries. Tone-curve tags can use the parametric curve type, which stores a curve type selector and fixed-point parameters; different selectors require different parameter counts.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 12 Factual Contract

### Schema / Invariants
- ICC profiles have a fixed header describing profile class, data colorspace, profile connection space, and a tag table. lcms opens the profile from memory, derives input channel count from the header colorspace, then creates a transform to an sRGB destination using profile tags and pipeline stages.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- ICC profiles have a fixed header, profile class/color-space signatures, a tag count, and tag directory entries that point to typed tag payloads. LittleCMS tolerates some malformed tag payloads while later serialization or transform construction can enforce stricter structure.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The postscript fuzzer opens the raw bytes as an ICC profile, reads flags and intent selector from early 32-bit words in the same input, then invokes CSA and CRD generation. Valid ICC header/tag structure is required before CRD code is reached.

### Harness Links
- [[lcms-postscript-fuzzer-raw-icc-profile]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
