---
type: causal-policy
title: "Raw Ipv4 Ositp Cotp Construct No Crash Parser Not Reached Unknown Negative Memory"
description: "Negative memory for raw-ipv4-ositp-cotp candidates that ended in no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "raw-ipv4-ositp-cotp"
harness_convention: "libfuzzer"
vuln_class: "unknown"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "raw-ipv4-ositp-cotp", "libfuzzer", "construct", "unknown", "negative-memory", "round-32"]
match_keys: ["no-crash", "parser-not-reached", "raw-ipv4-ositp-cotp", "libfuzzer", "construct", "unknown", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# Raw Ipv4 Ositp Cotp Construct No Crash Parser Not Reached Unknown Negative Memory

- key: `no_crash x parser_not_reached`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[raw-ipv4-ositp-cotp]]
- related harness facts: [[libfuzzer]]

## Policy
Treat `no_crash x parser_not_reached` for `[[raw-ipv4-ositp-cotp]]` under `[[libfuzzer]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: Constructed raw IPv4 packets that dispatch to OSITP/COTP and exercised empty user-data paths for data, connection, and connectionless TPDUs, including variants where the carrier advertises remaining transport payload without captured bytes. Also tried minimal payloads that satisfy several COTP heuristic subdissector gates. All local runs exited cleanly, and the official comparison confirmed the vulnerable image did not crash.
3. Rebuild around `[[raw-ipv4-ositp-cotp]]` and `[[libfuzzer]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- For this harness the input is a raw IPv4 packet, not a pcap. A complete IPv4 header is needed before OSITP is reached; the IP protocol field selects OSI transport, and the IP total length influences the reported payload length. COTP/CLTP packets begin with a length indicator followed by a TPDU type nibble. Data and connection TPDUs consume their fixed header, optional variable part, then hand the remaining tvb to COTP heuristic subdissectors; connectionless TPDUs use the CLTP heuristic list. Empty remaining payload can be represented either by matching carrier length exactly or by advertising additional payload that is not captured.

## Harness Contract
- Wireshark fuzzshark is built as a libFuzzer-style target configured for the IP dissector. The PoC file bytes are passed directly as the packet buffer to fuzzshark; there is no file-format wrapper and no FuzzedDataProvider split. The target registers the configured dissector as a postdissector, disables several unrelated dissectors at startup, and feeds the raw buffer through epan dissection with captured length equal to the PoC file size.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 17.
