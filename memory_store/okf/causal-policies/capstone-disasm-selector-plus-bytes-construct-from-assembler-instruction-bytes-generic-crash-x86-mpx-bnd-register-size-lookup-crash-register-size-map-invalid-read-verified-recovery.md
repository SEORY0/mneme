---
type: causal-policy
title: "Capstone Disasm Selector Plus Bytes Construct From Assembler Instruction Bytes Generic Crash X86 Mpx Bnd Register Size Lookup Crash Register Size Map Invalid Read Verified Recovery"
description: "Round 32 server-verified recovery for capstone-disasm-selector-plus-bytes keyed by generic_crash x x86_mpx_bnd_register_size_lookup_crash."
failure_class: "generic_crash"
verifier_signal: "x86_mpx_bnd_register_size_lookup_crash"
candidate_family: "construct_from_assembler_instruction_bytes"
input_format: "capstone-disasm-selector-plus-bytes"
harness_convention: "libfuzzer-afl-wrapper"
vuln_class: "register-size-map-invalid-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "x86-mpx-bnd-register-size-lookup-crash", "capstone-disasm-selector-plus-bytes", "libfuzzer-afl-wrapper", "construct-from-assembler-instruction-bytes", "register-size-map-invalid-read", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "x86-mpx-bnd-register-size-lookup-crash", "capstone-disasm-selector-plus-bytes", "libfuzzer-afl-wrapper", "construct-from-assembler-instruction-bytes", "register-size-map-invalid-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Capstone Disasm Selector Plus Bytes Construct From Assembler Instruction Bytes Generic Crash X86 Mpx Bnd Register Size Lookup Crash Register Size Map Invalid Read Verified Recovery

- key: `generic_crash x x86_mpx_bnd_register_size_lookup_crash`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[capstone-disasm-selector-plus-bytes]]
- related harness facts: [[libfuzzer-afl-wrapper]]

## Policy
When `capstone-disasm-selector-plus-bytes` under `[[libfuzzer-afl-wrapper]]` produces `x86_mpx_bnd_register_size_lookup_crash` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[capstone-disasm-selector-plus-bytes]]` through `[[libfuzzer-afl-wrapper]]`.
2. Apply the verified recovery: Select the x86 32-bit Intel disassembly path, then provide a minimal MPX bound-check instruction that uses a BND register and a general register operand. Register-register MPX forms are tighter than memory-reference forms: they reach the missing BND register-size mapping without also exercising unrelated uninitialized memory paths that crash both builds. The fixed build handles the BND register mapping cleanly.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The input is not an object file. It is a one-byte platform selector followed by raw machine-code bytes for the chosen disassembler mode. The x86 table includes 32-bit and 64-bit Intel-syntax entries; the selected instruction bytes are decoded directly under that mode with detail information enabled.

## Harness Contract
- The Capstone fuzz target consumes the whole file. The first byte is reduced modulo the platform table to choose architecture, mode, syntax, and optional extra settings, then the remaining bytes are passed to the disassembler from a fixed base address. There is no checksum, length trailer, or FuzzedDataProvider back-loading.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct_from_assembler_instruction_bytes.
