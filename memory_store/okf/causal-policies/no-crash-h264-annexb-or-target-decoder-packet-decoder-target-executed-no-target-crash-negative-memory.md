---
type: causal-policy
title: "No Crash H264 Annexb Or Target Decoder Packet Decoder Target Executed No Target Crash Negative Memory"
description: "Negative memory for no_crash with decoder_target_executed_no_target_crash on h264-annexb-or-target-decoder-packet inputs."
failure_class: no_crash
verifier_signal: decoder_target_executed_no_target_crash
candidate_family: construct
input_format: h264-annexb-or-target-decoder-packet
harness_convention: libfuzzer-ffmpeg-target-decoder
vuln_class: undefined-behavior-negative-vlc-index
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, decoder-target-executed-no-target-crash, h264-annexb-or-target-decoder-packet, undefined-behavior-negative-vlc-index, negative_memory]
match_keys: [no-crash, decoder-target-executed-no-target-crash, h264-annexb-or-target-decoder-packet, undefined-behavior-negative-vlc-index]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash H264 Annexb Or Target Decoder Packet Decoder Target Executed No Target Crash Negative Memory

- key: `no_crash x decoder_target_executed_no_target_crash`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[h264-annexb-or-target-decoder-packet]]

## Dead End
Constructed H.264 packets reached the selected FFmpeg decoder target but did not drive the CAVLC residual path into the invalid VLC-table index. The tested families covered start-code framed parameter sets plus a slice, alternate length-prefixed framing, explicit harness packet separators, residual-heavy slice payloads, and a context trailer. The missing gate is likely a valid slice-header and residual-coding combination that leaves the CAVLC zeros-left state below the legal range.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
