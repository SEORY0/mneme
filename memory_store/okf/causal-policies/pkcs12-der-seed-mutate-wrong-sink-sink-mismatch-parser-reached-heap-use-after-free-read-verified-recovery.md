---
type: causal-policy
title: "PKCS12 Der Seed Mutate Wrong Sink Sink Mismatch Parser Reached Heap Use After Free Read Verified Recovery"
description: "Round 32 server-verified recovery for pkcs12-der keyed by wrong_sink x sink_mismatch_parser_reached."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch_parser_reached"
candidate_family: "seed_mutate"
input_format: "pkcs12-der"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch-parser-reached", "pkcs12-der", "libfuzzer", "seed-mutate", "heap-use-after-free-read", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "sink-mismatch-parser-reached", "pkcs12-der", "libfuzzer", "seed-mutate", "heap-use-after-free-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# PKCS12 Der Seed Mutate Wrong Sink Sink Mismatch Parser Reached Heap Use After Free Read Verified Recovery

- key: `wrong_sink x sink_mismatch_parser_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[pkcs12-der]]
- related harness facts: [[libfuzzer]]

## Policy
When `pkcs12-der` under `[[libfuzzer]]` produces `sink_mismatch_parser_reached` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[pkcs12-der]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Start from a valid PKCS#12 DER seed containing key, certificate, and CRL material. Preserve the outer ASN.1 and safe-content structure, but mutate a byte inside the encrypted CRL content so the parser initializes the CRL output and then fails during CRL import. The vulnerable error path deinitializes the CRL object without clearing the caller-visible pointer, and the shared cleanup path deinitializes the stale pointer again. The fixed build clears or avoids the stale output on the failing path.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- PKCS#12 DER is an ASN.1 container with authenticated safe contents and nested bags for private keys, certificates, and optional CRLs. Valid encrypted-safe structure can be retained while perturbing decrypted bag contents enough to make one imported object fail after its output has been initialized.

## Harness Contract
- The GnuTLS libFuzzer harness passes raw bytes as a DER PKCS#12 blob, uses a fixed password, checks the MAC result but continues into simple parsing, and then deinitializes returned key, certificate-chain, extra-certificate, and CRL outputs according to the parser result.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed_mutate.
