---
type: negative-memory
title: "No Crash Off Target Both Image Crash Then Clean Universal Paths Mach O Universal Negative Memory"
description: "Round 28 negative memory for no_crash with verifier signal off_target_both_image_crash_then_clean_universal_paths."
failure_class: "no_crash"
verifier_signal: "off_target_both_image_crash_then_clean_universal_paths"
candidate_family: "construct+seed_mutate"
input_format: "mach-o-universal"
harness_convention: "libfuzzer-raw-file"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "off-target-both-image-crash-then-clean-universal-paths", "mach-o-universal", "libfuzzer-raw-file", "construct-seed-mutate", "heap-buffer-overflow-read", "negative-memory", "round-28"]
match_keys: ["no_crash", "off_target_both_image_crash_then_clean_universal_paths", "mach-o-universal", "libfuzzer-raw-file", "heap-buffer-overflow-read", "negative_memory", "construct", "seed-mutate", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 28
---
# No Crash Off Target Both Image Crash Then Clean Universal Paths Mach O Universal Negative Memory

- key: `no_crash x off_target_both_image_crash_then_clean_universal_paths`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[mach-o-universal]]
- harnesses: [[libfuzzer-raw-file]]

## Dead-End Shape
A constructed universal-object header reached the Mach-O universal detector and produced a heap read in the architecture-table handling path, but the official comparison showed the fixed image crashed too, so that candidate was over-broad rather than the target bug. Wrapping a real Mach-O seed in a valid universal envelope reached the parser cleanly, while truncated or inconsistent architecture-table relations either failed early with universal-object errors or completed without a crash.

## Policy
For `no_crash x off_target_both_image_crash_then_clean_universal_paths` on `mach-o-universal`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Treat `construct+seed_mutate` as useful only if it changes the missing gate, state relation, or sink path.

## Procedure
1. When this failure key repeats, preserve only the descriptive reachability facts and retarget the missing invariant before another official submission.
2. Do not spend attempts on candidates that are clean, rejected before the target path, fixed-build-crashing, or wrapper-only reproductions in this same shape.
3. Prefer a different construction family or a deeper harness/format contract when the verifier signal repeats without new parser-depth evidence.

## Format Contract
- Format [[mach-o-universal]]: Mach-O universal objects start with a fat header carrying an architecture count, followed by architecture records. The records are big-endian and describe embedded Mach-O slices by CPU metadata plus a file range. There are 32-bit and 64-bit architecture-record variants, and malformed table length or slice-range relations can be rejected before any embedded Mach-O slice is parsed. A standalone Mach-O seed can be used as the embedded slice when constructing a universal wrapper.
- Harness [[libfuzzer-raw-file]]: The libFuzzer harness writes the raw input bytes unchanged to a temporary file, then calls the libdwarf path-based initialization routines on that file and finishes any returned debug handle. There is no FuzzedDataProvider split, mode-selector byte, checksum, or secondary container. The detector requires enough raw bytes to pass its minimum object-size check before the universal-object header parser is reached.

## Negative Memory
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.
- Preserve descriptive format and harness facts separately from this causal negative policy.

## Evidence Shape
- Support: one diagnosed round-28 persistent failure.
- Scope: generator repair and retargeting only.
