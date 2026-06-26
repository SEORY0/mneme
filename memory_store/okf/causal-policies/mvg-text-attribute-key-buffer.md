---
type: causal-policy
title: MVG Text Attribute Key Buffer Recovery
description: Failure-keyed recovery for MVG text expansion crashes after the annotation parser is reached.
failure_class: generic_crash
verifier_signal: parser_reached_sink_match
candidate_family: construct
input_format: mvg
harness_convention: afl-file
vuln_class: stack-buffer-overflow-write
access_scope: generate
success_count: 1
confidence: medium
tags: [generic_crash, parser_reached_sink_match, mvg, text_expansion, attribute_lookup]
match_keys: [generic_crash, parser_reached_sink_match, mvg, text_expansion, attribute_lookup]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
When an MVG text-annotation task reaches the renderer but only generic crash evidence is visible, keep the MVG canvas valid and move the mutation into the text expansion lookup. The causal field is the image-attribute key used by the text translator, not random drawing geometry.

## Procedure
1. Begin with a valid MVG canvas gate so the renderer reaches annotation handling.
2. Add a single text annotation using the format-expansion syntax that requests an image attribute.
3. Keep the attribute namespace and expansion syntax valid while sizing only the lookup key.
4. Prefer an exactly boundary-filling key shape over adding trailing noise; the trigger is the translator's key-copy invariant.
5. Submit only after local verification shows parser reachability and a sink-compatible crash.

## Negative Memory
- Do not switch to ellipse, polygon, or color mutations once the task evidence points at text translation.
- Do not append arbitrary bytes after a valid MVG body; that usually preserves parsing while obscuring the causal key.
- Do not treat any renderer crash as sufficient unless the verifier signal says the parser reached the expected sink.

## Evidence Shape
- Support: 1 server-verified round observation.
- Scope: generator repair for MVG text expansion only.
