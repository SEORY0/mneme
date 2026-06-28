---
type: harness-contract
title: "Afl Libfuzzer File Harness"
description: "Input contract facts for afl-libfuzzer-file."
tags: ["afl-libfuzzer-file", "harness-contract", "round-19"]
okf_support: 0
train_only: true
---

# Afl Libfuzzer File Harness

## Round 19 Input Contract

- The libarchive fuzzer reads the raw input bytes as an archive file, enables all filters and formats, iterates entries, and drains entry data. There is no mode byte or FuzzedDataProvider carving; success depends on the archive parser accepting the RAR5 envelope and the file-data reader entering decompression.
- Format link: [[rar5-archive]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 22 Input Contract
- The harness counts file descriptors before and after each run and aborts on leaks. NCP mode creates a socketpair, passes one side to MainLoop as the NCP socket, writes selected bytes to the other side, and pumps the event loop between writes. Config mode writes the remaining bytes to a temporary file and calls fread_config before constructing MainLoop.
- The AFL-style wrapper feeds raw bytes to LJpegDecompressorFuzzer. The harness creates a RawImage from the front fields, allocates image data, constructs an LJpeg decompressor over the remaining ByteStream, and catches RawSpeed exceptions. Parser reachability therefore requires valid front fields plus enough LJpeg syntax for decode to write pixels.

## Format Links
- [[rawspeed-ljpeg-fuzzer-struct]]
- [[wpantund-fuzz]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
