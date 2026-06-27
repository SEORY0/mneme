---
type: format-family
title: Selinux Compiled Fcontext Fuzzer format
description: Format contract for selinux-compiled-fcontext-fuzzer inputs.
resource: cybergym://format/selinux-compiled-fcontext-fuzzer
tags: [selinux-compiled-fcontext-fuzzer, uninitialized-size-or-state, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The compiled SELinux file-context fuzzer uses a control prefix and separator-delimited data regions. For the compiled target, the main data segment must resemble the binary compiled fcontext representation rather than the plain-text file-context syntax; trailing separated regions supply lookup or auxiliary data.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-selabel-file-compiled]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
