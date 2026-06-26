---
type: causal-policy
title: "Mapfile Construct Parser Reached Verified Recovery"
description: "Round 7 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "mapfile"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-access"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "construct", "mapfile", "verified-recovery", "round-7"]
match_keys: ["generic_crash", "parser_reached", "mapfile", "libfuzzer", "out-of-bounds-access", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Mapfile Construct Parser Reached Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[mapfile]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `mapfile` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `generic_crash` with signal `parser_reached` on `mapfile` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Build a minimal valid MapServer map containing an inline vector symbol with a POINTS block whose
number of coordinate pairs exceeds the fixed point array capacity while keeping the overall input
under the fuzzer size limit.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
MapServer mapfiles are keyword-oriented text. A MAP can contain SYMBOL definitions; vector symbols
have a POINTS block containing coordinate pairs terminated by END markers.

## Harness Contract
The map fuzzer writes the raw input bytes to a temporary .map file and calls msLoadMap. It rejects
very small and overly large inputs before parsing.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
