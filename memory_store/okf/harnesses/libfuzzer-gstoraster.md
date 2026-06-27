---
type: harness-contract
title: "Libfuzzer Gstoraster harness"
description: "Input contract facts for libfuzzer gstoraster."
tags: ["libfuzzer-gstoraster", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Gstoraster Harness

## Round 11 Input Contract
- The gstoraster libFuzzer target runs the whole input through Ghostscript rasterization. There is no custom prefix; the interpreter chooses PDF or PostScript from the raw input syntax.

## Format Links
- [[pdf-postscript-font-resource]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 13 Facts
- The gstoraster harness passes the raw input bytes through Ghostscript stdin with cups output-device arguments, quiet/batch/no-pause flags, and no leading mode selector or FuzzedDataProvider carving.
- The harness is the same raw gstoraster libFuzzer target as other Ghostscript tasks: no input prefix, no external file dependencies, and Ghostscript is invoked with fixed cups rasterization arguments.
