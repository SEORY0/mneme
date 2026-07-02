---
type: harness-contract
title: "Libfuzzer Afl File Wrapper harness"
description: "Round 8 input contract facts for libfuzzer-afl-file-wrapper."
tags: ["libfuzzer-afl-file-wrapper", "round-8"]
okf_support: 2
---
# Libfuzzer Afl File Wrapper Harness

## Round 8 Input Contract
- The fuzz target writes the raw input bytes to a temporary file and calls gf_isom_open_file in read-dump mode, then closes the movie if opening succeeds. The input is a complete file image; there is no selector byte or FuzzedDataProvider carving.

## Round 8 Format Links
- [[isobmff]]

## Round 8 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 32 Input Contract
- The fuzzer reads fields from the front with a ByteStream helper: parser options first, encoding string metadata next, and the rest as file contents. It calls xmlReaderForFile on the temporary file and then repeatedly calls xmlTextReaderRead, touching node type and value before freeing the text reader. There is no FuzzedDataProvider back-consumption pattern and no mode selector byte.

## Round 32 Format Links
- [[libxml2-reader-bytestream-xml]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
