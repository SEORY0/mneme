---
type: causal-policy
title: No Crash Parser Clean Exit Negative Memory
description: Negative memory for no_crash with verifier signal parser_clean_exit.
failure_class: no_crash
verifier_signal: parser_clean_exit
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: high
tags: [no-crash, parser-clean-exit, negative_memory]
match_keys: [no-crash, parser-clean-exit, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Parser Clean Exit Negative Memory

- key: `no_crash x parser_clean_exit`
- outcome: persistent failure basin
- support_count: 6
- candidate_families: construct, seed-mutate
- observed_formats: json, mstp, rar5, ruby, udp-ieee1722-avtp, xml-fuzzer-frame

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Keep the accepted envelope but move from broad value changes to the feature selector or state transition described by the diagnosis. A clean exit means the parser path is real but the target state was absent.

## Diagnosed Dead Ends
- A valid compressed RAR5 corpus member and bounded truncations preserved the archive signature and reached normal libarchive handling, but did not reach the compressed-block Huffman table state where the declared table data outlives the available block bytes. The tested truncations were rejected or exhausted through clean parser paths.
- Candidates used the UDP postdissector entry point and attempted to wrap an AVTP NTSCF packet containing an ACF LIN message with padding larger than the remaining LIN payload. The target build exited cleanly, likely because the fuzzer invokes UDP as a postdissector with limited packet context and the crafted wrapper did not reach the column-formatting sink that consumes the unchecked payload length.
- Several Ruby snippets exercised constant-false or constant-true loop elimination in expression position, including assignments, block expressions, break values, return paths, and for-loop variants. They compiled and executed cleanly under the fuzzer, so the missing value-push invariant likely requires a more specific AST shape than the tested eliminated-loop expressions.
- Inputs were wrapped in the libxml2 fuzzer format with an options word, a main URL string, and a main XML entity. Malformed XML that stresses error-context printing and incomplete UTF-8 sequences placed near parser-buffer boundaries exited cleanly. The generic fuzzer error handler and push-parser chunking likely avoid the exact error-formatting state needed for this bug with the tested shapes.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
