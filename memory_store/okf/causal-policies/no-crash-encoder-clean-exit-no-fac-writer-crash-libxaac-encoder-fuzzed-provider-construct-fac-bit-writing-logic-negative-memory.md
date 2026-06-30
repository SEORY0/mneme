---
type: negative-memory
title: "No Crash Encoder Clean Exit No FAC Writer Crash Libxaac Encoder FUZZED Provider Construct FAC Bit Writing Logic Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal encoder_clean_exit_no_fac_writer_crash."
failure_class: "no_crash"
verifier_signal: "encoder_clean_exit_no_fac_writer_crash"
candidate_family: "construct"
input_format: "libxaac-encoder-fuzzed-provider"
harness_convention: "libfuzzer"
vuln_class: "fac-bit-writing-logic"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "encoder-clean-exit-no-fac-writer-crash", "libxaac-encoder-fuzzed-provider", "libfuzzer", "construct", "negative-memory", "round-26"]
match_keys: ["no_crash", "encoder_clean_exit_no_fac_writer_crash", "libxaac-encoder-fuzzed-provider", "libfuzzer", "fac-bit-writing-logic", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash Encoder Clean Exit No FAC Writer Crash Libxaac Encoder FUZZED Provider Construct FAC Bit Writing Logic Negative Memory

- key: `no_crash x encoder_clean_exit_no_fac_writer_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libxaac-encoder-fuzzed-provider]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The encoder harness was reached with USAC configurations, but all tested families exited cleanly. Distinct attempts covered exact tail-built FuzzedDataProvider configs, FD-only zero-FAC candidates, switched FD-to-TD candidates, TD-only candidates, valid WAV-front payloads, speech-like classifier payloads, multiple USAC frame-length/SBR classes, and high-bit-demand USAC tool combinations. The likely missing condition is a narrower encoder state where the FAC writer sees a zero-bit or byte-aligned FAC payload at the vulnerable write point while still producing an observable sanitizer failure.

## Policy
Treat `no_crash x encoder_clean_exit_no_fac_writer_crash` on `libxaac-encoder-fuzzed-provider` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `encoder_clean_exit_no_fac_writer_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `encoder_clean_exit_no_fac_writer_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is not a raw AAC stream. It is a FuzzedDataProvider-driven encoder input: scalar configuration chooses bitrate, MPS/ADTS/ES switches, TNS/noise flags, PCM word size, channel count, sample rate, frame length, AOT, USAC/SBR-related flags, DRC enablement, codec mode, loudness fields, and stream id. The remaining front bytes are then consumed as encoder input buffers or as fill values for process iterations.

## Harness Contract
The selected OSS-Fuzz target is the libxaac encoder fuzzer. FuzzedDataProvider consumes byte-buffer payloads from the front, while integral and boolean scalar fields are consumed from the back in little-endian order. For AOT_USAC, a loudness pass uses a separate provider over the full input before encoder creation. During processing, the per-frame read-versus-memset selector is also consumed from the back of the remaining data, so control bytes for process-loop behavior must be placed at the back of the front payload region, before the configuration tail.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 38 attempts.
- Scope: generator repair and basin avoidance only.
