---
type: causal-policy
title: Lwan Config Parser Reached Config Lexer No Sanitizer Signal Negative Memory
description: Negative memory for lwan-config candidates that ended in no_crash with verifier signal `parser_reached_config_lexer_no_sanitizer_signal`.
failure_class: no_crash
verifier_signal: parser_reached_config_lexer_no_sanitizer_signal
candidate_family: construct
input_format: lwan-config
harness_convention: libfuzzer
vuln_class: out-of-bounds-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-config-lexer-no-sanitizer-signal, lwan-config, libfuzzer, construct, out-of-bounds-read, negative-memory]
match_keys: [no-crash, parser-reached-config-lexer-no-sanitizer-signal, lwan-config, libfuzzer, construct, out-of-bounds-read, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `parser_reached_config_lexer_no_sanitizer_signal`` for `lwan-config` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `parser_reached_config_lexer_no_sanitizer_signal`.
2. Stop repeating the dead-end basin: Triple-quoted and boundary-sized config strings reached the config lexer and produced normal parse errors or clean EOF behavior. Empty, one-character, two-character, explicit multiline, key-value multiline, and static-buffer-boundary variants did not produce a sanitizer-visible overread.
3. Rebuild around `[[lwan-config]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 10.
