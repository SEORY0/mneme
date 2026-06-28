---
type: negative-memory
title: "Generic Crash Local Generic Nonrepro Official Clean XML Negative Memory"
description: "Round 19 negative memory for generic_crash with verifier signal local_generic_nonrepro_official_clean."
failure_class: "generic_crash"
verifier_signal: "local_generic_nonrepro_official_clean"
candidate_family: "construct"
input_format: "xml"
harness_convention: "libfuzzer"
vuln_class: "type-confusion"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-generic-nonrepro-official-clean", "xml", "libfuzzer", "construct", "negative-memory", "round-19"]
match_keys: ["generic-crash", "local-generic-nonrepro-official-clean", "xml", "libfuzzer", "type-confusion"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# Generic Crash Local Generic Nonrepro Official Clean XML Negative Memory

- key: `generic_crash x local_generic_nonrepro_official_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[xml]]
- harnesses: [[libfuzzer]]

## Failure Shape
DTD-backed namespace declarations with ID-typed xmlns attributes reached libxml2 XML memory parsing, and one fixed-default namespace variant crashed locally, but the submitted candidate did not reproduce under the official comparison. The likely missing condition is stable validation-option selection plus the exact namespace validation path rather than ordinary XML parsing.

## Policy
Treat `generic_crash x local_generic_nonrepro_official_clean` on `xml` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 19.
- Scope: generator repair and basin avoidance only.
