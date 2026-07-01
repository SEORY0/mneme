---
type: harness-contract
title: "Honggfuzz Compatible Libxml2 XML Fuzzer"
description: "Round 36 factual harness contract for honggfuzz-compatible-libxml2-xml-fuzzer."
tags: ["honggfuzz-compatible-libxml2-xml-fuzzer", "round-36", "harness-contract"]
okf_support: 1
train_only: true
---
# Honggfuzz Compatible Libxml2 XML Fuzzer

## Round 36 Input Contract
- The packaged target runs the libxml2 XML fuzz target through a honggfuzz-compatible single-input wrapper. The fuzzer runs pull, push, and reader parser paths over the main entity. In the reader path it calls xmlReaderForMemory with the parser options, repeatedly calls xmlTextReaderRead, iterates attributes for element nodes, and frees the text reader at the end. Local runner verify can report no_crash for this wrapper even when direct image execution and official submit show the target crash.

## Round 36 Format Links
- [[libxml2-xml-fuzzer-entity-envelope]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
