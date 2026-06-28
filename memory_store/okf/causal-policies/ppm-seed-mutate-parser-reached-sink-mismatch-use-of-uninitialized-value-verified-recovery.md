---
type: causal-policy
title: "Ppm Seed Mutate Parser Reached Sink Mismatch Use Of Uninitialized Value Verified Recovery"
description: "Round 22 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "seed_mutate"
input_format: "ppm"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-sink-mismatch", "ppm", "libfuzzer", "seed-mutate", "verified-recovery", "round-22"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch", "ppm", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 22
---
# Ppm Seed Mutate Parser Reached Sink Mismatch Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ppm]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a real high-bit-depth PPM seed that the image loader accepts as a 12-bit source image. The compression loop allocates the destination buffer with the general allocator for no-reallocation test cases and then touches the compressed output. In the vulnerable build, the destination buffer contains uninitialized bytes visible to MemorySanitizer; the fixed build uses the intended allocation or zeroing behavior.

## Policy
For `wrong_sink x parser_reached_sink_mismatch` on `ppm`, preserve the parser and harness gates first, then change the causal invariant identified by the verified recovery. Prefer `seed_mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `ppm` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `ppm` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 22 solve after 2 attempts.
- Scope: generator repair only.
