---
type: causal-policy
title: "PDF Construct Parser Reached Sink Mismatch But Official Target Match Stack Buffer Overflow Write Verified Recovery"
description: "Round 20 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer-ghostscript-gstoraster"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "pdf", "libfuzzer-ghostscript-gstoraster", "construct", "verified-recovery", "round-20"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "pdf", "libfuzzer-ghostscript-gstoraster", "stack-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 20
---
# PDF Construct Parser Reached Sink Mismatch But Official Target Match Stack Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch_but_official_target_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pdf]]
- harnesses: [[libfuzzer-ghostscript-gstoraster]]

## Failure Shape
Build a minimal valid PDF that paints through an ExtGState soft mask. The soft mask references a transparency group and a transfer function whose shape produces more output components than the transparency-mask code expects. The invariant violated is that the transfer function used for mask setup must behave as a single-output function.

## Policy
For `wrong_sink x parser_reached_sink_mismatch_but_official_target_match` on `pdf`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `pdf` carrier enough for the `libfuzzer-ghostscript-gstoraster` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `pdf` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 20 solve.
- Scope: generator repair only.
