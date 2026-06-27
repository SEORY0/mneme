---
type: causal-policy
title: Libredwg Json Parser Reached Dynapi Header Set Value Verified Recovery
description: Server-verified recovery for libredwg-json when wrong_sink pairs with parser_reached_dynapi_header_set_value.
failure_class: wrong_sink
verifier_signal: parser_reached_dynapi_header_set_value
candidate_family: construct
input_format: libredwg-json
harness_convention: libfuzzer
vuln_class: stack-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: high
tags: [wrong-sink, parser-reached-dynapi-header-set-value, libredwg-json, libfuzzer, construct, stack-buffer-overflow-read, verified-recovery]
match_keys: [wrong-sink, parser-reached-dynapi-header-set-value, libredwg-json, libfuzzer, construct, stack-buffer-overflow-read, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a libredwg-json candidate reaches `parser_reached_dynapi_header_set_value` under `wrong_sink`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer]]` and format contract `[[libredwg-json]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Use the JSON parser entry by starting with a JSON object containing a HEADER object. Populate several primitive header fields that are accepted by the dynamic API before the target field. When the vulnerable setter handles a primitive header field whose dynamic metadata size is much larger than the stack temporary used by the JSON importer, the memcpy in the dynamic helper reads beyond the stack object and crashes only in the vulnerable build.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: construct.
