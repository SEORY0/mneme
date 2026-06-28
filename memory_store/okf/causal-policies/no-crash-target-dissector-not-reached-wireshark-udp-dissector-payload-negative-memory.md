---
type: causal-policy
title: "No Crash Target Dissector Not Reached Wireshark UDP Dissector Payload Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal target_dissector_not_reached."
failure_class: "no_crash"
verifier_signal: "target_dissector_not_reached"
candidate_family: "construct-l2cap-and-udp-encapsulation-probes"
input_format: "wireshark-udp-dissector-payload"
harness_convention: "libfuzzer-fuzzshark-udp"
vuln_class: "tree-key-length-invariant-violation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "target-dissector-not-reached", "wireshark-udp-dissector-payload", "negative-memory", "round-20"]
match_keys: ["no-crash", "target-dissector-not-reached", "wireshark-udp-dissector-payload"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Target Dissector Not Reached Wireshark UDP Dissector Payload Negative Memory

- key: `no_crash x target_dissector_not_reached`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[wireshark-udp-dissector-payload]]
- harnesses: [[libfuzzer-fuzzshark-udp]]

## Dead End
The round 20 attempts for `wireshark-udp-dissector-payload` under `libfuzzer-fuzzshark-udp` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Bare L2CAP signaling, UDP-prefixed payloads, GSMTAP-like wrapping, H4 ACL-like wrapping, and repeated signaling commands all exited cleanly. The target dissector was not reached because the active fuzzshark entry point is the UDP dissector table, and the missing gate is the UDP-side encapsulation or decode-as path that hands payloads to Bluetooth L2CAP.

## Negative Policy
When retrieval matches `no_crash x target_dissector_not_reached`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[wireshark-udp-dissector-payload]] and [[libfuzzer-fuzzshark-udp]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
