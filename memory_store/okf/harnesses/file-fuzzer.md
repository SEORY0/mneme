---
type: harness-contract
title: "File Fuzzer harness"
description: "Input contract facts for file-fuzzer."
tags: ["file-fuzzer"]
okf_support: 0
---
# File Fuzzer Harness

## Round 10 Input Contract
- The verifier invokes the libmagic load-database fuzzer on the raw file as a magic rules file. It reports parser warnings for invalid rule syntax but accepts simple valid rules; there is no separate mode selector.
- The fuzz harness writes the raw bytes to a temporary object file and invokes the nm display path with symbol and line-number options enabled. There is no provider carving; BFD format recognition and object metadata drive all reachability.

## Round 10 Format Links
- [[ecoff-or-bfd-object]]
- [[libmagic-magic-database]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
