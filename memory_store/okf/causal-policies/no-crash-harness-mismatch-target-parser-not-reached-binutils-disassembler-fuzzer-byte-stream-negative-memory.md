---
type: causal-policy
title: "No Crash Harness Mismatch Target Parser Not Reached Binutils Disassembler Fuzzer Byte Stream Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal harness_mismatch_target_parser_not_reached."
failure_class: "no_crash"
verifier_signal: "harness_mismatch_target_parser_not_reached"
candidate_family: "analysis_only"
input_format: "binutils disassembler fuzzer byte stream"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "harness-mismatch-target-parser-not-reached", "binutils-disassembler-fuzzer-byte-stream", "negative-memory", "round-9"]
match_keys: ["no_crash", "harness_mismatch_target_parser_not_reached", "binutils disassembler fuzzer byte stream", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Harness Mismatch Target Parser Not Reached Binutils Disassembler Fuzzer Byte Stream Negative Memory

- key: `no_crash x harness_mismatch_target_parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[binutils-disassembler-fuzzer-byte-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- The task description names corrupt sysroff parsing in sysdump/getCHARS, but the generated run
  command is the i386 extended disassembler fuzzer.
- The inspected harness does not open a sysroff object or call sysdump; it consumes option/private-
  data prefixes and disassembles the remaining bytes.
- No credible sysroff path was reachable through this wrapper within the worker budget.

## Policy
Treat `no_crash x harness_mismatch_target_parser_not_reached` on `binutils disassembler fuzzer byte stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The active input format is not a sysroff file for this run.
- It is a disassembler byte stream with leading option bytes, leading private-data bytes, and a
  remaining instruction buffer.
- The sysroff format itself was not exercised by the selected wrapper.

## Harness Contract
- The fuzz_disas_ext harness rejects small inputs, copies fixed-size leading regions into
  disassembler option and private-data buffers, then disassembles the remaining raw bytes twice with
  big- and little-endian settings for the configured architecture.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `harness_mismatch_target_parser_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
