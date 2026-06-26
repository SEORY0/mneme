---
type: causal-policy
title: No Crash Protocol Not Classified To Target Negative Memory
description: Negative memory for no_crash with verifier signal protocol_not_classified_to_target.
failure_class: no_crash
verifier_signal: protocol_not_classified_to_target
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, protocol-not-classified-to-target, negative_memory]
match_keys: [no-crash, protocol-not-classified-to-target, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Protocol Not Classified To Target Negative Memory

- key: `no_crash x protocol_not_classified_to_target`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: pcap-iec104

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- Raw IEC104 and pcap-wrapped TCP payloads did not trigger the target path. The byte-level APDU length invariant was constructed, but the ntopng flow did not classify and dispatch the payload into the IEC104 statistics parser during these attempts.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
