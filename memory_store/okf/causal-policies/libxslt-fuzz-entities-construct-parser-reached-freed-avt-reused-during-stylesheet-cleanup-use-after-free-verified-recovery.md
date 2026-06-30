---
type: causal-policy
title: "Libxslt Fuzz Entities Construct Parser Reached Freed Avt Reused During Stylesheet Cleanup Use After Free Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_freed_avt_reused_during_stylesheet_cleanup."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_freed_avt_reused_during_stylesheet_cleanup"
candidate_family: "construct"
input_format: "libxslt-fuzz-entities"
harness_convention: "libfuzzer-libxslt-entity-framing-with-malloc-limit"
vuln_class: "use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-freed-avt-reused-during-stylesheet-cleanup", "libxslt-fuzz-entities", "libfuzzer-libxslt-entity-framing-with-malloc-limit", "construct", "use-after-free", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_freed_avt_reused_during_stylesheet_cleanup", "libxslt-fuzz-entities", "libfuzzer-libxslt-entity-framing-with-malloc-limit", "use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Libxslt Fuzz Entities Construct Parser Reached Freed Avt Reused During Stylesheet Cleanup Use After Free Verified Recovery

## Policy
For `wrong_sink x parser_reached_freed_avt_reused_during_stylesheet_cleanup`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build the libxslt fuzz-entity envelope with a valid stylesheet entity and a valid source-document entity.
2. In the stylesheet, put a literal result element inside a template and give it an attribute value template with enough alternating literal and expression segments to force AVT segment-array growth.
3. Then sweep the front allocation-limit word until the realloc in the AVT segment append path fails after prior segments were allocated.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The XSLT fuzz target input begins with a big-endian allocation-limit word.
- The rest is a sequence of escaped URL/content string pairs; each string is terminated by the harness escape-newline marker and literal backslashes are doubled.
- The first pair is the stylesheet, and the second pair is the source XML document.
- Harness [[libfuzzer-libxslt-entity-framing-with-malloc-limit]]:
  - The harness parses the fuzz-entity table, requires both stylesheet and source document entities, parses the source XML and stylesheet XML, installs XSLT namespaces and security preferences, then arms the allocation-failure limit immediately before stylesheet construction and parsing.
  - The limit controls xmlMalloc/xmlRealloc failures during stylesheet compilation and later clears before cleanup.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[libxslt-fuzz-entities]] and [[libfuzzer-libxslt-entity-framing-with-malloc-limit]].
