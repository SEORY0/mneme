---
type: harness-contract
title: "Honggfuzz File harness"
description: "Input contract facts for honggfuzz-file."
tags: ["honggfuzz-file", "round-9"]
okf_support: 5
---
# Honggfuzz File Harness

## Round 9 Input Contract
- The selected wrapper runs the GIF loader on the file bytes directly.
- The input is a complete GIF byte stream; there is no fuzzer selector byte or outer container
  beyond the image format itself.
- The harness consumes a raw file front-to-back.
- It rejects short inputs, uses leading selector and option bytes to build parser configuration,
  consumes fixed-width strings only when their option bit is enabled, and passes the remaining bytes
  to flb_parser_do.
- The honggfuzz-style target copies the raw input into a NUL-terminated buffer, opens a fresh mruby
  VM, calls mrb_load_string on the buffer, closes the VM, and frees the buffer.
- There is no leading mode byte or secondary file format.
- The fuzzer writes the submitted bytes to a temporary file, opens it with BFD, accepts only
  recognized object files, and then calls the dwarf separate-debug-file path.
- In this image the wrapper accepts a file path but does not report parser reachability beyond clean
  execution.

## Round 9 Format Links
- [[fluent-bit-parser-fuzzer-control-plus-record]]
- [[gif]]
- [[mmo-object]]
- [[mruby-script]]

## Round 9 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 13 Facts
- The source fuzzer writes raw input to a temporary file, opens it with BFD auto-detection, and calls archive-format checking. The arvo image wrapper for this task appears to be honggfuzz-oriented and did not produce the normal one-input libFuzzer execution transcript.

## Round 24 Factual Contract

### Input Contract
- The harness copies the raw file bytes into a NUL-terminated string, opens a fresh mruby VM, calls the string loader, then closes the VM. There is no leading selector byte or structured fuzzer-provider layout.

### Format Links
- [[mruby-source]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 25 Input Contract
- The active target accepts a whole file as UART bytes for cli-uart-received-fuzzer under a honggfuzz-style wrapper. It initializes an OpenThread instance, passes copied bytes to the UART receive hook, then processes tasklets. There is no FuzzedDataProvider layout.
- The honggfuzz-style wrapper passes the entire file as bytes to fuzz-read-print-write. The harness copies data into an Exiv2 DataBuf and opens it as an image; no selector byte, or provider-carved layout is present.

## Round 25 Format Links
- [[openthread-cli-uart-or-ip6-message]]
- [[exiv2-image-metadata-container]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
