---
type: causal-policy
title: "Libmagic Classified RAW Buffer Construct Parser Reached Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "construct"
input_format: "libmagic-classified raw buffer"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch", "libmagic-classified-raw-buffer", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch", "libmagic-classified raw buffer", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Libmagic Classified RAW Buffer Construct Parser Reached Sink Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[libmagic-classified-raw-buffer]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a minimal raw text-like buffer that satisfies a libmagic whitespace-compacted search rule while ending without a string terminator. This reaches the search-rule comparison path, where the vulnerable comparison computes the input slice length without a remaining-buffer bound before checking the rule text.

## Policy
For `wrong_sink x parser_reached_sink_mismatch` on `libmagic-classified raw buffer`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `libmagic-classified raw buffer` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `libmagic-classified raw buffer` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The harness loads libmagic's compiled rules and classifies the submitted file bytes directly. Search rules can scan the raw buffer without copying it into a NUL-padded value union; string rules with whitespace-compaction modifiers take the slower comparison path that reasons about input whitespace and may require an input slice length.

## Harness Contract
The libFuzzer entrypoint passes the whole PoC as the data buffer to magic_buffer after only a non-empty size gate. There is no leading mode selector, section carving, checksum, or FuzzedDataProvider back-to-front layout.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.
