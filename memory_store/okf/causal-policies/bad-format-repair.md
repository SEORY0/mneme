---
type: causal-policy
title: Bad Format Repair Policy
description: Abstract generator policy for candidates rejected before parser reachability.
failure_class: bad_format
verifier_signal: parser_not_reached
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 6
confidence: medium
tags: [bad_format, parser_not_reached, construct, magic_gate, checksum_gate, parser_reachability]
match_keys: [bad_format, parser_not_reached, construct, magic_gate, checksum_gate, parser_reachability]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat pre-parser rejection as a shape failure, not as evidence about the target sink. Keep the
candidate small, rebuild the minimum valid envelope, and change only the field needed to pass the
earliest gate.

## Procedure
1. Re-read the harness entry path and identify the first parser API that must be reached.
2. Preserve the format prefix: magic, version, declared container count, and required terminator.
3. If a checksum or length gate exists before the parser, recompute it or choose a format branch
   where the gate is absent.
4. Validate parser reachability before adding the vulnerability trigger.
5. Only after reachability is stable, add one narrow invariant violation.

## Negative Memory
- Do not keep mutating payload fields when the verifier says the parser was not reached.
- Do not combine a bad prefix with a sink trigger; the prefix failure hides the causal signal.
- Overlarge whole-file growth is a trap when early size gates reject before decoding.

## Evidence Shape
- Support: 6 abstract train-set observations.
- Confidence: medium.
- Scope: generator repair only.
