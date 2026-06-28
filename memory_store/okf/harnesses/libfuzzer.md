---
type: harness-contract
title: "Libfuzzer harness"
description: "Input contract facts for Libfuzzer."
tags: ["libfuzzer", "round-6", "round-16"]
okf_support: 129
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

## Round 12 Format Links
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

## Round 12 Notes
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

## Round 9 Input Contract
- The libFuzzer target receives raw file bytes, calls the Poppler raw-data loader, skips locked or
  unloadable documents, then renders every page with page_renderer.
- There is no front/back field carving or mode selector.
- libFuzzer passes raw file bytes directly to the open62541 JSON decode/encode harness.
- The harness decodes the raw bytes as a Variant, encodes the decoded value, decodes that generated
  JSON again, encodes it again, and compares generated buffers.
- The wrapper invokes a libFuzzer target through the image entrypoint with the submitted path.
- In this environment the target may interpret the mounted file path as a corpus input argument
  instead of always consuming raw bytes.
- The harness wraps all input bytes in an hb_blob, creates an hb_face and hb_font, installs OpenType
  font functions, shapes a fixed ASCII string, then if the input is large enough treats the last
  bytes as UTF-32 text, shapes that buffer too, and queries glyph extents for each shaped glyph.
- There is no input carving other than the final UTF-32 text reuse.
- The wrapper is fixed to fuzz_ndr_drsblobs_TYPE_STRUCT.
- It reads the header, pulls the chosen public struct with scalar and buffer flags, pushes the
  parsed struct back out, then walks the print routine.
- There is no FuzzedDataProvider carving beyond the NDR selector header.
- libFuzzer feeds raw bytes directly to hb-set-fuzzer.
- The vulnerable harness checks only a pointer-sized minimum before casting the beginning of the
  buffer to the instruction header, then advances by the full header size and interprets the rest as
  values.
- The submitted file is passed to a libFuzzer-style single-input runner; the runner reads the file,
  writes those bytes to a temporary scan path, and calls cl_scanfile with archive and heuristic
  scanning enabled.
- The Poppler C++ fuzzer loads the raw input as an in-memory document and renders pages with the
  page renderer.
- The input is not carved.
- BaseMemStream is used because the document is memory-backed; malformed PDFs must still pass enough
  catalog/page/xref parsing to reach rendering or stream decoding.
- The Assimp fuzzer passes the raw byte buffer directly to Importer::ReadFileFromMemory with the
  normal realtime postprocess preset.
- There is no prefix or mode byte; format selection is based on the model magic and importer
  probing.
- The libFuzzer target receives raw bytes, rejects Hermes bytecode, appends a terminator for the
  source buffer, creates a Hermes runtime, evaluates the source, and catches JSI exceptions.
- There is no input carving or FuzzedDataProvider contract.
- libFuzzer writes the raw bytes to a temporary file and invokes readelf-style processing with
  headers, sections, symbols, relocations, dynamic data, unwind, notes, and architecture reporting
  enabled.
- The harness does not use a length prefix or mode selector.
- The entrypoint launches a libFuzzer target through a path that requires a corpus directory in this
  local/server setup, so a mounted raw file can be rejected before the decompression target consumes
  it.
- The harness rejects inputs below a minimum size and consumes several bytes before the record: one
  format selector, optional fixed-width time_fmt/time_key/time_offset fields, one time_keep byte,
  one types-enable byte, and a decoder-enable byte.
- If decoders are enabled, additional bytes choose decoder rule type, backend, action, and
  optionally a second rule before one final unconditional byte is skipped.
- The remaining bytes are the parser record.
- The libFuzzer harness requires a minimum input size, consumes fields front-to-back, uses an
  odd/even selector for proxy mode, then constructs a Fluent Bit HTTP client from the carved proxy,
  URI, and method fields.
- The libFuzzer target receives raw chunk bytes.
- It rejects inputs shorter than the minimum header, requires the header compressed size to equal
  the file size and the uncompressed size to be nonzero, validates the compressed buffer, then calls
  chunk decompression into an allocated output buffer.
- libFuzzer provides raw CIL text.
- The harness adds the buffer as a CIL file, compiles it, builds a policy database, optimizes it,
  and writes the resulting policy to a sink file.
- There is no leading selector byte or external file envelope.
- The target is a libFuzzer single-input runner.
- It consumes the raw file directly, searches for the front separator, unserializes the remaining
  bytes, and conditionally invokes PHP hash operations on the resulting object.
- The md4c HTML fuzzer consumes two little-endian flag words from the front of the input, then
  passes all remaining bytes as the Markdown buffer to the HTML renderer.
- The fuzz target receives raw file bytes and lets libredwg auto-parse DWG/DXF-style content.
- There is no explicit mode byte or FuzzedDataProvider layout observed in the harness.
- The LibreDWG libFuzzer harness chooses the parser from the raw input prefix: DWG data begins with
  an AC signature, JSON begins with an opening object brace, and other inputs are treated as DXF
  text after null-termination is enforced.
- After reading, the harness writes the decoded drawing through a randomly selected output format.
- The libFuzzer target is parquet-arrow-fuzz and consumes the input as a raw Parquet-like file.
- No front/back carving was observed; parser reach depends on a coherent Parquet footer and page
  metadata.
- The fuzz_disas_ext harness rejects small inputs, copies fixed-size leading regions into
  disassembler option and private-data buffers, then disassembles the remaining raw bytes twice with
  big- and little-endian settings for the configured architecture.
- The fuzzer writes raw bytes to a temporary file, opens that file through BFD, checks object format
  acceptance, and only then calls the separate-debug-file loading path.
- The libFuzzer input is written to a temporary PCAP file and opened with libpcap.
- Each captured packet is copied into an exactly sized heap allocation before
  ndpi_workflow_process_packet processes it, so packet-record caplen directly controls the heap
  buffer boundary.
- The gstoraster fuzzer passes raw stdin-style document bytes into Ghostscript with a cups raster-
  oriented invocation.
- There is no carved header; Ghostscript language detection and document syntax select the parser.
- libFuzzer writes the raw input to a temporary assembly source file, initializes assembler state,
  and runs an assembly pass on that file.
- There is no prefix, checksum, or selector; the parser consumes ordinary assembler text.
- The wrapper is fixed to the Ghostscript xpswrite device fuzzer.
- It consumes raw document bytes with no front selector.
- The active device is not the generic raster fuzzer, so candidates must render through xpswrite-
  compatible document handling.
- The libFuzzer target selected by /bin/arvo consumed raw bytes with SkData and invoked image-filter
  deserialization.
- The build also produced a region deserializer, but the selected wrapper output showed
  image_filter_deserialize.
- No field carving or FuzzedDataProvider use was observed.
- libFuzzer feeds raw object bytes directly to the libdwarf `fuzz_die_cu_attrs_loclist` harness.
- The harness opens the object through libdwarf, iterates compile units and DIE attributes, and
  exercises location-list and attribute helper paths; there is no wrapper-level mode byte.
- The fuzzer writes raw input to a temporary file and invokes objdump-style BFD/disassembler logic
  on it.
- Local verification can show generic wrapper crashes that are not sufficient for official target
  matching.
- The libFuzzer target receives raw bytes, opens them as an in-memory PDF stream, counts pages, and
  renders each page to an RGB pixmap with a bounded custom allocator.
- Exceptions are caught; native faults are the relevant signal.
- LLVMFuzzerInitialize starts CPython before the input-specific callback.
- The selected fuzz target precompiles a fixed list of regex patterns on first use, then for each
  input creates a bytes object from the payload after the selector and calls the compiled pattern's
  match method.
- The harness consumes bytes front-to-back with libxml2's fuzz data provider, parses the XML before
  enabling malloc-failure limits, then enables the limit around XPath context creation and XPointer
  evaluation.
- LibFuzzer passes raw bytes to the target, but the harness consumes an initial setup bitfield
  before constructing the DNS message.
- That byte controls whether to append a signature, choose TSIG versus SIG-style data, set time
  adjustments, install query TSIG/key state, and enable keyring/view lookup.
- The next byte contributes to generated DNS header flags/opcode; the rest becomes signature RDATA
  only when a signature is enabled.
- libFuzzer writes the raw bytes to a temporary file, loads it as a GPAC filter source, attaches an
  inspect filter with deep bitstream analysis, runs the filter session, and deletes the file.
- The source probe recognizes M3U8 content from the playlist marker or related manifest detection;
  there is no leading mode selector.
- The fuzzshark target is configured for the UDP entry in the IP protocol dissector table.
- It supplies the raw input as UDP payload and disables many unrelated dissectors; reaching WLAN
  logic requires a UDP-carried encapsulation path rather than a bare 802.11 frame.
- The harness passes raw bytes directly to SkImageFilter::Deserialize and then exercises the
  deserialized filter at a fixed width.
- There is no mode selector or external image file contract.
- Ordinary encoded image bytes are treated as serialized-filter bytes and usually fail
  deserialization.

## Round 9 Format Links
- [[assimp-mdl7-model]]
- [[binutils-disassembler-fuzzer-byte-stream]]
- [[blosc-chunk]]
- [[blosc-compressed-buffer]]
- [[clamav-scanfile-archive]]
- [[cpython-sre-match-fuzzer-byte-stream]]
- [[dns-message-checksig-fuzzer-record]]
- [[dwg-dxf]]
- [[dxf-text]]
- [[elf-dwarf-object]]
- [[elf-with-msp430-relocation-records]]
- [[fluent-bit-http-fuzzer-buffer]]
- [[fluent-bit-parser-fuzzer-control-plus-record]]
- [[gas-assembly-text]]
- [[gpt-disk-image]]
- [[hb-set-fuzzer-binary-instruction-stream]]
- [[hls-m3u8-playlist-text]]
- [[javascript]]
- [[libxml2-xpath-fuzzer-input]]
- [[markdown]]
- [[object-file-for-objdump-disassembly]]
- [[object-file-with-debug-sections]]
- [[open62541-json-variant]]
- [[opentype-font]]
- [[parquet]]
- [[pcap]]
- [[pdf]]
- [[php-hashcontext-unserialize]]
- [[postscript-or-pdf]]
- [[postscript-or-xps-for-ghostscript-xpswrite]]
- [[samba-ndr-drsblobs]]
- [[selinux-cil-policy-text]]
- [[skia-serialized-image-filter]]
- [[skia-serialized-object]]
- [[wireshark-udp-dissector-payload]]

## Round 9 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 10 Input Contract
- The libFuzzer entry rejects only empty input, then calls magic_buffer on the entire byte string. There is no mode byte, file path, FuzzedDataProvider layout, or checksum gate.
- The local verifier runs a curl FTP libFuzzer target on the raw file bytes. No front/back FuzzedDataProvider carving was visible from the candidate behavior; the whole file is consumed by the target wrapper as its stimulus.
- Raw libFuzzer bytes are interpreted directly as a C string. There is no archive or file envelope despite the coarse card; parser reachability depends on a final terminator and no newline.
- The active binary was the HarfBuzz shape fuzzer. It consumes the entire file as an hb_blob, creates an hb_face and hb_font, shapes fixed ASCII text, then reuses trailing input bytes as UTF-32 text for a second shaping pass. There is no external wrapper or checksum.
- The libFuzzer input is raw bytes with a maximum-size gate. The 4i path is enabled only for word-aligned input; fields are consumed from the front with no file wrapper, checksum, or magic.
- The fuzz harness feeds the raw file bytes directly to the Lwan HTTP request parser. There is no mode byte or provider-carved trailer; preserving a valid request-line and header-line grammar is enough to reach header parsing.
- The harness installs a fake OpenSC reader, connects a card, binds PKCS15, and consumes APDU response chunks front-to-back. After binding, additional chunks supply operation inputs and parameters for object operations.
- The libFuzzer target passes the entire raw byte string to poppler::document::load_from_raw_data, skips locked or unloaded documents, creates each page, and renders each page with poppler::page_renderer. There is no FuzzedDataProvider carving.
- The fuzzer passes raw IE bytes to scan-result and probe-request P2P handlers, and also treats long inputs as action frames. No outer 802.11 frame is needed for the scan/probe IE path.
- Raw libFuzzer bytes are split by the target: most bytes are passed to the JPEG XL decoder and the final option word is consumed by the harness. A valid seed reaches basic-info, frame, image-output, and full-image decoder events; changing suffix bits alters the output-buffer path.
- The harness passes the raw file bytes to libbpf object open-from-memory and then closes the object. There is no extra provider-carved metadata; the ELF section graph itself must drive reachability.
- The fuzz target launches Ghostscript in-process with a CUPS raster output device and copies raw input bytes to Ghostscript stdin. There is no outer archive; parser selection is by document syntax.
- The fuzzer consumes the whole input as a little-endian ByteStream. It creates RawImage metadata from the front fields, reads offset and compatibility fields, allocates image data, constructs LJpegDecompressor over the remaining bytes, and catches RawSpeed exceptions.
- The selected GStreamer discoverer harness wraps the raw file bytes in an appsrc URI. Typefinding and parser selection happen inside the pipeline; there is no separate filename or container wrapper required for text subtitle inputs.
- The libFuzzer input is raw bytes. Inputs shorter than the configuration prefix are ignored; successful candidates must satisfy encoder initialization before frame bytes are passed to the encode API.
- Raw bytes are written to a temporary file, opened by libdwarf, and processed through repeated frame-list reads for debug-frame and exception-frame sections under several frame-rule settings.
- The fuzzer writes the raw bytes to a temporary file, opens it, calls dwarf_init_b, then repeatedly reads .debug_frame and .eh_frame while varying frame-rule default values. There is no selector byte or FuzzedDataProvider carving.
- The active verifier binary consumes raw file bytes as the XML fuzzer input. Some libxml2 fuzzers support option and allocation-limit fields, but the observed target accepted raw XML-style files directly and did not expose a separate mode byte in these attempts.
- Fuzzshark initializes Wireshark epan and passes raw bytes to one configured dissector handle. In this run the handle was the UDP dissector from the IP protocol table, not an IS-IS or CLNP dissector.
- The active binary was GPAC fuzz_probe_analyze. It writes or treats the raw bytes as a probed media input; there is no mode byte. Failed candidates produced an empty inspection document or a filter setup failure rather than a direct parser call.
- The harness copies raw bytes into a NUL-terminated buffer and executes them with the mruby string loader. There is no length trailer or multi-field provider contract; reachability depends on valid mruby syntax and runtime operations.
- The target compiles and executes raw PHP source bytes directly. There is no file-format wrapper; reaching the sink requires valid PHP code that creates attributes and forces reflection-based instantiation during execution.
- The fuzzer passes the entire raw byte string as a SIP message buffer, calls parse_msg, parse_headers, parse_sdp, and several SIP header parsers. There is no front selector or FuzzedDataProvider layout; SIP and Content-Length syntax are the main gates.
- The observed verifier runs an FFmpeg Media100 codec fuzzer over the raw file bytes plus wrapper-supplied codec context. There is no external container parser in these attempts; packet bytes must themselves satisfy the converter and downstream decoder gates.
- The FFmpeg demux fuzzer feeds raw bytes through a custom AVIO context. For non-flat builds it can reserve a trailer for IO controls and filename hints, but this run reported the image2 demux target rather than the expected animated JPEG XL demux target.

## Round 10 Format Links
- [[curl-protocol-fuzzer-input]]
- [[elf-dwarf-frame-object]]
- [[elf-dwarf-object]]
- [[elf-with-btf]]
- [[ffmpeg-media100-packet]]
- [[file-magic-raw-buffer]]
- [[http-request]]
- [[image-jpegxl-or-image2]]
- [[jpeg-xl-codestream]]
- [[libavc-encoder-config-plus-frame-bytes]]
- [[libidn2-raw-domain-or-uint32-codepoints]]
- [[mruby-script]]
- [[ogg-opus-or-gpac-probe-input]]
- [[opensc-fuzz-reader-chunks]]
- [[opentype-aat-morx-font]]
- [[ovs-odp-text]]
- [[pdf]]
- [[pdf-postscript]]
- [[php-script]]
- [[rawspeed-ljpeg-decompressor-envelope]]
- [[sip-message-with-sdp-body]]
- [[subtitle-text]]
- [[wifi-p2p-information-elements]]
- [[wireshark-udp-dissector-payload]]
- [[xml]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- libFuzzer passes the raw file bytes directly. The harness creates a RawImage from front-loaded fields, then consumes a full tile rectangle, constructs VC5Decompressor on the remaining stream, allocates image data, and calls decode. Exceptions are swallowed, so success requires satisfying parser gates and causing an actual sanitizer-detected memory error.

## Format Links
- [[rawspeed-vc5-fuzzer-envelope]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer target feeds raw bytes to FFmpeg target_dec_fuzzer. It scans forward packet by packet, opens a fixed decoder, optionally reads codec parameters from a trailing context block, and decodes each packet until input exhaustion or an iteration cap.

## Format Links
- [[ffmpeg-aac-decoder-packet-stream]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer target consumes the whole file as the decoder byte stream. A small number of bytes also select color format and core count, then the same buffer is used for header decoding followed by frame decoding.

## Format Links
- [[hevc-elementary-stream]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The selected libFuzzer target copies raw input into a fixed static buffer, truncates at the buffer size, and calls the config parser with an effective length one less than the copied size. It then walks parsed config lines recursively. The harness is not a file parser and no filename or sidecar files are available.

## Format Links
- [[lwan-config]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The reader harness installs a synthetic smart-card reader, connects a card from the first chunk, binds PKCS#15, then consumes later chunks during card operations. The decode harness loops over PKCS#15 entry decoders and also tries public-key, tokeninfo, and unused-space parsers directly on the raw blob.

## Format Links
- [[opensc-pkcs15-asn1-or-reader-chunk-stream]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer target passes the raw bytes to Assimp Importer.ReadFileFromMemory with no filename hint. Format detection is signature/content based, and material libraries are sidecar opens through Assimp's IO system rather than embedded in the main OBJ bytes.

## Format Links
- [[wavefront-obj-with-mtl]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer harness returns early for short inputs, then copies the first input region into the format string and the remaining region into the buffer string before calling flb_strptime with a stack tm object.

## Format Links
- [[fluent-bit-strptime-format-plus-buffer]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer target feeds raw bytes directly to the XSLT stylesheet fuzzer. It initializes a fixed source XML document internally, parses the input as a stylesheet, applies it, frees the transform result, and disallows external I/O through security preferences.

## Format Links
- [[xslt-stylesheet]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer target feeds the raw bytes to the sudoers parser through an in-memory file stream. It initializes defaults and invokes the sudoers grammar directly. Parser errors are non-crashing; the candidate must reach include expansion rather than merely trigger a syntax diagnostic.

## Format Links
- [[sudoers]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The selected fuzzer sends raw stdin to Ghostscript configured with the CUPS raster device. The harness exercises the full interpreter/rendering path. Clean PDF errors and successful rendering both exit normally, so the crash requires a specific interpreter repair/lifetime interaction.

## Format Links
- [[pdf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer target embeds Ghostscript, copies raw input bytes to Ghostscript stdin, and runs a CUPS raster output device with batch/no-pause options. Parser selection is by document syntax with no sidecar file or mode byte.

## Format Links
- [[postscript-ghostscript-pattern-document]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer target NUL-terminates the raw input, splits on the first two newlines, initializes both projections with the old PROJ API, parses the third line as coordinates, then calls the transform function.

## Format Links
- [[proj-parameter-lines]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer target consumes raw bytes directly. Inputs beginning with a JSON object are routed to the JSON reader. The crash occurs during parse-time assignment, before any need for a valid drawing body.

## Format Links
- [[libredwg-json]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The Ghostscript fuzz target reads raw document bytes from stdin into an in-process Ghostscript interpreter configured for raster output. There is no separate file system envelope; the font program must be embedded in the document stream itself.

## Format Links
- [[postscript-or-pdf-with-cff-type2-font]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The run_poc wrapper reads raw bytes from the PoC file and invokes the CPython fuzz target. The observed output shows source bytes are accepted directly; there is no separate file-format envelope or length prefix.

## Format Links
- [[python-source]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- fuzzshark initializes Wireshark dissectors, registers the configured target dissector as a postdissector, wraps the raw bytes in a packet record with synthetic metadata, and calls epan_dissect_run. There is no file-format wrapper around the packet bytes.

## Format Links
- [[wireshark-nbap-dissector-payload]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The target is the OpenSC pkcs15init fuzzer. It parses profile text, connects a virtual reader, binds the profile to the card driver, then exercises init, PIN storage, data object storage, key generation, finalization, sanity checks, and erase operations.

## Format Links
- [[opensc-pkcs15init-profile-plus-virtual-reader-stream]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer target NUL-terminates the raw input and calls jq_compile on it. It does not feed JSON input through the compiled program. Parser and compile diagnostics are non-crashing outcomes.

## Format Links
- [[jq-filter]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer target copies raw bytes into an Exiv2 DataBuf, opens an image by sniffing the bytes, calls readMetadata, prints metadata and structures, then calls writeMetadata inside a catch-all exception boundary.

## Format Links
- [[exiv2-image-metadata-container]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libFuzzer target feeds the raw input to libredwg, decodes DWG/DXF/JSON, then randomly exercises an output path such as encode, DXF, JSON, or GeoJSON before freeing the drawing.

## Format Links
- [[dwg-dxf-json-drawing-data]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The fuzz target writes raw input as a temporary file and runs GPAC probe/analyze filtering. It is not a direct call to gf_sdp_info_parse. If the probe graph cannot infer a supported input type, it fails setup and never reaches the SDP parser.

## Format Links
- [[sdp]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The fuzzer initializes an nDPI flow as QUIC over UDP, derives the QUIC version from the first input word, passes the rest to crypto-data extraction, and then processes either GQUIC CHLO tags or TLS data depending on the selected version.

## Format Links
- [[gquic-quic-crypto-data]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The libical extended fuzzer reads raw bytes as a NUL-terminated calendar string, parses it with libical, and normalizes parsed components. The observed harness did not require an external filename or archive wrapper.

## Format Links
- [[icalendar]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 12 Input Contract
- The GraphicsMagick coder fuzzer feeds the raw file bytes to the MNG image reader through a Magick blob; there is no fuzzer-side prefix or mode selector.
- The libFuzzer harness feeds the raw input buffer directly to libgit2 object parsing for selected object types. There is no fuzzer-side length prefix or mode byte; the buffer boundary itself is the parser boundary.
- The libFuzzer harness passes the raw input bytes through a Qt buffer and tries several KArchive readers. KAr is reached only when the raw bytes satisfy the ar magic/header gates.
- The libFuzzer input is copied as raw UART bytes and delivered to otPlatUartReceived after initializing a single OpenThread instance as a leader. There is no file wrapper, mode byte, checksum, or FuzzedDataProvider carving.
- The fuzzer caps input size, maps the first byte modulo the platform table, opens that architecture/mode, enables detail output, optionally enables alternate syntax from a selector bit, and disassembles the remaining bytes from a fixed base address.
- The libFuzzer harness replaces OpenSC's reader with a fuzz reader, consumes the first chunk during card connection, then consumes additional chunks during PKCS#15 bind and object operations. After binding, it consumes two more chunks as operation input and parameters.
- The libFuzzer target passes the raw input bytes directly to Samba's NMB packet parser as one datagram, then rebuilds and frees parsed packets only if parsing returns a packet. No selector byte or external file wrapper is used.
- The decoder fuzzer passes raw input bytes directly to avifDecoderSetIOMemory and then parses or decodes through libavif. There is no prefix selector or footer; the candidate must be a BMFF-like byte stream.
- The target requires a minimum input size. It initializes a Fluent Bit config, derives parser options from leading bytes, creates a parser, optionally parses the remaining bytes, destroys parser-owned structures or fallback type/decoder structures, then exits the config.
- The sndfile libFuzzer target feeds the raw buffer through virtual file I/O into libsndfile open/read paths. There is no harness prefix; all structure comes from the RIFF/WAV container.
- The libFuzzer target installs a fuzz reader, connects a card through OpenSC, attempts PKCS#15 binding, then consumes additional chunks for decipher, derive, wrap, unwrap, and signature operations only when binding succeeds. Chunk lengths are consumed from the front of the raw byte stream.
- The c-blosc2 harness consumes raw bytes as a single compressed chunk, not a frame. It rejects inputs smaller than the minimum header, rejects inconsistent header sizes, validates the chunk, then calls blosc2_decompress into a buffer sized from the compressed chunk length.
- The libFuzzer bytes are consumed as one raw CIL file. The harness adds the file to the CIL database, compiles, builds a policy database, and writes policy output; there is no archive wrapper or carved input layout.
- The execute fuzzer passes the raw input buffer as a PHP request body, ignores overly large source buffers, installs an execution-step budget, and executes the script. The local wrapper may mis-handle single-file verification as a corpus path, so official submit is the reliable signal for this task.
- The LibJS fuzzer treats the raw buffer as JavaScript source. It parses and executes the script directly; there is no file envelope, mode selector, or length prefix.
- The actual target is the SRW-specific TIFF decoder fuzzer, not the generic raw parser. The harness parses the raw input as a TIFF IFD tree, constructs SrwDecoder directly, disables crop/support failures, and calls decodeRaw followed by metadata decoding.
- The djxl fuzzer consumes the last few bytes as flags and decodes the preceding bytes as JPEG XL data. It may decode in one shot or streamed chunks and may request pixel, extra-channel, preview, or JPEG reconstruction output depending on flags.
- The local target feeds raw bytes to libexif data loading and then exercises entry iteration/value formatting and save paths. There is no fuzzer-side selector; reaching the bug depends on the EXIF loader accepting an entry that later survives to serializer callbacks.
- The mruby fuzzer copies the raw input into a NUL-terminated string and passes it to the mruby source loader. It does not accept precompiled bytecode in this harness path.
- The harness feeds raw input as stdin to Ghostscript configured with a CUPS raster output device. There is no mode selector; the input must be a self-contained Ghostscript-readable job, and parser reachability depends on normal PDF repair and object traversal.
- The Assimp harness passes raw fuzzer bytes to Importer::ReadFileFromMemory. The importer auto-detects the ASE text scene and runs normal parsing and postprocessing on the resulting scene.
- The HarfBuzz subset fuzzer treats the whole input as a font blob, creates a face, gathers Unicode coverage, and runs subsetting. For larger inputs, trailing bytes can influence subset text and flags, but there is no external wrapper format.
- The lcms fuzzer passes the raw input directly to profile-open-from-memory. If a source profile opens, it creates an sRGB destination profile, derives a source pixel format from the source colorspace, creates a transform, and executes one transform sample.
- The libFuzzer target passes the input buffer directly to Assimp Importer::ReadFileFromMemory with the realtime quality postprocess preset and no filename extension. Format detection is signature/content based, then normal post-processing invokes ScenePreprocessor.
- The actual target is the Ghostscript ps2write device fuzzer. It runs raw input as PostScript. The internal .parsecff operator is callable from PostScript with a boolean and a string or block array, so CFF bytes can be supplied as a hex string without a full font wrapper.
- The MuPDF PDF fuzzer consumes raw PDF bytes. The document must be structurally valid enough to load a page, resolve resources, load the font's ToUnicode CMap, and render or interpret text content.
- The libFuzzer target passes the entire input buffer to plist_from_openstep and then calls plist_free on the returned root node. There is no selector byte or outer file envelope.
- The harness writes the raw fuzzer bytes to a temporary configuration file and runs the broker in test-configuration mode with that file. It does not feed MQTT packets; successful parsing prints that the configuration file is OK and then exits through configuration cleanup.
- The libFuzzer input is written directly to a temporary Mosquitto configuration file and checked with broker test-config mode. Although the task metadata suggested an archive-like format, the active harness consumes raw config text with no wrapper.
- After reading entities, the harness parses the source document and stylesheet, installs namespaces and security preferences, applies a malloc-failure limit just before stylesheet construction/parsing, compiles the stylesheet, applies it, optionally serializes the result, then clears the allocation limit and frees all parser state.
- The file fuzzer checks file type, reads the full raw input into a heif_context, obtains primary and top-level image handles, decodes images, and queries thumbnails and metadata. There is no fuzzer-specific selector; the HEIF box graph must be structurally valid enough for context loading.
- The verifier runs curl_fuzzer_ws. The input is not a null-separated command-line argv contract. Some raw byte patterns are treated as paths or corpus-directory inputs by the harness wrapper, while plain header-like blobs execute the websocket fuzzer and exit normally.
- The fuzzer writes raw input bytes to a temporary file and runs a binutils/BFD display path that performs target detection, section dumping, disassembly, and synthetic symbol processing when the object format and options allow it.
- The fuzzer copies the entire input to a NUL-terminated buffer, opens an mruby state, calls mrb_load_string on the buffer, closes the state, and frees the copy. There is no length prefix, selector, or file container.
- The matio fuzzer writes the raw input to a temporary file, opens it as a MAT file, then iterates variable info and variable data. There is no harness prefix; HDF5 validity and MATLAB metadata drive reachability.
- The libFuzzer target consumes fields front-to-back from a little-endian ByteStream, creates a RawImage, reads slice metadata, constructs Cr2Decompressor on the remaining stream, allocates image storage, calls decode, and swallows RawSpeed exceptions.
- The GraphicsMagick coder fuzzer passes the raw input as a Magick blob to the MIFF decoder. There is no outer file carving; the header and pixel payload are exactly the fuzzer bytes.
- The fuzzer may consume a small leading options prefix when the input starts with the options sentinel; otherwise the bytes are interpreted as UTF-8 text format. It parses into a generated fuzz message and serializes or validates the message if parsing succeeds.
- The svc decoder fuzzer derives color format, core count, architecture, and target dependency layer from early input bytes, creates the decoder, decodes headers to establish output dimensions, allocates output frame buffers, then repeatedly decodes frames and reallocates when reported dimensions change.
- The target_dec_fuzzer scans raw input for packet separators, opens a fixed decoder, optionally reads codec context fields and extradata from a trailing block when the input is large enough, and decodes packet by packet until exhaustion or an iteration cap.
- The target binary is fuzz_probe_analyze. It runs GPAC file probing and inspection on the raw input as a media asset; successful probes emit XML inspection records. Inputs that do not map to a known media filter fail before HEVC parsing.
- The fuzzer writes raw bytes to a temporary image file, loads it with TurboJPEG image loading, allocates source-derived YUV and JPEG destination buffers with malloc, enables no-reallocation for compression, and touches compressed output bytes only when the API reports success.

## Round 12 Format Links
- [[ar-archive]]
- [[ase]]
- [[assimp-model]]
- [[avif-bmff]]
- [[blosc-compressed-chunk]]
- [[bmp-source-image]]
- [[capstone-disasm-selector-plus-bytes]]
- [[cil]]
- [[curl-websocket-fuzzer-input]]
- [[elf32-arm]]
- [[fluent-bit-parser-fuzzer-control-plus-record]]
- [[git-raw-object]]
- [[gpac-media-probe-input]]
- [[heif]]
- [[hevc-elementary-stream]]
- [[icc-profile]]
- [[javascript-source]]
- [[jpeg-exif-or-raw-exif]]
- [[jpeg-xl-fuzzer-input]]
- [[libxslt-fuzz-entities]]
- [[mat73-hdf5]]
- [[miff]]
- [[mng]]
- [[mosquitto-broker-config]]
- [[mosquitto-config-text]]
- [[mruby-script]]
- [[netbios-name-service-packet]]
- [[opensc-fuzz-reader-chunks]]
- [[opensc-pkcs15-reader-chunk-stream]]
- [[openstep-plist]]
- [[openthread-cli-uart]]
- [[opentype-font]]
- [[pdf]]
- [[pdf-cmap]]
- [[php-script]]
- [[postscript-with-cff-data]]
- [[rawspeed-cr2-decompressor-envelope]]
- [[ruby-source]]
- [[samsung-srw-tiff]]
- [[svc-h264-annex-b-stream]]
- [[swift-protobuf-text-format]]
- [[wav-riff-exif]]

## Round 12 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 13 Facts
- The selected wrapper is the GPG signature-verification libFuzzer target. It writes raw input bytes to a temporary GPG file, initializes a temporary homedir/trustdb, then runs signature verification APIs on that file. There is no front selector or FuzzedDataProvider carving.
- The libFuzzer target compiles a YARA rule importing the ELF module and scans the input buffer directly. There is no selector byte, file wrapper, argv layer, or FuzzedDataProvider carving.
- The arvo wrapper launches the Wireshark fuzzshark IP target on a single file copied to the fixed input path. There is no FuzzedDataProvider carving or mode byte in the input bytes.
- The selected wrapper is the OpenSSL X.509 fuzzer. It consumes the entire PoC as DER for d2i_X509, then prints the certificate and extensions to a null BIO. There is no command-line selector; standalone GENERAL_NAME DER does not reach the selected harness path.
- The harness uses FuzzedDataProvider from the front of the input: it consumes reader options first, then an encoding string, and writes the remaining bytes to a temporary file passed to xmlReaderForFile. Inputs that ignore this carving are interpreted as options and encoding before any XML bytes are seen.
- The libarchive harness feeds the entire input as one archive byte stream through archive_read_support_format_all and drains each entry with archive_read_data. It does not provide separate filenames or external multi-volume files.
- The readelf libFuzzer wrapper writes raw input bytes to a temporary file, enables broad readelf display modes including dynamic symbols, and calls process_file on that file. There is no input carving or front selector.
- The libFuzzer target passes the raw input buffer directly to blosc2_schunk_from_buffer, then attempts frame decompression. Valid seed frames from the in-repo corpus reach the frame parser; broad outer-frame corruption tends to stop before metalayer access.
- The harness feeds raw document bytes to the Ghostscript raster conversion target. There is no fuzzer-side byte carving; document syntax and font embedding are responsible for reaching the FreeType glyph path.
- The wrapper is fixed to the Ghostscript xpswrite device. It consumes raw document bytes from the PoC as stdin-style input with no selector, invokes Ghostscript with xpswrite output to a null destination, then exits the Ghostscript instance.
- The Ghostscript fuzzer consumes raw PostScript or PDF-like bytes as a document stream and renders through a selected device. There is no leading mode selector or FuzzedDataProvider layout.
- The selected target is the ImageMagick SUN encoder libFuzzer harness. The harness consumes the whole input as a blob, forces the read and write format to SUN, reads the image from raw bytes, and then writes it back to a SUN output blob. There is no leading mode selector and no FuzzedDataProvider carving.
- The fuzzer installs a fake smart subtransport whose read callback copies the raw input bytes into libgit2's network buffer. There is no outer file format or fuzzer-side carving; all structure is the Git wire protocol itself.
- The selected libFuzzer target writes the raw input bytes to a temporary Mosquitto configuration file and invokes the broker in test-configuration mode. There is no binary envelope, mode selector, MQTT packet wrapper, or FuzzedDataProvider carving.
- The RawSpeed fuzzer passes raw file bytes to RawParser and then to the selected decoder. There is no front selector; the parser chooses a decoder from TIFF/RAW metadata and then runs raw decoding and metadata decoding under exception handling.
- The C++ harness uses FuzzedDataProvider from the front of the byte stream for configuration and per-frame booleans. In this generated arvo image, the shell wrapper calls the libFuzzer binary without single-input mode, creating a mismatch with the worker runner's file-copy contract.
- The active fuzzer binary is selected by the executable name and, for DHCPv6, passes the raw libFuzzer byte buffer directly to the DHCPv6 protocol decoder. There is no leading mode byte and no FuzzedDataProvider carving; all selector behavior comes from the DHCPv6 message type and option codes inside the input.
- The oss-fuzz Assimp harness passes the raw libFuzzer byte buffer directly to Importer::ReadFileFromMemory with no extension hint. Format selection is signature based, and a recognized MD3 magic is enough to choose the MD3 importer. There is no leading mode byte, filename carving, or FuzzedDataProvider layout.
- The selected target is the pkcs15init fuzzer. It installs a fake reader, consumes virtual-card APDU chunks, and must be driven into a card-control key-generation operation. Raw APDU responses alone are insufficient unless the profile and operation input select the Starcos gen-key path.
- The target is the WMAVoice decoder fuzzer, not the ASF demuxer. It consumes raw decoder packets plus the decoder-fuzzer configuration tail; container bytes alone do not necessarily provide codec extradata or valid packet boundaries.
- The libFuzzer harness consumes the raw input file bytes directly. It writes those bytes to a temporary file, initializes a TurboJPEG compression handle, then loops over several pixel-format/subsampling/quality configurations. Each iteration tries to load the temporary file with the twelve-bit image loader; on success, most iterations allocate a fixed-size destination buffer, compress into it with reallocation disabled, and then reads the emitted compressed bytes to expose MemorySanitizer state. There is no leading mode byte and no FuzzedDataProvider layout.
- The individual FFmpeg demuxer fuzzer uses the Argo BRP demuxer directly. For inputs larger than the harness metadata threshold, the last metadata region is not part of the demuxer byte stream; it controls IO buffer size, seekability, advertised file size, filename suffix behavior, and interrupt budget. With seekability enabled, the harness exposes AVIO seeking to the demuxer, but reads still advance through the supplied byte stream, so a header lookahead can consume one block while later packet reading consumes following bytes.

## Round 14 Input Contract
- The libFuzzer target passes the input bytes directly to libgit2 object parsing helpers. There is no mode prefix or FuzzedDataProvider splitting; the harness supplies NUL-terminated object buffers internally before invoking object parsers.
- The libFuzzer target consumes the raw file bytes directly. The first byte is reduced modulo the platform table and the remaining bytes are disassembled with detail output enabled. There is no file-format wrapper, checksum, or length trailer.
- The MuPDF libFuzzer target consumes raw PDF bytes from memory, opens the document as PDF, iterates pages, rasterizes each page to an RGB pixmap, catches MuPDF exceptions, and treats only process-level sanitizer failures as crashes.
- Raw libFuzzer bytes are passed to stream_decompress. The first few bytes seed the harness PRNG and are not decompressed; the remaining bytes are split into pseudo-random input chunks and decompressed with pseudo-random output buffer sizes.
- The libFuzzer harness treats the final byte as the pcap linktype, then overwrites that byte with a string terminator and passes the remaining buffer to pcap_compile with optimization enabled. The filter text therefore must be complete before the last byte.
- The libFuzzer target consumes leading configuration bytes before constructing the parser input. The vulnerable parser receives a pointer into the buffer but retains a size or end relation from the uncarved input, so the harness contract matters more than JSON complexity.
- The fuzzer copies all raw bytes to a NUL-terminated buffer, opens an mruby state, calls the string loader, closes the state, and frees the copy. There is no selector, bytecode envelope, or FuzzedDataProvider layout.
- The binutils libFuzzer harness consumes raw object-file bytes, opens them through BFD, and runs the disassembler selected from the object architecture. Parser reachability depends on BFD accepting the ELF container and assigning the CRX architecture.
- The libFuzzer harness passes the raw byte buffer and explicit size directly to the UCL parser. There is no leading mode selector, no trailing checksum, and no requirement that the file be NUL terminated.
- The GraphicsMagick coder fuzzer treats the raw file bytes as a blob for a specific coder, reads the image, then, for writable coders, writes it back using the same coder. The selected binary was the PTIF-family TIFF coder; there was no extra fuzzer prefix.
- The htslib fuzzer copies raw bytes into an in-memory hFILE, opens it through hts_open logic, dispatches variant data to VCF read/write paths, and consumes the entire file as the candidate VCF/BCF stream.
- The uncompress fuzzer uses the first two input bytes to size the destination buffer, then passes the entire raw input, including those sizing bytes, to miniz uncompress. This means buffer sizing bytes are also part of the zlib stream unless the stream is arranged accordingly.
- The libFuzzer harness passes raw bytes to the chunk decompressor only after the total compressed-size field exactly matches the input size, the uncompressed size is nonzero, and the chunk validator accepts the header and block-start table.
- The libFuzzer target passes raw bytes to luaL_loadbufferx in text mode and then executes the compiled chunk. It does not call luaL_openlibs, so standard library functions are unavailable unless they are language builtins or explicitly defined by the input.
- The njs libFuzzer target treats the full byte string as a script, creates a VM with silent options, runs the process-script path once, and destroys the VM. There is no leading mode byte or external file wrapper.
- The njs libFuzzer target consumes raw bytes as a script, creates a VM with silent options, processes the script once, and reports only process-level crashes. There is no file or envelope header.
- The relevant fuzzers feed raw bytes to libexif constructors and then enumerate/dump EXIF entries and maker-note values. Reaching the sink requires the input to parse far enough that a recognized maker-note entry is later formatted, not merely loaded.
- The intended fuzzer is a raw WGSL reader to WGSL writer libFuzzer target. In this run, the local task wrapper expected a directory-style input path and exited before consuming the raw file bytes, so parser reachability could not be confirmed.
- The binutils libFuzzer wrapper feeds raw object-file bytes to an objdump-style target. Local verify labeled the low-level read helper as a sink mismatch, but the crashing stack traversed the AArch64 synthetic-symbol dynamic-section parser, so submission was required.
- The secilc fuzzer adds the raw input as a CIL source file, compiles the CIL database, builds a policydb, optimizes it, and writes it to a null output. The input is not binary policy and has no checksum or selector.
- The LibreDWG libFuzzer target consumes raw bytes, autodetects DWG/DXF/JSON, decodes into an in-memory DWG object, then randomly exercises output encoders. The target bug is in the DWG decode phase before output conversion.
- The jplist fuzz target passes the libFuzzer byte buffer directly to plist_from_json with the exact byte length and then frees the produced plist root.
- The libFuzzer harness passes raw bytes to Exiv2's read/print/write flow. The JP2 detector requires the signature box framing before the file-type box is parsed; no external filename extension or checksum is supplied by the harness.
- The H3 libFuzzer target rejects inputs smaller than the native argument structure, casts raw bytes directly to that structure, calls cellToVertex with the supplied index and vertex number, then also calls cellToVertexes, vertexToLatLng, and isValidVertex on the supplied index.
- The config fuzzer copies raw bytes into a NUL-terminated string, zeroes the domain global structure after default init, calls ddsi_config_init, and finalizes the returned config state if parsing succeeds.
- The mruby libFuzzer harness copies raw bytes into a NUL-terminated Ruby script and evaluates it with mrb_load_string. Crashes must be triggered by script execution; ordinary Ruby exceptions are caught by the interpreter path and do not count.
- The selected libFuzzer binary feeds the raw bytes directly to mruby as source code. There is no protobuf schema, no leading mode byte, and no FuzzedDataProvider splitting for this task.
- The binutils harness consumes raw object bytes, opens the file through BFD, and runs an addr2line-style lookup path. It prints unresolved source locations for accepted objects that do not contain a usable target line mapping.
- Although the source harness is a MuPDF document fuzzer, the task binary accepts raw image bytes and reaches the BMP loader directly. No leading selector, archive wrapper, or checksum was needed for the accepted carrier.
- The binutils harness consumes raw object bytes and runs an objcopy-like path. It accepts ELF containers and reports no recognized debugging information when the object lacks enough usable debug metadata for higher-level processing.
- Although the source harness is named pdf_fuzzer and opens the memory stream with a PDF label, MuPDF registers all document handlers and content recognition can route archive-like inputs into the CBZ/ZIP handler before rendering pages.
- The libFuzzer harness treats the input as raw bytes for a temporary protocols-file stream. Newlines delimit rules; there is no length prefix or checksum. A protocol-name delimiter must be present for the attribute parser to process the left-hand side.
- The libFuzzer target passes raw bytes to the MVC decoder. Several bytes at fixed positions are used as decoder configuration selectors such as architecture, color format, and core count, but the stream bytes are otherwise decoded directly through a header pass followed by repeated frame decode calls.
- The libxml2 harness forces DTD validation, disables XInclude, loads the escaped entity table, then runs pull parsing, post-parse validation, push parsing, and reader traversal under the same allocation-failure limit. It checks whether malloc failure reporting matches each parser mode.
- The GDAL harness maps the raw fuzz bytes as a virtual tar file and opens a fixed data-file path inside that tar. It then reads up to a bounded raster window from opened datasets, which is what exercises EHdrRasterBand block reads.
- The mruby libFuzzer harness evaluates the raw byte buffer as a NUL-terminated Ruby script. There is no binary bytecode wrapper or length prefix; the script must both reach the BigInt path and exercise a later operation that exposes the bad state.
- The UPX fuzzer writes raw input bytes to a temporary file and runs the packed-file test/list path through PackMaster. There is no fuzzer prefix; a syntactically plausible Mach-O sample is needed before the Mach-O packer logic is reached.
- The libheif file fuzzer consumes raw HEIF file bytes, checks file type and brand, reads a context from memory, obtains the primary image and all top-level image handles, queries metadata and dimensions, and attempts image decoding for primary, top-level, and thumbnail handles.
- The fuzz target builds an xmllint argv internally from structured front-loaded fields, then registers the first entity as the main input document unless its URL begins with a dash. Resource loading resolves URLs from the serialized entity table.
- The FFmpeg target decoder fuzzer treats the main prefix as packet data. When the input is large enough, the final fixed-size suffix is consumed as decoder configuration, including dimensions, parser enablement, flags, extradata size, keyframe patterning, and flush behavior.

## Round 14 Format Links
- [[blosc2-chunk]]
- [[bmp]]
- [[capstone-disasm-selector-plus-bytes]]
- [[cyclonedds-xml-config]]
- [[dwg-dxf-json-autodetect]]
- [[ehdr-tar]]
- [[elf]]
- [[elf-crx-object]]
- [[elf-shf-compressed-debug-section]]
- [[elf-with-stabs-debug-sections]]
- [[git-raw-object]]
- [[h264-annexb-mvc]]
- [[h3-raw-native-struct]]
- [[heif-isobmff]]
- [[hevc-elementary-stream]]
- [[javascript]]
- [[javascript-source]]
- [[jp2]]
- [[jpeg-exif]]
- [[json]]
- [[json-with-settings-prefix]]
- [[libxml2-lint-fuzzdata]]
- [[libxml2-valid-fuzzer-envelope]]
- [[lua-source]]
- [[macho]]
- [[mruby-script]]
- [[ndpi-custom-protocol-rule]]
- [[pcap-filter-expression]]
- [[pdf]]
- [[ruby-script]]
- [[ruby-source]]
- [[selinux-cil-policy-text]]
- [[tiff]]
- [[vcf-text]]
- [[wgsl]]
- [[zip]]
- [[zlib-deflate]]
- [[zstd-legacy]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 15 Input Contract
- The fuzzer passes the input bytes directly as a C string after requiring at least one payload byte,
  a trailing NUL, and no newline. The same string is tried as flow keys and then as ODP actions; there
  is no outer file format, selector byte, checksum, or FuzzedDataProvider layout.
- The libFuzzer object harness feeds the raw input buffer to libgit2 object decoding for several
  object types, including tree. There is no leading selector byte and no FuzzedDataProvider carving;
  the same bytes are parsed as the tree body when that object type is attempted.
- The fuzzshark target was configured for the IP dissector and consumes the PoC bytes directly as an
  IP packet. There is no pcap file envelope, no libpcap record header, and no external filename-based
  dispatch.
- The libFuzzer harness passes raw bytes as the candidate binary input. The target opens the bytes as
  a file or buffer and dispatches binary format plugin detection directly; there is no leading mode
  selector and no FuzzedDataProvider layout.
- The libFuzzer target opens the FDK-AAC decoder in the LOAS transport mode, fills the decoder
  directly from the raw fuzzer buffer, and calls DecodeFrame in a loop. There is no outer file wrapper
  or FuzzedDataProvider field layout.
- The libFuzzer harness feeds raw bytes to ass_read_memory, then renders each parsed event at a
  timestamp inside the event. No outer file envelope or byte carving is used.
- The TIFF decoder fuzzer parses raw bytes as a TIFF-family image and directly exercises the SRW
  decoder when the metadata selects it. There is no filename gate, mode selector, or
  FuzzedDataProvider layout.
- The active executable reported by the verifier is a RawSpeed Threefr TIFF decoder fuzzer that
  consumes the raw file bytes. It does not use a FuzzedDataProvider layout. CIFF-shaped bytes alone
  were not enough to make the active target exercise the CIFF parser path.
- The selected libFuzzer target passes the raw file bytes directly to the gd GIF memory loader; there
  is no leading selector, sidecar file, checksum, or FuzzedDataProvider split.
- The libFuzzer harness passes the raw buffer to the SIP message parser and then exercises selected
  parsed header/address paths. There is no leading selector byte and no FuzzedDataProvider layout.
- The libFuzzer target converts the raw input to a zero-terminated string and calls uloc_canonicalize
  with a fixed-capacity output buffer. There is no length prefix, mode selector, or FuzzedDataProvider
  consumption.
- The FreeRADIUS fuzzer passes raw bytes to the selected protocol decode test point. There is no IP or
  UDP envelope; the input is the DNS message buffer passed directly to protocol decoding.
- The libFuzzer target forwards the entire input buffer to the JSON plist parser. There is no leading
  selector, length prefix, FuzzedDataProvider split, or external file envelope.
- The harness copies the raw bytes into a NUL-terminated string and calls mrb_load_string in a fresh
  mruby state. There is no front selector, no binary mrbc loader, and no FuzzedDataProvider layout.
- The libFuzzer bytes are passed to the GStreamer discoverer target as a file-like input. The file
  must look enough like a subtitle stream for type detection to select SubRip; there is no leading
  selector and no FuzzedDataProvider layout.
- The libFuzzer target passes the complete input buffer directly to the OpenStep plist parser. There
  is no mode byte, FuzzedDataProvider carving, or filename container around the supplied bytes.
- The generated target is the MIFF encoder fuzzer. It treats the entire raw input as a MIFF image
  blob, reads it through Magick++ with the MIFF encoder selected, and then writes it back if reading
  succeeds. There is no harness prefix or separate option carving.
- The selected libFuzzer target was the OpenEXR core-check fuzzer. It consumes a raw EXR-like file and
  runs structural file checks; there is no pcap, archive wrapper, or front selector byte.
- The libFuzzer harness copies raw bytes into a NUL-terminated source string and executes it with the
  mruby string loader. There is no file container, selector byte, or FuzzedDataProvider layout.
- The libFuzzer entry point constructs a VP9 decoder and calls receive_sample with the raw input span.
  No container parser, filename, length prefix, mode byte, or FuzzedDataProvider field extraction is
  involved.
- The HTML fuzzer consumes a front control area before the document: parser options are read first,
  then an allocation limit is derived, and the remaining bytes are the HTML document. It runs both
  pull parsing and push parsing over the same remaining document, with the push parser feeding bounded
  chunks.
- The libFuzzer harness passes raw bytes to the libxaac decoder wrapper. The first bytes influence
  ADTS detection and decoder configuration; there is no file container outside the codec byte stream.
- The libFuzzer harness passes raw decoder bytes to the libxaac decoder target. There is no leading
  mode selector, archive layer, or FuzzedDataProvider layout.
- The selected libFuzzer binary was the libxml2 API target. It interprets the input as a sequence of
  API operations and operands, so reachability depends on selecting the namespace-search operation and
  constructing a tree state through prior operations.
- The ERS-specialized GDAL fuzzer stores bytes in a virtual archive and opens a fixed ERS filename
  through the virtual tar path, so sibling files in the archive are visible to the driver. There is no
  selector byte and no FuzzedDataProvider layout.
- The packaged run command selected the cranelift-fuzzgen libFuzzer binary. It passes the raw input to
  Arbitrary-derived test-case generation, then compiles/interprets generated Cranelift functions.
  There is no stable byte offset contract comparable to a file format header.
- The fuzz target reads the raw input as an IPP file using ippReadIO, then resets the request state
  and writes it to a null output using ippWriteIO. There is no front selector or FuzzedDataProvider
  layout; the complete file must be a syntactically plausible IPP message.
- The harness is a libFuzzer target for the selected FFmpeg encoder. It opens a codec context from the
  trailer configuration, allocates an AVFrame, copies front-region bytes into available frame buffers
  with zero-fill for the rest, and repeatedly sends the frame to the encoder.
- The VC1 target_dec_fuzzer treats the raw prefix as one or more decoder packets split by a fixed tag
  marker. If the input is large enough, the final control block is consumed as little-endian fuzzer
  configuration; optional extradata is carved from the end of the remaining prefix before packet
  decoding. The video get_buffer hook allocates exact image planes without zero-initializing them,
  which is the relevant harness difference from production allocation.

## Format Links
- [[aac-loas]]
- [[aac-usac]]
- [[aac-xaac-decoder-stream]]
- [[ass-subtitle]]
- [[dns-message]]
- [[ers-fuzzer-archive]]
- [[ffmpeg-target-encoder-frame]]
- [[gif]]
- [[git-tree-object-body]]
- [[html]]
- [[icu-locale-id]]
- [[ipp]]
- [[json]]
- [[libfuzzer-arbitrary-cranelift]]
- [[libxml2-api-fuzzer-envelope]]
- [[miff]]
- [[mruby-script]]
- [[mruby-source]]
- [[omf]]
- [[openexr-file]]
- [[openstep-plist]]
- [[ovs-odp-action-text]]
- [[raw-ip-packet]]
- [[rawspeed-ciff]]
- [[sip]]
- [[subrip]]
- [[tiff-srw]]
- [[vc1-elementary-stream]]
- [[vp9-frame]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 16 Input Contract
- The YARA harness consumes the file bytes directly as a scan target; there is no leading mode selector or FuzzedDataProvider envelope. Parser reachability depends on the PE loader mapping sections and the dotnet module accepting the CLR metadata streams.
- The GraphicsMagick coder fuzzer feeds the raw input bytes as a Magick blob to the MNG reader. There is no leading mode byte, container wrapper, or FuzzedDataProvider carving.
- The libFuzzer harness carves the last bytes of the input into flavour, machine and architecture controls and passes the remaining leading bytes as the disassembler buffer. Parser reach requires the architecture and machine controls to select the intended disassembler.
- The Leptonica fuzzer reads raw file bytes as an image and then runs image operations after successful decode. There is no external wrapper; reaching the vulnerable path requires the TIFF loader to produce a Pix from the old-JPEG branch before the rotate/shear operation.
- The stb_image fuzzer receives raw bytes, first calls the info parser, rejects very large decoded dimensions, and then decodes the same memory buffer with a requested RGBA output. There is no prefix or external file wrapper.
- The harness feeds the raw file bytes directly to the Blosc decompression fuzzer. There is no leading mode byte or datasource envelope; parser reach depends on a self-consistent chunk header and enough block/table data for the decompressor selected by the header.
- The decompression fuzzer consumes raw chunk bytes. It rejects short inputs, rejects a header compressed size different from the file size, rejects zero uncompressed size, validates the compressed buffer, allocates an output buffer, then calls Blosc decompression.
- The selected binary is the wolfSSL RSA libFuzzer target. Bytes are not raw RSA keys; they are consumed front-to-back by the datasource. Choosing fixed P, Q and E skips their string fields, while D is always parsed. An operation selector outside the implemented cases still exercises key-field parsing before returning.
- The fuzzer consumes fields front-to-back: optional proxy text, URI text, method byte, authentication text, buffer-size controls, a large custom-header key view, and finally a fixed-size null-terminated response slice assigned to the client response before calling the parser helper.
- The MuPDF fuzzer opens the raw bytes as a PDF stream, counts pages, and renders every page to an RGB pixmap with the identity transform. It does not use a prefix, mode selector, or FuzzedDataProvider layout.
- The secilc libFuzzer harness treats the input as one raw CIL source file, adds it to a policy database, compiles it and attempts policydb output. There is no binary envelope or mode selector; syntactic validity and enough base policy declarations are required before optional-block reset logic is reached.
- The BFD fuzzer consumes raw bytes as an input file and lets BFD auto-detect the format. There is no selector byte; reaching the sink requires BFD to classify the bytes as a VMS object/library and invoke the VMS index traversal code.
- The mruby fuzzer copies the raw input into a NUL-terminated buffer, opens a fresh mruby VM, calls mrb_load_string on that source, closes the VM, and frees the buffer. No bytes are carved before parsing.
- The HarfBuzz subset fuzzer consumes raw font bytes as a whole font. There is no datasource envelope. Parser reach requires a valid enough sfnt/OpenType structure for the subset pipeline to load faces and build subset maps.
- The Ghostscript raster fuzzer passes raw stdin bytes to gsapi with a cups raster output device. There is no fuzzer envelope; a valid enough PDF header, objects, xref stream, startxref, and EOF marker are required for the PDF interpreter to reach xref processing.
- The nDPI fuzzer passes the raw input bytes directly to ndpi_detection_process_packet. The input is not pcap-framed; IP/TCP headers, ports, and TLS record shape determine whether the TLS parser path is selected.
- The harness creates a fresh Lua state, loads the raw bytes with text-only mode and executes the chunk only if loading succeeds. Standard libraries are not opened, so candidates must avoid depending on library globals for reachability.
- The lcms harness consumes raw profile bytes from memory and exercises profile opening plus color-management operations. There is no wrapper; the profile header and tag table must remain coherent enough for profile creation before malformed tag internals matter.
- The H3 fuzzer treats the raw bytes as the struct when enough bytes are present. It calls grid distance/path helpers on the two indexes, calls localIjToCell with mode zero, calls cellToLocalIj, then repeats local-IJ conversion using the supplied mode.
- The LibRaw fuzzer feeds the raw input buffer to `open_buffer`, then attempts unpacking and processing modes. There is no extra envelope. Inputs above the harness size limit are ignored; valid seed-mutation is preferable to constructing a RAW file from scratch.
- The libxml2 valid fuzzer consumes fixed-size option fields first, configures validation-oriented parsing, then reads entity strings from the remaining bytes. Raw XML bytes without this envelope do not exercise the same parser path.
- The libxml2 HTML fuzzer does not treat all bytes purely as document text; a leading control area can select parser options and allocation behavior before the remaining bytes are parsed as HTML. The harness exercises both pull and push parsing paths with bounded chunks.
- The active binary is the generic raw disassembler fuzzer, not the extended two-region disassembler harness. It uses little-endian display/endian settings, derives the architecture and machine from the trailing selector fields, then repeatedly calls the selected disassembler on the instruction buffer.
- The libxaac encoder fuzzer consumes configuration fields before any PCM bytes. If creation succeeds, it obtains the encoder input buffer, initializes it, then loops over remaining provider bytes choosing either copied bytes or a repeated fill value before each process call.
- The ntopng harness wraps the raw bytes with `fmemopen`, opens them through libpcap offline parsing, sets the datalink from the PCAP and passes each packet record to the packet dissector. Packet record captured length and original length influence the trusted L4 length used by the ICMP parser.
- The ntopng fuzzer opens the input as an offline pcap stream, sets the datalink from the pcap handle, and passes each packet to packet dissection. Reaching the DHCP option parser requires pcap framing, link/IP/UDP decoding, ndpi protocol classification as DHCP, and host/flow state sufficient for the DHCP branch.
- The Wireshark fuzzshark target is configured for the DNS dissector in the UDP-port dissector table and passes the raw input buffer as packet data through epan. The input is not a pcap file and does not need IP or UDP headers for this target.
- The Pulley fuzzer consumes raw bytes with `arbitrary::Unstructured`. In interpreter mode it parses a vector of materialized ops, filters out unsafe ops, appends a return operation, encodes the retained ops to Pulley bytecode and runs the interpreter. The vulnerable filter permits `GetSp` even when its destination is a special register.

## Round 16 Format Links
- [[arbitrary-pulley-op-vector]]
- [[binutils-disassembler-frame]]
- [[blosc-chunk]]
- [[blosc-compressed-chunk]]
- [[cil-policy-text]]
- [[dns-message]]
- [[fluent-bit-http-fuzzer-envelope]]
- [[fuji-raf-raw]]
- [[fuzzeddataprovider-encoder-config-plus-pcm]]
- [[fuzzing-datasource-rsa-fields]]
- [[h3-raw-native-struct]]
- [[html]]
- [[icc-profile]]
- [[ipv4-tcp-tls]]
- [[jpeg]]
- [[libxml2-valid-fuzzer-entity-envelope]]
- [[lua-source]]
- [[mng]]
- [[mruby-source]]
- [[opentype-font]]
- [[pcap-dhcpv4]]
- [[pcap-ethernet-ip-icmp]]
- [[pdf]]
- [[pdf-xref-stream]]
- [[pe-dotnet]]
- [[raw-disassembler-buffer]]
- [[tiff-ojpeg]]
- [[vms-bfd-object-or-library]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 17 Input Contract
- The MuPDF pdf_fuzzer consumes raw PDF bytes from the input file, opens them as a PDF stream, counts pages, and renders page pixmaps.
- There is no fuzzer-side prefix or mode byte; malformed xrefs may be repaired locally but often form an off-target basin.
- The harness is libFuzzer raw bytes passed to fuzzshark.
- It initializes a packet record with a generic encapsulation value and runs epan dissection directly; there is no filename, archive, or length prefix added by the harness.
- The htslib hts_open fuzzer opens raw input bytes as an in-memory hts file.
- When the detected category is sequence data, it reads the SAM/BAM/CRAM header, then loops over records and writes them to a SAM sink, exercising both read-time validation logs and write-time formatting.
- The harness writes the raw fuzz bytes to a temporary pcap path, opens it with PcapFileReaderDevice, reads one packet, constructs a Packet from the RawPacket, and queries IPv4 layers.
- There is no extra carving beyond the file bytes.
- The libFuzzer harness consumes raw bytes directly and interprets the leading bytes as mode and request fields for the Fluent Bit signv4 canonical request path.
- No checksum or external file wrapper is used.
- The secilc fuzzer consumes raw CIL policy text, adds it as an in-memory policy file, compiles it, builds the policy database, and runs optimization/write paths.
- There is no leading mode selector or length prefix.
- The harness passes raw bytes to RawSpeed Buffer and RawParser, obtains a decoder, disables strict unknown-camera failure, then calls decodeRaw and decodeMetaData while swallowing RawspeedException at the outer level.
- The fuzz_policy target reads raw newline-delimited text with no binary framing.
- It iterates multiple policy passes over the same parsed arrays, invokes the sudoers policy plugin, and stubs some platform services.
- Environment variables must be supplied through env lines, but policy may reject them unless the settings allow them.
- The harness feeds raw bytes to OpenEXR checkFile in memory.
- It exercises both C++ stream checks and the core in-memory read callback; no filename extension or archive wrapper is required.
- The MuPDF pdf_fuzzer reads raw PDF bytes directly, opens them as a document stream, and renders pages.
- There is no harness-level selector; failures caught by MuPDF exception handling may be swallowed unless they corrupt state across the protected region.
- The harness writes the carved affix and dictionary halves to temporary files, constructs Hunspell from them, calls spell on the carved word, and only calls suggest if spell rejects the word.
- The fuzzshark harness consumes raw bytes but is configured for a specific dissector/table pair, not automatically for every Wireshark dissector.
- For this task the observable initialization disabled other protocol paths and configured UDP under the IP protocol table; raw wiretap-encapsulation ALP bytes were not dispatched to the target dissector.
- The harness writes raw bytes as a temporary object file, opens it with BFD, checks object format, and asks BFD to load separate debug-file information.
- There is no archive wrapper unless the input itself is an archive.
- The php-fuzz-execute harness executes raw PHP source from the input file.
- There is no leading mode byte.
- Engine startup and script execution complete normally unless the PHP code itself invokes the vulnerable API path.
- The harness first parses FuzzBuffer chunks.
- Each chunk becomes a DLT_RAW Packet passed to Zeek packet_mgr, and event cleanup runs after each chunk.
- Inputs lacking the packet magic are ignored before packet parsing.
- The generated libxml2 fuzzer consumes raw XML-like bytes and initializes the fuzz target internally.
- There is no external length prefix or FuzzedDataProvider contract.
- The observable output confirms fuzzer initialization and normal execution even when XML parsing errors are present.
- The harness stores raw bytes as a tar in /vsimem and opens /vsitar/{...}/testavc with the AVCBIN OGR driver.
- It uses the OGR generic fuzzer path to open the dataset and iterate layers/features.
- The newer hts_open fuzzer first sniffs the raw input as an in-memory hts file, then for sequence data reopens the same bytes and writes them through SAM, BAM, and CRAM output modes.
- This means a SAM input can trigger CRAM encoder bugs even though the input itself is not a CRAM file.
- The libFuzzer harness executes the raw buffer as a PHP request from memory.
- It compiles and runs the supplied source with normal PHP runtime semantics; no filename wrapper or length prefix is required beyond the fuzz buffer size.

## Round 17 Format Links
- [[avcbin-tar-coverage]]
- [[bam]]
- [[cil-policy-text]]
- [[elf-dwarf-aranges]]
- [[fluent-bit-signv4-fuzzer-buffer]]
- [[hunspell-aff-dic-word]]
- [[openexr]]
- [[pcap]]
- [[pdf]]
- [[php-script]]
- [[php-source]]
- [[sam]]
- [[sony-arw-tiff]]
- [[sudo-policy-lines]]
- [[wireshark-fuzzshark]]
- [[wireshark-rrc-packet]]
- [[xml]]
- [[zeek-fuzzbuffer-ip-gre-ieee80211]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[pdf]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 18 Input Contract

### Schema / Invariants
- The decoder fuzzer feeds the raw input as a complete FLAC byte stream to the FLAC decoder. There is no FuzzedDataProvider carving or mode selector in the extracted target; file structure gates are the FLAC marker, metadata, frame headers, and per-frame CRC checks.
- The libFuzzer harness feeds the raw byte buffer to multiple KArchive handlers, including the 7z handler, without a selector byte or FuzzedDataProvider layout.
- The libFuzzer bytes are consumed directly by a little-endian ByteStream helper. The harness builds a RawImage from leading scalar fields, reads a declared number of strip records from the remaining bytes, runs PhaseOneDecompressor::decompress, and then checks the allocated image buffer for initialized memory. There is no outer file magic or mode selector.
- The harness is libFuzzer over raw chunk bytes. It rejects inputs shorter than the Blosc minimum header, rejects total-size mismatches, validates the header, allocates an output buffer, and calls the Blosc decompressor directly. There is no mode selector or FuzzedDataProvider carving.
- OpenThread fuzz targets feed raw bytes to specific subsystems such as IP6 send, radio receive, NCP UART, and CLI UART. Some harnesses carve a leading byte as a link-security option before appending the remaining bytes to an OpenThread message.
- The OTS fuzzer passes the entire raw input buffer to OTSContext::Process with no leading selector. If the input is a font collection, the harness also processes each contained face. A single standalone sfnt font is therefore accepted as raw fuzzer input.
- The fuzzer passes the entire raw byte buffer directly to LibTTF load_from_memory. There is no wrapper, mode byte, checksum enforcement, or fuzzer-side carving.
- The harness consumes data with FuzzedDataProvider. It first consumes a capability array and init flags, may consume bytes to build an unserialized state, then repeatedly consumes booleans to choose serialization and parser read/write operations.
- The subset fuzzer treats the full byte buffer as the font blob. It always performs one subset attempt with a built-in codepoint list, and for sufficiently large inputs it also reads subset flags and a codepoint list from the tail of the same buffer. There is no separate container; appended tail data changes the second subset request as well as the font bytes.
- The LibRaw fuzzer consumes the front of the input as the camera file and uses a FuzzedDataProvider-style tail for runtime options and output-parameter toggles. Scalar consumers are taken from the back, so preserving the file bytes at the front while appending a configuration tail is required to avoid corrupting the image parser.
- The harness copies the entire raw input into a NUL-terminated buffer and evaluates it with mrb_load_string. There is no filename wrapper, selector byte, or FuzzedDataProvider carving.
- The observed local verifier ran the universal transform fuzzer rather than a raw CGATS loader. That harness reads leading scalar fields for source and destination pixel formats, then treats a fixed-size following slice as an ICC profile and the remaining bytes as transform data. Plain CGATS text therefore does not satisfy the active harness contract.
- The MuPDF PDF renderer harness consumes the whole raw buffer as a PDF memory stream, opens the document, counts pages, and renders pages. It has no prefix carving, and ordinary MuPDF exceptions are caught rather than counted as crashes.
- The fuzzer passes the raw input bytes as an in-memory PDF stream to the document loader, counts pages, and renders pages when available. There is no leading selector or carved metadata. Loader exceptions and repair failures are caught, so malformed PDFs often become no-crash warnings.
- The fuzz target feeds raw bytes directly to ddsi_typemap_deser, then iterates complete identifier-object pairs, maps complete identifiers to minimal identifiers, constructs dependent type-info arrays, calls ddsi_type_ref_proxy, adds the type object, and unreferences it. There is no fuzzer byte carving beyond the CDR deserializer.
- The Assimp harness passes the entire raw input to ReadFileFromMemory with the realtime-quality post-processing preset. There is no fuzzer selector byte or secondary container around the model.
- The observed fuzzer writes the raw input to a temporary file, initializes libdwarf from that file, walks compilation-unit and sibling DIE state, calls source-file and line-context helper paths, then performs cleanup. It is raw file input with no fuzzer prefix, but it did not match the location-list harness named in the task description.
- The libxaac encoder harness uses FuzzedDataProvider rather than raw AAC framing. Fields are consumed from the provider to configure encoder parameters and input data before invoking encoder processing.
- The first input byte is a selector and also influences the fixed-size byte-sink capacity. The remaining bytes are interpreted as a NUL-terminated locale string. Selector values congruent to the language-tag case call Locale::toLanguageTag with a CheckedArrayByteSink over a stack buffer, so the same leading byte both chooses the target path and constrains output space.
- The visible codebase includes URI and SIP stack consumers, but the generated arvo harness selection was not identified as a direct raw URI parser. No FuzzedDataProvider layout was observed for this task.
- The Poppler fuzzer passes raw bytes to load a PDF document from memory, skips locked or unloadable documents, then renders every page. There is no leading selector. The target JBIG2 code is reached only through page rendering of an image stream using the JBIG2 decoder.
- The visible libvips generic buffer harness feeds the whole raw input to vips_image_new_from_buffer and then writes the image to an output buffer. In this generated run, local verify reported a matrix-save buffer fuzzer, indicating the active harness did not match the task description.
- The miniz fuzzer passes raw bytes to the in-memory ZIP reader. If initialization succeeds, it iterates files, validates file headers, obtains names and stats, and attempts extraction. There is no leading selector or wrapper beyond normal ZIP structures.
- The FFmpeg target decoder harness runs the fixed H.264 decoder on the raw input as decoder packets. There is no outer media container requirement and no front selector byte; sufficiently large inputs may reserve tail bytes for codec context options.
- The targeted FFmpeg decoder fuzzer sends packet bytes directly to the selected decoder, optionally using a trailing fuzzer-control block to set codec context fields, parser use, flags, and extradata. Packets are split on an internal tag if present; otherwise the leading packet payload is decoded as one packet. There is no media container requirement for this target.

### Format Links
- [[7z-archive]]
- [[assimp-model]]
- [[blosc-chunk]]
- [[dds-xtypes-typemap-cdr]]
- [[elf-dwarf-object]]
- [[ffmpeg-notchlc-packet]]
- [[flac]]
- [[fuji-raf-raw]]
- [[h264-annex-b-stream]]
- [[icu-locale-id]]
- [[lcms-cgats-or-icc-transform-harness]]
- [[libxaac-encoder-fuzzed-provider-stream]]
- [[mruby-script]]
- [[openthread-meshcop-tlv-or-packet]]
- [[opentype-font-subset-input]]
- [[opentype-truetype-font]]
- [[pdf]]
- [[pdf-jbig2-image-stream]]
- [[pdf-with-tounicode-cmap]]
- [[rawspeed-phaseone-decompressor-envelope]]
- [[sip-uri-or-sip-message]]
- [[tiff]]
- [[truetype-sfnt]]
- [[usbredir-fuzzed-provider-stream]]
- [[zip]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 19 Input Contract

- libFuzzer feeds the entire file as the raw data buffer to libgit2 object parsing for multiple object types. There is no mode byte, length prefix, argv file format, or fuzzer-side terminator.
- Format link: [[git-raw-object]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 20 Input Contract
- The HarfBuzz fuzzer consumes the file bytes as a font blob. The subset-oriented harness also treats a trailing codepoint block as input text, so font data and selected glyph coverage can both influence reachability. No external filename or archive envelope is required.
- The libFuzzer target feeds raw file bytes directly into a jbig2 decoder context, then completes and outputs decoded pages. There is no extra mode selector or front/back field carving outside the JBIG2 stream.
- The harness passes the raw input as a NUL-terminated template string capped to an internal fixed buffer, compiles it with a descriptor exposing path strings and a file-list sequence, and frees the compiled template if compilation succeeds. There is no surrounding file header.
- The libFuzzer harness consumes the first four bytes from the front as a little-endian settings mask and passes all remaining bytes as the JSON buffer to JsonCpp's CharReader. There is no checksum or outer file container.
- The harness passes raw bytes directly to the Shell parser once. There is no container format, no leading mode byte, and no FuzzedDataProvider field carving.
- The harness consumes little-endian chunk lengths from the input. It connects a virtual reader, binds a PKCS#15 card, and only after a successful bind reads more chunks as operation inputs for object operations such as decipher, derive, wrap, unwrap, or signature.
- The harness searches for a NUL split marker. Bytes before it are parsed as WKT, and parsing the WKB begins at the split marker itself, so the marker also serves as the WKB endian selector. The harness then runs set-operation APIs on the two parsed geometries.
- The Ghostscript raster fuzz target consumes raw PostScript or PDF bytes through the interpreter. There is no task-level mode byte in the observed raster harness; accepted input must be a document that Ghostscript can initialize and process.
- The harness uses LLVM FuzzedDataProvider to consume many output-parameter scalars and then passes the remaining bytes to LibRaw::open_buffer. For this provider pattern, preserving the raw file as the remaining payload and placing parameter material where the provider consumes it is necessary to reach unpack and processing stages.
- The generated command uses a Ghostscript ps2write device fuzz target. It consumes raw document bytes, not standalone font bytes, so TrueType data needs a PostScript or PDF carrier that causes font loading and glyph rendering.
- The harness reads a leading word length and word bytes, then splits the remaining bytes evenly into temporary AFF and DIC files. It constructs Hunspell with those files, calls spell on the word, and calls suggest when the word is not accepted.
- The harness passes raw encoded image bytes to SkCodec, wraps the codec in SkAndroidCodec, constructs SkAnimatedImage, and repeatedly calls decodeNextFrame while drawing and advancing frames. There is no external mode selector or file wrapper beyond the image format.
- The Serenity FuzzTTF harness gives the entire input buffer directly to OpenType::Font::try_load_from_externally_owned_memory. There is no filename, archive, or mode byte; successful reachability depends on a structurally coherent sfnt directory and table set.
- The GPAC target is the probe/analyze fuzzer. It consumes raw media bytes and emits inspection output when a stream is recognized. There is no visible mode byte or FuzzedDataProvider field split in front of the media data.
- The actual harness parses the whole input as a TIFF structure, checks whether the DNG decoder is appropriate, constructs a DNG decoder, disables several optional failure modes, then calls raw decode and metadata decode. It does not pass the bytes directly to LJpegDecompressor.
- The FFmpeg SEGAFILM demuxer fuzzer consumes raw CPK bytes directly and dispatches to the Sega FILM demuxer. There is no extra wrapper, selector byte, or checksum outside the container format.

## Round 20 Format Links
- [[animated-image]]
- [[hunspell-aff-dic-word-triple]]
- [[jbig2]]
- [[json-with-settings-prefix]]
- [[libraw-fuzzed-provider-plus-raw-image]]
- [[lwan-template]]
- [[ogg-opus]]
- [[opensc-virtual-reader-apdu-stream]]
- [[opentype-font]]
- [[postscript-pdf-cmap]]
- [[postscript-pdf-truetype-font]]
- [[rawspeed-dng-tiff-raw-container]]
- [[sega-film-cpk]]
- [[shell-script]]
- [[wkt-plus-wkb-split-stream]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (http-request-with-proxy-v2-prefix)

- Raw bytes are copied into a fixed static request buffer and parsed from that copy. The harness always enables proxy-protocol parsing, but addressability is determined by the copied buffer rather than the original file length.

## Round 21 Format Links (http-request-with-proxy-v2-prefix)
- [[http-request-with-proxy-v2-prefix]]

## Round 21 Notes (http-request-with-proxy-v2-prefix)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (pe-dotnet)

- The YARA dotnet libFuzzer target scans the raw file bytes as a memory buffer with rules importing the dotnet module. There is no leading mode byte or FuzzedDataProvider carving.

## Round 21 Format Links (pe-dotnet)
- [[pe-dotnet]]

## Round 21 Notes (pe-dotnet)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (pdf)

- The Poppler harness feeds raw PDF bytes, loads the document from memory, iterates pages, and renders each page. There is no byte carving before the PDF parser.

## Round 21 Format Links (pdf)
- [[pdf]]

## Round 21 Notes (pdf)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (binutils-disassemble-buffer-with-selector-suffix)

- Raw libFuzzer bytes are used directly. The final bytes are carved by the harness into architecture and machine selectors; only the preceding bytes are disassembled.

## Round 21 Format Links (binutils-disassemble-buffer-with-selector-suffix)
- [[binutils-disassemble-buffer-with-selector-suffix]]

## Round 21 Notes (binutils-disassemble-buffer-with-selector-suffix)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (pcap-ipv6)

- The fuzzer writes the raw bytes to a temporary pcap file, opens it with PcapPlusPlus, reads the first packet, and constructs a parsed Packet. The PoC is the pcap file, not only the packet payload.

## Round 21 Format Links (pcap-ipv6)
- [[pcap-ipv6]]

## Round 21 Notes (pcap-ipv6)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (redis-format-string)

- The harness copies raw bytes into a NUL-terminated string, declares the output command pointer without initialization, calls redisFormatCommand with no variadic arguments, and frees the output pointer if it appears non-null.

## Round 21 Format Links (redis-format-string)
- [[redis-format-string]]

## Round 21 Notes (redis-format-string)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (c-blosc2-frame)

- The fuzzer passes raw bytes to blosc2_schunk_from_buffer and then decompresses chunks from the resulting super-chunk. The local wrapper reported a directory expectation for verify, so official submit was the reliable signal.

## Round 21 Format Links (c-blosc2-frame)
- [[c-blosc2-frame]]

## Round 21 Notes (c-blosc2-frame)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (dxf-text)

- The LibreDWG libFuzzer harness receives raw bytes, dispatches by leading syntax to DWG, JSON, or DXF text, adds null termination when needed, parses into a drawing, then may write the drawing through output encoders.

## Round 21 Format Links (dxf-text)
- [[dxf-text]]

## Round 21 Notes (dxf-text)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (shell-script)

- The libFuzzer harness passes the raw input bytes directly as a Shell::Parser source string and calls parse once. There is no container, selector byte, or FuzzedDataProvider carving.

## Round 21 Format Links (shell-script)
- [[shell-script]]

## Round 21 Notes (shell-script)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (apfs-disk-image)

- Raw bytes are wrapped by a memory-backed Sleuthkit image. The selected harness opens an APFS pool from that image, derives a pool image at a hard-coded container block, then calls the APFS filesystem walker.

## Round 21 Format Links (apfs-disk-image)
- [[apfs-disk-image]]

## Round 21 Notes (apfs-disk-image)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (sony-arw-tiff)

- The active RawSpeed TIFF decoder fuzzer consumes the raw bytes directly, parses the TIFF root, constructs ArwDecoder, disables crop/unknown-fail behavior, and catches RawSpeed exceptions. Sanitizer-visible faults must occur after parser acceptance.

## Round 21 Format Links (sony-arw-tiff)
- [[sony-arw-tiff]]

## Round 21 Notes (sony-arw-tiff)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (zstd-sequence-compression-api-bytes)

- The sequence_compression_api fuzzer consumes has-dictionary, dictionary size, window log, compression level, and block-delimiter mode from the end of the byte buffer. Explicit delimiter mode is selected by a consumed control value; the remaining bytes influence generated source and sequence content.

## Round 21 Format Links (zstd-sequence-compression-api-bytes)
- [[zstd-sequence-compression-api-bytes]]

## Round 21 Notes (zstd-sequence-compression-api-bytes)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (opensc-virtual-card-stream-asn1)

- The active OpenSC binary is fuzz_card. It consumes raw bytes as a virtual-card/card-driver transcript rather than as a bare ASN.1 object, with no separate file envelope.

## Round 21 Format Links (opensc-virtual-card-stream-asn1)
- [[opensc-virtual-card-stream-asn1]]

## Round 21 Notes (opensc-virtual-card-stream-asn1)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (ipv4-tcp-http)

- The harness initializes nDPI once, allocates a flow, passes the raw input bytes directly to ndpi_detection_process_packet, calls detection giveup, serializes the resulting flow, and frees the flow. There is no FuzzedDataProvider or filename-level parsing.

## Round 21 Format Links (ipv4-tcp-http)
- [[ipv4-tcp-http]]

## Round 21 Notes (ipv4-tcp-http)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (truetype-font-hdmx)

- Raw input is used as a HarfBuzz blob. The harness creates a face, subsets with default text, and optionally reads a tail region as flags and codepoints; appending unrelated tail bytes can make later over-reads addressable, so table placement inside the sfnt matters.

## Round 21 Format Links (truetype-font-hdmx)
- [[truetype-font-hdmx]]

## Round 21 Notes (truetype-font-hdmx)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (jpeg)

- The libjpeg-turbo source includes fuzzers and seed corpora for compression, decompression, and transform paths. The relevant harness is expected to consume a whole JPEG-like byte stream, not a separate parameter file.

## Round 21 Format Links (jpeg)
- [[jpeg]]

## Round 21 Notes (jpeg)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (icu-locale-id)

- The harness wraps raw bytes with MakeZeroTerminatedInput and calls uloc_isRightToLeft directly. There is no leading mode selector and no back-to-front field consumption.

## Round 21 Format Links (icu-locale-id)
- [[icu-locale-id]]

## Round 21 Notes (icu-locale-id)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (pcap-udp-bittorrent-utp)

- Raw bytes are opened with fmemopen and pcap_fopen_offline. Each decoded packet is passed to NetworkInterface::dissectPacket; the BitTorrent-specific flow hook is downstream of packet decoding and protocol classification.

## Round 21 Format Links (pcap-udp-bittorrent-utp)
- [[pcap-udp-bittorrent-utp]]

## Round 21 Notes (pcap-udp-bittorrent-utp)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (tpm2-command)

- The harness initializes libtpms TPM2 state, runs a fixed Startup command, processes the raw input as one TPM command, snapshots volatile/permanent state, restores it, and terminates. There is no file format wrapper beyond the TPM command bytes.

## Round 21 Format Links (tpm2-command)
- [[tpm2-command]]

## Round 21 Notes (tpm2-command)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (mruby-source)

- Raw libFuzzer bytes are treated as a null-terminated mruby source string and executed with mrb_load_string. There is no outer file format; syntax validity and source execution are the only harness gates.

## Round 21 Format Links (mruby-source)
- [[mruby-source]]

## Round 21 Notes (mruby-source)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (opentype-cff2-font)

- FreeType ftfuzzer treats the raw input as either a single font file or an archive of font files, opens faces and named instances, and exercises face loading and variation-coordinate paths. There is no leading mode selector byte.

## Round 21 Format Links (opentype-cff2-font)
- [[opentype-cff2-font]]

## Round 21 Notes (opentype-cff2-font)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (gdal-mrf-lerc)

- The GDAL fuzzer writes the raw input into a virtual or temporary dataset name, registers drivers, opens it, and for raster datasets reads checksums from bands. It does not automatically create MRF sidecar index or data files from separate inputs.

## Round 21 Format Links (gdal-mrf-lerc)
- [[gdal-mrf-lerc]]

## Round 21 Notes (gdal-mrf-lerc)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (liblouis-table-plus-escaped-text)

- Raw libFuzzer bytes are carved by the harness: the leading block is written to a temporary table file, lou_checkTable gates execution, and the remaining bytes are copied to a mutable string before _lou_extParseChars and translation.

## Round 21 Format Links (liblouis-table-plus-escaped-text)
- [[liblouis-table-plus-escaped-text]]

## Round 21 Notes (liblouis-table-plus-escaped-text)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (heif-isobmff)

- The libheif file fuzzer consumes the whole input as a HEIF file from memory, checks file type and brand, reads a context, obtains the primary and top-level image handles, queries dimensions and metadata, and attempts decoding. There is no selector byte or external corpus directory for this generated task.

## Round 21 Format Links (heif-isobmff)
- [[heif-isobmff]]

## Round 21 Notes (heif-isobmff)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (ffmpeg-av1-obu-stream)

- The demuxer fuzzer feeds raw bytes to the configured AV1 OBU demuxer. Small inputs are interpreted as the stream body; the demuxer repeatedly reads a bounded stack header and calls the OBU size parser during packet reads.

## Round 21 Format Links (ffmpeg-av1-obu-stream)
- [[ffmpeg-av1-obu-stream]]

## Round 21 Notes (ffmpeg-av1-obu-stream)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 22 Input Contract
- The GraphicsMagick coder fuzzer treats the whole input as a PTIF/TIFF blob and drives image loading. There is no external selector or FuzzedDataProvider contract; all reachability gates are TIFF header and IFD tag consistency.
- The libFuzzer harness passes the input bytes as a seekable raw WavPack file. It opens with tags, editable tags, wrapper handling, DSD-as-PCM, checksum bypass, and normalization flags, then exercises metadata, wrapper, layout, and sample decode APIs.
- The selected nDPI target is the pcap reader fuzzer, not the raw packet fuzzer. The input must be a capture file; packets inside the capture are fed through the nDPI workflow and then through TLS TCP detection.
- The libFuzzer input is carved from the back: final selector fields configure BFD architecture and machine, and the prefix becomes the buffer passed to the disassembler. Reaching the sink requires a valid selector combination before instruction bytes matter.
- The source tree contains a color-conversion fuzzer that consumes a raw front-to-back field layout, but the container wrapper for this task runs the file-fuzzer binary on the provided path. The worker can provide only a single file path as the PoC, so the described raw color-conversion harness was not the executed harness.
- The harness feeds raw bytes directly to LibRaw. There is no mode selector or FuzzedDataProvider carving; the first bytes must identify the raw-camera subformat.
- The libFuzzer harness rejects inputs below a small minimum size. Accepted bytes are written unchanged to a temporary file and passed to the HAProxy configuration reader; there is no file-format wrapper, checksum, or mode byte.
- The harness initializes libxml2, installs a custom entity loader, parses the main entity through tree, push, and reader APIs, then iterates reader nodes and attributes. Input is not raw XML; the XML document must be wrapped in the fuzzer entity envelope.
- The container wrapper invokes dct_fuzzer on the PoC path. The described decompressor path and the source-level JPEG image parser are not directly selected by this wrapper, so the harness contract is a raw fuzzer input for the DCT target rather than a normal JPEG decode command.
- The libssh2 client fuzzer writes the raw input to the server side of a socketpair, shuts down writing, and calls libssh2_session_handshake on the client side. The bytes must therefore be a mock server stream, not a complete bidirectional transcript or file format.
- The active fuzzer is the raw sudoers parser. It rejects tiny inputs, initializes fixed globals for a root user context running an id command with arguments, parses the byte stream as sudoers syntax, and only after a successful parse performs sudoers lookup twice and displays privileges.
- The harness feeds the entire raw input buffer as one c-blosc2 frame to the frame-loading path and then asks for variable-length metalayers. There is no mode selector, integrity side channel, or FuzzedDataProvider carving.
- The libFuzzer bytes are copied into a freshly allocated buffer, a string terminator is appended, and the result is passed directly to the speech synthesis API with SSML parsing enabled. There is no mode selector, checksum, or length-prefixed wrapper.
- The wrapper runs the Serenity FuzzJs target. The fuzzer feeds raw JavaScript source to the parser and executes it in the engine; there is no leading mode byte, corpus directory requirement, or structured binary container. The task generation step required manual recovery because source extraction hit an absolute-link packaging issue, but the runtime wrapper and source were available.
- Verify identifies the active target as a wolfSSL server fuzzer. The input is a raw client-to-server TLS byte stream; there is no length prefix, packet capture wrapper, or FuzzedDataProvider selector.
- The libFuzzer harness passes the raw byte buffer directly to Kamailio's parse_msg path, then asks follow-on parsers to inspect parsed headers. There is no wrapper or checksum; parser reachability depends on making the first line and target header recognizable.
- The harness compiles a fixed rule importing the PE module and scans the entire raw input buffer as a candidate PE file. There is no selector byte or FuzzedDataProvider split; the rule calls into PE helpers during the scan.
- The harness passes the raw input bytes to the libbpf in-memory object opener with a generated object name and closes the object only if opening succeeds. There is no archive wrapper or command-line option encoded in the input.
- The harness feeds raw bytes to LibRaw identification. There is no carved prefix; parser reachability depends on the first top-level atoms looking like a CR3 file.
- The oss-fuzzshark wrapper configures the IP dissector and disables several unrelated dissectors before processing capture-file inputs. The input is not raw packet bytes; it must be a valid capture envelope containing packets.
- The harness uses LLVM FuzzedDataProvider. A small selector is consumed from the back and must choose the gunzip path; a random-length string is then consumed as the compressed input. Treating the first byte as the mode selector is a dead end.
- The harness passes the raw input buffer directly to the PAC parser after enforcing a small minimum size and a bounded maximum size. There is no file container, checksum, or mode selector; all bytes are interpreted as the PAC blob.
- The active Ghostscript target was a device fuzzer that consumes the raw document bytes as a PDF/PostScript-like input. There is no FuzzedDataProvider carving; the input must be a complete document accepted by the interpreter.
- The libFuzzer harness parses the stylesheet and source document normally first. Only after both documents are accepted does it enable the allocation limit and call the XSLT stylesheet parser and transformer, so malformed XML or missing secondary entities prevents reaching the target allocation-failure path.
- The harness prefix contains two little-endian part lengths, a flags byte, and a decoder configuration struct. Part one is passed to decoder initialization, then parts two and three are decoded sequentially. A flag chooses between regular initialization and AudioSpecificConfig initialization.
- The harness opens the raw bytes as a PDF stream, iterates every page, and renders each page to a pixmap with a stack-local transform matrix. The input is not carved by a leading selector and is not a path to an external file.
- The harness passes raw config text to the Net-SNMP config reader. There is no binary envelope or selector byte; the first token on a line determines the parser feature.
- The active binary is the libxml2 DTD validation fuzzer. It forces DTD validation, sets the fuzz external-entity loader, enables the memory limit around pull, post-validation, push, and reader parser paths, and consumes raw libFuzzer bytes through the custom front-carved entity format.
- The GraphicsMagick coder fuzzer reads the raw input as a PDB blob through Magick++ image loading. There is no extra harness selector or FuzzedDataProvider carving; parser reachability depends on the PDB magic fields and record header consistency.
- The fuzzer loads raw bytes as a PDF document through the C++ Poppler API, skips locked or unloadable documents, and renders each page through a page renderer. The input is not a pcap, archive, or multi-file corpus; it is a single PDF byte stream.
- The fuzzer writes raw input bytes to a temporary file and invokes UPX list or test mode on that file. The input is not length-prefixed and has no selector; parser reachability depends on UPX recognizing the temporary file as a packed executable.
- The libFuzzer harness passes the raw byte vector to WAMR runtime initialization and wasm_runtime_load, then unloads any loaded module and destroys the runtime. There is no fuzzer prefix or archive wrapper; invalid modules are normally rejected during load.
- The harness passes the raw input bytes to libbpf as an in-memory object file. There is no selector byte or FuzzedDataProvider layout; the ELF section table and BTF/BTF.ext headers determine parser reachability.
- FuzzedDataProvider scalar fields are consumed from the back, leaving the front as the image buffer. The harness opens the remaining buffer, unpacks image and thumbnail data, converts raw data to an image, then runs several interpolation modes through dcraw processing.
- The harness is FFmpeg's target_dec_fuzzer built for the MVHA video decoder. If the input is long enough, the last fixed-size trailer sets width, height, parser flags, keyframe pattern, extradata size, and related context fields. The decoder receives raw packets from the prefix; normal media containers are not demuxed.
- The FFmpeg target decoder fuzzer treats front bytes as one or more decoder packets separated by a fixed fuzz tag. When the input is large enough, a fixed-size trailer at the back configures codec context fields such as bits per coded sample, flags, sample rate, and channel count. There is no file header requirement for this decoder target.
- The libFuzzer target is FFmpeg's target_dec_fuzzer compiled for the H263I decoder. It installs a custom video get_buffer2 callback that allocates frame buffers without zeroing, optionally initializes an AVParser from tail flags, decodes until iteration or pixel limits are hit, and treats clean decoded-pixel output as a non-crashing run.
- For larger inputs, the FFmpeg demuxer harness carves the tail into a binary control block and a filename block. The control block sets I/O buffer size, seekability flags, virtual file size, optional extension selection, and interrupt behavior; the remaining leading bytes are served through a custom AVIO reader.
- The harness initializes one FFmpeg decoder selected at build time, installs a custom get-buffer callback for video frames, and allocates frame planes without zeroing in the vulnerable variant. Inputs must match the selected codec family; otherwise they are rejected before slice-state behavior is reached.
- The wrapper runs the compress12 libFuzzer target on a single file path. The target writes raw input bytes to a temporary file, loads the image repeatedly with different pixel formats and compression options, and sums the compressed destination bytes to expose uninitialized data.
- The FFmpeg demuxer harness consumes raw file bytes. There is no selector byte or trailer context; the RIFF/QCP magic and chunk layout must be present at the start of the input.

## Format Links
- [[binutils-disassembler-buffer-with-trailer-selector]]
- [[c-blosc2-frame]]
- [[cr3-isobmff-atoms]]
- [[elf-btf]]
- [[elf-with-btf-ext]]
- [[faad2-split-aac]]
- [[ffmpeg-apac-decoder-packet]]
- [[ffmpeg-demuxer-fuzzer-carved-stream]]
- [[ffmpeg-raw-decoder-packet]]
- [[ffmpeg-target-decoder-packet]]
- [[fuzzed-provider-gzip-stream]]
- [[haproxy-config]]
- [[heif]]
- [[javascript]]
- [[jpeg-dct-fuzzer-raw]]
- [[libraw-fuzzed-provider-plus-raw-image]]
- [[libxml2-fuzzer-entity-envelope]]
- [[libxml2-valid-fuzz-entities]]
- [[libxslt-fuzz-entities]]
- [[mvha-raw-packet]]
- [[net-snmp-config-text]]
- [[pac]]
- [[pcap-or-pcapng-ip-capture]]
- [[pcap-tls-clienthello]]
- [[pdb-imageviewer]]
- [[pdf]]
- [[pe]]
- [[ppm]]
- [[riff-qcp]]
- [[rollei-raw-text-header]]
- [[sip-message]]
- [[ssh-server-byte-stream]]
- [[ssml]]
- [[sudoers-policy]]
- [[tiff]]
- [[tls-client-byte-stream]]
- [[upx-packed-elf]]
- [[wasm]]
- [[wavpack]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 23 Input Contract
- The libFuzzer harness feeds raw PDF bytes to Poppler's raw-data loader, then walks and renders pages. There is no leading mode byte or FuzzedDataProvider split.
- The MuPDF fuzzer consumes raw PDF bytes from memory, opens them as a PDF stream, renders every page to an RGB pixmap, and treats sanitizer findings during load or rendering as crashes. There is no outer byte carving or length prefix.
- The harness consumes three little-endian signed 16-bit fields from the front for angle and rotation center values, then passes the remaining bytes to Leptonica pixReadMem before applying pixRotateShear.
- The harness feeds raw bytes directly to pixReadMemSpix. If that succeeds it runs connected-component border extraction and display helpers; no mode selector or back-loaded fields are used.
- The json_fuzzer passes the entire input buffer directly to the JSON parser; no prefix, mode byte, checksum, or external container is required.
- The pix4 fuzzer passes raw input bytes directly to the SPIX reader. After a successful parse, it runs a fixed sequence of Leptonica pix operations and calls the color-map histogram-in-rectangle helper; there is no mode byte or secondary container.
- The libFuzzer harness exposes the raw file through libsndfile virtual IO, opens it for reading, allocates a float frame buffer based on reported channels, and repeatedly reads one frame. There is no extra byte carving.
- The uncompress_fuzzer passes the raw input to miniz uncompress with the same bytes serving as zlib header and compressed payload. The output capacity is derived from the first input bytes, so choosing a normal zlib header also gives a nonzero destination buffer.
- The secilc libFuzzer harness treats the input as raw CIL source bytes, adds it as a policy file, compiles and builds the policy database, then exercises optimization/write paths. There is no byte carving or FuzzedDataProvider layout.
- The selected fuzzer is ip6-send. The first input byte selects whether otIp6NewMessage creates a secure message; the remaining bytes are appended as an IPv6 packet and submitted through otIp6Send on an initialized leader-mode instance.
- The RawSpeed decoder fuzzer consumes raw file bytes as an in-memory TIFF-like file. It constructs the NEF decoder, calls raw decoding, and catches normal parser exceptions; sanitizer crashes and assertions during decompressor setup or execution still terminate the vulnerable build.
- The harness compiles a fixed YARA rule importing the PE module and scans the raw input buffer with no selector byte, file wrapper, or FuzzedDataProvider carving. The rule compares rva_to_offset of the first section's virtual address with that section's raw-data offset.
- The fuzzer writes raw input bytes to a memfd used as the database file, then runs a fixed gdbmtool command script. The fuzz bytes are not shell commands; the script opens the memfd-backed database and executes operations including sequential first/next traversal.
- The binary is curl_fuzzer_http and consumes the PoC as raw fuzzer input. It is not the curl command-line tool, and simple CLI strings are treated as fuzzer bytes rather than process arguments.
- The objcopy fuzzer writes raw bytes to a temporary input file, initializes BFD, and invokes objcopy's copy routine with a temporary output file. There is no input carving; BFD and objcopy parse the raw archive/file directly.
- The harness consumes the first byte as the spell-check word length, writes that many bytes as the word, splits all remaining bytes equally into temporary aff and dic files, constructs a Hunspell dictionary, calls spell, and calls suggest only when the word is not accepted.
- The parser fuzzer passes the raw SIP message bytes directly to parse_msg; there is no file envelope, selector byte, or checksum. The final line need not be terminated by an extra delimiter for the parser to inspect it.
- The selected target is fuzz_nm. It feeds raw bytes as a temporary file to BFD/nm-style symbol listing. Archive members may be inspected, but the fuzz bytes are otherwise a raw object or archive file with no leading harness selector.
- The assimp_fuzzer passes the entire input buffer directly to Importer::ReadFileFromMemory. The model importer is selected from the raw content; no additional fuzzer prefix is needed.
- The harness writes raw bytes to a temporary file, calls dwarf_init_b on the file descriptor, and then queries macro details only if initialization succeeds. No input bytes are carved by the harness.
- This is not the raw ExoPlayer FLAC parser despite a similarly named source file in the tree. The harness embeds flac main(), parses fuzzer-provided arguments from the front of the buffer, writes the rest to a temporary file, appends that file name to argv, and runs the tool.
- The harness passes the raw bytes directly to SkReadBuffer, calls readPath, returns if the buffer becomes invalid, then draws the resulting path on a small raster surface.
- The harness writes raw bytes to a temporary file and invokes upx with decompression and an output path inside a catch-all wrapper. There is no mode selector; all parsing is driven by UPX's file-format detection.
- The actual binary is fuzz_findfuncbypc. It writes the raw bytes to a temporary file, opens them with dwarf_init_path, and walks compile units and DIEs looking for a target program-counter range. It is not the die-cu-attrs harness.
- The fuzzer uses FuzzedDataProvider: it consumes an output-format selector from the front, then passes all remaining bytes as the compressed JPEG-R buffer. A later floating-point value is requested after the remaining bytes are consumed, so the main carrier must be in the remaining byte segment.
- The fuzz_json target parses the raw input as a complete JSON configuration string and then runs configuration validation. There is no mode byte or external length field; inputs outside the harness size bounds are ignored before parsing.
- The oss-fuzz MuPDF PDF fuzzer consumes raw PDF bytes, opens the input as a PDF document stream, counts pages, and renders each page to an RGB pixmap. There is no outer file wrapper beyond the PDF itself.

## Round 23 Format Links
- [[ar-archive]]
- [[bfd-object-or-archive]]
- [[cil]]
- [[elf-dwarf]]
- [[fbx-ascii]]
- [[flac-tool-input]]
- [[gdbm-database]]
- [[http-response-stream]]
- [[hunspell-aff-dic-word-triple]]
- [[ipv6-udp-coap-meshcop-tlv]]
- [[jpeg-r-ultrahdr]]
- [[json]]
- [[macho-fat64]]
- [[nef-tiff]]
- [[pdf]]
- [[pe]]
- [[sip-message]]
- [[skia-serialized-path]]
- [[spix]]
- [[tiff-ojpeg-image]]
- [[unit-json-config]]
- [[upx-packed-macho]]
- [[wav-ms-adpcm]]
- [[zlib-deflate]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
