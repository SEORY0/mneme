---
type: causal-policy
title: "No Crash Fuzzshark Ip Reached Clean Exit Wireshark Fuzzshark Ip Payload Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal fuzzshark_ip_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "fuzzshark_ip_reached_clean_exit"
candidate_family: "seed_mutate"
input_format: "wireshark-fuzzshark-ip-payload"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "fuzzshark-ip-reached-clean-exit", "wireshark-fuzzshark-ip-payload", "negative-memory", "round-13"]
match_keys: ["no_crash", "fuzzshark_ip_reached_clean_exit", "wireshark-fuzzshark-ip-payload", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Fuzzshark Ip Reached Clean Exit Wireshark Fuzzshark Ip Payload Negative Memory

- key: `no_crash x fuzzshark_ip_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wireshark-fuzzshark-ip-payload]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A real Wireshark capture reached the fuzzshark IP harness but did not exercise the VWR wiretap rate-calculation path. The likely missing gate is that this image is configured for raw IP-family packet dissection, while the described bug is in a capture-file reader path.

## Policy
Treat `no_crash x fuzzshark_ip_reached_clean_exit` on `wireshark-fuzzshark-ip-payload` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `fuzzshark_ip_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
This harness accepts raw IP-family packet bytes for fuzzshark rather than a full pcap or pcapng envelope. Capture-file formats present in the source tree can run cleanly but are not the natural input contract for this image.

## Harness Contract
The arvo wrapper launches the Wireshark fuzzshark IP target on a single file copied to the fixed input path. There is no FuzzedDataProvider carving or mode byte in the input bytes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x fuzzshark_ip_reached_clean_exit`
- related format facts: [[wireshark-fuzzshark-ip-payload]]
- related harness facts: [[libfuzzer]]

### Failure Shape Delta
A real Wireshark capture reached the fuzzshark IP harness but did not exercise the VWR wiretap rate-calculation path. The likely missing gate is that this image is configured for raw IP-family packet dissection, while the described bug is in a capture-file reader path.

### Format Contract Delta
This harness accepts raw IP-family packet bytes for fuzzshark rather than a full pcap or pcapng envelope. Capture-file formats present in the source tree can run cleanly but are not the natural input contract for this image.

### Harness Contract Delta
The arvo wrapper launches the Wireshark fuzzshark IP target on a single file copied to the fixed input path. There is no FuzzedDataProvider carving or mode byte in the input bytes.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
