---
type: causal-policy
title: "Openpgp Signed Message Seed Mutate Parser Reached Proc Plaintext Uaf Heap Use After Free Read Verified Recovery"
description: "Round 13 verified recovery for wrong_sink with verifier signal parser_reached_proc_plaintext_uaf."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_proc_plaintext_uaf"
candidate_family: "seed_mutate"
input_format: "openpgp signed message"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-proc-plaintext-uaf", "openpgp-signed-message", "seed-mutate", "verified-recovery", "round-13"]
match_keys: ["wrong_sink", "parser_reached_proc_plaintext_uaf", "openpgp signed message", "libfuzzer", "heap-use-after-free-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 13
---
# Openpgp Signed Message Seed Mutate Parser Reached Proc Plaintext Uaf Heap Use After Free Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_proc_plaintext_uaf`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a structurally valid signed OpenPGP message that routes through signature verification and plaintext packet processing. The useful carrier is a signed compressed/plaintext sample; preserving the signature-message envelope is more important than mutating packet bytes. The vulnerable build frees plaintext-related packet state and later reads it while processing the signed data path; the fixed build avoids that stale access.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, exact offsets, checksums, or submit metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- OpenPGP signed-message inputs must preserve packet framing well enough for GPG verification to parse literal/plaintext content under a signature. Signed and clearsigned repository samples reached the plaintext handler; encrypted-message samples did not exercise the same verification path.

## Harness Contract
- The selected wrapper is the GPG signature-verification libFuzzer target. It writes raw input bytes to a temporary GPG file, initializes a temporary homedir/trustdb, then runs signature verification APIs on that file. There is no front selector or FuzzedDataProvider carving.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, task-local identifiers, or submit metadata.

## Evidence Shape
- Support: one round-13 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
## Round 13 Reinforcement

- key: `wrong_sink x parser_reached_proc_plaintext_uaf`
- candidate family: `seed_mutate`
- related format facts: [[openpgp-signed-message]]
- related harness facts: [[libfuzzer]]

### Procedure Delta
Use a structurally valid signed OpenPGP message that routes through signature verification and plaintext packet processing. The useful carrier is a signed compressed/plaintext sample; preserving the signature-message envelope is more important than mutating packet bytes. The vulnerable build frees plaintext-related packet state and later reads it while processing the signed data path; the fixed build avoids that stale access.

### Format Contract Delta
OpenPGP signed-message inputs must preserve packet framing well enough for GPG verification to parse literal/plaintext content under a signature. Signed and clearsigned repository samples reached the plaintext handler; encrypted-message samples did not exercise the same verification path.

### Harness Contract Delta
The selected wrapper is the GPG signature-verification libFuzzer target. It writes raw input bytes to a temporary GPG file, initializes a temporary homedir/trustdb, then runs signature verification APIs on that file. There is no front selector or FuzzedDataProvider carving.

### Evidence Shape
- Support: additional round-13 official target match.
- Scope: generator repair for the same failure-keyed basin.
