---
type: causal-policy
title: "No Crash Wrapper Expected Corpus Directory H264 Annexb Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal wrapper_expected_corpus_directory."
failure_class: "no_crash"
verifier_signal: "wrapper_expected_corpus_directory"
candidate_family: "seed_mutate"
input_format: "h264-annexb"
harness_convention: "libfuzzer-wrapper-mismatch"
vuln_class: "bitstream-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrapper-expected-corpus-directory", "h264-annexb", "negative-memory", "round-7"]
match_keys: ["no_crash", "wrapper_expected_corpus_directory", "h264-annexb", "libfuzzer-wrapper-mismatch", "bitstream-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Wrapper Expected Corpus Directory H264 Annexb Negative Memory

- key: `no_crash x wrapper_expected_corpus_directory`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[h264-annexb]]
- related harness facts: [[libfuzzer-wrapper-mismatch]]

## Failure Shape
The task description points at encoder emulation-prevention overflow, but the generated build script
produced the decoder fuzzer. A constructed encoder-style raw-frame input and a decoder seed path
both failed at the wrapper/corpus contract before exercising the described encoder sink.

## Policy
Treat `no_crash x wrapper_expected_corpus_directory` on `h264-annexb` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `wrapper_expected_corpus_directory`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
H.264 decoder seeds are byte streams with NAL units and start-code style framing. The encoder fuzzer
source, although not built here, would instead consume a fixed configuration prefix followed by raw
YUV frame bytes.

## Harness Contract
The actual generated target is the libavc decoder fuzzer from ossfuzz.sh. Local verifier output
showed the wrapper treating the supplied path as a required directory, indicating a harness
invocation mismatch rather than a normal raw-file libFuzzer single-input run.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
