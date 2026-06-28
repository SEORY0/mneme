---
type: causal-policy
title: "No Crash Clean Execution Hunspell Aff Dic Word Triple Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal clean_execution."
failure_class: "no_crash"
verifier_signal: "clean_execution"
candidate_family: "construct"
input_format: "hunspell-aff-dic-word-triple"
harness_convention: "afl-file-wrapper"
vuln_class: "negative-array-index"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-execution", "hunspell-aff-dic-word-triple", "negative-memory", "round-15"]
match_keys: ["no_crash", "clean_execution", "hunspell-aff-dic-word-triple", "afl-file-wrapper", "negative-array-index", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Clean Execution Hunspell Aff Dic Word Triple Negative Memory

- key: `no_crash x clean_execution`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[hunspell-aff-dic-word-triple]]
- related harness facts: [[afl-file-wrapper]]

## Failure Shape
- The active wrapper executed Hunspell's affix/dictionary fuzzer, but malformed REP, MAP, PHONE,
  ICONV, OCONV, BREAK, prefix, and compound-pattern tables all parsed or rejected cleanly. The likely
  missing piece is the exact malformed affix directive relation that reaches the negative-index path
  after dictionary initialization.

## Policy
Treat `no_crash x clean_execution` on `hunspell-aff-dic-word-triple` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The affix/dictionary fuzz target consumes a front word-length selector, then uses the following
  bytes as the word and splits the remaining bytes into affix-file and dictionary-file halves. The
  dictionary still needs a count line and valid entries for Hunspell initialization; the affix half
  can contain SET, conversion, suggestion, break, prefix/suffix, and compound-pattern directives.

## Harness Contract
- The /bin/arvo wrapper invokes the affix/dictionary fuzzer on the PoC file path. The target writes
  temporary word, affix, and dictionary files, constructs a Hunspell instance from them, and calls
  spell followed by suggest if the word is not accepted.

## Negative Memory
- Do not resubmit variants that only reproduce `clean_execution`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
