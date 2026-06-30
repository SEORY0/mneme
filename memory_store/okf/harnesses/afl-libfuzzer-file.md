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

## Round 23 Input Contract
- The harness runs an AFL/libFuzzer-compatible image decoder on the raw file bytes; there is no fuzzer-side selector or length prefix.
- The TiffDecoderFuzzer-DngDecoder target reads raw file bytes from the input file/stdin using an AFL-compatible driver. There is no mode selector, but an empty file trips a harness assertion rather than the target vulnerability.
- The GPAC fuzz_parse harness writes raw bytes to a temporary file and calls the ISO media file opener. There is no mode byte or length prefix. Reaching the gzip helper requires a valid-enough top-level compressed box recognized by the ISO box parser.

## Round 23 Format Links
- [[dng-tiff]]
- [[isobmff-compressed-box]]
- [[tga]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 28 Input Contract

- The harness reads the raw file bytes as one ByteStream. There is no prefix selector or FuzzedDataProvider split. It creates a RawImage from the front scalar fields, reads tile offset and flag fields, allocates image data, constructs LJpegDecompressor over the remaining bytes, and catches RawSpeed exceptions, so clean exits usually mean a parser gate or slice-write relation was not reached.
- The NCP-input harness creates a socketpair, configures wpantund to use one descriptor as the NCP socket, then writes remaining fuzz bytes one at a time through the other descriptor while pumping MainLoop. A special command byte in the byte stream can wait for outbound frames or fast-forward simulated time. The selector for NCP mode is required before any HDLC data; the control-interface selector is a stub.

## Round 28 Format Links
- [[rawspeed-ljpeg-fuzzer-struct]]
- [[wpantund-fuzz]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
