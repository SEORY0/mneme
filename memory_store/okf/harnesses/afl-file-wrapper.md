---
type: harness-contract
title: "Afl File Wrapper harness"
description: "Round 8 input contract facts for afl-file-wrapper."
tags: ["afl-file-wrapper", "round-8"]
okf_support: 2
---
# Afl File Wrapper Harness

## Round 8 Input Contract
- The AFL-style file wrapper passes the entire file to the OpenJPEG J2K decompression fuzzer. It reads the header, bounds the decode area, and then decodes; no leading selector byte or separate metadata file is used.
- The AFL-style wrapper passes the whole file to the curl fuzzer, which parses TLVs from the front and configures a mocked socket manager. No FuzzedDataProvider back-loading is used; response ordering and protocol phase determine whether a response slot is consumed.

## Round 8 Format Links
- [[curl-fuzzer-tlv]]
- [[jpeg2000-j2k]]

## Round 8 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

