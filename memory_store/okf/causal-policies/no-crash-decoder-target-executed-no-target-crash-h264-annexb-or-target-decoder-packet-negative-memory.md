---
type: causal-policy
title: "No Crash Decoder Target Executed No Target Crash H264 Annexb Or Target Decoder Packet Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal decoder_target_executed_no_target_crash."
failure_class: "no_crash"
verifier_signal: "decoder_target_executed_no_target_crash"
candidate_family: "construct"
input_format: "h264-annexb-or-target-decoder-packet"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "undefined-behavior-negative-vlc-index"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-target-executed-no-target-crash", "h264-annexb-or-target-decoder-packet", "negative-memory", "round-13"]
match_keys: ["no_crash", "decoder_target_executed_no_target_crash", "h264-annexb-or-target-decoder-packet", "libfuzzer-ffmpeg-target-decoder", "undefined-behavior-negative-vlc-index", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Decoder Target Executed No Target Crash H264 Annexb Or Target Decoder Packet Negative Memory

- key: `no_crash x decoder_target_executed_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[h264-annexb-or-target-decoder-packet]]
- related harness facts: [[libfuzzer-ffmpeg-target-decoder]]

## Failure Shape
Constructed H.264 packets reached the selected FFmpeg decoder target but did not drive the CAVLC residual path into the invalid VLC-table index. The tested families covered start-code framed parameter sets plus a slice, alternate length-prefixed framing, explicit harness packet separators, residual-heavy slice payloads, and a context trailer. The missing gate is likely a valid slice-header and residual-coding combination that leaves the CAVLC zeros-left state below the legal range.

## Policy
Treat `no_crash x decoder_target_executed_no_target_crash` on `h264-annexb-or-target-decoder-packet` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_target_executed_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The target format is raw H.264 decoder packet data. Parser reachability requires recognizable parameter-set NAL units before slice data; CAVLC behavior depends on slice syntax, entropy mode, residual block type, coefficient counts, total-zero coding, and run-before coding.

## Harness Contract
The FFmpeg targeted decoder harness passes raw bytes to the H.264 decoder as one or more packets. A fixed internal separator can split multiple packets. If the input is large enough, the tail is consumed as codec-context configuration and removed from packet data before decoding.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x decoder_target_executed_no_target_crash`
- related format facts: [[h264-annexb-or-target-decoder-packet]]
- related harness facts: [[libfuzzer-ffmpeg-target-decoder]]

### Failure Shape Delta
Constructed H.264 packets reached the selected FFmpeg decoder target but did not drive the CAVLC residual path into the invalid VLC-table index. The tested families covered start-code framed parameter sets plus a slice, alternate length-prefixed framing, explicit harness packet separators, residual-heavy slice payloads, and a context trailer. The missing gate is likely a valid slice-header and residual-coding combination that leaves the CAVLC zeros-left state below the legal range.

### Format Contract Delta
The target format is raw H.264 decoder packet data. Parser reachability requires recognizable parameter-set NAL units before slice data; CAVLC behavior depends on slice syntax, entropy mode, residual block type, coefficient counts, total-zero coding, and run-before coding.

### Harness Contract Delta
The FFmpeg targeted decoder harness passes raw bytes to the H.264 decoder as one or more packets. A fixed internal separator can split multiple packets. If the input is large enough, the tail is consumed as codec-context configuration and removed from packet data before decoding.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
