---
type: causal-policy
title: "Generic Crash Wrong Sink Opensc Pkcs15 Reader Chunk Stream Seed Mutate Unsigned Integer Underflow Negative Memory"
description: "Round 30 negative memory for generic_crash with verifier signal wrong_sink."
failure_class: "generic_crash"
verifier_signal: "wrong_sink"
candidate_family: "seed_mutate"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "libfuzzer"
vuln_class: "unsigned-integer-underflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "wrong-sink", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "seed-mutate", "negative-memory", "round-30"]
match_keys: ["generic-crash", "wrong-sink", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "unsigned-integer-underflow", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# Generic Crash Wrong Sink Opensc Pkcs15 Reader Chunk Stream Seed Mutate Unsigned Integer Underflow Negative Memory

- key: `generic-crash x wrong-sink`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[opensc-pkcs15-reader-chunk-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
The SetCOS security-attribute underflow appears reachable only after card selection and select-file FCI parsing choose the SetCOS driver. Synthetic SetCOS transcripts stayed clean, while a PKCS#15 reader seed and a SetCOS-mutated variant reached parser code but crashed later in a generic PKCS#15 unwrap path. The server rejected that crash as non-target, so it should be treated as a wrong-sink basin rather than evidence for the described SetCOS bug.

## Negative Policy
For `generic-crash x wrong-sink` on `opensc-pkcs15-reader-chunk-stream`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, generic-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[opensc-pkcs15-reader-chunk-stream]] and [[libfuzzer]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
