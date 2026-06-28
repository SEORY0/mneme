---
type: negative-memory
title: "No Crash Ast Literal Eval Clean Or Rejected Python Source Expression Construct Heap Use After Free Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal ast_literal_eval_clean_or_rejected."
failure_class: "no_crash"
verifier_signal: "ast_literal_eval_clean_or_rejected"
candidate_family: "construct"
input_format: "python-source-expression"
harness_convention: "libfuzzer-cpython-ast-literal-eval"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ast-literal-eval-clean-or-rejected", "python-source-expression", "libfuzzer-cpython-ast-literal-eval", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "ast_literal_eval_clean_or_rejected", "python-source-expression", "libfuzzer-cpython-ast-literal-eval", "heap-use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Ast Literal Eval Clean Or Rejected Python Source Expression Construct Heap Use After Free Negative Memory

- key: `no_crash x ast_literal_eval_clean_or_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[python-source-expression]]
- related harness facts: [[libfuzzer-cpython-ast-literal-eval]]

## Failure Shape
Nested literal-expression candidates executed through ast.literal_eval without triggering the AST repr use-after-free. The exposed fuzzer path evaluates literals and clears common parser exceptions; it does not directly construct custom AST object graphs for repr.

## Policy
Treat `no_crash x ast_literal_eval_clean_or_rejected` on `python-source-expression` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `ast_literal_eval_clean_or_rejected` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `ast_literal_eval_clean_or_rejected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The observed input is Python source text for literal evaluation, terminated so the C API can build a Unicode string. Valid carriers are Python literals such as lists, tuples, constants, and nested literal containers.

## Harness Contract
The built fuzzer initializes CPython, imports ast.literal_eval, ignores inputs without NUL termination for this target, converts bytes to a Unicode string, calls ast.literal_eval, and clears common parse/evaluation exceptions.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 2 attempts.
- Scope: generator repair and basin avoidance only.
