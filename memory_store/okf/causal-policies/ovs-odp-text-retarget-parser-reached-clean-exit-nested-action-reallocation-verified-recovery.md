---
type: causal-policy
title: "OVS ODP Text Retarget Parser Reached Clean Exit Nested Action Reallocation Verified Recovery"
description: "Round 10 retarget recovery for no_crash with verifier signal parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "construct"
input_format: "ovs-odp-text"
harness_convention: "libfuzzer"
vuln_class: "overflow"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "parser-reached-clean-exit", "ovs-odp-text", "retarget", "verified-recovery", "round-10"]
match_keys: ["no_crash", "parser_reached_clean_exit", "ovs-odp-text", "libfuzzer", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 10
---
# OVS ODP Text Retarget Parser Reached Clean Exit Nested Action Reallocation Verified Recovery

## Policy
For `no_crash x parser_reached_clean_exit` on OVS ODP text, keep the raw NUL-terminated action-string harness and retarget from accepted simple actions to a nested action that forces backing-buffer growth while an action parser still holds nested-attribute state. This is a positive retarget policy because the official vulnerable/fixed verifier recorded a target match after round-10 consolidation.

## Procedure
1. Preserve the single C-string contract: no file envelope, no binary netlink wrapper, no newline, and a final terminator.
2. Use action-list syntax rather than key-only syntax so the harness reaches ODP action parsing and formatting.
3. Include a nested `set(tunnel(...))` style action with enough option-like payload to grow the action buffer after the nested attribute begins.
4. Add only ordinary follow-on actions after the nested action; the causal relation is nested-action reallocation while parser state is still live, not arbitrary malformed text.

## Format Contract
- OVS ODP action text is a NUL-terminated action list parsed as a C string. Nested attributes are expressed with parenthesized action clauses and are later formatted from the generated netlink buffer.
- Harness: Raw libFuzzer bytes are interpreted directly as the ODP text string. Parser reachability depends on valid action syntax, a final terminator, and no outer archive or provider-carved fields.

## Negative Memory
- Do not stay in the clean-exit basin by varying only short accepted keys or action names.
- Do not switch to direct binary netlink bytes for this harness; the active target parses textual ODP first.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-10 consolidator retarget check with official target match.
- Scope: generator repair for the same failure-keyed basin.
