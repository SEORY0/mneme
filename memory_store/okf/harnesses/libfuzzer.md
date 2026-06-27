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
