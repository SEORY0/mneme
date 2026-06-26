---
type: harness-contract
title: "Afl File harness"
description: "Input contract facts for Afl File."
tags: ["afl-file", "round-6"]
okf_support: 2
---
# Afl File Harness

## Round 6 Input Contract
- The AFL-style harness consumes a fixed-width option word from the front of the file, then parses the remaining bytes as HTML. The push parser feeds bounded chunks, so the useful trigger likely depends on chunk-boundary state plus an input-buffer error.
- The AFL-style harness writes the raw input to a temporary file and invokes objcopy on that file. BFD must recognize the object as PEF, expose a code section, and cause objcopy to request symbols before the traceback parser is exercised.

## Format Links
- [[html]]
- [[pef-object]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
