---
type: causal-policy
title: Raw Disassembler Buffer With Trailer Selector Parser Reached Disassembler Table Boundary Read Verified Recovery
description: Server-verified recovery for raw-disassembler-buffer-with-trailer-selector when wrong_sink pairs with parser_reached_disassembler_table_boundary_read.
failure_class: wrong_sink
verifier_signal: parser_reached_disassembler_table_boundary_read
candidate_family: construct
input_format: raw-disassembler-buffer-with-trailer-selector
harness_convention: libfuzzer-binutils-disassembler
vuln_class: global-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: high
tags: [wrong-sink, parser-reached-disassembler-table-boundary-read, raw-disassembler-buffer-with-trailer-selector, libfuzzer-binutils-disassembler, construct, global-buffer-overflow-read, verified-recovery]
match_keys: [wrong-sink, parser-reached-disassembler-table-boundary-read, raw-disassembler-buffer-with-trailer-selector, libfuzzer-binutils-disassembler, construct, global-buffer-overflow-read, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a raw-disassembler-buffer-with-trailer-selector candidate reaches `parser_reached_disassembler_table_boundary_read` under `wrong_sink`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer-binutils-disassembler]]` and format contract `[[raw-disassembler-buffer-with-trailer-selector]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Build the binutils disassembler fuzzer frame with a tiny instruction payload followed by the harness trailer selecting the XGATE disassembler. Choose an instruction shape that enters the DYA operand decoder; the vulnerable decoder uses the global opcode-table cursor instead of the selected opcode descriptor, so operand bit extraction reads past the table boundary.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: construct.
