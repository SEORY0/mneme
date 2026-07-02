---
type: causal-policy
title: "Git Patch Construct No Crash Clean Exit No Sanitizer Signal Null Pointer Dereference Negative Memory"
description: "Round 34 negative memory for git-patch when no_crash pairs with clean_exit_no_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "clean_exit_no_sanitizer_signal"
candidate_family: "construct"
input_format: "git-patch"
harness_convention: "libfuzzer"
vuln_class: "null-pointer-dereference"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-no-sanitizer-signal", "git-patch", "libfuzzer", "construct", "negative-memory", "round-34"]
match_keys: ["no-crash", "clean-exit-no-sanitizer-signal", "git-patch", "libfuzzer", "construct", "null-pointer-dereference", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Git Patch Construct No Crash Clean Exit No Sanitizer Signal Null Pointer Dereference Negative Memory

- key: `no_crash x clean_exit_no_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[git-patch]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `no_crash x clean_exit_no_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- candidate family: `construct`
- vulnerability class: `null-pointer-dereference`
- related format facts: [[git-patch]]
- related harness facts: [[libfuzzer]]

### Failure Shape
Empty old-path, new-path, paired-path, quoted-path, added/deleted-file, diff-header fallback, and prefix variants all exited cleanly. The parser either rejected the malformed header relation or fell back to nonempty diff-header paths; in the parse-and-free harness, accepted NULL path fields were not dereferenced in a sanitizer-visible way.

### Policy
Treat `no_crash x clean_exit_no_sanitizer_signal` on `git-patch` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
Git patch input uses a diff header, optional mode/index metadata, old/new file path headers, and hunk headers with line bodies. The path parser trims header payloads and can represent an empty path as a NULL detached buffer. Filename validation compares diff-header paths with file-header paths and falls back to the diff-header path when a file-header path is absent.

### Harness Contract
The libFuzzer target treats the leading input byte as the patch prefix-length option and passes all remaining bytes directly to the patch parser. The harness then frees the returned patch object; it does not print, apply, or otherwise traverse the parsed patch after parsing.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `construct`.
- Verifier key: `no_crash x clean_exit_no_sanitizer_signal`.
- Vulnerability class: `null-pointer-dereference`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
