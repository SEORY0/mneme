---
type: causal-policy
title: "Fuzzing Datasource RSA Fields Construct Parser Reached Target Sink Out Of Bounds Read Verified Recovery"
description: "Round 15 server-verified recovery for fuzzing-datasource-rsa-fields keyed by wrong_sink x parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "fuzzing-datasource-rsa-fields"
harness_convention: "libfuzzer-wolfssl-rsa"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink", "fuzzing-datasource-rsa-fields", "libfuzzer-wolfssl-rsa", "construct", "out-of-bounds-read", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "fuzzing-datasource-rsa-fields", "libfuzzer-wolfssl-rsa", "out-of-bounds-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# Fuzzing Datasource RSA Fields Construct Parser Reached Target Sink Out Of Bounds Read Verified Recovery

- key: `wrong_sink x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[fuzzing-datasource-rsa-fields]]
- related harness facts: [[libfuzzer-wolfssl-rsa]]

## Policy
When `fuzzing-datasource-rsa-fields` under `libfuzzer-wolfssl-rsa` reaches `parser_reached_target_sink` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Use the RSA fuzzing datasource envelope rather than raw hex. Keep the arbitrary input and scalar
   controls minimal, choose fixed values for the unrelated RSA components, and place a valid
   nonzero hexadecimal string exactly at the fast-math full-limb boundary in one parsed RSA integer
   field. This causes the radix-16 reader to advance the word index after filling the last limb and
   then clamp using an out-of-range used count.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- The RSA fuzzer consumes length-prefixed byte vectors and strings using the fuzzing-headers
  datasource format. Each variable-length field starts with a little-endian length, while scalar and
  boolean fields are also preceded by a length word that is clamped to the scalar size. The RSA path
  parses P, Q, E, and D from hex strings unless boolean controls select built-in fixed values.

## Harness Contract
- The selected target is the wolfSSL RSA libFuzzer harness. It first reads an input blob, output size
  and operation controls, then booleans deciding whether P, Q, and E are fixed. It parses the
  remaining RSA integer strings with mp_read_radix before running the selected RSA operation; choosing
  an operation outside the handled cases avoids needing additional operation-specific blobs.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.
