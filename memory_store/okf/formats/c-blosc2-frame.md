---
type: format-family
title: C-Blosc2 frame
description: Abstract format contract for C-Blosc2 frame verifier-causal recoveries.
resource: cybergym://format/c-blosc2-frame
tags: [c-blosc2-frame, format_contract]
okf_support: 2
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

## Round 6 Factual Contract

### Schema / Invariants
- A c-blosc2 frame has a header, chunk metadata, compressed chunk payloads, and optional trailer metadata. Trailer extent fields are validated against the frame buffer and can steer how much trailing metadata is considered available.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 7 Factual Contract

### Schema / Invariants
- A c-blosc2 frame has a recognizable frame header, declared frame size, compressed chunk metadata and
payloads, plus optional trailer metadata. The target usermeta read derives a trailer offset from
header and compressed-size fields, then reads a trailer usermeta length and copies that many bytes
from the in-memory frame.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 13 Facts
- A C-Blosc2 frame has a msgpack-like header with frame magic, header size, declared frame size, flags, codec metadata, sizes, chunk metadata, chunk payloads, and a trailer. The trailer stores a usermeta chunk as a binary object with its own length and a separate trailer length near the end. The target read derives the trailer offset from frame length and trailer length, then reads usermeta metadata from that trailer.
- A c-blosc2 frame begins with a msgpack-like frame header containing the frame magic/name, declared frame length, byte counts, chunk size/count, optional metadata flags, chunk offsets, compressed chunks, and a trailer. The trailer includes a versioned array, a variable-length metalayer section, a declared trailer length near the footer, and a fingerprint extension footer. Variable-length metalayers are represented by a small name-to-content-offset index and serialized bin content records.
- A c-blosc2 frame has an accepted frame header, declared frame length, compressed chunk metadata, chunk payloads, and optional header and trailer metalayer metadata encoded with msgpack-like markers. The header metalayer index maps names to declared content locations, and the vulnerable reader accounts for one cursor while copying from a separate declared content location.

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- A c-blosc2 frame has a msgpack-like frame header, declared frame size, compressed chunk metadata, chunk payloads, compressed chunk offsets, and optional trailer metadata. Chunk reads in the contiguous in-memory path derive pointers from decompressed chunk offsets relative to the frame header.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 22 Factual Contract

### Schema / Invariants
- A c-blosc2 frame is a binary frame with a msgpack-like header, one or more chunk payloads, and a trailer that can hold variable-length metalayer records. The trailer contains indexed metadata records and a footer with trailer extent information; the parser trusts trailer-relative content positions while walking metalayer records.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 26 Factual Contract


### Schema / Invariants
- A c-blosc2 frame has a msgpack header with magic, frame length, total uncompressed/compressed sizes, type size, chunk size, codec flags, filter pipeline, and metalayer index, followed by sequential Blosc chunks, an offsets/index chunk, and a msgpack trailer. Embedded Blosc chunks may use the extended chunk header when both shuffle flags are present; in that form, the block-start table follows the filter metadata. Each block then contains one or more compressed streams, each introduced by a signed cbytes token; negative token values encode run-filled streams.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 28 Factual Contract

### Schema / Invariants
- A contiguous C-Blosc2 frame has a msgpack-like header with magic, declared header length, declared total frame length, uncompressed and compressed byte counts, frame type, codec/filter metadata, frame-level type size, block size, chunk size, optional metalayers, compressed chunk payloads, a compressed offsets/index chunk, and a trailer. The frame-level type size is distinct from ordinary chunk header metadata and matters when a frame offset denotes a special synthesized chunk.
- A C-Blosc2 frame uses a msgpack-like header with frame magic, declared header size, declared frame size, byte counts, chunk sizing metadata, compressed chunk payloads, a compressed offset-table chunk, and a msgpack-like trailer. The trailer can contain variable-length metalayer metadata: an index maps a metalayer name to a trailer-relative content record, and the content record carries a binary marker plus a declared content length. The trailer footer stores the trailer extent and a fingerprint marker.

### Harness Links
- [[afl-libfuzzer-compatible-whole-buffer-frame-decompressor]]
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- A C-Blosc2 frame has a msgpack-like header with frame magic, declared header length, declared total frame length, byte counts, type size, chunk size, codec/filter metadata, compressed chunk payloads, a compressed offsets/index chunk, and a msgpack-like trailer.
- The trailer footer carries a trailer extent and marker; frame_get_usermeta derives the trailer start from the accepted frame length and this trailer extent, then reads a usermeta length and copies usermeta content from trailer-relative positions.
- A c-blosc2 frame is a serialized container with an outer frame header, compressed chunk payloads, an offsets/index area, and a trailer.
- The trailer can contain user metadata plus a footer that declares the trailer extent and carries a marker used during reverse parsing.
- Parser reach depends on preserving the valid frame envelope, chunk metadata, offset index, and trailer marker while changing the relation between trailer extent and the metadata fields it contains.
- A C-Blosc2 frame has a msgpack-like header, declared total frame length, byte counts, type size, chunk size, codec/filter metadata, a metalayer index area, optional chunk/offset data, and a msgpack-like trailer.
- The trailer stores a usermeta length near its start and a trailer extent marker near the end.
- This source variant interprets the frame's multibyte numeric fields according to the buggy helper used by the parser, so seed bytes from a different endian convention can be useful for layout but still fail the parser gates.
- A zero-data frame can reach frame_get_usermeta when the header, empty metalayer index, total frame length, and trailer extent are internally consistent.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
