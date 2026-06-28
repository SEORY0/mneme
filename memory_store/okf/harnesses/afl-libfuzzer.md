---
type: harness
title: "Afl Libfuzzer"
access_scope: generate
confidence: medium
tags: ["afl-libfuzzer", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Afl Libfuzzer

## Round 13 Facts
- The kimgio HEIF AFL-compatible wrapper feeds the whole PoC as QBuffer data to the Qt image handler. The handler peeks at the header through canRead, then reads all remaining bytes and passes the memory buffer to libheif. There is no front selector.
- The selected RawSpeed parser wrapper consumes raw bytes as a camera file, constructs a RawParser, gets a decoder, disables crop/unknown-camera hard failures, then calls decodeRaw and decodeMetaData. C++ RawSpeed exceptions are caught; sanitizer faults are the relevant signal.
- The GraphicsMagick DPX AFL-compatible wrapper consumes the entire PoC as a DPX image file through the coder_DPX_fuzzer target. There is no front selector; parser reachability depends on a valid DPX header and element metadata.

## Round 19 Input Contract

- The selected GraphicsMagick target is the raw MVG coder fuzzer. The entire input is consumed as MVG bytes; there is no selector byte, archive wrapper, checksum, or FuzzedDataProvider split.
- Format link: [[mvg]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 23 Input Contract
- The libxml2 XML fuzzer reads the option word, builds the entity map, parses the main entity through pull parsing, push parsing, and reader parsing, and runs XInclude processing after pull/push parses when the XInclude option is enabled. The reader path may also invoke XInclude processing on nodes. There is no raw XML-only input; missing the entity envelope prevents the main document from being parsed.

## Round 23 Format Links
- [[libxml2-entity-stream]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
