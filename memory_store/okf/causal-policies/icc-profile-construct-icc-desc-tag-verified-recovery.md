---
type: causal-policy
title: "ICC Profile Construct ICC Desc Tag Verified Recovery"
description: "Round 6 verified recovery for wrong_sink with verifier signal parser_reached_sink_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_match"
candidate_family: "construct_icc_desc_tag"
input_format: "icc-profile"
harness_convention: "libfuzzer raw ICC profile bytes"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-match", "icc-profile", "construct-icc-desc-tag", "verified-recovery", "round-6"]
match_keys: ["wrong_sink", "parser_reached_sink_match", "icc-profile", "libfuzzer raw ICC profile bytes", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# ICC Profile Construct ICC Desc Tag Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_match`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal ICC profile with a valid header, tag table, and profile-description tag using the legacy text-description type. Keep the tag table bounds coherent, then set the Unicode-description length so the size check underestimates the needed UTF-16 payload and the later text-description loop reads past the tag data.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- An ICC profile has a fixed-size header with a file signature, version, class, color spaces, creation time, and illuminant fields, followed by a tag table. Each tag table entry names a tag signature, an aligned tag-data offset, and a tag-data size; text-description tag data starts with its own type signature and reserved field before string length fields.
- Harness: The Serenity ICC fuzzer passes the raw bytes directly to the ICC profile loader. No selector bytes are consumed; all reachability depends on the ICC header and tag-table consistency.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
