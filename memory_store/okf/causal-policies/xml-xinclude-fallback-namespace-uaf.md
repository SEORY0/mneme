---
type: causal-policy
title: Xml Xinclude Fallback Namespace Uaf
description: Verified recovery for wrong_sink with serializer_use_after_free on xml-fuzzer-entities inputs.
failure_class: wrong_sink
verifier_signal: serializer_use_after_free
candidate_family: construct
input_format: xml-fuzzer-entities
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, serializer-use-after-free, construct, xml-fuzzer-entities, verified_recovery]
match_keys: [wrong-sink, serializer-use-after-free, xml-fuzzer-entities, heap-use-after-free]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Xml Xinclude Fallback Namespace Uaf

- key: `wrong_sink x serializer_use_after_free`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[xml-fuzzer-entities]]

## Failure Shape
A prior candidate family produced `wrong_sink` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `xml-fuzzer-entities` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Use the XML fuzzer entity envelope with XInclude processing and no include marker nodes enabled. Make an include fail so fallback children are spliced without copying, while a namespace used by a fallback child is owned by the removed fallback wrapper; serialization then reads the freed namespace.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `wrong_sink` toward `serializer_use_after_free`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.
