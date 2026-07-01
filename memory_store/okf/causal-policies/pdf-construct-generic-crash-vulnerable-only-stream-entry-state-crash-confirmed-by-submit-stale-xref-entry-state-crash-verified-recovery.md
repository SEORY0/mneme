---
type: causal-policy
title: "PDF Construct Generic Crash Vulnerable Only Stream Entry State Crash Confirmed By Submit Stale Xref Entry State Crash Verified Recovery"
description: "Round 32 server-verified recovery for pdf keyed by generic_crash x vulnerable_only_stream_entry_state_crash_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "vulnerable_only_stream_entry_state_crash_confirmed_by_submit"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer-raw-poppler-renderer"
vuln_class: "stale-xref-entry-state-crash"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "vulnerable-only-stream-entry-state-crash-confirmed-by-submit", "pdf", "libfuzzer-raw-poppler-renderer", "construct", "stale-xref-entry-state-crash", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "vulnerable-only-stream-entry-state-crash-confirmed-by-submit", "pdf", "libfuzzer-raw-poppler-renderer", "construct", "stale-xref-entry-state-crash", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# PDF Construct Generic Crash Vulnerable Only Stream Entry State Crash Confirmed By Submit Stale Xref Entry State Crash Verified Recovery

- key: `generic_crash x vulnerable_only_stream_entry_state_crash_confirmed_by_submit`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer-raw-poppler-renderer]]

## Policy
When `pdf` under `[[libfuzzer-raw-poppler-renderer]]` produces `vulnerable_only_stream_entry_state_crash_confirmed_by_submit` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[pdf]]` through `[[libfuzzer-raw-poppler-renderer]]`.
2. Apply the verified recovery: Build a compact renderable PDF with a normal catalog, page tree, page, and content stream. Give the stream dictionary an indirect Length reference that is present in the body but absent from the initial xref table, so resolving Length during makeStream forces xref reconstruction while the current stream entry is marked as parsing. The vulnerable build later reuses the stale entry state and crashes; the fixed build keeps the entry lifetime/scoping safe.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- PDF reachability for this harness requires a recognizable header, indirect catalog/pages/page objects, a content stream, xref or repairable object locations, trailer/root linkage, and an EOF marker. Stream dictionaries can use indirect Length objects, and Poppler may repair or reconstruct xref state when an indirect reference is missing from the active table but present in the body.

## Harness Contract
- The Poppler C++ libFuzzer target passes the raw input bytes to load_from_raw_data, ignores locked or unloadable documents, then creates and renders every page. There is no byte carving, selector, secondary file, or FuzzedDataProvider layout.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.
