---
type: causal-policy
title: "Binutils Disassembler Buffer With Trailer Selector Construct Parser Reached Sink Match Use Of Uninitialized Value Verified Recovery"
description: "Round 22 verified recovery for wrong_sink with verifier signal parser_reached_sink_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_match"
candidate_family: "construct"
input_format: "binutils-disassembler-buffer-with-trailer-selector"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-sink-match", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer", "construct", "verified-recovery", "round-22"]
match_keys: ["wrong-sink", "parser-reached-sink-match", "binutils-disassembler-buffer-with-trailer-selector", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 22
---
# Binutils Disassembler Buffer With Trailer Selector Construct Parser Reached Sink Match Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_sink_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[binutils-disassembler-buffer-with-trailer-selector]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the harness trailer to select the Z80 family backend in the extended addressing mode, and place a short instruction prefix that enters suffix decoding without supplying the bytes needed to initialize the temporary suffix buffer. The vulnerable backend then formats data derived from uninitialized stack contents, while the fixed backend returns cleanly.

## Policy
For `wrong_sink x parser_reached_sink_match` on `binutils-disassembler-buffer-with-trailer-selector`, preserve the parser and harness gates first, then change the causal invariant identified by the verified recovery. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `binutils-disassembler-buffer-with-trailer-selector` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `binutils-disassembler-buffer-with-trailer-selector` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 22 solve after 1 attempts.
- Scope: generator repair only.
