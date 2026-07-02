---
type: "negative-memory"
title: "Jpeg2000 J2k Seed Mutate Construct Wrong Sink Target Path Crashes But Fixed Also Crashes Heap Buffer Overflow Read Negative Memory"
description: "Round 38 negative memory for wrong_sink with verifier signal target_path_crashes_but_fixed_also_crashes."
failure_class: "wrong_sink"
verifier_signal: "target_path_crashes_but_fixed_also_crashes"
candidate_family: "seed_mutate|construct"
input_format: "jpeg2000-j2k"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["wrong-sink", "target-path-crashes-but-fixed-also-crashes", "jpeg2000-j2k", "libfuzzer", "seed-mutate-construct", "heap-buffer-overflow-read", "negative-memory", "round-38"]
match_keys: ["wrong_sink", "target_path_crashes_but_fixed_also_crashes", "jpeg2000-j2k", "libfuzzer", "heap-buffer-overflow-read", "negative-memory", "seed_mutate|construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Jpeg2000 J2k Seed Mutate Construct Wrong Sink Target Path Crashes But Fixed Also Crashes Heap Buffer Overflow Read Negative Memory

- key: `wrong_sink x target_path_crashes_but_fixed_also_crashes`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg2000-j2k]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A valid custom-MCT codestream with a later subsampled component reached opj_mct_decode_custom and produced a heap-buffer-overflow read, but the official fixed build crashed as well, so this was outside the intended benchmark target. Header-only component-count, sampling, and standard-MCT mutations decoded cleanly or were rejected before the vulnerable transform.

## Observed Basin
- Failure trajectory classes: no_crash, wrong_sink.
- Official confirmation: no server target match for this basin.

## Policy
Treat `wrong_sink x target_path_crashes_but_fixed_also_crashes` on `[[jpeg2000-j2k]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `target_path_crashes_but_fixed_also_crashes` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `target_path_crashes_but_fixed_also_crashes`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 17 attempts.
- Candidate family: seed_mutate|construct.
- Scope: generator repair and basin avoidance only.
