---
type: causal-policy
title: "No Crash Wrong Envelope For Configured Dissector Wireshark IP Dissector Input Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal wrong_envelope_for_configured_dissector."
failure_class: "no_crash"
verifier_signal: "wrong_envelope_for_configured_dissector"
candidate_family: "construct"
input_format: "wireshark-ip-dissector-input"
harness_convention: "fuzzshark"
vuln_class: "buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrong-envelope-for-configured-dissector", "wireshark-ip-dissector-input", "negative-memory", "round-20"]
match_keys: ["no-crash", "wrong-envelope-for-configured-dissector", "wireshark-ip-dissector-input"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Wrong Envelope For Configured Dissector Wireshark IP Dissector Input Negative Memory

- key: `no_crash x wrong_envelope_for_configured_dissector`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[wireshark-ip-dissector-input]]
- harnesses: [[fuzzshark]]

## Dead End
The round 20 attempts for `wireshark-ip-dissector-input` under `fuzzshark` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- The source bug is in the VJ-compressed TCP dissector, but the generated harness is configured for the IP dissector and accepts raw IP payload bytes rather than pcap or PPP envelopes. PPP and PPP-with-direction envelopes carrying VJ protocol selectors did not route to the vulnerable dissector. A successful candidate likely needs an IP-level route that causes Wireshark to invoke the VJ dissector or a different harness configuration.

## Negative Policy
When retrieval matches `no_crash x wrong_envelope_for_configured_dissector`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[wireshark-ip-dissector-input]] and [[fuzzshark]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
