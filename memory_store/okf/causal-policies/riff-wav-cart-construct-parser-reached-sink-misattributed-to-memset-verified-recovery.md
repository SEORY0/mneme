---
type: causal-policy
title: "Riff Wav Cart Construct Parser Reached Sink Misattributed To Memset Verified Recovery"
description: "Round 7 verified recovery for wrong_sink with verifier signal parser_reached_sink_misattributed_to_memset."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_misattributed_to_memset"
candidate_family: "construct"
input_format: "riff-wav-cart"
harness_convention: "libfuzzer-virtual-io-libsndfile"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-misattributed-to-memset", "construct", "riff-wav-cart", "verified-recovery", "round-7"]
match_keys: ["wrong_sink", "parser_reached_sink_misattributed_to_memset", "riff-wav-cart", "libfuzzer-virtual-io-libsndfile", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Riff Wav Cart Construct Parser Reached Sink Misattributed To Memset Verified Recovery

- key: `wrong_sink x parser_reached_sink_misattributed_to_memset`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[riff-wav-cart]]
- harnesses: [[libfuzzer-virtual-io-libsndfile]]

## Failure Shape
The verifier-confirmed candidate preserved the `riff-wav-cart` parser envelope under `libfuzzer-virtual-io-libsndfile` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_sink_misattributed_to_memset` on `riff-wav-cart` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Build a minimal RIFF/WAVE envelope and use a CART metadata chunk. Keep the RIFF and chunk length
accounting coherent, but set the CART chunk length in the boundary region where the parser accepts
it as fitting the in-memory structure while it still exceeds the actual file-layout text storage
area.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
RIFF/WAVE data is chunked with little-endian sizes. The CART chunk file layout omits an internal
tag-text-size field that exists in the library structure, so a chunk length near the structure-size
boundary can make the parser copy more text bytes than the destination field can hold.

## Harness Contract
The libFuzzer harness exposes the raw bytes through libsndfile virtual I/O. There is no carved
prefix; the RIFF magic, WAVE form type, and chunk sizes drive parser reachability.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
