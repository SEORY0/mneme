---
type: causal-policy
title: "Lossless JPEG Construct Parser Reached Scaled Lossless Decode Overrun Heap Buffer Overflow Write Verified Recovery"
description: "Round 19 verified recovery for wrong_sink with verifier signal parser_reached_scaled_lossless_decode_overrun."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_scaled_lossless_decode_overrun"
candidate_family: "construct"
input_format: "lossless-jpeg"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-scaled-lossless-decode-overrun", "lossless-jpeg", "libfuzzer", "construct", "verified-recovery", "round-19"]
match_keys: ["wrong-sink", "parser-reached-scaled-lossless-decode-overrun", "lossless-jpeg", "libfuzzer", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 19
---
# Lossless JPEG Construct Parser Reached Scaled Lossless Decode Overrun Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_scaled_lossless_decode_overrun`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[lossless-jpeg]]
- harnesses: [[libfuzzer]]

## Failure Shape
Create a valid small lossless JPEG using the project compressor, not a hand-assembled partial JPEG. The decompression fuzzer reads the header, accepts the dimensions, and then requests scaled decompression on its second pixel-format pass. The vulnerable build allocates for the scaled dimensions even though lossless JPEG output is not actually scaled, so decode writes past the destination buffer; the fixed build detects the lossless case and avoids the undersized allocation.

## Policy
For `wrong_sink x parser_reached_scaled_lossless_decode_overrun` on `lossless-jpeg`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `lossless-jpeg` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `lossless-jpeg` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 19 solve.
- Scope: generator repair only.
