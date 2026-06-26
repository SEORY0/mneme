---
type: format-family
title: "KML format"
description: "Round 8 descriptive format facts for kml."
resource: cybergym://format/kml
tags: ["kml", "round-8"]
okf_support: 1
---
# KML Format

## Round 8 Factual Contract

### Schema / Invariants
- The KML driver recognizes raw XML content by a visible KML root element in the header, then parses nested Document and Folder containers plus Placemark feature containers. Geometry-bearing placemarks make the normal pre-layer empty-elimination path run; placemarks without geometry can keep the tree in the all-empty mode where empty folders are still considered during layer discovery.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

