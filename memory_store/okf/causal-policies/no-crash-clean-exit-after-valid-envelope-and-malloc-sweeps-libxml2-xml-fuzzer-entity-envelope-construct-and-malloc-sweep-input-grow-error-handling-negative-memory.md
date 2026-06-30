---
type: causal-policy
title: "No Crash Clean Exit After Valid Envelope And Malloc Sweeps Libxml2 Xml Fuzzer Entity Envelope Construct And Malloc Sweep Input Grow Error Handling Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal clean_exit_after_valid_envelope_and_malloc_sweeps."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_valid_envelope_and_malloc_sweeps"
candidate_family: "construct_and_malloc_sweep"
input_format: "libxml2-xml-fuzzer-entity-envelope"
harness_convention: "libfuzzer"
vuln_class: "input-grow-error-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-after-valid-envelope-and-malloc-sweeps", "libxml2-xml-fuzzer-entity-envelope", "libfuzzer", "construct-and-malloc-sweep", "negative-memory", "round-30"]
match_keys: ["no-crash", "clean-exit-after-valid-envelope-and-malloc-sweeps", "libxml2-xml-fuzzer-entity-envelope", "libfuzzer", "input-grow-error-handling", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Clean Exit After Valid Envelope And Malloc Sweeps Libxml2 Xml Fuzzer Entity Envelope Construct And Malloc Sweep Input Grow Error Handling Negative Memory

- key: `no-crash x clean-exit-after-valid-envelope-and-malloc-sweeps`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[libxml2-xml-fuzzer-entity-envelope]]
- harnesses: [[libfuzzer]]

## Failure Shape
Five distinct source-guided hypotheses stayed clean: an external-subset conditional-section envelope with allocation-limit sweep, a large external-parameter-entity expansion with allocation-limit sweep, a SAX1 parser-mode incomplete-start carrier, a long encoded XML document intended to force memory-buffer growth through an encoder, and a truncated encoded-tail carrier intended to stop at a character-boundary growth/error condition. The likely missing relation is a more precise parser state in which a direct input-grow failure occurs while a caller still assumes context-aware error propagation; the tested carriers either parsed cleanly or failed allocation paths without surfacing the target sanitizer condition.

## Negative Policy
For `no-crash x clean-exit-after-valid-envelope-and-malloc-sweeps` on `libxml2-xml-fuzzer-entity-envelope`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, no-crash, no-crash, no-crash, no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[libxml2-xml-fuzzer-entity-envelope]] and [[libfuzzer]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
