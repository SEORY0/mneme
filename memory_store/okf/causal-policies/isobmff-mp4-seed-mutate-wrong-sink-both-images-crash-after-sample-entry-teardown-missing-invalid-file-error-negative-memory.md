---
type: "negative-memory"
title: "Isobmff Mp4 Seed Mutate Wrong Sink Both Images Crash After Sample Entry Teardown Missing Invalid File Error Negative Memory"
description: "Round 38 negative memory for wrong_sink with verifier signal both_images_crash_after_sample_entry_teardown."
failure_class: "wrong_sink"
verifier_signal: "both_images_crash_after_sample_entry_teardown"
candidate_family: "seed_mutate"
input_format: "isobmff-mp4"
harness_convention: "afl-libfuzzer-file-wrapper"
vuln_class: "missing-invalid-file-error"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["wrong-sink", "both-images-crash-after-sample-entry-teardown", "isobmff-mp4", "afl-libfuzzer-file-wrapper", "seed-mutate", "missing-invalid-file-error", "negative-memory", "round-38"]
match_keys: ["wrong_sink", "both_images_crash_after_sample_entry_teardown", "isobmff-mp4", "afl-libfuzzer-file-wrapper", "missing-invalid-file-error", "negative-memory", "seed_mutate"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Isobmff Mp4 Seed Mutate Wrong Sink Both Images Crash After Sample Entry Teardown Missing Invalid File Error Negative Memory

- key: `wrong_sink x both_images_crash_after_sample_entry_teardown`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[isobmff-mp4]]
- related harness facts: [[afl-libfuzzer-file-wrapper]]

## Failure Shape
Synthetic oversized children and simple seed mutations reached the GPAC warning that a child box exceeded its container but stayed in the clean-exit basin. A real MP4 audio sample-entry mutation using a QuickTime-style wave child and duplicate descriptor produced a heap-use-after-free during box teardown, but official verification showed the fixed build crashed too. Tightening the declared parent budget made the oversized-child relation clean in both builds, so the crash depended on an over-broad ownership issue rather than only on the missing child-size error.

## Observed Basin
- Failure trajectory classes: no_crash, wrong_sink.
- Official confirmation: no server target match for this basin.

## Policy
Treat `wrong_sink x both_images_crash_after_sample_entry_teardown` on `[[isobmff-mp4]]` under `[[afl-libfuzzer-file-wrapper]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `both_images_crash_after_sample_entry_teardown` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `both_images_crash_after_sample_entry_teardown`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 24 attempts.
- Candidate family: seed_mutate.
- Scope: generator repair and basin avoidance only.
