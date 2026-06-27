---
type: causal-policy
title: Som Library Archive Parser Reached Sink Mismatch But Official Target Match Verified Recovery
description: Server-verified recovery for som-library-archive when wrong_sink pairs with parser_reached_sink_mismatch_but_official_target_match.
failure_class: wrong_sink
verifier_signal: parser_reached_sink_mismatch_but_official_target_match
candidate_family: construct
input_format: som-library-archive
harness_convention: libfuzzer-tempfile-bfd
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: high
tags: [wrong-sink, parser-reached-sink-mismatch-but-official-target-match, som-library-archive, libfuzzer-tempfile-bfd, construct, heap-buffer-overflow-read, verified-recovery]
match_keys: [wrong-sink, parser-reached-sink-mismatch-but-official-target-match, som-library-archive, libfuzzer-tempfile-bfd, construct, heap-buffer-overflow-read, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a som-library-archive candidate reaches `parser_reached_sink_mismatch_but_official_target_match` under `wrong_sink`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer-tempfile-bfd]]` and format contract `[[som-library-archive]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Build a valid archive envelope containing a SOM library symbol-table member. Keep the symbol-table header, hash area, dictionary, symbol record, and symbol-name area mutually consistent enough for archive-map parsing, then make a symbol record refer to a dictionary entry beyond the number of dictionary records. The vulnerable build indexes past the allocated dictionary while the fixed build rejects the inconsistent module index.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: construct.
