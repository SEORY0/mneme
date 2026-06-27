---
type: causal-policy
title: "No Crash Xml Parser Reached No Target Crash Negative Memory"
description: "Negative memory for no_crash with parser_reached_no_target_crash on xml inputs."
failure_class: no_crash
verifier_signal: parser_reached_no_target_crash
candidate_family: construct
input_format: xml
harness_convention: libfuzzer
vuln_class: use-after-free
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-no-target-crash, xml, use-after-free, negative_memory]
match_keys: [no-crash, parser-reached-no-target-crash, xml, use-after-free]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Xml Parser Reached No Target Crash Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[xml]]

## Dead End
The XML reader accepted multiple entity and DTD shapes but did not reproduce the entity-reference lifetime ordering needed for the described reader free path. Attempts varied raw XML, front-carved reader options, explicit encodings, parser flags, and internal versus external entity references.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
