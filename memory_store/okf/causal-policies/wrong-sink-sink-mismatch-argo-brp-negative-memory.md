---
type: causal-policy
title: "Wrong Sink Sink Mismatch Argo Brp Negative Memory"
description: "Round 13 negative memory for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "argo_brp"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "sink-mismatch", "argo-brp", "negative-memory", "round-13"]
match_keys: ["wrong_sink", "sink_mismatch", "argo_brp", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# Wrong Sink Sink Mismatch Argo Brp Negative Memory

- key: `wrong_sink x sink_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[argo-brp]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A constructed BRP container reached the intended BASF packet path and local verification reported MemorySanitizer use of uninitialized stack data in the BRP packet reader after parsing a short ASF chunk header. Direct local runs showed the fixed image returning cleanly for the same candidate, but the official scorer repeatedly reported a nonzero fixed exit and target_match=false for byte-distinct variants, so this remains an official failure despite reaching the described bug locally.

## Policy
Treat `wrong_sink x sink_mismatch` on `argo_brp` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `sink_mismatch`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Argonaut BRP starts with a small little-endian file header containing the BRP magic, stream count, and byte rate, followed by one fixed-size stream header per stream. A BASF stream header uses an embedded ASF file header as extradata; that ASF header must have the ASF magic, a nonzero chunk count, and a chunk offset at least as large as the ASF file header. BRP media blocks then use a fixed-size block header with stream id, timestamp, and block size. BASF blocks begin with an ASF chunk header containing block count, sample count, sample rate, flags, and related fields; accepted chunk headers need the expected sample count and standard flags before audio packet timing is derived from them.

## Harness Contract
The individual FFmpeg demuxer fuzzer uses the Argo BRP demuxer directly. For inputs larger than the harness metadata threshold, the last metadata region is not part of the demuxer byte stream; it controls IO buffer size, seekability, advertised file size, filename suffix behavior, and interrupt budget. With seekability enabled, the harness exposes AVIO seeking to the demuxer, but reads still advance through the supplied byte stream, so a header lookahead can consume one block while later packet reading consumes following bytes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
