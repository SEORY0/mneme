---
type: harness-contract
title: "Libfuzzer Raw Poppler Renderer harness"
description: "Input contract facts for Libfuzzer Raw Poppler Renderer."
tags: ["libfuzzer-raw-poppler-renderer", "round-21"]
okf_support: 1
---
# Libfuzzer Raw Poppler Renderer Harness

## Round 21 Input Contract (pdf)

- The fuzzer passes raw PDF bytes to Poppler's raw-data document loader. If the document loads and is not locked, the harness creates and renders every page, deletes each page object, then deletes the document, so page annotation loading and object destruction both run.

## Round 21 Format Links (pdf)
- [[pdf]]

## Round 21 Notes (pdf)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
