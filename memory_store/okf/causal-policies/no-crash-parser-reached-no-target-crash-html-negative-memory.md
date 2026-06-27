---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Html Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "html"
harness_convention: "libfuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "html", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "html", "libfuzzer", "use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Reached No Target Crash Html Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[html]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- HTML inputs with explicit harness controls, meta charset changes, and high-bit text reached the HTML
  fuzzer but did not trigger the use-after-free in htmlCurrentChar. The missing condition is likely a
  push-parser buffer growth or encoding-switch sequence that invalidates the current input pointer
  between grow and current-character decoding.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `html` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The parsed document is ordinary HTML. Encoding can be inferred from high-bit bytes or from meta
  charset declarations, and malformed or late declarations can cause the parser to switch encoders
  during tokenization.

## Harness Contract
- The HTML fuzzer consumes a front control area before the document: parser options are read first,
  then an allocation limit is derived, and the remaining bytes are the HTML document. It runs both
  pull parsing and push parsing over the same remaining document, with the push parser feeding bounded
  chunks.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
