---
type: harness-contract
title: "Libfuzzer Libxml2 Html harness"
description: "Input contract facts for libfuzzer-libxml2-html."
tags: ["libfuzzer-libxml2-html", "round-16"]
okf_support: 1
---
# Libfuzzer Libxml2 Html Harness

## Round 16 Input Contract
- The first bytes are consumed as an integer options field. The remaining bytes are parsed through both the normal HTML parser and a push parser that feeds bounded chunks from the same buffer. There is no filename, archive wrapper, or checksum gate.

## Round 16 Format Links
- [[html]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
