---
type: causal-policy
title: "Binutils Disassembler Frame Construct Parser Reached Sink Match Use Of Uninitialized Value Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_sink_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_match"
candidate_family: "construct"
input_format: "binutils-disassembler-frame"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-match", "binutils-disassembler-frame", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_sink_match", "binutils-disassembler-frame", "libfuzzer", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Binutils Disassembler Frame Construct Parser Reached Sink Match Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_sink_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[binutils-disassembler-frame]]
- harnesses: [[libfuzzer]]

## Failure Shape
Construct the disassembler fuzzer frame rather than an object file. Select an i386-family machine mode and options that force 16-bit addressing, then place a VEX/VSIB gather-style instruction whose ModRM addressing form is not a real SIB form in that mode. The decoder reaches the VSIB operand path without get_sib having populated SIB state, and OP_VEX consumes the uninitialized SIB index; the fixed build tracks whether SIB data is present before using it.

## Policy
For `wrong_sink x parser_reached_sink_match` on `binutils-disassembler-frame`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `binutils-disassembler-frame` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `binutils-disassembler-frame` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
This harness input is a disassembler-control frame: leading bytes form the disassembler option string, another leading region is copied as target-private data, the middle region is the instruction stream, and trailing control bytes select flavour, chunking, and machine mode. It does not parse ELF, PE, or any other binary container.

## Harness Contract
The specialized i386 disassembly fuzzer copies the option and private-data regions first, then invokes the i386 disassembler twice over the remaining instruction buffer with both endian settings. Integral control fields are read from the back of the frame in little-endian form; no FuzzedDataProvider is used.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 2 attempts.
- Scope: generator repair and retargeting only.
