---
type: "negative-memory"
title: "Assimp Model Construct No Crash Secondary Io Reached No Target Crash Out Of Bounds Read Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal secondary_io_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "secondary_io_reached_no_target_crash"
candidate_family: "construct"
input_format: "assimp-model"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "secondary-io-reached-no-target-crash", "assimp-model", "libfuzzer", "construct", "out-of-bounds-read", "negative-memory", "round-38"]
match_keys: ["no_crash", "secondary_io_reached_no_target_crash", "assimp-model", "libfuzzer", "out-of-bounds-read", "negative-memory", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Assimp Model Construct No Crash Secondary Io Reached No Target Crash Out Of Bounds Read Negative Memory

- key: `no_crash x secondary_io_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[assimp-model]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Several candidates reached importer parsing and some reached secondary-file resolution through the FileSystemFilter, but no input produced an ASAN-visible read in Cleanup. OBJ material-library parsing skips leading whitespace before building the filename. glTF and GLB external-resource ideas were not viable because the extensionless memory filename prevents the glTF importers from winning selection. LWS can be selected by content and can drive external object paths through Exists/Open, but its line parser strips leading whitespace before the path; suffix and separator boundary variants stayed clean.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x secondary_io_reached_no_target_crash` on `[[assimp-model]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `secondary_io_reached_no_target_crash` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `secondary_io_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 10 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
