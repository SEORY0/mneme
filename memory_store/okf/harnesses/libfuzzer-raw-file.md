---
type: harness-contract
title: "Libfuzzer Raw File harness"
description: "Input contract facts for libfuzzer-raw-file."
tags: ["libfuzzer-raw-file", "round-28"]
okf_support: 0
---
# Libfuzzer Raw File Harness

## Round 28 Input Contract

- libFuzzer bytes are written unchanged to a temporary file. The harness only requires a small minimum size, opens the file as binary input, initializes the sudoers parser, and calls the LDIF parser directly. There is no FuzzedDataProvider layout, checksum, command-line argument, or additional envelope.
- The libFuzzer wrapper writes the raw input bytes unchanged to a temporary file and drives the objdump display path with section contents, headers, private headers, debug sections, stabs, and disassembly enabled. There is no FuzzedDataProvider layout, checksum, mode selector, or extra envelope. BFD determines the object flavor from the raw file, and the objdump configuration avoids global decompression when raw section-content dumping is enabled.
- The libFuzzer harness writes the raw input bytes unchanged to a temporary file, then calls the libdwarf path-based initialization routines on that file and finishes any returned debug handle. There is no FuzzedDataProvider split, mode-selector byte, checksum, or secondary container. The detector requires enough raw bytes to pass its minimum object-size check before the universal-object header parser is reached.

## Round 28 Format Links
- [[bfd-object]]
- [[ldif]]
- [[mach-o-universal]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
