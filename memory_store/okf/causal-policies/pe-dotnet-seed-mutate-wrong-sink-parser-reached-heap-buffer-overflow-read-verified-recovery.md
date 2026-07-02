---
type: causal-policy
title: "Pe Dotnet Seed Mutate Wrong Sink Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for pe-dotnet when wrong_sink pairs with parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "seed_mutate"
input_format: "pe-dotnet"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached", "pe-dotnet", "libfuzzer", "seed-mutate", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached", "pe-dotnet", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Pe Dotnet Seed Mutate Wrong Sink Parser Reached Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[pe-dotnet]]
- related harness facts: [[libfuzzer]]

## Policy
When `wrong_sink x parser_reached` appears for `pe-dotnet`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `pe-dotnet` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Start from a valid PE/.NET corpus sample so DOS, PE, section, CLR, metadata-root, and stream-header gates all pass. Preserve the metadata envelope, but retarget the user-string stream to a tiny valid stream at EOF whose compressed blob length is accepted when checked at the length-prefix address; after the parser advances past the prefix, the same length causes set_sized_string to copy past the mapped file boundary by the minimum margin.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[pe-dotnet]]. PE/.NET inputs need a valid DOS header, PE signature, section mapping, CLR COM descriptor, CLI metadata root, padded stream headers, and accepted metadata stream names. The dotnet parser walks #~ tables plus #Strings/#Blob when present, and parses #US as a sequence with an initial reserved empty entry followed by compressed-length user-string blobs. The vulnerable relation is that a blob length is bounds-checked before adding the encoded-length prefix size, then copied after advancing past that prefix.

## Harness Contract
Use [[libfuzzer]]. The libFuzzer harness feeds the PoC file bytes directly to YARA rule scanning with import dotnet. There is no leading mode byte, no argv/stdin wrapper, and no FuzzedDataProvider front/back carving; parser reachability is entirely through the raw PE/.NET file structure.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: seed_mutate.
- Verifier key: `wrong_sink x parser_reached`.
- Vulnerability class: `heap-buffer-overflow-read`.
- Recovery summary: Start from a valid PE/.NET corpus sample so DOS, PE, section, CLR, metadata-root, and stream-header gates all pass. Preserve the metadata envelope, but retarget the user-string stream to a tiny valid stream at EOF whose compressed blob length is accepted when checked at the length-prefix address; after the parser advances past the prefix, the same length causes set_sized_string to copy past the mapped file boundary by the minimum margin.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
