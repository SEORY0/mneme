---
type: causal-policy
title: "Wrong Sink Parser Reached Sink Mismatch Ppm Negative Memory"
description: "Round 24 negative memory for wrong_sink with verifier signal parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "seed_mutate"
input_format: "ppm"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "parser-reached-sink-mismatch", "ppm", "libfuzzer", "seed-mutate", "negative-memory", "round-24"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch", "ppm", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# Wrong Sink Parser Reached Sink Mismatch Ppm Negative Memory

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[ppm]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
PPM corpus seeds reached the libjpeg-turbo compression path and triggered MSan in entropy encoding, but the official submit path reported both vulnerable and fixed images exiting nonzero. The likely gap is that the seed exercises a generic uninitialized-buffer basin rather than the destination-buffer allocation differential required by the task.

## Policy
For `wrong_sink x parser_reached_sink_mismatch` on `ppm`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate` only while this format and harness contract are present.

## Procedure
1. When `wrong_sink x parser_reached_sink_mismatch` appears for `ppm`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.
