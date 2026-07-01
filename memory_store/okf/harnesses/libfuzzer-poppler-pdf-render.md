---
type: harness-contract
title: "Libfuzzer Poppler Pdf Render harness"
description: "Input contract facts for libfuzzer-poppler-pdf-render."
tags: ["libfuzzer-poppler-pdf-render", "round-33"]
okf_support: 1
---
# Libfuzzer Poppler Pdf Render Harness

## Round 33 Input Contract

### Input Contract
- The libFuzzer input is used directly as PDF bytes through Poppler's raw-data document loader. If the document loads and is not locked, the harness renders pages, including annotations. There is no mode selector, FuzzedDataProvider consumption, or external file wrapper.

### Format Links
- [[pdf]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 36 Input Contract
- The libFuzzer target feeds the entire file buffer directly to poppler::document::load_from_raw_data, skips unloadable or locked documents, then iterates every page and renders through poppler::page_renderer. There is no mode selector, filename wrapper, checksum, length suffix, or FuzzedDataProvider split; all bytes are raw PDF document bytes.

## Round 36 Format Links
- [[pdf]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
