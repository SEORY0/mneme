---
type: causal-policy
title: "Classic Pcap Raw Ip Packet Construct Wrong Sink Parser Reached Sink Mismatch But Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "classic-pcap-raw-ip-packet"
harness_convention: "libfuzzer-pcap-file-reader"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "classic-pcap-raw-ip-packet", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "classic-pcap-raw-ip-packet", "libfuzzer-pcap-file-reader", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Classic Pcap Raw Ip Packet Construct Wrong Sink Parser Reached Sink Mismatch But Official Target Match Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_sink_mismatch_but_official_target_match` on `classic-pcap-raw-ip-packet` under `libfuzzer-pcap-file-reader`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Build a complete classic pcap file with a valid global header and one packet record.
2. Use a raw-IP link-layer type so the packet read path stores that enum into the RawPacket, then make the captured packet shorter than a full IPv4 header while preserving the first nibble that selects IPv4 parsing.
3. This reaches getNextPacket and then trips the insufficient-length invariant in the first-layer parser; the fixed build rejects or guards the short raw-IP packet.

## Format Contract
- Input format: [[classic-pcap-raw-ip-packet]].
- Harness contract: [[libfuzzer-pcap-file-reader]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `classic-pcap-raw-ip-packet` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.

## Diagnosis Notes
Arbitrary unsupported link-layer values were accepted or rejected without a sanitizer crash, and an undersized loopback packet crashed both images. The successful family used a supported raw-IP link-layer value with a minimal short packet so the fixed image's validation covered the target path.
