---
type: harness-contract
title: "Libfuzzer File Fuzzipp harness"
description: "Input contract facts for libfuzzer-file-fuzzipp."
tags: ["libfuzzer-file-fuzzipp", "round-28"]
okf_support: 0
---
# Libfuzzer File Fuzzipp Harness

## Round 28 Input Contract

- The harness writes the fuzz input bytes directly to a temporary file and passes that file to the libcups IPP fuzzer. There is no leading selector byte, archive wrapper, or FuzzedDataProvider carving. The fuzzer reads the file with ippReadIO, then resets the parsed request state and writes it back with ippWriteIO, so parser-accepted inconsistent attributes can crash during either read-side string handling or later serialization.

## Round 28 Format Links
- [[ipp]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
