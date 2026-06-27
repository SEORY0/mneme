---
type: harness-contract
title: "Honggfuzz File harness"
description: "Input contract facts for honggfuzz-file."
tags: ["honggfuzz-file", "round-9"]
okf_support: 4
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
