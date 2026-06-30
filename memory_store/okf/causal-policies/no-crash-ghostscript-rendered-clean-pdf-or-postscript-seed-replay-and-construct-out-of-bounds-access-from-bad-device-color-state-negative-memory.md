---
type: negative-memory
title: "No Crash Ghostscript Rendered Clean PDF Or Postscript Seed Replay And Construct Out Of Bounds Access From Bad Device Color State Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal ghostscript_rendered_clean."
failure_class: "no_crash"
verifier_signal: "ghostscript_rendered_clean"
candidate_family: "seed_replay-and-construct"
input_format: "pdf-or-postscript"
harness_convention: "libfuzzer-ghostscript-psdcmyk"
vuln_class: "out-of-bounds-access-from-bad-device-color-state"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ghostscript-rendered-clean", "pdf-or-postscript", "libfuzzer-ghostscript-psdcmyk", "seed-replay-and-construct", "negative-memory", "round-26"]
match_keys: ["no_crash", "ghostscript_rendered_clean", "pdf-or-postscript", "libfuzzer-ghostscript-psdcmyk", "out-of-bounds-access-from-bad-device-color-state", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash Ghostscript Rendered Clean PDF Or Postscript Seed Replay And Construct Out Of Bounds Access From Bad Device Color State Negative Memory

- key: `no_crash x ghostscript_rendered_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf-or-postscript]]
- related harness facts: [[libfuzzer-ghostscript-psdcmyk]]

## Failure Shape
Renderable PDF and PostScript carriers were accepted by the psdcmyk fuzzer but did not trigger the bad forwarded-device color-state invariant. Attempts covered real spot-color samples, explicit spot-name and page-spot setup, explicit separation order, gray/RGB/CMYK painting, non-identity transfer functions, PDF ExtGState transfer, transparency groups, and inline or XObject images. The missing relation appears to be a narrower rendering path where color mapping is performed with a forwarded or subclass device whose DeviceN parameters are only valid through the ret_devn_params device call.

## Policy
Treat `no_crash x ghostscript_rendered_clean` on `pdf-or-postscript` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `ghostscript_rendered_clean` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `ghostscript_rendered_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Ghostscript accepts raw PostScript jobs and complete PDF documents. Useful PDF carriers need a catalog, pages tree, page, resources, content stream, and renderable operators. Spot-color state can be introduced through PDF Separation color spaces in page resources, through PostScript setpagedevice SeparationColorNames, PageSpotColors, MaxSeparations, and SeparationOrder, or through PDF page scanning that writes SeparationColorNames and PageSpotColors to the device. Transfer functions can be supplied by PostScript settransfer or setcolortransfer, or by PDF ExtGState transfer entries.

## Harness Contract
The selected oss-fuzz target is gs_device_psdcmyk_fuzzer. It feeds the raw input as Ghostscript stdin to the psdcmyk device with banding-oriented device options and writes output to a null file path. There is no fuzzer-side prefix, selector byte, or FuzzedDataProvider layout; parser selection is determined by PDF or PostScript syntax in the raw bytes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 34 attempts.
- Scope: generator repair and basin avoidance only.
