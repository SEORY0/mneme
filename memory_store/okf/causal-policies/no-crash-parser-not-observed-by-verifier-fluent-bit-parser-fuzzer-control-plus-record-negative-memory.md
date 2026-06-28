---
type: causal-policy
title: "No Crash Parser Not Observed By Verifier Fluent Bit Parser Fuzzer Control Plus Record Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal parser_not_observed_by_verifier."
failure_class: "no_crash"
verifier_signal: "parser_not_observed_by_verifier"
candidate_family: "construct"
input_format: "fluent-bit-parser-fuzzer-control-plus-record"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-observed-by-verifier", "fluent-bit-parser-fuzzer-control-plus-record", "negative-memory", "round-9"]
match_keys: ["no_crash", "parser_not_observed_by_verifier", "fluent-bit-parser-fuzzer-control-plus-record", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Parser Not Observed By Verifier Fluent Bit Parser Fuzzer Control Plus Record Negative Memory

- key: `no_crash x parser_not_observed_by_verifier`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fluent-bit-parser-fuzzer-control-plus-record]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- The initial logfmt payload accidentally let record bytes serve as decoder-control bytes.
- Corrected candidates reached the intended record layout, but decoder string-output paths and
  typecast warning paths still exited cleanly.
- The boolean typecast path is the only conversion branch that sets the unsafe error flag, but short
  and long EOF-placed keys did not produce an ASAN-visible read in this harness run.

## Policy
Treat `no_crash x parser_not_observed_by_verifier` on `fluent-bit-parser-fuzzer-control-plus-record` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The payload format is selected by the first control byte: JSON, regex, LTSV, or logfmt.
- Logfmt records are key=value pairs with optional quoted values; LTSV records are key:value pairs
  separated by tabs.
- Parser typecasting only affects fixed keys named AAA, BBB, CCC, DDD, and EEE when the types
  control byte is enabled.
- Among those fixed types, DDD is boolean and invalid boolean text triggers the cast-error path.

## Harness Contract
- The harness rejects inputs below a minimum size and consumes several bytes before the record: one
  format selector, optional fixed-width time_fmt/time_key/time_offset fields, one time_keep byte,
  one types-enable byte, and a decoder-enable byte.
- If decoders are enabled, additional bytes choose decoder rule type, backend, action, and
  optionally a second rule before one final unconditional byte is skipped.
- The remaining bytes are the parser record.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_observed_by_verifier`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
