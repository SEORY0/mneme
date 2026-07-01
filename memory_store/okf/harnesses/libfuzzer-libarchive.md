---
type: harness-contract
title: "Libfuzzer Libarchive harness"
description: "Input contract facts for libfuzzer-libarchive."
tags: ["libfuzzer-libarchive"]
okf_support: 1
---
# Libfuzzer Libarchive Harness

## Round 10 Input Contract
- The libarchive fuzzer feeds the raw input as an archive byte stream with all read formats enabled. A candidate must be a whole ISO image; the parser performs archive format detection before reaching ISO directory traversal.

## Round 10 Format Links
- [[iso9660]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 32 Input Contract
- The libarchive fuzzer provides the entire PoC as one in-memory archive stream through archive_read_open with all filters and formats enabled. There is no leading selector and no FuzzedDataProvider layout. The harness repeatedly calls archive_read_next_header and archive_read_data, so a candidate must be a whole archive that passes format detection and reaches member data decompression; mutating only the compressed data after valid RAR5 headers preserves this contract.

## Round 32 Format Links
- [[rar5]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
