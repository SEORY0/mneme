---
type: "negative-memory"
title: "Libredwg JSON Construct No Crash Parser Reached Without Sanitizer Signal Buffer Overflow Read Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal parser_reached_without_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "parser_reached_without_sanitizer_signal"
candidate_family: "construct"
input_format: "libredwg-json"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow-read"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "parser-reached-without-sanitizer-signal", "libredwg-json", "libfuzzer", "construct", "buffer-overflow-read", "negative-memory", "round-38"]
match_keys: ["no_crash", "parser_reached_without_sanitizer_signal", "libredwg-json", "libfuzzer", "buffer-overflow-read", "negative-memory", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Libredwg JSON Construct No Crash Parser Reached Without Sanitizer Signal Buffer Overflow Read Negative Memory

- key: `no_crash x parser_reached_without_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libredwg-json]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Constructed JSON inputs reached the LibreDWG JSON importer but did not produce a sanitizer-visible source overread. Distinct attempts covered top-level metadata strings, header text fields, summary-info strings, class-name strings, dictionary item strings, valid escaped Unicode expansion, and raw truncated UTF-8 lead bytes after a valid JSON escape. The likely missing condition is a reachable call where the converter's source pointer can be advanced past the actual allocated input boundary; the JSON harness always copies and NUL-terminates the input, and ordinary object delimiters after string tokens appear to keep the vulnerable source reads inside the copied allocation.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x parser_reached_without_sanitizer_signal` on `[[libredwg-json]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_without_sanitizer_signal` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_without_sanitizer_signal`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 12 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
