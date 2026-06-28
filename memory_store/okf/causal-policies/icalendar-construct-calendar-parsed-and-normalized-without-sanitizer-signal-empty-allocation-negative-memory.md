---
type: causal-policy
title: Icalendar Calendar Parsed And Normalized Without Sanitizer Signal Negative Memory
description: Negative memory for icalendar candidates that ended in no_crash with verifier signal `calendar_parsed_and_normalized_without_sanitizer_signal`.
failure_class: no_crash
verifier_signal: calendar_parsed_and_normalized_without_sanitizer_signal
candidate_family: construct
input_format: icalendar
harness_convention: libfuzzer
vuln_class: empty-allocation
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, calendar-parsed-and-normalized-without-sanitizer-signal, icalendar, libfuzzer, construct, empty-allocation, negative-memory]
match_keys: [no-crash, calendar-parsed-and-normalized-without-sanitizer-signal, icalendar, libfuzzer, construct, empty-allocation, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `calendar_parsed_and_normalized_without_sanitizer_signal`` for `icalendar` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `calendar_parsed_and_normalized_without_sanitizer_signal`.
2. Stop repeating the dead-end basin: Valid VCALENDAR and VEVENT inputs containing REQUEST-STATUS values with an empty debug clause parsed and normalized without crashing. Duplicate request-status properties, non-empty debug controls, folded lines, and X-LIC-ERROR conversion candidates also produced clean execution. The bug may require a harness path that serializes or leak-checks the empty debug allocation differently than the observed normalization path.
3. Rebuild around `[[icalendar]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 7.
