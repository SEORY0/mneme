---
type: causal-policy
title: "Selinux Cil Policy Text Construct Parser Reached Optional Reset Uaf Server Match Heap Use After Free Verified Recovery"
description: "Round 9 verified recovery for wrong_sink with verifier signal parser_reached_optional_reset_uaf_server_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_optional_reset_uaf_server_match"
candidate_family: "construct"
input_format: "SELinux CIL policy text"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-optional-reset-uaf-server-match", "selinux-cil-policy-text", "construct", "verified-recovery", "round-9"]
match_keys: ["wrong_sink", "parser_reached_optional_reset_uaf_server_match", "SELinux CIL policy text", "libfuzzer", "heap-use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Selinux Cil Policy Text Construct Parser Reached Optional Reset Uaf Server Match Heap Use After Free Verified Recovery

## Policy
For `wrong_sink x parser_reached_optional_reset_uaf_server_match`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a minimal valid CIL policy with the required class, SID, user, role, type, category,
  sensitivity, and context declarations.
1. Declare a classpermission, populate it inside an optional block that is later disabled by an
  unresolved rule, then reference the classpermission after optional resolution.
1. The vulnerable resolver/reset path continues after an error and destroys a stale classpermission
  list twice; the fixed build stops cleanly.

## Format Contract
- CIL policy text is parenthesized S-expression syntax.
- A minimal compilable policy needs class and classorder declarations, SID and sidorder
  declarations, user/role/type declarations, category and sensitivity ordering, sensitivity-category
  mapping, user ranges, role/type and user/role relations, and a SID context.
- Classpermission references in allow rules use the bare classpermission name, not a nested list.

## Harness Contract
- libFuzzer provides raw CIL text.
- The harness adds the buffer as a CIL file, compiles it, builds a policy database, optimizes it,
  and writes the resulting policy to a sink file.
- There is no leading selector byte or external file envelope.

## Related Knowledge
- Format facts: [[selinux-cil-policy-text]]
- Harness facts: [[libfuzzer]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
