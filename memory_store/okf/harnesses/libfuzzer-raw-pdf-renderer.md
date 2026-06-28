---
type: harness-contract
title: "Libfuzzer Raw PDF Renderer harness"
description: "Input contract facts for libfuzzer-raw-pdf-renderer."
tags: ["libfuzzer-raw-pdf-renderer"]
okf_support: 0
---
# Libfuzzer Raw PDF Renderer Harness

## Round 10 Input Contract
- The harness feeds the whole byte buffer to Poppler as a PDF, opens the document from raw memory, skips encrypted documents, then walks pages through render/text paths. There is no mode byte or FuzzedDataProvider carving.
- The harness feeds raw PDF bytes to Poppler and renders pages. There is no FuzzedDataProvider split; parser reachability depends on PDF validity and page renderability.

## Round 10 Format Links
- [[pdf]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
