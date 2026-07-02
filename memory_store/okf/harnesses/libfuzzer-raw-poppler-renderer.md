---
type: harness-contract
title: "Libfuzzer Raw Poppler Renderer harness"
description: "Input contract facts for Libfuzzer Raw Poppler Renderer."
tags: ["libfuzzer-raw-poppler-renderer", "round-21"]
okf_support: 2
---
# Libfuzzer Raw Poppler Renderer Harness

## Round 21 Input Contract (pdf)

- The fuzzer passes raw PDF bytes to Poppler's raw-data document loader. If the document loads and is not locked, the harness creates and renders every page, deletes each page object, then deletes the document, so page annotation loading and object destruction both run.

## Round 21 Format Links (pdf)
- [[pdf]]

## Round 21 Notes (pdf)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 32 Input Contract
- The Poppler C++ libFuzzer target passes the raw input bytes to load_from_raw_data, ignores locked or unloadable documents, then creates and renders every page. There is no byte carving, selector, secondary file, or FuzzedDataProvider layout.

## Round 32 Format Links
- [[pdf]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
