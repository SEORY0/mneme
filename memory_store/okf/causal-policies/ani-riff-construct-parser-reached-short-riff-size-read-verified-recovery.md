---
type: causal-policy
title: "Ani Riff Construct Parser Reached Short Riff Size Read Verified Recovery"
description: "Round 7 verified recovery for wrong_sink with verifier signal parser_reached_short_riff_size_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_short_riff_size_read"
candidate_family: "construct"
input_format: "ani-riff"
harness_convention: "libfuzzer-raw-qbuffer"
vuln_class: "uninitialized-or-out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-short-riff-size-read", "construct", "ani-riff", "verified-recovery", "round-7"]
match_keys: ["wrong_sink", "parser_reached_short_riff_size_read", "ani-riff", "libfuzzer-raw-qbuffer", "uninitialized-or-out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Ani Riff Construct Parser Reached Short Riff Size Read Verified Recovery

- key: `wrong_sink x parser_reached_short_riff_size_read`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[ani-riff]]
- harnesses: [[libfuzzer-raw-qbuffer]]

## Failure Shape
The verifier-confirmed candidate preserved the `ani-riff` parser envelope under `libfuzzer-raw-qbuffer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_short_riff_size_read` on `ani-riff` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Provide the RIFF magic and a short, nonempty but incomplete RIFF-size field. The image handler
scanner casts the short buffer as a little-endian size before checking that the full size field was
read; the fixed build rejects the incomplete field cleanly.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
ANI is a RIFF-family format: an outer RIFF marker is followed by a little-endian RIFF size and then
an ACON form marker before chunk records. Chunk records use an identifier plus a little-endian size
and payload.

## Harness Contract
LibFuzzer supplies raw bytes through a Qt QBuffer to the image handler. The harness calls canRead
and then still calls read, so partial RIFF prefixes can reach the scanner even when the full ANI
header is not accepted.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
