---
type: causal-policy
title: No Crash Parser Reached Unknown Negative Memory
description: Negative memory for no_crash with verifier signal parser_reached_unknown.
failure_class: no_crash
verifier_signal: parser_reached_unknown
candidate_family: seed-mutate
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: high
tags: [no-crash, parser-reached-unknown, negative_memory]
match_keys: [no-crash, parser-reached-unknown, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Parser Reached Unknown Negative Memory

- key: `no_crash x parser_reached_unknown`
- outcome: persistent failure basin
- support_count: 4
- candidate_families: seed-mutate, seed-sweep
- observed_formats: executable-object, h264-svc, pe-dotnet, postscript-pdf

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- The dotnet fuzzer accepted valid PE/.NET corpus inputs, but direct stream-count, stream-name, and stream-size mutations did not reach a crashing metadata parser state. The likely missing piece is a valid managed metadata envelope whose stream table remains internally consistent while violating only the dotnet module's unchecked stream-header invariant.
- The gstoraster wrapper processed bundled Ghostscript seeds without reproducing the described countdown/stale-cache failure. The failing path likely requires a PDF or PostScript object graph that enters an error cleanup branch after caching a counted object, then reuses the same cache entry later; simple corpus seeds did not satisfy that object-lifetime sequence.
- The selected addr2line/BFD wrapper accepted ordinary object-file seeds and completed normally. The described VMS Alpha debug parser path requires an object that BFD recognizes as the VMS-family format and whose module debug record contains an out-of-range source-setfile item; the available generic executable seeds did not enter that parser.
- The SVC decoder wrapper accepted H.264 corpus seeds but none produced the described base-mode reference-index failure. Triggering likely requires a valid SVC enhancement-layer bitstream where base-mode flags are enabled while the reference index points outside the populated reference mapping; simple seed replay did not satisfy that cross-field bitstream state.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
