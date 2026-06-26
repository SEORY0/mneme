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

## Round 8 Input Contract
- libFuzzer passes the raw file bytes directly to the HarfBuzz shape fuzzer. There is no leading mode byte or FuzzedDataProvider carving in this selected harness.
- The libFuzzer target opens the raw input as a PDF document and renders every page into an RGB pixmap. There is no mode selector or FuzzedDataProvider carving; all bytes are the candidate PDF.
- The libFuzzer harness writes the exact input bytes to an in-memory file named without a KML extension, registers OGR drivers, opens that memory file read-only through OGR, iterates all layers and features if open succeeds, and destroys the datasource. There is no selector byte or FuzzedDataProvider carving.
- The selected libFuzzer target initializes an OpenThread instance as a leader, initializes the NCP, copies the raw input to a UART receive buffer, calls the platform UART receive hook once, and then drains tasklets/platform work for a bounded number of iterations.
- The decoder fuzzer consumes raw FLAC file bytes. No front selector is used; a valid stream marker and coherent metadata are the primary reachability gates.
- The libFuzzer target copies the entire input into an owned buffer, calls TraceProcessorStorage.Parse once, and then calls NotifyEndOfFile only when parsing reports success. There is no leading mode byte and no FuzzedDataProvider layout.
- The libFuzzer harness scans the raw input bytes with a compiled YARA rule importing the PE module. There is no file wrapper, selector byte, or FuzzedDataProvider carving; the PE module is loaded while evaluating the rule and walks the memory block directly.
- The libFuzzer target feeds the raw byte stream through a memory-backed FILE object into the libspectre document loader; there is no outer container, filename carving, or FuzzedDataProvider splitting.
- The fuzzer carves the first three little-endian signed 16-bit fields as rotation/shear parameters and passes the remaining bytes to the image reader. PoCs must prepend those parameter bytes before the actual image container.
- The fuzzer feeds raw bytes through fmemopen into spectre_document_load_from_stream, then checks document status and frees the document. There is no mode selector, sidecar file, or back-loaded FuzzedDataProvider field.
- The ClamAV scanfile fuzzer writes the raw input to a temporary file and invokes the normal scanner with broad parse options enabled. The harness does not carve fields from the byte stream.
- The libFuzzer target writes the raw input bytes to a temporary pcap file, opens it with PcapFileReaderDevice, reads the first packet, constructs a parsed Packet, and only prints IPv4 addresses after parsing. There is no selector byte or FuzzedDataProvider carving.
- The subset fuzzer consumes the raw input as a font blob. It also derives deterministic allocator pressure from total input size and optionally reads subset flags and text-selection data from the end of the input, so changing trailing length can change allocator behavior and the selected text without changing leading font bytes.
- The fuzzer passes raw bytes to the Blosc decompression entrypoint after header validation. There is no external mode selector; the internal Blosc header controls codec and block layout.
- The libFuzzer target requires the raw input itself to be a valid SPIX buffer, then calls dewarpSinglePage with debug output enabled and also tries to read the same bytes as a compressed PIXA. No bytes are carved before the image parser.
- The harness installs a synthetic reader, connects a card from the first chunk, binds PKCS#15, and then consumes further chunks during card operations. Response chunks shorter than a status word synthesize an unsupported-instruction status.
- The fuzz target passes the raw input bytes directly as a shell source string to the parser and calls parse once. There is no container format, mode byte, or FuzzedDataProvider field carving.
- The fuzzer passes raw bytes to ucl_parser_add_string with an explicit length. It does not add variables, does not prepend a selector, and does not use FuzzedDataProvider carving.
- The libFuzzer target gives the entire raw byte buffer to RawParser, obtains a decoder, disables crop/unknown-model failure, then calls decodeRaw and decodeMetaData. Rawspeed exceptions are caught by the harness, so non-target parser errors become clean exits.
- The harness passes raw bytes as a NUL-terminated buffer, splits exactly on the first two newlines, initializes both projection strings with pj_init_plus, parses coordinates, and calls pj_transform if both initializations succeed.
- The libFuzzer target scans the raw input bytes with a compiled YARA rule importing the PE module and calling rva_to_offset on the first section. There is no wrapper or selector byte; the PE module receives the raw memory block.
- The libFuzzer target creates a fresh Lua state without opening libraries, loads the raw bytes as text-only Lua source, executes the chunk if loading succeeds, then closes the state. No filename or binary chunk mode is available.
- The fuzzer passes raw message bytes to parse_msg and then frees the parsed message. There is no mode byte; the input must satisfy the SIP message/header envelope before To-parameter parsing matters.
- The gstoraster libFuzzer target consumes raw PDF/PostScript-like bytes and invokes Ghostscript rendering. A minimal page that selects the embedded font is enough to force font loading during page interpretation; there is no mode byte or FuzzedDataProvider contract.
- The Ghostscript raster fuzzer sends raw input as the interpreter input stream using the cups raster device path. There is no byte carving; parser reachability depends on the document syntax forcing the PDF interpreter and repair code.
- The libFuzzer harness feeds the input as raw stdin to Ghostscript configured for the CUPS raster device. There is no fuzzer-byte carving or FuzzedDataProvider layout; Ghostscript auto-detects PDF/PostScript and processes pages through the normal interpreter.
- The fuzzer runs the nDPI pcap reader. It opens the raw input as an offline pcap, copies each captured packet according to its captured length, and passes packets through the normal workflow classifier before protocol-specific dissectors run.
- The fuzzer passes raw file bytes to LibRaw open_buffer, then calls unpack and processing routines. There is no explicit selector; the file signature chooses the camera decoder.
- The profile fuzzer writes raw input to a temporary ICC file, opens it with lcms, reads selected raw and structured tags, saves the profile again, and closes it. The raw fuzz bytes are not carved; all structure comes from the ICC parser.
- The libFuzzer harness passes the entire input buffer to Assimp Importer::ReadFileFromMemory with no extension and no outer selector. Importer detection is signature-based, and successful reachability is visible from the PLY importer log before parser crashes.
- The selected Ghostscript fuzzer treats the raw input as a document for a pdfwrite/device pipeline rather than as a bare font file. Inputs must satisfy the Ghostscript document parser before embedded font programs can run.
- The harness writes the raw bytes to a temporary file, initializes libdwarf from that file, advances to a compilation unit, obtains a sibling DIE, and then calls DIE attribute APIs. There is no front selector.
- The gs_device_psdcmyk libFuzzer target consumes raw PDF bytes and renders a page through Ghostscript. Selecting an embedded font in page content is sufficient to reach PDF font loading and CFF table extraction.
- The harness passes the entire raw byte buffer to OpenCV imdecode. There is no fuzzer-side header, mode selector, or FuzzedDataProvider contract.
- The libFuzzer target reads raw bytes with a fixed front matter: len1, len2, flags, decoder configuration, then three payload chunks. Flags select Init versus Init2, optional post-seek resets, optional Decode2 output-buffer mode, and optional DRM initialization. There is no file-extension or container detection outside this harness-specific split.
- The MuPDF fuzzer opens the raw bytes as a document stream and renders pages. Although the open call names a PDF document path, MuPDF can route recognized image streams to image loaders, so raw BMP-array bytes can reach the BMP parser without wrapping in a PDF.
- The selected libdwarf fuzzers consume raw object/debug file bytes via a temporary file and libdwarf initialization. The input is not carved by a FuzzedDataProvider.
- The libFuzzer target feeds the entire buffer directly to the XAAC decoder wrapper. It checks only for an ADTS-like sync prefix to choose ADTS versus MP4-style mode, then calls init, config, and decode in sequence while advancing by consumed bytes. There is no external selector byte or FuzzedDataProvider layout.
- The libFuzzer target uses FuzzedDataProvider from the front of the input for encoder configuration fields, with some booleans selecting enum-like choices versus raw values. After initialization, the remaining bytes are consumed as input buffers or fill values for repeated encoder process calls.
- The hts_open fuzzer reads raw file bytes through the HTS memory-file interface and dispatches by file signature. BAM needs a valid binary header and record envelope; there is no separate mode selector.
- The harness reads fields front-to-back from a ByteStream, creates a RawImage, reads slice count, regular slice width, and last-slice width, then constructs Cr2Decompressor and calls decode. Exceptions are swallowed; only memory safety failures count.
- The libFuzzer target writes the raw input to a temporary file and opens it through GDAL/OGR vector autodetection. There is no selector byte or structured harness prefix; the bytes must simply form enough of a file-backed datasource for the OGR_GMT driver identify/open path.
- The MuPDF fuzzer opens the raw bytes as a PDF stream and renders available pages to pixmaps. There is no leading mode selector or FuzzedDataProvider split; the input must be a self-contained PDF document.

## Round 8 Format Links
- [[aac-sbr-fuzzer-buffer]]
- [[aac-usac]]
- [[blosc-compressed-buffer]]
- [[bmp-array]]
- [[dwarf-object-debug-file]]
- [[encoded-image]]
- [[flac]]
- [[ghostscript-document-with-truetype-font]]
- [[gmt]]
- [[icc-profile]]
- [[kml]]
- [[lua-source]]
- [[ole-cfb-vba]]
- [[opensc-fuzz-reader-apdu-stream]]
- [[openthread-ncp-uart]]
- [[opentype-cff-font]]
- [[opentype-font]]
- [[pcap-ipv4-tcp-http]]
- [[pcap-tcp-tinc]]
- [[pdf]]
- [[pdf-with-opentype-cff-font]]
- [[pe]]
- [[pe-delay-import]]
- [[perfetto-trace]]
- [[ply]]
- [[postscript]]
- [[postscript-eps]]
- [[proj-params]]
- [[raw-camera-image]]
- [[raw-camera-tiff-or-orf]]
- [[rawspeed-cr2-decompressor-envelope]]
- [[sam-bam-cram-sequence-data]]
- [[shell-script]]
- [[sip-message]]
- [[spix]]
- [[tiff-ojpeg-image]]
- [[ucl-configuration]]
- [[xaac-encoder-fdp]]

## Round 8 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
