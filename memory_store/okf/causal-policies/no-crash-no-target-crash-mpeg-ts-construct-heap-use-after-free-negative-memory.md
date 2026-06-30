---
type: negative-memory
title: "No Crash No Target Crash Mpeg Ts Negative Memory"
description: "Round 28 negative memory for no_crash with verifier signal no_target_crash."
failure_class: "no_crash"
verifier_signal: "no_target_crash"
candidate_family: "construct"
input_format: "mpeg-ts"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "no-target-crash", "mpeg-ts", "libfuzzer", "construct", "heap-use-after-free", "negative-memory", "round-28"]
match_keys: ["no_crash", "no_target_crash", "mpeg-ts", "libfuzzer", "heap-use-after-free", "negative_memory", "construct", "use-after-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 28
---
# No Crash No Target Crash Mpeg Ts Negative Memory

- key: `no_crash x no_target_crash`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[mpeg-ts]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Valid-looking MPEG-TS carriers with PAT and PMT sections were accepted cleanly but did not expose the gf_m2ts_es_del use-after-free. Distinct hypotheses covered a plain PMT update that changes an elementary stream declaration, PCR-reuse before update, PES-to-section and section-to-PES replacement, shared elementary PID across programs, shared PID plus PCR aliasing, redeclaring the PCR alias as an ES, repeated PMT updates around the alias, a packet after shared-PID update, and duplicate elementary PID entries inside an update PMT. The missing condition is likely a more specific stale-reference relation around demuxer ownership or an event/flush path not reached by these compact probe streams.

## Policy
For `no_crash x no_target_crash` on `mpeg-ts`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Treat `construct` as useful only if it changes the missing gate, state relation, or sink path.

## Procedure
1. When this failure key repeats, preserve only the descriptive reachability facts and retarget the missing invariant before another official submission.
2. Do not spend attempts on candidates that are clean, rejected before the target path, fixed-build-crashing, or wrapper-only reproductions in this same shape.
3. Prefer a different construction family or a deeper harness/format contract when the verifier signal repeats without new parser-depth evidence.

## Format Contract
- Format [[mpeg-ts]]: MPEG-TS input is packetized with sync-marked fixed-size packets. PAT sections map programs to PMT packet IDs, and PMT sections declare a PCR carrier plus elementary streams with stream type, elementary PID, and descriptor length. PMT version changes are needed for the demuxer to treat a later table as an update rather than a repeat.
- Harness [[libfuzzer]]: The libFuzzer target writes the raw input bytes to a temporary file and calls the GPAC MPEG-TS probe routine. The probe reads raw file bytes, synchronizes on transport packets, processes PAT and PMT sections through the demuxer, then destroys the demuxer; there is no leading mode selector and no FuzzedDataProvider split.

## Negative Memory
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.
- Preserve descriptive format and harness facts separately from this causal negative policy.

## Evidence Shape
- Support: one diagnosed round-28 persistent failure.
- Scope: generator repair and retargeting only.
