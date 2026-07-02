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

## Round 38 Factual Contract

### Schema / Invariants
- ISOBMFF boxes use a big-endian size and four-character type header. Container sizes must stay coherent through the moov, trak, mdia, minf, stbl, and stsd hierarchy. Audio sample entries contain fixed sample-entry fields followed by child boxes; an MP4 audio entry may carry an esds descriptor directly or inside a QuickTime-style wave child, and malformed siblings can affect GPAC's sample-entry child registration and teardown.

### Harness Links
- [[afl-libfuzzer-file-wrapper]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
