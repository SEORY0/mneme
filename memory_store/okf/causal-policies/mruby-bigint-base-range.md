---
type: causal-policy
title: mruby Bigint Base Range Recovery
description: Failure-keyed recovery for mruby bigint conversion crashes that bypass shared base validation.
failure_class: generic_crash
verifier_signal: parser_reached_sink_match
candidate_family: construct
input_format: mruby-script
harness_convention: libfuzzer
vuln_class: integer-range-check-bypass
access_scope: generate
success_count: 1
confidence: medium
tags: [generic_crash, parser_reached_sink_match, mruby, bigint, base_range]
match_keys: [generic_crash, parser_reached_sink_match, mruby, bigint, base_range]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
For mruby script tasks involving numeric conversion, create a bigint receiver before passing an invalid base. The bigint-specific dispatch can reach arithmetic conversion code before the shared base-range guard rejects the request.

## Procedure
1. Use a syntactically valid mruby script so the interpreter reaches runtime dispatch.
2. Construct or coerce the receiver into the bigint path before conversion.
3. Invoke the base-sensitive conversion through that receiver.
4. Supply a base value outside the accepted range only after the bigint route is selected.
5. Keep the script minimal; extra numeric operations can normalize the receiver or trigger unrelated exceptions first.

## Negative Memory
- Do not call the same conversion on small integers or strings when the task names bigint-specific behavior.
- Do not rely on syntax errors or exception-only behavior; the crash requires runtime conversion dispatch.
- Do not add unrelated arithmetic that may coerce away from the bigint representation.

## Evidence Shape
- Support: 1 server-verified round observation.
- Scope: generator repair for mruby bigint conversion range bugs.
