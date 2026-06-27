---
type: harness-contract
title: "Afl File Wrapper harness"
description: "Round 8 input contract facts for afl-file-wrapper."
tags: ["afl-file-wrapper", "round-8"]
okf_support: 4
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

## Round 15 Input Contract
- The AFL-style wrapper feeds the PoC file bytes to fuzz_process_packet. The fuzzer initializes nDPI
  once, clears flow/source/destination state per input, and calls ndpi_detection_process_packet with
  the raw buffer.
- The /bin/arvo wrapper invokes the affix/dictionary fuzzer on the PoC file path. The target writes
  temporary word, affix, and dictionary files, constructs a Hunspell instance from them, and calls
  spell followed by suggest if the word is not accepted.

## Format Links
- [[hunspell-aff-dic-word-triple]]
- [[ipv4-udp-kerberos-packet]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
