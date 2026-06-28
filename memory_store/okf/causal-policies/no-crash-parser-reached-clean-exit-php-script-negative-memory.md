---
type: causal-policy
title: "No Crash Parser Reached Clean Exit Php Script Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "construct"
input_format: "php-script"
harness_convention: "libfuzzer-php-function-jit"
vuln_class: "optimizer-delayed-binding-state"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-exit", "php-script", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_reached_clean_exit", "php-script", "libfuzzer-php-function-jit", "optimizer-delayed-binding-state", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Reached Clean Exit Php Script Negative Memory

- key: `no_crash x parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[php-script]]
- related harness facts: [[libfuzzer-php-function-jit]]

## Failure Shape
- Valid PHP scripts with top-level parent and child classes, unreachable child declarations, return or
  goto-skipped blocks, multiple delayed class declarations, and early new expressions all executed
  cleanly. These reached the function-JIT fuzzer but did not produce either a sanitizer crash or a
  vulnerable-only semantic failure, suggesting the missing trigger is a more specific delayed-binding
  list corruption pattern than simple unreachable class declarations.

## Policy
Treat `no_crash x parser_reached_clean_exit` on `php-script` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The input is PHP source text. Normal PHP opening tags are needed for execution as script code. Top-
  level classes with an extends clause can become delayed class declarations under OPcache
  compilation; constant-control-flow blocks such as always-true return branches can make following
  declarations unreachable to optimizer passes.

## Harness Contract
- The selected target is the PHP function-JIT fuzzer. It runs the same script first with JIT disabled
  to detect bailout, invalidates OPcache state, and then reruns with function JIT enabled if the first
  run did not bail out. Inputs are capped in size and passed as raw request source for a fixed
  temporary filename.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
