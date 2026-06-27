---
type: causal-policy
title: "ICU Calendar Fuzz Record Stream Construct Target Sink Crash Out Of Bounds Write Verified Recovery"
description: "Server-verified recovery for icu-calendar-fuzz-record-stream when generic_crash pairs with target_sink_crash."
failure_class: "generic_crash"
verifier_signal: "target_sink_crash"
candidate_family: "construct"
input_format: "icu-calendar-fuzz-record-stream"
harness_convention: "libfuzzer-fuzzed-data-provider-style"
vuln_class: "out-of-bounds-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-crash", "icu-calendar-fuzz-record-stream", "libfuzzer-fuzzed-data-provider-style", "construct", "verified-recovery", "round-18"]
match_keys: ["generic-crash", "target-sink-crash", "icu-calendar-fuzz-record-stream", "libfuzzer-fuzzed-data-provider-style", "construct", "out-of-bounds-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 18
---
# ICU Calendar Fuzz Record Stream Construct Target Sink Crash Out Of Bounds Write Verified Recovery

- key: `generic_crash x target_sink_crash`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[icu-calendar-fuzz-record-stream]]
- related harness facts: [[libfuzzer-fuzzed-data-provider-style]]

## Policy
When `generic_crash x target_sink_crash` appears for `icu-calendar-fuzz-record-stream`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Satisfy the calendar fuzzer's initial locale/timezone/calendar selectors, then provide repeated command records that normalize to the Calendar::set operation with field and amount data that drive the internal calendar field arrays outside their valid range.
2. The key invariant is that Calendar::set must reject invalid field state before indexing its internal storage.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, or clean parser reachability as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[icu-calendar-fuzz-record-stream]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer-fuzzed-data-provider-style]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 18 solve.
- Candidate family: construct.

## Round 18 Verified Evidence
- Verifier key: `generic_crash x target_sink_crash`.
- Vulnerability class: `out-of-bounds-write`.
- Recovery summary: Satisfy the calendar fuzzer's initial locale/timezone/calendar selectors, then provide repeated command records that normalize to the Calendar::set operation with field and amount data that drive the internal calendar field arrays outside their valid range.
