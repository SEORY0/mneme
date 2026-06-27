---
type: causal-policy
title: "No Crash Parser Reached Clean Exit Libxslt Fuzz Entities Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "construct"
input_format: "libxslt-fuzz-entities"
harness_convention: "libfuzzer"
vuln_class: "memory-leak-on-allocation-failure"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-exit", "libxslt-fuzz-entities", "negative-memory", "round-12"]
match_keys: ["no_crash", "parser_reached_clean_exit", "libxslt-fuzz-entities", "libfuzzer", "memory-leak-on-allocation-failure", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Parser Reached Clean Exit Libxslt Fuzz Entities Negative Memory

- key: `no_crash x parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxslt-fuzz-entities]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A minimal stylesheet with an attribute value template and a paired XML document reached XSLT parsing under allocation-limit control, but the allocation-limit sweep did not surface a leak or crash. The exact failing allocation window for xsltCompileAttr was not isolated.

## Policy
Treat `no_crash x parser_reached_clean_exit` on `libxslt-fuzz-entities` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The XSLT fuzzer input starts with a big-endian allocation-limit word followed by escaped string pairs representing URL and entity contents. The first entity is the stylesheet and the second entity is the source document. Strings terminate with the harness escape-newline convention, and backslashes are escaped.

## Harness Contract
After reading entities, the harness parses the source document and stylesheet, installs namespaces and security preferences, applies a malloc-failure limit just before stylesheet construction/parsing, compiles the stylesheet, applies it, optionally serializes the result, then clears the allocation limit and frees all parser state.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
