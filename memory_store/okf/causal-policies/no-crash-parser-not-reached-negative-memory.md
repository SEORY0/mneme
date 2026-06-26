---
type: causal-policy
title: No Crash Parser Not Reached Negative Memory
description: Negative memory for no_crash with verifier signal parser_not_reached.
failure_class: no_crash
verifier_signal: parser_not_reached
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-not-reached, negative_memory]
match_keys: [no-crash, parser-not-reached, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Parser Not Reached Negative Memory

- key: `no_crash x parser_not_reached`
- outcome: persistent failure basin
- support_count: 2
- candidate_families: construct
- observed_formats: ftp-wildcard-pattern, jpeg-exif

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Rebuild the carrier around the exact harness envelope before adding a vulnerability trigger. Validate parser reachability first, then add one target invariant.

## Diagnosed Dead Ends
- A structurally valid JPEG envelope with an EXIF TIFF directory was built, including oversized component-count variants. The local wrapper selected a GraphicsMagick JPEG fuzzer invocation that rejected flat-file replay as a corpus-path issue before exercising the image bytes, so the EXIF parser was not reached through the provided local command.
- A direct wildcard-pattern payload did not reach curl's FTP wildcard matching path. The unsatisfied gate is the curl-fuzzer FTP transaction envelope that supplies a wildcard URL and directory listing so the default fnmatch implementation sees a trailing open character class.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
