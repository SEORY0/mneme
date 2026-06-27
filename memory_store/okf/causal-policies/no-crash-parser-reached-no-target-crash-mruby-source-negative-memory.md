---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Mruby Source Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "mruby-source"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "mruby-source", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "mruby-source", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Reached No Target Crash Mruby Source Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mruby-source]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Several ways to create apparent zero-valued big integers, including large zero literals and
  exponentiation paths that avoid obvious normalization, executed without hitting the digit-count
  sink. The missing path is likely a runtime Bigint method that returns a raw zero-length Bigint
  object and then immediately dispatches a method such as string conversion or size-in-base on that
  same object.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `mruby-source` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The input is plain mruby source text. Big integer literals and arithmetic are parsed or executed by
  mruby and can allocate RBigint objects whose internal limb array has a sign, size, and pointer. Most
  arithmetic return paths normalize zero back to a fixnum, avoiding the vulnerable zero-length Bigint
  state.

## Harness Contract
- The harness copies the raw bytes into a NUL-terminated string and calls mrb_load_string in a fresh
  mruby state. There is no front selector, no binary mrbc loader, and no FuzzedDataProvider layout.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.

## Round 16 Evidence Addendum

### Failure Key
- `no_crash x parser_reached_no_target_crash` for `mruby source` under `libfuzzer`.

### Procedure Update
- Syntax-valid Ruby snippets combining loops, break/next/redo, rescue, ensure, lambdas, and conditional jumps compiled and executed without target crash. The missing trigger likely requires a narrower compiler control-flow form where a generated jump bypasses the helper that records jump destinations.
- Keep the previously recorded negative-memory policy active; this addendum only strengthens the same basin-to-avoid with another diagnosed persistent failure.

### Format Contract
- The input is ordinary mruby source text. Relevant syntax families include loops, rescue/ensure blocks, lambda return behavior, boolean short-circuit operators, and jump-like statements such as break, next, redo, and return.
- Harness: The mruby fuzzer copies the raw input into a NUL-terminated buffer, opens a fresh mruby VM, calls mrb_load_string on that source, closes the VM, and frees the buffer. No bytes are carved before parsing.

### Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
