---
type: causal-policy
title: "FLAC CLI Fuzzer Input Construct Target Stack Observed But Local Classifier Missed Fixed Clean Assertion Abort Verified Recovery"
description: "Round 26 verified recovery for no_crash with verifier signal target_stack_observed_but_local_classifier_missed_fixed_clean."
failure_class: "no_crash"
verifier_signal: "target_stack_observed_but_local_classifier_missed_fixed_clean"
candidate_family: "construct"
input_format: "flac-cli-fuzzer-input"
harness_convention: "libfuzzer"
vuln_class: "assertion-abort"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "target-stack-observed-but-local-classifier-missed-fixed-clean", "flac-cli-fuzzer-input", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["no_crash", "target_stack_observed_but_local_classifier_missed_fixed_clean", "flac-cli-fuzzer-input", "libfuzzer", "assertion-abort", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# FLAC CLI Fuzzer Input Construct Target Stack Observed But Local Classifier Missed Fixed Clean Assertion Abort Verified Recovery

- key: `no_crash x target_stack_observed_but_local_classifier_missed_fixed_clean`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[flac-cli-fuzzer-input]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build a FLAC tool-fuzzer input whose argv section enables ReplayGain application while decoding to raw output. The FLAC payload must place ReplayGain comments before the stream-info metadata has established the output bit depth, then later provide stream-info and a minimal audio frame using a sample width that violates ReplayGain synthesis assumptions. The vulnerable build leaves ReplayGain application enabled when the comments are seen with unknown bit depth; the fixed build disables that path, so the later frame reaches the assertion only in the vulnerable build.

## Policy
For `no_crash x target_stack_observed_but_local_classifier_missed_fixed_clean` on `flac-cli-fuzzer-input`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `flac-cli-fuzzer-input` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `flac-cli-fuzzer-input` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
FLAC files begin with the FLAC marker, followed by metadata blocks and then audio frames. Vorbis-comment metadata contains a vendor string and key/value comments such as ReplayGain reference, gain, and peak fields. Stream-info metadata later supplies sample geometry including bits per sample. Valid frames require internally consistent frame headers and frame checksums for the decoder to reach audio synthesis.

## Harness Contract
The FLAC libFuzzer tool harness uses a leading control byte to choose the maximum number of command-line arguments and whether stdin is used. It then parses NUL-delimited argv strings from the front of the input; the remaining bytes become the FLAC file payload or stdin data according to the control bit. There is no checksum or length wrapper outside the CLI-argument carving.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 6 attempts.
- Scope: generator repair and retargeting only.
