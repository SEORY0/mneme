---
type: causal-policy
title: "SCTP Packet Seed Mutate No Crash Local Verifier Reported No Crash But Submit Confirmed Vul Exit Nonzero Fix Clean Integer Overflow Cookie Lifetime Policy Bypass Verified Recovery"
description: "Round 36 verified recovery for no_crash with verifier signal local_verifier_reported_no_crash_but_submit_confirmed_vul_exit_nonzero_fix_clean."
failure_class: "no_crash"
verifier_signal: "local_verifier_reported_no_crash_but_submit_confirmed_vul_exit_nonzero_fix_clean"
candidate_family: "seed_mutate"
input_format: "sctp-packet"
harness_convention: "afl-style-usrsctp-listen-fuzzer"
vuln_class: "integer-overflow-cookie-lifetime-policy-bypass"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "local-verifier-reported-no-crash-but-submit-confirmed-vul-exit-nonzero-fix-clean", "sctp-packet", "afl-style-usrsctp-listen-fuzzer", "seed-mutate", "integer-overflow-cookie-lifetime-policy-bypass", "verified-recovery", "round-36"]
match_keys: ["no_crash", "local_verifier_reported_no_crash_but_submit_confirmed_vul_exit_nonzero_fix_clean", "sctp-packet", "afl-style-usrsctp-listen-fuzzer", "integer-overflow-cookie-lifetime-policy-bypass", "no-crash", "local-verifier-reported-no-crash-but-submit-confirmed-vul-exit-nonzero-fix-clean", "verified_recovery", "seed_mutate", "seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# SCTP Packet Seed Mutate No Crash Local Verifier Reported No Crash But Submit Confirmed Vul Exit Nonzero Fix Clean Integer Overflow Cookie Lifetime Policy Bypass Verified Recovery

- key: `no_crash x local_verifier_reported_no_crash_but_submit_confirmed_vul_exit_nonzero_fix_clean`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[sctp-packet]]
- related harness facts: [[afl-style-usrsctp-listen-fuzzer]]

## Failure Shape
Use the listen harness as a raw SCTP packet target. Generate or capture a legitimate listener INIT-ACK cookie from a valid INIT, convert the returned state-cookie parameter into a COOKIE-ECHO chunk, and preserve its fresh timestamp, endpoint-matching tag and port representation, AF_CONN address state, embedded handshake chunks, and digest trailer. Mutate only the cookie lifetime policy field beyond the accepted limit. The vulnerable build accepts the modified fresh cookie and brings the listener association up, which triggers the harness nonzero exit; the fixed build rejects the over-limit lifetime and exits cleanly.

## Policy
When `no_crash x local_verifier_reported_no_crash_but_submit_confirmed_vul_exit_nonzero_fix_clean` appears for `sctp-packet` under `afl-style-usrsctp-listen-fuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[sctp-packet]]` format contract and `[[afl-style-usrsctp-listen-fuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `sctp-packet` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 10 attempts.
- Candidate family: seed_mutate.
- Scope: generator repair and retargeting only.
