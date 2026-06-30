---
type: negative-memory
title: "No Crash Interpreter Error Or Clean Exit Without Sanitizer Postscript Construct Dangling Reference After Restore Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal interpreter_error_or_clean_exit_without_sanitizer."
failure_class: "no_crash"
verifier_signal: "interpreter_error_or_clean_exit_without_sanitizer"
candidate_family: "construct"
input_format: "postscript"
harness_convention: "libfuzzer"
vuln_class: "dangling-reference-after-restore"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "interpreter-error-or-clean-exit-without-sanitizer", "postscript", "libfuzzer", "construct", "negative-memory", "round-26"]
match_keys: ["no_crash", "interpreter_error_or_clean_exit_without_sanitizer", "postscript", "libfuzzer", "dangling-reference-after-restore", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash Interpreter Error Or Clean Exit Without Sanitizer Postscript Construct Dangling Reference After Restore Negative Memory

- key: `no_crash x interpreter_error_or_clean_exit_without_sanitizer`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The raw PostScript harness was reached, but every constructed candidate either completed cleanly or produced an ordinary Ghostscript interpreter fatal without a sanitizer signal. Distinct attempts covered normal stopped errors, direct calls into the stack-recording error handler, explicit job save and end-of-job restore, manual old-dictionary writes into the error dictionary, large restored local arrays, dynamic local-VM caps, VM-threshold pairing, and disabled automatic reclamation. The likely missing condition is a narrower allocator timing window where the stack arrays are successfully stored in the error dictionary while the save-change record for that old dictionary update fails, followed by a job restore and final GC that scans the stale references.

## Policy
Treat `no_crash x interpreter_error_or_clean_exit_without_sanitizer` on `postscript` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `interpreter_error_or_clean_exit_without_sanitizer` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `interpreter_error_or_clean_exit_without_sanitizer`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
PostScript inputs are executable programs. Ghostscript's error dictionary records non-VM errors through an internal error handler that sets the error name and command, and when stack recording is enabled stores operand, execution, and dictionary stack snapshots as arrays. Direct VM errors do not preserve those stack snapshots. Job control can create an encapsulated job save and later restore it, and explicit VM reclamation can request garbage collection after the restore. Local VM pressure can be adjusted from PostScript with user parameters for maximum local VM, VM threshold, and VM reclamation behavior.

## Harness Contract
The active fuzz target passes the raw input bytes to Ghostscript as stdin for a fax-oriented device wrapper. There is no leading mode selector, no corpus envelope, and no FuzzedDataProvider front/back carving. The wrapper runs Ghostscript in safer, batch, no-pause mode with stdout and stderr mostly discarded by the harness, so verifier output mainly distinguishes sanitizer crashes from clean execution or ordinary Ghostscript interpreter errors.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 48 attempts.
- Scope: generator repair and basin avoidance only.
