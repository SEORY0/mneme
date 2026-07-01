---
type: causal-policy
title: "Pe Dotnet Seed Mutate Generic Crash Parser Reached Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "seed_mutate"
input_format: "pe-dotnet"
harness_convention: "libfuzzer-yara-dotnet-scan-mem"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 2
confidence: high
tags: ["generic-crash", "parser-reached-target-match", "pe-dotnet", "libfuzzer-yara-dotnet-scan-mem", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "parser_reached_target_match", "pe-dotnet", "libfuzzer-yara-dotnet-scan-mem", "heap-buffer-overflow-read", "verified-recovery", "seed_mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Pe Dotnet Seed Mutate Generic Crash Parser Reached Target Match Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_match`
- outcome: server-verified target match
- success_count: 2
- related format facts: [[pe-dotnet]]
- related harness facts: [[libfuzzer-yara-dotnet-scan-mem]]

## Failure Shape
Start from an in-repo managed PE seed that already reaches YARA's dotnet metadata parser and preserves the DOS, PE, section, CLR metadata, stream, table, string, and blob heap gates. Reuse an existing assembly CustomAttribute path that resolves through MemberRef and TypeRef to GuidAttribute, then retarget only that attribute's blob reference to a minimal appended custom-attribute blob with a valid prolog and a non-null short string placed close to the end of the mapped file. The vulnerable parser validates the declared string length but then copies a fixed maximum-sized typelib buffer from the string start, crossing the mapped-file boundary; the fixed image rejects or bounds the copy cleanly.

## Policy
When `generic_crash x parser_reached_target_match` appears for `pe-dotnet` under `libfuzzer-yara-dotnet-scan-mem`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[pe-dotnet]]` format contract and `[[libfuzzer-yara-dotnet-scan-mem]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 2 official target matches. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `pe-dotnet` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 1 attempts.
- Candidate family: seed_mutate.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
