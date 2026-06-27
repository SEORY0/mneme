---
type: format-family
title: "hls-m3u8-playlist-text format"
description: "Structure and reachability facts for HLS M3U8 playlist text."
resource: cybergym://format/hls-m3u8-playlist-text
tags: ["hls-m3u8-playlist-text"]
okf_support: 1
---
# HLS M3u8 Playlist Text Format

## Round 9 Factual Contract

### Schema / Invariants
- M3U8 playlists are line-oriented text beginning with an EXTM3U marker.
- Important tags include target duration, version, media sequence, key attributes, initialization
  map, stream-info entries, media renditions, partial segments, byte ranges, and media segment URI
  lines.
- Attribute values are comma-separated and many URI-like fields require quoted values.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
