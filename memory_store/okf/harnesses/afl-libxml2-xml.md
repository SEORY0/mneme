---
type: harness-contract
title: "Afl Libxml2 Xml harness"
description: "Input contract facts for afl-libxml2-xml."
tags: ["afl-libxml2-xml", "round-24"]
okf_support: 1
---
# Afl Libxml2 Xml Harness

## Round 24 Factual Contract

### Input Contract
- The AFL-style wrapper passes the whole file to libxml2 fuzz glue. The target runs pull parsing, push parsing, reader traversal, optional XInclude processing, and serialization over the main entity from the envelope.

### Format Links
- [[xml-entity-envelope]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
