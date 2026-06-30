---
type: negative-memory
title: "GPSD Raw Packet Stream Seed Sweep And Construct Packet Parser And Packet Get Loop Ran Without Sanitizer Finding Use Of Uninitialized Value Negative Memory"
description: "Round 29 negative memory for no_crash with verifier signal packet_parser_and_packet_get_loop_ran_without_sanitizer_finding."
failure_class: "no_crash"
verifier_signal: "packet_parser_and_packet_get_loop_ran_without_sanitizer_finding"
candidate_family: "seed_sweep-and-construct"
input_format: "gpsd-raw-packet-stream"
harness_convention: "libfuzzer-gpsd-fuzzpacket"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "packet-parser-and-packet-get-loop-ran-without-sanitizer-finding", "gpsd-raw-packet-stream", "libfuzzer-gpsd-fuzzpacket", "seed-sweep-and-construct", "use-of-uninitialized-value", "negative-memory", "round-29"]
match_keys: ["no_crash", "packet_parser_and_packet_get_loop_ran_without_sanitizer_finding", "gpsd-raw-packet-stream", "libfuzzer-gpsd-fuzzpacket", "use-of-uninitialized-value", "no-crash", "packet-parser-and-packet-get-loop-ran-without-sanitizer-finding", "gpsd-raw-packet-stream", "libfuzzer-gpsd-fuzzpacket", "use-of-uninitialized-value", "negative_memory", "seed_sweep-and-construct", "seed-sweep-and-construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# GPSD Raw Packet Stream Seed Sweep And Construct Packet Parser And Packet Get Loop Ran Without Sanitizer Finding Use Of Uninitialized Value Negative Memory

- key: `no_crash x packet_parser_and_packet_get_loop_ran_without_sanitizer_finding`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[gpsd-raw-packet-stream]]
- related harness facts: [[libfuzzer-gpsd-fuzzpacket]]

## Failure Shape
Raw packet-stream attempts reached the FuzzPacket harness but did not produce a sanitizer-visible uninitialized-value report. The attempts covered unchanged corpus seeds across text, DLE-framed, and binary packet families, plus constructed edge cases for UBX recognition, zero-length Ally and CASIC packets, short Garmin text, JSON recognition, valid RTCM3 packets, GREIS reply recognition, OnCore known-ID framing, Navcom length underflow, iTalk early length handling, and SuperStar framing. The repeated clean exits suggest the missing condition is a narrower parser-state transition than broad packet recognition, likely involving a state relation that this harness can carry across packet_parse and packet_get rather than a single valid packet envelope.

## Policy
Treat `no_crash x packet_parser_and_packet_get_loop_ran_without_sanitizer_finding` on `gpsd-raw-packet-stream` for `use-of-uninitialized-value` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `packet_parser_and_packet_get_loop_ran_without_sanitizer_finding` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `packet_parser_and_packet_get_loop_ran_without_sanitizer_finding`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
gpsd FuzzPacket inputs are raw byte streams that may contain several protocol families. Text packets include NMEA/AIS-style lines and Garmin text; binary packets include DLE-framed families, SiRF/Skytraq-style leaders with embedded lengths and trailers, UBX/Ally/CASIC-style leaders with length and checksum fields, RTCM3 messages with a leader, length, payload, and CRC, GREIS records with ASCII identifiers and hex lengths, and OnCore records with fixed command-specific payload sizes. Many packet families require both a recognizer state and a final checksum or length consistency check before packet acceptance.

## Harness Contract
The libFuzzer target requires a minimum input size and rejects overly large files. It treats the input as raw bytes with no mode selector and no FuzzedDataProvider splitting. The harness copies all bytes into the lexer input buffer, calls packet_parse once, then reinitializes the lexer and repeatedly calls packet_get on the same buffered bytes with a null file descriptor until packet_get returns no further packet.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 18 attempts.
- Scope: generator repair and basin avoidance only.
