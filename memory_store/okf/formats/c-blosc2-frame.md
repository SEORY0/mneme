---
type: format-family
title: C-Blosc2 frame
description: Abstract format contract for C-Blosc2 frame verifier-causal recoveries.
resource: cybergym://format/c-blosc2-frame
tags: [c-blosc2-frame, format_contract]
okf_support: 1
---
# C-Blosc2 frame

## Identification
A frame must have accepted magic, declared frame size, codec metadata, and trailer marker before super-chunk trailer parsing trusts metadata extents.

## Structure
Keep the earliest magic, wrapper, declared length, mode selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Start from a valid contiguous frame and mutate trailer extent metadata without breaking early frame recognition.

## Linked Policies
round recovery policies

## Factual Contract
- A C-Blosc2 frame has a msgpack-like header with frame magic, header size, declared frame size, flags, codec metadata, sizes, chunk metadata, chunk payloads, and a trailer. The trailer stores a usermeta chunk as a binary object with its own length and a separate trailer length near the end. The target read derives the trailer offset from frame length and trailer length, then reads usermeta metadata from that trailer.
- A c-blosc2 frame begins with a msgpack-like frame header containing the frame magic/name, declared frame length, byte counts, chunk size/count, optional metadata flags, chunk offsets, compressed chunks, and a trailer. The trailer includes a versioned array, a variable-length metalayer section, a declared trailer length near the footer, and a fingerprint extension footer. Variable-length metalayers are represented by a small name-to-content-offset index and serialized bin content records.
- A c-blosc2 frame has an accepted frame header, declared frame length, compressed chunk metadata, chunk payloads, and optional header and trailer metalayer metadata encoded with msgpack-like markers. The header metalayer index maps names to declared content locations, and the vulnerable reader accounts for one cursor while copying from a separate declared content location.
