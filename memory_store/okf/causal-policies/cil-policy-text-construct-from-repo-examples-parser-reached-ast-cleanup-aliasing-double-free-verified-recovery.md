---
type: causal-policy
title: "Cil Policy Text Construct From Repo Examples Parser Reached Ast Cleanup Aliasing Double Free Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_ast_cleanup_aliasing."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_ast_cleanup_aliasing"
candidate_family: "construct_from_repo_examples"
input_format: "cil-policy-text"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-ast-cleanup-aliasing", "cil-policy-text", "libfuzzer", "construct-from-repo-examples", "double-free", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_ast_cleanup_aliasing", "cil-policy-text", "libfuzzer", "double-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Cil Policy Text Construct From Repo Examples Parser Reached Ast Cleanup Aliasing Double Free Verified Recovery

## Policy
For `wrong_sink x parser_reached_ast_cleanup_aliasing`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal valid CIL policy scaffold, then define a macro that accepts a classpermission parameter.
2. Inside the macro, add a classpermissionset rule whose target is that parameter, and call the macro with an inline anonymous classpermission.
3. Resolution aliases the rule's classperms into the anonymous argument so AST destruction later sees shared ownership and the vulnerable cleanup path frees the same classperms structure twice; the fixed build avoids resolving a classpermissionset target to an anonymous classpermission.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- CIL policy text is parenthesized S-expression syntax.
- A minimal compile path needs class and classorder declarations plus SID, user, role, type, sensitivity, category, role/type, user/role, userlevel, userrange, and SID context scaffolding.
- Classpermission macro parameters can be supplied either by a named classpermission or by an inline anonymous class/permission tuple; classpermissionset rules populate a classpermission from class/permission pairs.
- Harness [[libfuzzer]]:
  - The secilc libFuzzer target treats the input buffer as CIL source, adds it as an in-memory policy file, compiles it, builds and optimizes a policy database, writes to a null output when compilation succeeds, then destroys the CIL database.
  - There is no file wrapper, selector byte, integrity field, or FuzzedDataProvider layout.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[cil-policy-text]] and [[libfuzzer]].
