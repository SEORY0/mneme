---
type: negative-memory
title: "Bad Format Verify Config Missing After Gen Extract Failure Wireshark Fuzzshark Raw Frame Construct Sigcomp Udvm Dissector Unsafe Decompression Negative Memory"
description: "Round 25 negative memory for bad_format with verifier signal verify_config_missing_after_gen_extract_failure."
failure_class: "bad_format"
verifier_signal: "verify_config_missing_after_gen_extract_failure"
candidate_family: "construct"
input_format: "wireshark-fuzzshark-raw-frame"
harness_convention: "libfuzzer"
vuln_class: "sigcomp-udvm-dissector-unsafe-decompression"
access_scope: generate
success_count: 0
confidence: medium
tags: ["bad-format", "verify-config-missing-after-gen-extract-failure", "wireshark-fuzzshark-raw-frame", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["bad_format", "verify_config_missing_after_gen_extract_failure", "wireshark-fuzzshark-raw-frame", "libfuzzer", "sigcomp-udvm-dissector-unsafe-decompression", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# Bad Format Verify Config Missing After Gen Extract Failure Wireshark Fuzzshark Raw Frame Construct Sigcomp Udvm Dissector Unsafe Decompression Negative Memory

- key: `bad_format x verify_config_missing_after_gen_extract_failure`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wireshark-fuzzshark-raw-frame]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The task source was recoverable from the downloaded tarball, but runner generation failed before writing verifier configuration because Python's safe tar extraction rejected an absolute symlink in the repository archive. Several raw SIGCOMP/SIP/IP-shaped payload hypotheses were prepared, but the local verifier could not run for this task without the missing verifier configuration.

## Policy
Treat `bad_format x verify_config_missing_after_gen_extract_failure` on `wireshark-fuzzshark-raw-frame` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `verify_config_missing_after_gen_extract_failure` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `verify_config_missing_after_gen_extract_failure`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
SIGCOMP messages can carry UDVM bytecode, returned feedback, state references, and compressed message bytes. The vulnerable Wireshark paths are controlled by preferences that dissect UDVM bytecode and decompress messages; UDP/TCP ports in the SIGCOMP range and SIP comp=sigcomp routing are relevant dispatch routes.

## Harness Contract
The available source shows fuzzshark's FUZZ_EPAN mode feeds the raw input as a packet buffer with an unknown encapsulation rather than reading a pcap file. The run directory for this task lacks verifier configuration because generation fails during repository extraction.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 5 attempts.
- Scope: generator repair and basin avoidance only.
