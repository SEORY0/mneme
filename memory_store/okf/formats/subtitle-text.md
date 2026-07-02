---
type: format-family
title: subtitle-text format
description: Structure and reachability facts for subtitle-text inputs.
tags: [subtitle-text]
okf_support: 0
---
# Subtitle Text Format

## Round 10 Factual Contract

### Schema / Invariants
- Subtitle formats such as WebVTT and SubRip are line-oriented text with timestamp cues followed by cue text. Markup tags inside cue text are escaped/unescaped and then passed to cleanup that tracks allowed open and close tags.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 26 Factual Contract


### Schema / Invariants
- The relevant subtitle carrier is line-oriented text. LRC autodetection is entered by a leading bracketed line and then walks newline-separated entries looking for bracket and colon structure; a blank line before another line becomes a zero-length split entry.

### Harness Links
- [[libfuzzer-typefind]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
