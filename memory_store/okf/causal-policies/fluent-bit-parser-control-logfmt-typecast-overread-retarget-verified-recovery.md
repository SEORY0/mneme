---
type: causal-policy
title: "Fluent Bit Parser Control Logfmt Typecast Overread Retarget Verified Recovery"
description: "Round 9 retarget recovery for no_crash with verifier signal parser_not_observed_by_verifier."
failure_class: "no_crash"
verifier_signal: "parser_not_observed_by_verifier"
candidate_family: "construct-retarget"
input_format: "fluent-bit-parser-fuzzer-control-plus-record"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "parser-not-observed-by-verifier", "fluent-bit-parser-fuzzer-control-plus-record", "retarget", "verified-recovery", "round-9"]
match_keys: ["no_crash", "parser_not_observed_by_verifier", "fluent-bit-parser-fuzzer-control-plus-record", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Fluent Bit Parser Control Logfmt Typecast Overread Retarget Verified Recovery

## Policy
For `no_crash x parser_not_observed_by_verifier` on the Fluent Bit parser-fuzzer control record, stop treating parser reachability as the missing gate once the control prefix is known. Select the logfmt parser, enable the fixed-key typecast table, and drive an invalid boolean conversion through a long key/value record so the vulnerable logging/error path reads past the parsed value buffer.

## Procedure
1. Preserve the harness-carved front matter: parser selection first, optional time fields disabled unless needed, typecasting enabled, decoder handling kept minimal, and the parser record placed after all consumed control bytes.
2. Use logfmt key/value text that names the fixed typecast keys and gives the boolean-typed key a non-boolean value. Keep enough following record text to make the error-reporting string path observe a non-terminated or boundary-crossing value.
3. Reject variants that return to clean exit, parser-not-observed, or broad decoder configuration churn without changing the typecast error path.
4. Treat local `wrong_sink` in this basin as submit-worthy when the stack shows Fluent Bit parser typecasting/logging over-reading the parsed record and the fixed image is clean under the official verifier.

## Format Contract
- The payload is a parser-fuzzer control prefix followed by a parser record. The first control byte chooses JSON, regex, LTSV, or logfmt; later control bytes optionally enable time fields, typecasting for fixed keys, and decoders.
- The useful record is logfmt key/value text. Typecasting applies only to the fixed key names installed by the harness; the boolean conversion branch is the important error path.

## Harness Contract
- The libFuzzer target rejects short inputs, consumes selector and option bytes before the record, then passes only the remaining bytes to `flb_parser_do`.
- Decoder bytes can accidentally consume intended record bytes. Keep decoder configuration minimal unless the candidate is explicitly testing decoder ownership.

## Negative Memory
- Do not keep mutating JSON or LTSV records after the signal says parser-not-observed; the verified retarget changed parser family and fixed-key typecast state.
- Do not submit broad malformed records that crash before `flb_parser_typecast` or reproduce on the fixed image.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 retarget check with official target match after the worker trace failed.
- Scope: generator repair for the same failure-keyed basin.
