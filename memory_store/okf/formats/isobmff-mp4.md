---
type: format-family
title: "Isobmff MP4 Format"
description: "Round 26 descriptive structure and invariant facts for isobmff-mp4."
tags: ["isobmff-mp4", "round-26"]
okf_support: 1
train_only: true
---
# Isobmff MP4 Format

## Round 26 Factual Contract

### Schema / Invariants
- ISO BMFF boxes use big-endian size and four-character type headers, with container sizes that must remain consistent up the moov/trak/mdia/minf/stbl/stsd chain. Audio sample entries contain fixed sample-entry and audio fields followed by child boxes such as esds or QuickTime wave. A wave child can itself contain codec configuration boxes, and malformed sibling boxes can force the audio sample-entry fallback that scans raw child payload for a descriptor box.

### Harness Links
- [[libfuzzer-file-wrapper]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
