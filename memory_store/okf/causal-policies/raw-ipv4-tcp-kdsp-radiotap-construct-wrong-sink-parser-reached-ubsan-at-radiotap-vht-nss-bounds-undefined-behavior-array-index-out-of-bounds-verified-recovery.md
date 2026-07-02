---
type: causal-policy
title: "Raw Ipv4 Tcp Kdsp Radiotap Construct Wrong Sink Parser Reached Ubsan At Radiotap Vht Nss Bounds Undefined Behavior Array Index Out Of Bounds Verified Recovery"
description: "Server-verified recovery for raw-ipv4-tcp-kdsp-radiotap when wrong_sink pairs with parser_reached_ubsan_at_radiotap_vht_nss_bounds."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_ubsan_at_radiotap_vht_nss_bounds"
candidate_family: "construct"
input_format: "raw-ipv4-tcp-kdsp-radiotap"
harness_convention: "libfuzzer-fuzzshark-ip"
vuln_class: "undefined-behavior-array-index-out-of-bounds"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-ubsan-at-radiotap-vht-nss-bounds", "raw-ipv4-tcp-kdsp-radiotap", "libfuzzer-fuzzshark-ip", "construct", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-ubsan-at-radiotap-vht-nss-bounds", "raw-ipv4-tcp-kdsp-radiotap", "libfuzzer-fuzzshark-ip", "construct", "undefined-behavior-array-index-out-of-bounds", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Raw Ipv4 Tcp Kdsp Radiotap Construct Wrong Sink Parser Reached Ubsan At Radiotap Vht Nss Bounds Undefined Behavior Array Index Out Of Bounds Verified Recovery

- key: `wrong_sink x parser_reached_ubsan_at_radiotap_vht_nss_bounds`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[raw-ipv4-tcp-kdsp-radiotap]]
- related harness facts: [[libfuzzer-fuzzshark-ip]]

## Policy
When `wrong_sink x parser_reached_ubsan_at_radiotap_vht_nss_bounds` appears for `raw-ipv4-tcp-kdsp-radiotap`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-fuzzshark-ip` harness contract and the `raw-ipv4-tcp-kdsp-radiotap` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Reach the IP-target fuzzshark through a syntactically valid raw IPv4 packet carrying a TCP KDSP capture message. In the KDSP capture-data header, select the radiotap datalink subdissector and report a payload length matching the nested radiotap frame. In radiotap, set the VHT present field and the known flags needed for guard interval and bandwidth so rate calculation remains enabled, then make one VHT user carry a valid MCS with the maximum accepted one-based spatial-stream count. The vulnerable radiotap code checks the NSS as if it were bounded but indexes the validity table without converting from one-based NSS to the zero-based array index.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[raw-ipv4-tcp-kdsp-radiotap]]. fuzzshark_ip expects a raw IP packet, not a pcap file. KDSP is reachable through TCP from IP dissection and frames messages with a fixed command/length header followed by a capture-packet bitmap. A KDSP capture-data header can carry both a reported payload length and a datalink selector; the radiotap datalink selector hands the remaining payload to the radiotap dissector. Radiotap uses a little-endian header with a present bitmap; present fields are naturally aligned. The VHT radiotap field includes known flags, flag bits, bandwidth, and per-user MCS/NSS nibbles; rate calculation requires known bandwidth and guard interval.

## Harness Contract
Use [[libfuzzer-fuzzshark-ip]]. The libFuzzer input is consumed as raw packet bytes by fuzzshark_ip. There is no FuzzedDataProvider, no leading mode selector, and no pcap reader in this path. The IP dissector is registered as a postdissector over the full input buffer, so nested protocols must be carried by a valid raw IP packet and then dispatched through normal IP, TCP, and dissector-table routing.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x parser_reached_ubsan_at_radiotap_vht_nss_bounds`.
- Vulnerability class: `undefined-behavior-array-index-out-of-bounds`.
- Recovery summary: Reach the IP-target fuzzshark through a syntactically valid raw IPv4 packet carrying a TCP KDSP capture message. In the KDSP capture-data header, select the radiotap datalink subdissector and report a payload length matching the nested radiotap frame. In radiotap, set the VHT present field and the known flags needed for guard interval and bandwidth so rate calculation remains enabled, then make one VHT user carry a valid MCS with the maximum accepted one-based spatial-stream count. The vulnerable radiotap code checks the NSS as if it were bounded but indexes the validity table without converting from one-based NSS to the zero-based array index.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
