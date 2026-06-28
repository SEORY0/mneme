---
type: causal-policy
title: "No Crash Flow Summary Target Not Reached Pcap Containing IP Packets Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal flow_summary_target_not_reached."
failure_class: "no_crash"
verifier_signal: "flow_summary_target_not_reached"
candidate_family: "construct_pcap_rsh_candidate"
input_format: "pcap containing IP packets"
harness_convention: "nDPI reader pcap-file harness"
vuln_class: "invalid-read-or-segv"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "flow-summary-target-not-reached", "pcap-containing-ip-packets", "negative-memory", "round-20"]
match_keys: ["no-crash", "flow-summary-target-not-reached", "pcap-containing-ip-packets"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Flow Summary Target Not Reached Pcap Containing IP Packets Negative Memory

- key: `no_crash x flow_summary_target_not_reached`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[pcap-containing-ip-packets]]
- harnesses: [[ndpi-reader-pcap-file-harness]]

## Dead End
The round 20 attempts for `pcap containing IP packets` under `nDPI reader pcap-file harness` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- A minimal Ethernet/IPv4/TCP pcap with RSH-shaped payload did not reach the crashing flow-summary state. The likely missing gate is nDPI protocol classification plus flow completion state that leaves a non-TLS protocol union populated when the TLS summary branch reads it.

## Negative Policy
When retrieval matches `no_crash x flow_summary_target_not_reached`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[pcap-containing-ip-packets]] and [[ndpi-reader-pcap-file-harness]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
