---
type: causal-policy
title: Config Hex Digest Stack Buffer Recovery
description: Recover config parser stack writes by selecting the hex digest option parser and oversizing the digest value.
failure_class: wrong_sink
verifier_signal: sanitizer_crash
candidate_family: construct
input_format: config
harness_convention: libfuzzer
vuln_class: stack-buffer-overflow-write
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong_sink, sanitizer_crash, config, hex_digest, option_parser]
match_keys: [wrong_sink, sanitizer_crash, config, hex_digest_option]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
For broker or service config targets that name a hex digest option, preserve a syntactically valid config and place the overflow in the digest option value. Leading zero-pair dominated hex text can keep conversion active while exceeding the fixed stack buffer.

## Procedure
1. Build a minimal accepted configuration envelope.
2. Select the SHA-style or digest-style hexadecimal option parser.
3. Use a long hex-looking value dominated by simple pairs.
4. Keep option names, separators, and section syntax valid.
5. Treat helper-level sanitizer crashes as candidates when they occur inside the digest conversion path.

## Negative Memory
- Do not mutate unrelated config keys after the digest option is identified.
- Do not use non-hex characters that stop conversion before the stack buffer copy.
- Do not corrupt section syntax while testing digest length.
