---
type: causal-policy
title: "Openthread Cli Uart Dataset Tlv Construct Cli Command Wrong Sink Parser Reached Channelmask Getter Stack Buffer Overflow Read Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_channelmask_getter."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_channelmask_getter"
candidate_family: "construct-cli-command"
input_format: "openthread-cli-uart-dataset-tlv"
harness_convention: "honggfuzz-file-cli-uart"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-channelmask-getter", "openthread-cli-uart-dataset-tlv", "honggfuzz-file-cli-uart", "construct-cli-command", "stack-buffer-overflow-read", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_channelmask_getter", "openthread-cli-uart-dataset-tlv", "honggfuzz-file-cli-uart", "stack-buffer-overflow-read", "verified-recovery", "construct-cli-command"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Openthread Cli Uart Dataset Tlv Construct Cli Command Wrong Sink Parser Reached Channelmask Getter Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_channelmask_getter`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[openthread-cli-uart-dataset-tlv]]
- related harness facts: [[honggfuzz-file-cli-uart]]

## Failure Shape
Feed the CLI UART a dataset update command whose hex payload parses as MeshCoP dataset TLVs. Use an accepted padding/unknown TLV shape before a ChannelMask TLV encoded with the extended-length form and an empty logical value, placing the malformed TLV near the end of the copied dataset object. Dataset walking accepts the extended TLV size, but the ChannelMask getter interprets the base length marker as a large entry span and walks past the dataset buffer.

## Policy
When `wrong_sink x parser_reached_channelmask_getter` appears for `openthread-cli-uart-dataset-tlv` under `honggfuzz-file-cli-uart`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[openthread-cli-uart-dataset-tlv]]` format contract and `[[honggfuzz-file-cli-uart]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `openthread-cli-uart-dataset-tlv` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 3 attempts.
- Candidate family: construct-cli-command.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
