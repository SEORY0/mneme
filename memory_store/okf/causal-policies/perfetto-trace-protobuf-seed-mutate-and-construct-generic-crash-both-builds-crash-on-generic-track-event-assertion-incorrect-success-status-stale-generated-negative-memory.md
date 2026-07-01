---
type: causal-policy
title: "Perfetto Trace Protobuf Seed Mutate And Construct Generic Crash Both Builds Crash On Generic Track Event Assertion Incorrect Success Status Stale Generated Negative Memory"
description: "Round 34 negative memory for perfetto-trace-protobuf when generic_crash pairs with both_builds_crash_on_generic_track_event_assertion."
failure_class: "generic_crash"
verifier_signal: "both_builds_crash_on_generic_track_event_assertion"
candidate_family: "seed_mutate-and-construct"
input_format: "perfetto-trace-protobuf"
harness_convention: "libfuzzer"
vuln_class: "incorrect-success-status-stale-generated-proto"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "both-builds-crash-on-generic-track-event-assertion", "perfetto-trace-protobuf", "libfuzzer", "seed-mutate-and-construct", "negative-memory", "round-34"]
match_keys: ["generic-crash", "both-builds-crash-on-generic-track-event-assertion", "perfetto-trace-protobuf", "libfuzzer", "seed-mutate-and-construct", "incorrect-success-status-stale-generated-proto", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Perfetto Trace Protobuf Seed Mutate And Construct Generic Crash Both Builds Crash On Generic Track Event Assertion Incorrect Success Status Stale Generated Negative Memory

- key: `generic_crash x both_builds_crash_on_generic_track_event_assertion`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[perfetto-trace-protobuf]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `generic_crash x both_builds_crash_on_generic_track_event_assertion`
- outcome: persistent failure / basin to avoid
- candidate family: `seed_mutate-and-construct`
- vulnerability class: `incorrect-success-status-stale-generated-proto`
- related format facts: [[perfetto-trace-protobuf]]
- related harness facts: [[libfuzzer]]

### Failure Shape
The selected wrapper executes the storage trace-processor fuzzer on raw trace bytes rather than the generated-proto presubmit script named in the task prose. Empty input, an in-repo TrackEvent seed, constructed ftrace compact-scheduling traces, a protoc-encoded TrackEvent seed, and a malformed typed TrackEvent argument all ran cleanly. A valid TrackEvent envelope with unsupported enum states reached the parser and crashed, but the fixed build crashed the same way, so those were over-broad parser assertions rather than the target stale-generated-proto/status distinction.

### Policy
Treat `generic_crash x both_builds_crash_on_generic_track_event_assertion` on `perfetto-trace-protobuf` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
Perfetto trace inputs are protobuf-framed Trace messages containing TracePacket records. The trace type guesser treats inputs without JSON, Fuchsia, systrace, ctrace, or gzip signatures as protobuf traces. TrackEvent packets require a usable packet sequence and incremental-state reset before later event packets are parsed; each parsed event also needs a timestamp from either the packet or event-level timestamp fields.

### Harness Contract
The libFuzzer harness consumes raw bytes with no mode byte and no FuzzedDataProvider splitting, copies them to an owned buffer, calls TraceProcessorStorage::Parse, and then flushes end-of-file parsing. This storage-only factory registers the proto tokenizer and TrackEvent path but not the full shell module set, so ftrace, heap graph, graphics, Android probes, and system probes were not active target paths in this harness.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `seed_mutate-and-construct`.
- Verifier key: `generic_crash x both_builds_crash_on_generic_track_event_assertion`.
- Vulnerability class: `incorrect-success-status-stale-generated-proto`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
