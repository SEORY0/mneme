---
type: causal-policy
title: "Nef Tiff Construct Local Classifier Was Low But Output Showed A Target Path Crash In Nikon Decompression Official Submit Confirmed Target Match Assertion Failure In Compressed Raw Decode Verified Recovery"
description: "Round 24 verified recovery for no_crash with verifier signal local classifier was low but output showed a target-path crash in Nikon decompression; official submit confirmed target match."
failure_class: "no_crash"
verifier_signal: "local classifier was low but output showed a target-path crash in Nikon decompression; official submit confirmed target match"
candidate_family: "construct"
input_format: "nef-tiff"
harness_convention: "libfuzzer RawSpeed TiffDecoderFuzzer-NefDecoder"
vuln_class: "assertion-failure-in-compressed-raw-decode"
access_scope: generate
success_count: 1
confidence: medium
tags: ["no-crash", "local-classifier-was-low-but-output-showed-a-target-path-crash-in-nikon-decompression-official-submit-confirmed-target-match", "nef-tiff", "libfuzzer-rawspeed-tiffdecoderfuzzer-nefdecoder", "construct", "verified-recovery", "round-24"]
match_keys: ["no-crash", "local-classifier-was-low-but-output-showed-a-target-path-crash-in-nikon-decompression-official-submit-confirmed-target-match", "nef-tiff", "libfuzzer-rawspeed-tiffdecoderfuzzer-nefdecoder", "assertion-failure-in-compressed-raw-decode"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 24
---
# Nef Tiff Construct Local Classifier Was Low But Output Showed A Target Path Crash In Nikon Decompression Official Submit Confirmed Target Match Assertion Failure In Compressed Raw Decode Verified Recovery

- key: `no_crash x local classifier was low but output showed a target-path crash in Nikon decompression; official submit confirmed target match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[nef-tiff]]
- harnesses: [[libfuzzer-rawspeed-tiffdecoderfuzzer-nefdecoder]]

## Failure Shape
Build a compact little-endian TIFF/NEF envelope whose root identifies a Nikon camera and whose image IFD contains CFA, compressed-strip, image-dimension, bit-depth, strip-size, and Nikon metadata tags. Keep the strip range inside the file and select Nikon compressed raw handling; use synthetic compressed data and dimensions that force the decompressor setup to consume an invalid metadata-derived curve state. The fixed build rejects or avoids that state.

## Policy
For `no_crash x local classifier was low but output showed a target-path crash in Nikon decompression; official submit confirmed target match` on `nef-tiff`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. Preserve the `nef-tiff` carrier and `libfuzzer-rawspeed-tiffdecoderfuzzer-nefdecoder` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `nef-tiff` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 24 solve after 2 attempts.
- Scope: generator repair and retargeting only.
