---
type: causal-policy
title: "Zstd Legacy Frame Construct Generic Crash Parser Reached Target Match Official Buffer Overflow Write Verified Recovery"
description: "Server-verified recovery for zstd-legacy-frame when generic_crash pairs with parser_reached_target_match_official."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match_official"
candidate_family: "construct"
input_format: "zstd-legacy-frame"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-match-official", "zstd-legacy-frame", "libfuzzer", "construct", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "parser-reached-target-match-official", "zstd-legacy-frame", "libfuzzer", "construct", "buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Zstd Legacy Frame Construct Generic Crash Parser Reached Target Match Official Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_target_match_official`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[zstd-legacy-frame]]
- related harness facts: [[libfuzzer]]

## Policy
When `generic_crash x parser_reached_target_match_official` appears for `zstd-legacy-frame`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `zstd-legacy-frame` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Build a complete legacy zstd frame after the harness seed prefix. Use a legacy version whose raw literals decoder copies oversized raw literals into a fixed literals buffer. Make the frame scanner happy by keeping the compressed-block size consistent with the raw-literals header and by appending an end block. The only violated invariant is that the raw literal length is just beyond the fixed scratch buffer capacity; the vulnerable decoder copies it before sequence decoding, while the fixed build rejects or bounds it.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[zstd-legacy-frame]]. A legacy zstd frame starts with a version-specific legacy magic, followed by three-byte block headers. The block header encodes block type and compressed block size. A compressed block begins with a literals sub-block; a raw literals sub-block carries a compact header encoding the raw literal block type and literal length, followed by literal bytes. The frame-size scanner must see a terminating end block before the simple decompressor dispatches to the legacy decoder.

## Harness Contract
Use [[libfuzzer]]. The libFuzzer simple_decompress target consumes a four-byte RNG seed prefix from the input before passing the remaining bytes to ZSTD_decompressDCtx. It reuses one decompression context and runs the same frame through several randomized output-buffer capacities. There is no FuzzedDataProvider layout beyond the seed prefix; the post-prefix bytes are treated as the complete compressed frame stream.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `generic_crash x parser_reached_target_match_official`.
- Vulnerability class: `buffer-overflow-write`.
- Recovery summary: Build a complete legacy zstd frame after the harness seed prefix. Use a legacy version whose raw literals decoder copies oversized raw literals into a fixed literals buffer. Make the frame scanner happy by keeping the compressed-block size consistent with the raw-literals header and by appending an end block. The only violated invariant is that the raw literal length is just beyond the fixed scratch buffer capacity; the vulnerable decoder copies it before sequence decoding, while the fixed build rejects or bounds it.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
