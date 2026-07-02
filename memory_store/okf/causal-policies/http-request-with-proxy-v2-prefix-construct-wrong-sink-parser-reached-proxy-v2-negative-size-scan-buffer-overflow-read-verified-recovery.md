---
type: causal-policy
title: "Http Request With Proxy V2 Prefix Construct Wrong Sink Parser Reached Proxy V2 Negative Size Scan Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for http-request-with-proxy-v2-prefix when wrong_sink pairs with parser_reached_proxy_v2_negative_size_scan."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_proxy_v2_negative_size_scan"
candidate_family: "construct"
input_format: "http-request-with-proxy-v2-prefix"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-proxy-v2-negative-size-scan", "http-request-with-proxy-v2-prefix", "libfuzzer", "construct", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-proxy-v2-negative-size-scan", "http-request-with-proxy-v2-prefix", "libfuzzer", "construct", "buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Http Request With Proxy V2 Prefix Construct Wrong Sink Parser Reached Proxy V2 Negative Size Scan Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_proxy_v2_negative_size_scan`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[http-request-with-proxy-v2-prefix]]
- related harness facts: [[libfuzzer]]

## Policy
When `wrong_sink x parser_reached_proxy_v2_negative_size_scan` appears for `http-request-with-proxy-v2-prefix`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `http-request-with-proxy-v2-prefix` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Construct raw libFuzzer request bytes that begin with a syntactically recognized PROXY protocol v2 prefix. Keep the command, address-family selector, and declared address span acceptable to the parser, but make the logical input shorter than that declared span. The parser advances past the logical end and then recomputes the remaining request length, underflowing the size used for the next header-terminator scan. The fixed build rejects the inconsistent buffer and length relation.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[http-request-with-proxy-v2-prefix]]. A PROXY v2-prefixed HTTP request starts with a fixed binary signature, then version/command, family/protocol, a network-order declared length, a family-specific address block, and finally the HTTP request bytes. The Lwan request parser recognizes the proxy prefix before normal HTTP parsing and uses the declared proxy span to advance to the HTTP request.

## Harness Contract
Use [[libfuzzer]]. The libFuzzer harness passes raw bytes directly. It copies them into a fixed static request buffer, enables proxy-protocol parsing in the request flags, runs the request finalizer that scans for an HTTP header terminator, and then invokes the HTTP request parser. There is no FuzzedDataProvider layout or mode-selector byte.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x parser_reached_proxy_v2_negative_size_scan`.
- Vulnerability class: `buffer-overflow-read`.
- Recovery summary: Construct raw libFuzzer request bytes that begin with a syntactically recognized PROXY protocol v2 prefix. Keep the command, address-family selector, and declared address span acceptable to the parser, but make the logical input shorter than that declared span. The parser advances past the logical end and then recomputes the remaining request length, underflowing the size used for the next header-terminator scan. The fixed build rejects the inconsistent buffer and length relation.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
