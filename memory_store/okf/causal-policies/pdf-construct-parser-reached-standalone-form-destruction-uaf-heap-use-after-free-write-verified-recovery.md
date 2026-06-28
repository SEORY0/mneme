---
type: causal-policy
title: "Pdf Construct Parser Reached Standalone Form Destruction Uaf Heap Use After Free Write Verified Recovery"
description: "Round 21 verified recovery for wrong-sink with verifier signal parser-reached-standalone-form-destruction-uaf."
failure_class: "wrong-sink"
verifier_signal: "parser-reached-standalone-form-destruction-uaf"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer-raw-poppler-renderer"
vuln_class: "heap-use-after-free-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-standalone-form-destruction-uaf", "pdf", "libfuzzer-raw-poppler-renderer", "construct", "verified-recovery", "round-21"]
match_keys: ["wrong-sink", "parser-reached-standalone-form-destruction-uaf", "pdf", "libfuzzer-raw-poppler-renderer", "heap-use-after-free-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 21
---
# Pdf Construct Parser Reached Standalone Form Destruction Uaf Heap Use After Free Write Verified Recovery

- key: `wrong-sink x parser-reached-standalone-form-destruction-uaf`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pdf]]
- harnesses: [[libfuzzer-raw-poppler-renderer]]

## Failure Shape
Build a minimal valid PDF with a page annotation array containing an indirect widget annotation that is not referenced from the catalog form field array. Make the widget a button-style form field with enough page and rectangle metadata for Poppler to create a standalone form field during page annotation loading. Rendering the page then deleting the document reaches destruction of the standalone field and triggers the stale object reference path; the fixed build avoids the extra unref.

## Policy
For `wrong-sink x parser-reached-standalone-form-destruction-uaf` on `pdf`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `pdf` carrier enough for the `libfuzzer-raw-poppler-renderer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `pdf` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 21 solve after 24 attempts.
- Scope: generator repair only.
