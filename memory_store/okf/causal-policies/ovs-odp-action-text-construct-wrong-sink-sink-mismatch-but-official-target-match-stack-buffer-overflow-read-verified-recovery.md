---
type: causal-policy
title: "Ovs Odp Action Text Construct Wrong Sink Sink Mismatch But Official Target Match Stack Buffer Overflow Read Verified Recovery"
description: "Round 32 server-verified recovery for ovs-odp-action-text keyed by wrong_sink x sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "ovs-odp-action-text"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch-but-official-target-match", "ovs-odp-action-text", "libfuzzer", "construct", "stack-buffer-overflow-read", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "sink-mismatch-but-official-target-match", "ovs-odp-action-text", "libfuzzer", "construct", "stack-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Ovs Odp Action Text Construct Wrong Sink Sink Mismatch But Official Target Match Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x sink_mismatch_but_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ovs-odp-action-text]]
- related harness facts: [[libfuzzer]]

## Policy
When `ovs-odp-action-text` under `[[libfuzzer]]` produces `sink_mismatch_but_official_target_match` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[ovs-odp-action-text]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Reach the raw OVS ODP action parser with a single newline-free C string, then use the NSH push action in its variable-length metadata form. Keep the action syntactically valid enough for the action parser to build the nested Netlink attribute, but make the metadata field exceed the fixed stack workspace consumed during action-to-attribute conversion. The local classifier reports the resulting sanitizer read as a sink mismatch, but official differential execution confirms the vulnerable build crashes and the fixed build exits cleanly.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- OVS ODP text inputs are comma-separated datapath key or action expressions, not an archive. The same textual surface can contain key attributes such as encap and tunnel fields, and action attributes such as set, sample, clone, userspace, and push_nsh. Nested constructs are parenthesized. The underlying Netlink writer uses length-bearing attributes, while several action parsers first collect variable textual fields into fixed local workspaces before serializing them as attributes. Geneve option text has strict per-option size and alignment limits, so very large Geneve strings can be rejected before reaching the intended serialization path.

## Harness Contract
- The libFuzzer target treats the input as raw bytes for one NUL-terminated string. It rejects inputs that are too short, do not end in NUL, or contain a newline before the final terminator. The harness then tries the same string through key parsing, wildcard key parsing, and action-list parsing; there is no tar framing or length-prefixed outer envelope.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.
