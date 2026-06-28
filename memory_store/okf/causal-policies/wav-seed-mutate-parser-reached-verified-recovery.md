---
type: causal-policy
title: "Wav Seed Mutate Parser Reached Verified Recovery"
description: "Round 7 verified recovery for wrong_sink with verifier signal parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "seed_mutate"
input_format: "wav"
harness_convention: "libfuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached", "seed-mutate", "wav", "verified-recovery", "round-7"]
match_keys: ["wrong_sink", "parser_reached", "wav", "libfuzzer", "use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Wav Seed Mutate Parser Reached Verified Recovery

- key: `wrong_sink x parser_reached`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[wav]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `wav` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached` on `wav` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Start from a valid WAV seed, insert a valid metadata LIST/INFO block before audio data, update the
enclosing RIFF length, and include a metadata subchunk so the WAV loader compares a metadata id view
after the temporary owner has gone out of scope.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
WAV files use RIFF/WAVE framing with chunk ids and little-endian chunk lengths. A fmt chunk
describes audio layout, LIST chunks can carry INFO metadata subchunks, and chunk payloads are padded
to even length before the data chunk.

## Harness Contract
The WAV fuzzer feeds raw bytes into a fixed memory stream and constructs a WavLoaderPlugin. There is
no leading mode byte; parser reachability depends on valid RIFF/WAVE chunk framing.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
