---
type: "negative-memory"
title: "Fluent Bit Parser Fuzzer Control Plus Record Construct No Crash Parser Setup Reached Clean Exit Double Free Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal parser_setup_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_setup_reached_clean_exit"
candidate_family: "construct"
input_format: "fluent-bit-parser-fuzzer-control-plus-record"
harness_convention: "honggfuzz-style-file-fuzzer"
vuln_class: "double-free"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "parser-setup-reached-clean-exit", "fluent-bit-parser-fuzzer-control-plus-record", "honggfuzz-style-file-fuzzer", "construct", "double-free", "negative-memory", "round-38"]
match_keys: ["no_crash", "parser_setup_reached_clean_exit", "fluent-bit-parser-fuzzer-control-plus-record", "honggfuzz-style-file-fuzzer", "double-free", "negative-memory", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Fluent Bit Parser Fuzzer Control Plus Record Construct No Crash Parser Setup Reached Clean Exit Double Free Negative Memory

- key: `no_crash x parser_setup_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fluent-bit-parser-fuzzer-control-plus-record]]
- related harness facts: [[honggfuzz-style-file-fuzzer]]

## Failure Shape
The active target was the general parser fuzzer rather than a raw JSON-only entry point. Raw JSON missed the harness contract; control-prefix JSON reached parser setup but exited cleanly. Time-key primitive candidates were stopped by the current JSON parser type guard, decoder-list plus invalid time-offset cleanup did not double-free, and logfmt typecast retargeting only reached a warning path. The missing condition appears to be a more specific JSON ownership or cleanup relation beyond basic parser reachability.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x parser_setup_reached_clean_exit` on `[[fluent-bit-parser-fuzzer-control-plus-record]]` under `[[honggfuzz-style-file-fuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_setup_reached_clean_exit` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_setup_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 15 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
