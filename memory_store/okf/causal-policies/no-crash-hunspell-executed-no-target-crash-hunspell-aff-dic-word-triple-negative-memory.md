---
type: negative-memory
title: "No Crash Hunspell Executed No Target Crash Hunspell Aff Dic Word Triple Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal hunspell-executed-no-target-crash."
failure_class: "no-crash"
verifier_signal: "hunspell-executed-no-target-crash"
candidate_family: "construct"
input_format: "hunspell-aff-dic-word-triple"
harness_convention: "libfuzzer-front-carved"
vuln_class: "buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "hunspell-executed-no-target-crash", "hunspell-aff-dic-word-triple", "libfuzzer-front-carved", "construct", "negative-memory", "round-21"]
match_keys: ["no-crash", "hunspell-executed-no-target-crash", "hunspell-aff-dic-word-triple", "libfuzzer-front-carved", "buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Hunspell Executed No Target Crash Hunspell Aff Dic Word Triple Negative Memory

- key: `no-crash x hunspell-executed-no-target-crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[hunspell-aff-dic-word-triple]]
- harnesses: [[libfuzzer-front-carved]]

## Failure Shape
Constructed UTF-8 prefix-rule dictionaries loaded and executed spell/suggest paths but did not trigger the prefix condition out-of-bounds read. The likely gap is an exact affix condition and word boundary combination that makes the prefix test compare a continuation-byte condition after consuming the whole word.

## Policy
Treat `no-crash x hunspell-executed-no-target-crash` on `hunspell-aff-dic-word-triple` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, both-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 21.
- Scope: generator repair and basin avoidance only.
