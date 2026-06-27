---
type: format-family
title: file-magic-corpus-directory format
description: Structure and reachability facts for file-magic-corpus-directory inputs.
tags: [file-magic-corpus-directory]
okf_support: 0
---
# File Magic Corpus Directory Format

## Round 10 Factual Contract

### Schema / Invariants
- The visible source includes a libmagic fuzz entry that can consume raw buffers, but the selected runtime wrapper did not run that entry as a single-file raw-buffer target. File-magic offset arithmetic bugs require a magic rule path that computes derived offsets from matched input.

### Harness Links
- [[afl-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
