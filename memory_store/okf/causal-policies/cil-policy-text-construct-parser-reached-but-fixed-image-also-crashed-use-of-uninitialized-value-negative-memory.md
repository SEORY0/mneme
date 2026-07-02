---
type: negative-memory
title: "CIL Policy Text Construct Parser Reached But Fixed Image Also Crashed Use Of Uninitialized Value Negative Memory"
description: "Round 29 negative memory for wrong_sink with verifier signal parser_reached_but_fixed_image_also_crashed."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_but_fixed_image_also_crashed"
candidate_family: "construct"
input_format: "cil-policy-text"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-but-fixed-image-also-crashed", "cil-policy-text", "libfuzzer", "construct", "use-of-uninitialized-value", "negative-memory", "round-29"]
match_keys: ["wrong_sink", "parser_reached_but_fixed_image_also_crashed", "cil-policy-text", "libfuzzer", "use-of-uninitialized-value", "wrong-sink", "parser-reached-but-fixed-image-also-crashed", "cil-policy-text", "libfuzzer", "use-of-uninitialized-value", "negative_memory", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# CIL Policy Text Construct Parser Reached But Fixed Image Also Crashed Use Of Uninitialized Value Negative Memory

- key: `wrong_sink x parser_reached_but_fixed_image_also_crashed`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[cil-policy-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A minimal CIL carrier reached the resolver and the strongest candidate used an optional block to create stale filename-name state before a macro typetransition reused the same symbolic relation through a non-name parameter. That produced a sanitizer signal in the vulnerable resolver path, but confirmation showed the fixed image also crashed, so the candidate was over-broad. Pure non-name parameter collisions without the stale optional state were rejected cleanly before the target invariant, while name/string parameter variants compiled without a target crash.

## Policy
Treat `wrong_sink x parser_reached_but_fixed_image_also_crashed` on `cil-policy-text` for `use-of-uninitialized-value` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_but_fixed_image_also_crashed` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_but_fixed_image_also_crashed`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
CIL policy text is an S-expression policy language. A minimal compile path needs class and classorder declarations, SID and sidorder declarations, user, role, type, role/type and user/role relations, category and sensitivity ordering, sensitivity-category mapping, user levels/ranges, a SID context, and at least one allow-style rule. A filename typetransition is represented as a typetransition form with source type, target type, object class, filename/name token, and result type. Macro parameters can be declared with flavors such as name/string, type, class, classpermission, level, levelrange, and ipaddr; anonymous classpermission and level-like arguments are accepted by the call-argument builder but are not valid filename-name datums.

## Harness Contract
The secilc libFuzzer target consumes the input bytes directly as one raw CIL source buffer. The harness adds the buffer as an in-memory CIL file, compiles it, builds and optimizes a policy database, writes the policy to a null sink on success, then destroys the CIL database. There is no file wrapper, selector byte, integrity trailer, or FuzzedDataProvider front/back layout.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 35 attempts.
- Scope: generator repair and basin avoidance only.
