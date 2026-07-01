---
type: causal-policy
title: "No Crash Parser Reached Markdown Renderer But No Sanitizer Signal Markdown Heap Buffer Overflow Read Negative Memory"
description: "Negative memory for persistent no_crash / parser_reached_markdown_renderer_but_no_sanitizer_signal basin."
failure_class: "no_crash"
verifier_signal: "parser_reached_markdown_renderer_but_no_sanitizer_signal"
candidate_family: "construct"
input_format: "markdown"
harness_convention: "afl-compatible-raw-input"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "construct", "markdown", "heap-buffer-overflow-read", "negative-memory"]
match_keys: ["no-crash", "parser-reached-markdown-renderer-but-no-sanitizer-signal", "markdown", "afl-compatible-raw-input", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Parser Reached Markdown Renderer But No Sanitizer Signal Markdown Heap Buffer Overflow Read Negative Memory

## Policy
For `no_crash` with verifier signal `parser_reached_markdown_renderer_but_no_sanitizer_signal` on `markdown` under `afl-compatible-raw-input`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- The vulnerable code-fence probe was reachable, including from an unterminated fenced block and from a footnote/list carrier where a list marker left only indentation for the probe.
- Space-only top-level and continuation lines were often consumed by empty-line filters before code-fence detection.
- When the probe was reached on a boundary-shaped subspan, the read remained inside allocator-usable slack in the AFL/ASAN build, so no sanitizer signal was produced.
- Seed corpus replay also produced only clean exits.

## Recovery Direction
- Keep the parser/harness reachability facts in [[markdown]] and [[afl-compatible-raw-input]].
- Retarget away from the failed relation named by `parser_reached_markdown_renderer_but_no_sanitizer_signal`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
