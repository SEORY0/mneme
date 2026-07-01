---
type: "negative-memory"
title: "Php Source Construct No Crash Official Wrapper Did Not Execute Raw File Generic Crash Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal official_wrapper_did_not_execute_raw_file."
failure_class: "no_crash"
verifier_signal: "official_wrapper_did_not_execute_raw_file"
candidate_family: "construct"
input_format: "php-source"
harness_convention: "libfuzzer"
vuln_class: "generic-crash"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "official-wrapper-did-not-execute-raw-file", "php-source", "libfuzzer", "construct", "generic-crash", "negative-memory", "round-38"]
match_keys: ["no_crash", "official_wrapper_did_not_execute_raw_file", "php-source", "libfuzzer", "generic-crash", "negative-memory", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Php Source Construct No Crash Official Wrapper Did Not Execute Raw File Generic Crash Negative Memory

- key: `no_crash x official_wrapper_did_not_execute_raw_file`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[php-source]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The strongest candidate is raw PHP source that creates a shutdown destructor, forces the fuzzer step-budget bailout in normal user code, then has the destructor start a fiber that also exhausts the step budget from inside the fiber. Under direct single-input libFuzzer execution this crashes the vulnerable build and the fixed build exits cleanly. The official verify/submit wrapper for this task invokes the PHP fuzzer without the single-input run flag, causing libFuzzer to treat the mounted PoC path as a corpus directory and return without executing the raw PHP file, so official submit reports no vulnerable exit.

## Observed Basin
- Failure trajectory classes: no_crash, generic_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x official_wrapper_did_not_execute_raw_file` on `[[php-source]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `official_wrapper_did_not_execute_raw_file` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `official_wrapper_did_not_execute_raw_file`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 4 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
