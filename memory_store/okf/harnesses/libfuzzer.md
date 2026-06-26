---
type: harness-contract
title: "Libfuzzer harness"
description: "Input contract facts for Libfuzzer."
tags: ["libfuzzer", "round-6"]
okf_support: 22
---
# Libfuzzer Harness

## Round 6 Input Contract
- The libFuzzer harness treats the input prefix as the binary message and consumes a fixed-width suffix from the back as a memory limit. The crash depends on satisfying the binary message parser and then forcing allocation failure through that suffix.
- The libFuzzer harness consumes raw bytes, clamps very large inputs, selects a platform from the first byte modulo the platform table, enables Capstone detail mode, disassembles the remaining bytes, then prints instruction names, implicit registers, and groups to a sink file. No file envelope or checksum is used.
- The harness is libFuzzer over raw bytes copied to a fixed input path. It opens the MIMIC decoder directly, accepts only the supported frame dimensions, and may derive codec context fields from a trailing configuration area only when the input is large enough.
- The harness passes the raw input bytes directly to the PostGIS WKB importer with parser checks disabled. There is no mode selector or FuzzedDataProvider carving; reachability is controlled entirely by a syntactically plausible WKB record tree.
- The libFuzzer harness rejects very short and oversized inputs, treats the leading region as the disassembly buffer, reads the final selector fields from the end of the input, looks up a BFD architecture, then calls the selected disassembler repeatedly with an in-memory disassemble_info buffer.
- The harness creates sockets, iterates through the socket option range, calls setsockopt with the entire fuzzer byte buffer and its explicit size, and then tries getsockopt. It does not carve selector fields from the input; reachability depends on the loop hitting the vulnerable option with a buffer length in the sensitive range.
- The harness is libFuzzer over a single raw file path. The wrapper runs the selected fuzzer directly against the copied input and reports clean execution for short arbitrary bytes.
- The generated run directory invoked the generic local arvo wrapper, but verifier output identified the active binary as a qpdf fuzzer rather than a JPEG decoder harness. Official target matching rejected the local off-target crash.
- The libFuzzer harness treats the input as raw CIL source, adds it as a policy file, compiles it, builds and optimizes a policydb, and writes the result to a null output. Triggering this bug requires reaching compile-time resolution and verification, not policydb serialization alone.
- The secilc libFuzzer target consumes the raw file as policy text, reports syntax errors for malformed text, and ships a seed corpus from the upstream policy test directory.
- The libFuzzer harness passes the raw bytes to c-blosc2 frame reconstruction, checks the declared uncompressed size, allocates an output buffer, attempts chunk decompression, and then frees the reconstructed container. There is no front selector; valid frame reconstruction is the main gate.
- The wrapper invokes the dav1d multithreaded fuzzer on the copied raw input. Local signal can disagree with the official server for wrapper-level crashes, so official vul/fix comparison is required.
- The harness feeds raw bytes to the Ghostscript raster path through the arvo wrapper. It does not expose a separate mode selector; the payload must be a self-contained PostScript/PDF resource that makes Ghostscript load and execute the CMap parser.
- The raster harness pipes the raw input as a Ghostscript job on stdin using a CUPS raster device. There is no fuzzer-carved selector; the input must be a complete enough PostScript/PDF job to reach font stream decoding.
- The libFuzzer harness passes the raw file bytes to RawSpeed's DcrDecoder-specific TIFF decoder fuzzer. There is no FuzzedDataProvider layout; malformed headers may crash earlier than the target decoder method.
- The harness feeds raw bytes to Ghostscript configured with the pdfwrite device. The input must be a valid enough document or PostScript program for pdfwrite conversion, and the vulnerable sink is behind font embedding/subsetting rather than basic page rendering.
- The MuPDF pdf_fuzzer consumes the raw file as a PDF and attempts parsing/repair through the normal document machinery. Non-PDF bytes fail at version/object recognition before the target path.
- The DuckDB parse/query fuzzer runs the raw input as SQL with verification enabled and reports only crashes or selected internal-result mismatches. There is no binary framing or mode selector; the payload must be executable SQL that reaches aggregate execution.
- The harness consumes raw PDF bytes, opens the document from memory, iterates pages, and renders them. There is no explicit selector; page/resource traversal is needed to force indirect object loading after xref repair.
- The fuzz_process_packet libFuzzer target passes the raw file bytes directly to nDPI packet detection as one L3 packet. IPv4 total length and TCP header length must match the HTTP payload for the parser to reach the HTTP dissector.
- The libFuzzer harness treats input as a raw PDF document, opens it from memory, iterates pages, adds or reads annotations, and renders pages. There is no selector byte; the PDF catalog, page tree, page object, and annotation object must all be coherent enough for Poppler to reach annotation processing.
- The wrapper invokes the Capstone disassembly fuzzer directly on the copied raw input. It accepts arbitrary byte strings, but only specific encodings exercise detailed ARM memory operand handling.

## Format Links
- [[c-blosc2-frame]]
- [[cil-policy]]
- [[cil-policy-text]]
- [[dav1d-fuzzer-input]]
- [[dcr-tiff-raw]]
- [[ffmpeg-target-decoder-frame]]
- [[ipv4-tcp-http-request]]
- [[jpeg-card-but-qpdf-runtime]]
- [[jpeg-or-vips-fuzzer-input]]
- [[opc-ua-binary-message]]
- [[pdf]]
- [[postscript-cmap]]
- [[postscript-pdf-with-type2-cff-font]]
- [[postscript-pfb-font-stream]]
- [[raw-disassembler-buffer]]
- [[raw-disassembler-buffer-with-trailer-selector]]
- [[raw-instruction-stream]]
- [[raw-socket-option-value]]
- [[sql]]
- [[wkb]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 7 Input Contract
- The libFuzzer target feeds raw bytes as a DER PKCS#12 blob to the key parser fuzzer. The harness
uses a fixed password, calls simple_parse with output pointers for key, chain, extras, and CRL, and
manually deinitializes returned objects only when simple_parse reports success.
- The GraphicsMagick MAT fuzzer feeds the raw file bytes to the MAT coder. There is no mode selector
or FuzzedDataProvider layout; the input must be a complete MAT-like byte stream.
- The local wrapper ran the simple decompression libFuzzer target on raw file bytes. No outer file
format or length prefix is used, but the decompressor performs legacy-frame and block-header
validation before reaching literal decoding.
- The target is fuzz_pkcs15_reader. It installs a synthetic reader, connects a card, binds PKCS15,
then consumes more chunks as operation inputs and parameters only if a card was successfully bound.
- The harness opens the raw input via libsndfile virtual I/O, allocates a float buffer sized from the
parsed channel count, and repeatedly reads one frame at a time. The raw fuzzer bytes must therefore
be a recognizable sound-file container before ALAC decoding is reached.
- The libFuzzer target passes raw bytes to blosc2_schunk_open_sframe, then decompresses chunks from
the returned super-chunk. Parser reachability depends on a coherent in-memory frame; the fuzzer does
not carve a mode byte.
- The trace processor fuzzer parses the raw input as Perfetto trace data and calls NotifyEndOfFile,
which flushes accumulated memory tracker snapshots. There is no separate mode byte.
- The harness passes raw input bytes directly to the TTF memory loader. There is no file-name
extension, mode selector, or FuzzedDataProvider split; collection magic and subfont offset
arithmetic control the path.
- The harness writes raw fuzzer bytes to a temporary GML file and calls igraph_read_graph_gml on that
file. If parsing succeeds, it destroys the graph; invalid parse errors are normally non-crashing.
- The RawSpeed harness feeds raw bytes to RawParser, calls decodeRaw, then decodeMetaData, and catches
RawspeedException. The input must be a recognizable RAW/TIFF-family file for the CR2 decoder to be
selected.
- The libFuzzer harness copies raw bytes into a NUL-terminated string, calls stringToH3, duplicates
the resulting index into a two-element array, then exercises compactCells, uncompactCells, and
h3NeighborRotations with fixed directions. It does not consume a file container or length fields.
- FuzzJs wraps the raw bytes in a StringView, lexes and parses a program, and only runs it if parsing
has no errors. There is no mode selector or length-prefixed layout.
- The harness passes raw bytes directly to the OpenSIPS message parser. There is no length prefix,
mode selector, or checksum gate; the buffer contents themselves form the SIP message.
- The libFuzzer harness passes raw bytes directly to parse_msg and then frees the parsed message.
There is no file wrapper or length prefix; truncation at the end of the raw input is visible to the
header parser.
- The Assimp fuzzer feeds raw bytes to Importer::ReadFileFromMemory with no explicit extension. The
in-memory loader assigns a synthetic filename and then performs signature-based format detection.
- The FreeRADIUS fuzzer binary selects a protocol decoder from its target name; for this run the local
wrapper executed the DHCPv4 protocol decoder on the raw input buffer.
- The from-data libFuzzer target feeds raw bytes to exif_data_new_from_data, then traverses Exif
contents and maker-note values, serializes the data, fixes it, and releases the object. No leading
selector byte is carved.
- The nDPI fuzzer passes the input bytes directly to ndpi_detection_process_packet. The input is not
pcap-framed; the first bytes must be an IP packet, and port/payload shape influence TLS protocol
detection.
- The harness opens raw bytes as an image, reads metadata, prints EXIF/IPTC/XMP entries and structure
variants, then calls writeMetadata. A candidate must pass ImageFactory recognition and reach both
metadata parsing and the relevant print/write path.
- The map fuzzer writes the raw input bytes to a temporary .map file and calls msLoadMap. It rejects
very small and overly large inputs before parsing.
- The harness passes raw bytes to LibreDWG. Inputs starting like DWG select binary decoding, inputs
starting with a JSON object select JSON import, and other text-like inputs can fall through to DXF
handling.
- The libFuzzer harness passes the raw byte buffer and its exact size to plist_from_openstep, then
frees any resulting root node. The input is not NUL-terminated by the harness.
- The binutils wrapper writes the raw input to a temporary file and runs the safe objdump fuzzer path.
BFD determines the object format from the raw bytes and objdump requests headers, sections, symbols,
and related metadata.
- The active harness writes the leading portion of the fuzz input to a temporary table file, parses
the remaining bytes with the liblouis extended character parser, and calls lou_translateString with
an output buffer derived from the parsed input length.
- The source tree contains a raw mp_datetime fuzzer that passes bytes directly to datetime_unpack, but
the local wrapper output for this image showed a different protobuf-backed Lua fuzzer. This mismatch
made local parser-reachability feedback unreliable for the described MsgPack extension bug.
- The WAV fuzzer feeds raw bytes into a fixed memory stream and constructs a WavLoaderPlugin. There is
no leading mode byte; parser reachability depends on valid RIFF/WAVE chunk framing.
- The harness loads raw bytes as a PDF document and renders every page with poppler::page_renderer.
The input must be a parseable PDF; rendering operations in the content stream determine whether the
Splash font path code is reached.

## Round {ROUND} Format Links
- [[assimp-zip-archive]]
- [[c-blosc2-frame]]
- [[caf-alac]]
- [[coff-object]]
- [[cr2-tiff-raw]]
- [[dhcpv4]]
- [[dwg-r11]]
- [[gml]]
- [[h3-index-string]]
- [[image-metadata]]
- [[ipv4-tcp-tls]]
- [[javascript]]
- [[jpeg-exif]]
- [[liblouis-generic-table-plus-escaped-text]]
- [[mapfile]]
- [[mat]]
- [[msgpack-ext]]
- [[opensc-fuzz-reader-chunks]]
- [[openstep-plist]]
- [[pdf]]
- [[perfetto-trace-protobuf]]
- [[pkcs12-der]]
- [[sip]]
- [[sip-message]]
- [[ttc-opentype-font]]
- [[wav]]
- [[zstd-legacy-frame]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
