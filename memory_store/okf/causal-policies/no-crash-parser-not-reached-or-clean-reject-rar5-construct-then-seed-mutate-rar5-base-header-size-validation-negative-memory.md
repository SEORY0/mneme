---
type: negative-memory
title: "No Crash Parser Not Reached Or Clean Reject Rar5 Negative Memory"
description: "Round 28 negative memory for no_crash with verifier signal parser_not_reached_or_clean_reject."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_clean_reject"
candidate_family: "construct_then_seed_mutate"
input_format: "rar5"
harness_convention: "libfuzzer"
vuln_class: "rar5-base-header-size-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-clean-reject", "rar5", "libfuzzer", "construct-then-seed-mutate", "rar5-base-header-size-validation", "negative-memory", "round-28"]
match_keys: ["no_crash", "parser_not_reached_or_clean_reject", "rar5", "libfuzzer", "rar5-base-header-size-validation", "negative_memory", "construct", "seed-mutate", "other"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 28
---
# No Crash Parser Not Reached Or Clean Reject Rar5 Negative Memory

- key: `no_crash x parser_not_reached_or_clean_reject`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[rar5]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Constructed and seed-mutated archives satisfied the RAR5 marker and base-header checksum gate, including the invalid zero-sized base-block invariant, but the vulnerable reader returned cleanly or reported a non-crashing format error. Adding lookahead padding for the varint reader and mutating real RAR5 fixtures avoided early parser starvation, but did not produce an ASAN-visible target crash.

## Policy
For `no_crash x parser_not_reached_or_clean_reject` on `rar5`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Treat `construct_then_seed_mutate` as useful only if it changes the missing gate, state relation, or sink path.

## Procedure
1. When this failure key repeats, preserve only the descriptive reachability facts and retarget the missing invariant before another official submission.
2. Do not spend attempts on candidates that are clean, rejected before the target path, fixed-build-crashing, or wrapper-only reproductions in this same shape.
3. Prefer a different construction family or a deeper harness/format contract when the verifier signal repeats without new parser-depth evidence.

## Format Contract
- Format [[rar5]]: RAR5 archives begin with a fixed marker followed by CRC-protected base blocks. A base block carries a variable-length header-size field, then a header type and flags; file/service blocks may additionally carry extra-data and data-size varints before file metadata. The vulnerable path computes the checksum over only the declared header-size span, so a too-small declared span can leave later header fields outside the checksum-covered area.
- Harness [[libfuzzer]]: The libFuzzer harness feeds raw file bytes to libarchive from memory, enables all filters and formats, then repeatedly reads headers and drains entry data. There is no mode byte or FuzzedDataProvider framing. The RAR5 varint reader requires sufficient forward lookahead even when the encoded value itself is short.

## Negative Memory
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.
- Preserve descriptive format and harness facts separately from this causal negative policy.

## Evidence Shape
- Support: one diagnosed round-28 persistent failure.
- Scope: generator repair and retargeting only.
