---
type: causal-policy
title: "Openthread Cli Uart Construct Cli Command Generic Crash Parser Reached Target Sink Null Dereference Read Verified Recovery"
description: "Server-verified recovery for openthread-cli-uart when generic_crash pairs with parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct_cli_command"
input_format: "openthread-cli-uart"
harness_convention: "libfuzzer"
vuln_class: "null-dereference-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "openthread-cli-uart", "libfuzzer", "construct-cli-command", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "parser-reached-target-sink", "openthread-cli-uart", "libfuzzer", "construct-cli-command", "null-dereference-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Openthread Cli Uart Construct Cli Command Generic Crash Parser Reached Target Sink Null Dereference Read Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[openthread-cli-uart]]
- related harness facts: [[libfuzzer]]

## Policy
When `generic_crash x parser_reached_target_sink` appears for `openthread-cli-uart`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `openthread-cli-uart` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Use the CLI UART harness to invoke an address-management command that forwards one argument into the IPv6 address string parser. Make that argument look like an embedded dotted-decimal tail without any preceding IPv6 colon group, so the parser enters the embedded-address branch before its saved colon pointer has been initialized. The vulnerable build dereferences that missing saved pointer; the fixed build rejects the malformed address.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[openthread-cli-uart]]. The relevant input is CLI text delivered over the UART fuzzer. Commands are newline-terminated and tokenized before address-bearing subcommands call the IPv6 string parser. The parser supports compressed IPv6 groups and embedded dotted-decimal tails, stops an address token at NUL or space, and expects the embedded tail to follow a prior colon-delimited IPv6 prefix.

## Harness Contract
Use [[libfuzzer]]. The selected OpenThread libFuzzer target is the CLI UART receive harness. It copies the raw PoC bytes into a UART buffer after initializing a single OpenThread instance, then processes CLI tasklets. There is no file header, mode byte, checksum, or FuzzedDataProvider carving.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct_cli_command.
- Verifier key: `generic_crash x parser_reached_target_sink`.
- Vulnerability class: `null-dereference-read`.
- Recovery summary: Use the CLI UART harness to invoke an address-management command that forwards one argument into the IPv6 address string parser. Make that argument look like an embedded dotted-decimal tail without any preceding IPv6 colon group, so the parser enters the embedded-address branch before its saved colon pointer has been initialized. The vulnerable build dereferences that missing saved pointer; the fixed build rejects the malformed address.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
