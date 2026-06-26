---
type: causal-policy
title: No Crash Header Parsed Without Sanitizer Abort Negative Memory
description: Negative memory for no_crash with verifier signal header_parsed_without_sanitizer_abort.
failure_class: no_crash
verifier_signal: header_parsed_without_sanitizer_abort
candidate_family: seed-mutate
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, header-parsed-without-sanitizer-abort, negative_memory]
match_keys: [no-crash, header-parsed-without-sanitizer-abort, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Header Parsed Without Sanitizer Abort Negative Memory

- key: `no_crash x header_parsed_without_sanitizer_abort`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: seed-mutate
- observed_formats: blosc2-frame

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- Valid frame and chunk corpus seeds parsed cleanly. Mutating the frame compressed-size metadata to very large positive values made the header report the overflow-prone arithmetic inputs, but the available verifier did not abort on the signed addition path. A next attempt should ensure the decompression path actually asks for compressed offsets after header parsing, or use a build configuration that traps signed-integer overflow.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
