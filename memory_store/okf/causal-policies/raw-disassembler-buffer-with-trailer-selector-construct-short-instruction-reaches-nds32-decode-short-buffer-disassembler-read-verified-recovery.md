---
type: causal-policy
title: Raw Disassembler Buffer With Trailer Selector Short Instruction Reaches Nds32 Decode Verified Recovery
description: Server-verified recovery for raw-disassembler-buffer-with-trailer-selector when generic_crash pairs with short_instruction_reaches_nds32_decode.
failure_class: generic_crash
verifier_signal: short_instruction_reaches_nds32_decode
candidate_family: construct
input_format: raw-disassembler-buffer-with-trailer-selector
harness_convention: libfuzzer-binutils-disassembler
vuln_class: short-buffer-disassembler-read
access_scope: generate
success_count: 1
confidence: high
tags: [generic-crash, short-instruction-reaches-nds32-decode, raw-disassembler-buffer-with-trailer-selector, libfuzzer-binutils-disassembler, construct, short-buffer-disassembler-read, verified-recovery]
match_keys: [generic-crash, short-instruction-reaches-nds32-decode, raw-disassembler-buffer-with-trailer-selector, libfuzzer-binutils-disassembler, construct, short-buffer-disassembler-read, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a raw-disassembler-buffer-with-trailer-selector candidate reaches `short_instruction_reaches_nds32_decode` under `generic_crash`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer-binutils-disassembler]]` and format contract `[[raw-disassembler-buffer-with-trailer-selector]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Build the disassembler fuzzer frame so the trailer selects NDS32 and the instruction payload ends with only a short instruction-sized fragment. The vulnerable path still enters machinery that expects a wider instruction buffer at the end of input, while the fixed build treats the short tail as non-decodable and exits cleanly.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: construct.
