---
type: causal-policy
title: "No Crash Cli Processed Without Target Crash Openthread Cli Uart Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal cli_processed_without_target_crash."
failure_class: "no_crash"
verifier_signal: "cli_processed_without_target_crash"
candidate_family: "construct_cli_commands"
input_format: "openthread-cli-uart"
harness_convention: "libfuzzer"
vuln_class: "parse-validation-bypass"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "cli-processed-without-target-crash", "openthread-cli-uart", "negative-memory", "round-12"]
match_keys: ["no_crash", "cli_processed_without_target_crash", "openthread-cli-uart", "libfuzzer", "parse-validation-bypass", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Cli Processed Without Target Crash Openthread Cli Uart Negative Memory

- key: `no_crash x cli_processed_without_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[openthread-cli-uart]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Malformed embedded-IPv4 address strings reached CLI command handlers but did not produce a sanitizer-visible failure. Variants covered direct address addition, prefix parsing with trailing tokens, UDP binding, and CoAP destination parsing; all returned or errored cleanly under the UART harness.

## Policy
Treat `no_crash x cli_processed_without_target_crash` on `openthread-cli-uart` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The input is CLI text, usually newline-terminated commands. Address-bearing commands pass tokenized arguments into IPv6 string parsing; IPv6 literals may include compressed hextets and an embedded dotted IPv4 tail. The parser treats a space as an address terminator.

## Harness Contract
The libFuzzer input is copied as raw UART bytes and delivered to otPlatUartReceived after initializing a single OpenThread instance as a leader. There is no file wrapper, mode byte, checksum, or FuzzedDataProvider carving.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `cli_processed_without_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
