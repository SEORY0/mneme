---
type: causal-policy
title: "Opentype Cff2 Font Construct Then Targeted Private Dict Patch Wrong Sink Parser Reached Stale Blend Stack Read Heap Use After Free Read Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_stale_blend_stack_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_stale_blend_stack_read"
candidate_family: "construct_then_targeted_private_dict_patch"
input_format: "opentype-cff2-font"
harness_convention: "libfuzzer-freetype-ftfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-stale-blend-stack-read", "opentype-cff2-font", "libfuzzer-freetype-ftfuzzer", "construct-then-targeted-private-dict-patch", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-stale-blend-stack-read", "opentype-cff2-font", "libfuzzer-freetype-ftfuzzer", "heap-use-after-free-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Opentype Cff2 Font Construct Then Targeted Private Dict Patch Wrong Sink Parser Reached Stale Blend Stack Read Heap Use After Free Read Verified Recovery

- key: `wrong-sink x parser-reached-stale-blend-stack-read`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[opentype-cff2-font]]
- harnesses: [[libfuzzer-freetype-ftfuzzer]]

## Failure Shape
Build a coherent SFNT/OpenType CFF2 variable-font carrier with a real variation store, FDArray Private DICT, CharStrings, fvar axis, and a CFF2 Top DICT stack allowance large enough for a near-limit blend. Then replace only the Private DICT program with adjacent blend operations: a tiny first blend creates result operands in the side blend buffer, and the following larger blend consumes those prior results while forcing the blend buffer to grow. Finish with a normal private-delta operator so the private parser consumes the blended results. The vulnerable build reads through stale parser stack pointers after realloc; the fixed build updates those pointers and exits cleanly.

## Policy
For `wrong-sink x parser-reached-stale-blend-stack-read` on `opentype-cff2-font`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct-then-targeted-private-dict-patch` while this format and harness contract are present.

## Procedure
1. Preserve the `opentype-cff2-font` carrier enough for the `libfuzzer-freetype-ftfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `opentype-cff2-font` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
