---
type: causal-policy
title: "Postscript Construct Postscript Interpreter Error Then Double Finalize Uaf Heap Use After Free Read Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal postscript_interpreter_error_then_double_finalize_uaf."
failure_class: "wrong_sink"
verifier_signal: "postscript_interpreter_error_then_double_finalize_uaf"
candidate_family: "construct"
input_format: "postscript"
harness_convention: "libfuzzer-gstoraster-stdin"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "postscript-interpreter-error-then-double-finalize-uaf", "postscript", "libfuzzer-gstoraster-stdin", "construct", "heap-use-after-free-read", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "postscript_interpreter_error_then_double_finalize_uaf", "postscript", "libfuzzer-gstoraster-stdin", "heap-use-after-free-read", "wrong-sink", "postscript-interpreter-error-then-double-finalize-uaf", "postscript", "libfuzzer-gstoraster-stdin", "heap-use-after-free-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Postscript Construct Postscript Interpreter Error Then Double Finalize Uaf Heap Use After Free Read Verified Recovery

- key: `wrong_sink x postscript_interpreter_error_then_double_finalize_uaf`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[postscript]]
- related harness facts: [[libfuzzer-gstoraster-stdin]]

## Policy
For `wrong_sink x postscript_interpreter_error_then_double_finalize_uaf` on `postscript`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a syntactically valid PostScript document that reaches Ghostscript through stdin, then trigger a controlled interpreter/file-access error rather than a malformed-document rejection. The vulnerable cleanup path finalizes the interpreter state after the init error and then the harness exits the same instance again, causing a use-after-free during temporary-name cleanup. Keep the document compact and avoid broad PDF corruption or large allocation loops that do not enter this cleanup sequence.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[postscript]]: Ghostscript stdin inputs are raw PostScript or PDF documents selected by their own syntax. A PostScript program can execute operators that raise interpreter errors while still passing the language-recognition gate. Safe-mode file access failures are sufficient to make initialization return an error without needing an external sidecar file.
- Harness [[libfuzzer-gstoraster-stdin]]: The gstoraster libFuzzer target feeds the entire PoC as Ghostscript stdin with fixed CUPS raster output arguments. There is no mode byte, archive wrapper, or FuzzedDataProvider layout; the harness continues into exit/delete cleanup after init returns an error.

## Negative Memory
- Do not corrupt the outer `postscript` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[postscript]] and [[libfuzzer-gstoraster-stdin]].
