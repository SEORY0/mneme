---
type: harness-contract
title: "Libfuzzer Libxslt Entity Framing With Malloc Limit Harness"
description: "Input contract facts for libfuzzer-libxslt-entity-framing-with-malloc-limit."
tags: ["libfuzzer-libxslt-entity-framing-with-malloc-limit", "round-27"]
okf_support: 1
---
# Libfuzzer Libxslt Entity Framing With Malloc Limit Harness

## Round 27 Input Contract
- The harness parses the fuzz-entity table, requires both stylesheet and source document entities, parses the source XML and stylesheet XML, installs XSLT namespaces and security preferences, then arms the allocation-failure limit immediately before stylesheet construction and parsing.
- The limit controls xmlMalloc/xmlRealloc failures during stylesheet compilation and later clears before cleanup.

## Round 27 Format Links
- [[libxslt-fuzz-entities]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
