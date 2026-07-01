---
type: format-family
title: Libredwg Json format
description: Format contract for libredwg-json inputs.
resource: cybergym://format/libredwg-json
tags: [libredwg-json, stack-buffer-overflow-read, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
LibreDWG JSON accepts a top-level object with a HEADER member. Header keys map to dynamic metadata entries, and primitive numeric values are converted by the JSON importer before being assigned through the dynamic API. Unknown or late fields can stop progress, so a compact set of known primitive header names is preferable.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.

## Round 29 Factual Contract

### Schema / Invariants
- libredwg's JSON input is a top-level object with section objects. FILEHEADER metadata controls the DWG version used by later sections, and HEADER keys are looked up through dynapi metadata. For pre-R13 versions, selected header string variables are handled as fixed TFv strings even though the JSON token is ordinary text.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- LibreDWG JSON is a top-level object whose recognized section keys include FILEHEADER and HEADER. Unknown top-level keys are rejected, while HEADER member names are looked up through dynapi metadata. String values containing backslashes are copied through json_string and then converted by the legacy TV converter; malformed escape structure can affect converter source reads. Compact known section/member structure is enough; no filename or external extension gate is needed.
- The harness chooses JSON when the first byte is an object opener. LibreDWG JSON is a top-level object whose recognized sections include metadata keys, HEADER, CLASSES, OBJECTS, and other named sections. json_string only calls the UTF-8-to-TV converter when the JSON token contains a backslash escape; otherwise it copies the token normally. CLASSES entries have string fields for class names and mandatory numeric identity fields. OBJECTS entries require an object or entity name, type, and handle before object-specific fields such as dictionary item text are accepted.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
