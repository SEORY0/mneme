---
type: negative-memory
title: "No Crash Parser Reached Markdown Renderer But No Sanitizer Signal Markdown Negative Memory"
description: "Round 22 negative memory for no_crash with verifier signal parser_reached_markdown_renderer_but_no_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "parser_reached_markdown_renderer_but_no_sanitizer_signal"
candidate_family: "construct"
input_format: "markdown"
harness_convention: "afl-compatible-raw-input"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-markdown-renderer-but-no-sanitizer-signal", "markdown", "afl-compatible-raw-input", "construct", "negative-memory", "round-22"]
match_keys: ["no-crash", "parser-reached-markdown-renderer-but-no-sanitizer-signal", "markdown", "afl-compatible-raw-input", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# No Crash Parser Reached Markdown Renderer But No Sanitizer Signal Markdown Negative Memory

- key: `no_crash x parser_reached_markdown_renderer_but_no_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[markdown]]
- harnesses: [[afl-compatible-raw-input]]

## Failure Shape
Distinct line-shape attempts targeted the code-fence probe after indentation and inside block/list contexts, but the one-byte overread condition did not become sanitizer-visible. The likely dead end is allocator slack in the hoedown input buffer or a line-splitting path that keeps the probe inside allocated storage.

## Policy
Treat `no_crash x parser_reached_markdown_renderer_but_no_sanitizer_signal` on `markdown` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, wrapper-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 22.
- Scope: generator repair and basin avoidance only.
