---
type: strategy
title: fuzzer strategy
description: What
resource: cybergym://strategy/fuzzer
tags: [fuzzer, reachability_unknown, multi_fuzzer, no_instrument]
timestamp: 2026-06-24T00:00:00Z
okf_support: 80
---
## What
Run the project's OWN libFuzzer/AFL harness binary as a FUZZER (not single-input) so coverage-guided
mutation rediscovers the crash. The CyberGym/OSS-Fuzz bug was originally found this way, so the same
harness finds it again — no hand-construction of the exact input needed.

## When
DEEP STATEFUL bugs (multi-step protocol/parser flows where hand-building the input is impractical:
smartcard PKCS#15, TLS, DB engines) and FLAKY/uninitialized bugs (a single crafted input crashes only
sometimes — the fuzzer finds the canonical minimal reproducer that crashes reliably).

## Steps
1. Find the harness binary (`/out/<name>_fuzzer`) + its seed corpus zip (`*_seed_corpus.zip`); unzip it.
2. Fuzz with the corpus: `BIN -jobs=8 -workers=8 -max_total_time=1500 -rss_limit_mb=4096 corp/`.
3. On a find, libFuzzer writes `crash-<sha1>` — that file IS the PoC. Copy it out.
4. Validate it reproduces and confirm the ASan/MSan sink matches description.txt.

## Pitfalls
- Confirm the crash sink/class matches the DESCRIBED bug; a fuzzer may surface a different bug.
- Deep flows need long campaigns; a short run finding nothing means "not yet", not "unreproducible".

## Observed
- Support: 80 train-set solves.
- Winning strategies (observed): {'fuzzer': 80}
- Format families (observed): {'cff2-font': 4, 'media-container': 18, 'file-magic': 2, 'pdf': 1, 'text-expr': 14, 'executable': 6, 'sip-text': 4, 'json': 4, 'isobmff': 1, 'config': 5, 'xml': 1, 'pcap': 1, 'elf': 1}
- Abstract sink shapes (observed): allocation-size-too-big:?, double-free:?, global-buffer-overflow:READ, global-buffer-overflow:WRITE, heap-buffer-overflow:READ, heap-buffer-overflow:WRITE, heap-use-after-free:READ, segv:?, stack-buffer-overflow:READ, undefined-behavior:?, use-of-uninitialized-value:?

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `fuzzer`
- observed: 1 traces; solved: 0 (illustrative — not for ranking)
- top vuln_classes: other (1)
- top input_formats: libxml2-valid-fuzzer-envelope (1)
- collapsed aliases: xml-fuzzer-envelope-with-entities-and-alloc-limit
<!-- END observed-census -->
