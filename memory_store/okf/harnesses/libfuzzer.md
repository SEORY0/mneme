---
type: harness-contract
title: "Libfuzzer harness"
description: "Input contract facts for Libfuzzer."
tags: ["libfuzzer", "round-6", "round-16"]
okf_support: 299
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

## Round 24 Factual Contract

### Input Contract
- The libFuzzer target feeds raw bytes through an in-memory FILE. The first header bytes are consumed before decoding and may also select threaded decoder configuration in threaded builds; there is no filename, stdin protocol, or FuzzedDataProvider layout.
- The FFmpeg decoder fuzzer consumes raw packet bytes split by a fixed delimiter. Large inputs may also carry a trailing context block with dimensions, bit rate, sample format hints, parser flags, keyframe flags, and optional extradata copied from the bytes before the tail.
- The libFuzzer harness passes raw bytes directly to the HEVC decoder wrapper. Early bytes are also sampled as harness controls for output format, core count, and architecture, then the same buffer is decoded as stream data.
- The libFuzzer harness consumes raw bytes as one or more concatenated OpenFlow messages. It uses each message header length to carve complete messages and passes each one to the OpenFlow pretty-printer; there is no FuzzedDataProvider or mode selector.
- The libFuzzer target passes raw bytes to the autodetect reader and enforces a trailing terminator copy for text-like inputs. It may then randomly choose an output encoder after a successful read, so parser acceptance is only the first gate.
- The libFuzzer harness feeds raw font bytes to hb-subset-fuzzer. The harness derives allocation-failure state from the input size and consumes trailing option data for subset flags/text when present, so corpus seed size and tail layout influence reachability.
- The harness stores raw bytes at a virtual tar path, reads cmd.txt from the archive, prepends a fixed output-size limit, filters only later occurrences of that same option name, opens the archive member named in as the source, checks band count and estimated source size, then calls GDALTranslate to a virtual output path.
- The libFuzzer target passes the entire raw input as a JSON string to TinyGLTF LoadASCIIFromString. There is no GLB wrapper requirement, file-system base directory, leading mode selector, or FuzzedDataProvider carving.
- The fuzzer writes the raw input bytes to a temporary file, opens it as an ELF object, calls dwfl_core_file_report, then ends reporting. The local runner wrapper for this task reported a corpus-directory mismatch for file inputs, so direct target execution and official submit were used for outcome checks.
- The raw libFuzzer input is split front-to-back by the harness: the first record segment is converted from JSON, and the remainder is NUL-terminated and parsed as a record accessor. The fuzz allocator failure counter is reset at the start of each input.
- The binutils/BFD harness consumes a raw object file from disk and drives object-format detection plus selected BFD inspection paths. It is not a container or carved-input harness.
- The active target is a RawSpeed CR2 TIFF decoder fuzzer that consumes raw camera-file bytes. It is not the lower-level Cr2Decompressor synthetic envelope harness.
- The harness feeds raw bytes as a temporary .map file, rejects very small or overly large inputs, calls msLoadMap, then frees the returned map and resets the error list. There is no archive, length prefix, or FuzzedDataProvider contract.
- The Zeek generic analyzer fuzzer requires chunks delimited by the FuzzBuffer magic marker. The byte following each marker selects originator versus responder, and bytes until the next marker are delivered as one stream chunk.
- The Wireshark oss-fuzzshark target reads a capture file from the raw fuzzer input and dispatches packets through dissectors. The generated run directory required manual extraction repair, which left local verify configuration absent; official submit was used for the final fallback check.
- The FFmpeg target_dec_fuzzer opens a codec-specific decoder, optionally initializes a parser from context-tail flags, then sends packet chunks split by a magic delimiter. The context tail is read from the back of large inputs, and extradata is copied from the bytes immediately before that tail.
- The MuPDF libFuzzer target feeds raw bytes as a PDF memory stream, opens the document, counts pages, and renders each page to a pixmap. The content stream must execute during page rendering; parsing alone is not enough.
- The libFuzzer harness selected by the image runs the libjpeg-turbo compression fuzzer directly on raw image bytes. There is no leading mode byte in the PoC file; format selection comes from the image header parsed by the fuzzer.

### Format Links
- [[av1-ivf]]
- [[coff-object]]
- [[cr2-tiff-raw]]
- [[dxf-or-json-cad]]
- [[elf-core]]
- [[ffmpeg-huffyuv-packet]]
- [[ffmpeg-mlp-packet]]
- [[fluent-bit-record-accessor-fuzzer]]
- [[font]]
- [[gltf-json]]
- [[hevc-elementary-stream]]
- [[mapserver-mapfile]]
- [[openflow]]
- [[packet-capture]]
- [[pdf]]
- [[ppm]]
- [[tar]]
- [[zeek-fuzzbuffer-smtp-stream]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 25 Input Contract
- The libFuzzer target wraps the raw input with an in-memory file, requires the container header read to succeed, initializes the AV1 decoder, then repeatedly reads IVF frames and drains decoded images. There is no FuzzedDataProvider carving or mode selector.
- The fuzzer passes the whole input as a C string only if it has at least one payload byte, a final NUL terminator, and no newline. The same string is tried as key text and action text; there is no binary netlink envelope, or provider-carved layout.
- The harness is the FFmpeg targeted decoder fuzzer for the Tiertex codec. It is not a container demuxer: raw input bytes before a delimiter become an AVPacket, while trailing context bytes initialize AVCodecContext fields before avcodec_open2.
- libFuzzer passes raw bytes directly. The harness requires a minimum size, assigns the data prefix to disassemble_info.buffer, derives target selectors from a suffix, and calls one decoded instruction printer if the selected architecture is known.
- The libFuzzer target passes the entire input byte string directly to the JSON decoder as a Variant. There is no file wrapper, checksum, or external mode byte; all reachability is controlled by JSON token structure and the Variant/ExtensionObject fields.
- The libFuzzer harness feeds the whole file bytes into BFD by way of a temporary file. There is no stdin protocol or FuzzedDataProvider carving; the bytes must form whatever BFD top-level format is needed to reach the inner object parser.
- The harness copies the raw libFuzzer input into a nul-terminated request body and runs the PHP parser/execute fuzzer on it. There is no byte carving or FuzzedDataProvider layout; normal PHP opening and closing tag state transitions determine lexer mode.
- The source harness casts raw libFuzzer bytes to a char buffer and calls json_tokener_parse_ex with the exact byte length. In this generated run, local verify did not actually exercise that parser because the wrapper treated the supplied path as an invalid corpus argument.
- The libFuzzer target rejects very small inputs, extracts the architecture controls from the end of the buffer, looks up a BFD architecture/machine pair, then repeatedly invokes the selected disassembler over the leading byte buffer.
- libFuzzer passes the PoC file bytes directly to LLVMFuzzerTestOneInput. The harness rejects only empty input, creates a default UCL parser, calls ucl_parser_add_string with the raw data and size, then checks the parser error before freeing the parser.
- libFuzzer raw bytes are passed directly to coap_pdu_parse as a UDP PDU. The harness then queries URI/path helpers, prints the PDU, re-encodes the header, and frees derived strings.
- The libFuzzer target ignores tiny inputs, opens the raw bytes with an in-memory FILE, initializes the sudoers parser, parses once, then reinitializes parser state and closes the memory stream. It does not load sudo plugins from sudo.conf.
- The harness feeds raw bytes into a p11_buffer, initializes the mock module, and calls the RPC server handler directly. There is no outer transport framing beyond the RPC message itself; repository seeds under the fuzz corpus are valid starting points.
- The libredwg LLVM fuzzer autodetects raw bytes as DWG, JSON, or DXF. Non-DWG/non-JSON data is passed to the DXF reader, then the harness may encode/write/free the parsed Dwg_Data object.
- The libFuzzer target passes the entire input directly to Assimp's ReadFileFromMemory with standard post-processing enabled. There is no harness-level carving; importer selection and secondary file opening are controlled entirely by model syntax.
- The harness copies the entire input to a newly NUL-terminated string, opens an mruby VM, loads and executes the source, then closes the VM. There is no file header, selector byte, or provider carving.
- The decoder fuzzer consumes the last option word from the end of the input and decodes the preceding bytes as JPEG XL. The callback path calls the image-output callback setter with the selected JxlPixelFormat; the buffer path performs size validation first.
- libFuzzer raw bytes are copied into a NUL-terminated buffer, split on the first two newlines, parsed as two projections, then transformed using either textual or binary coordinates if both projections initialize.
- The Kamailio fuzzer feeds raw bytes directly to parse_msg, then exercises SDP, Contact, Refer-To, To, PAI, Diversion, and Privacy header parsing before freeing the sip_msg structure.
- The gstoraster fuzzer feeds the raw input to Ghostscript as a document stream. Reaching the target requires not just a standalone CMap, but document processing that asks the PDF font machinery to consume ToUnicode data.
- The libFuzzer harness initializes nDPI once, allocates a flow, calls ndpi_detection_process_packet with the whole byte buffer and its size, then gives up detection and frees the flow. No outer pcap header or provider-carved fields are used by this target.
- The effective target is the PHP execute fuzzer, which runs a source file as a PHP request. There is no byte carving; the raw file contents are the script.
- The libFuzzer target consumes the whole file as image data for a selected ImageMagick encoder fuzzer. There is no leading selector in the PoC file itself; the wrapper chooses the target binary outside the input bytes.
- The harness writes the raw input to a temporary file, initializes libdwarf from that file, loads rnglists contexts, then iterates offset entries and range-list entries. Bare rnglists bytes are not sufficient; a valid ELF/DWARF carrier reaches the target parser.
- The LibreDWG fuzzer detects DWG by an AC prefix, JSON by an object prefix, and otherwise treats raw NUL-terminated input as DXF text. After reading, it writes the decoded drawing to one of several output formats.
- The harness consumes control scalars through FuzzedDataProvider and then uses remaining bytes as short strings or binary payloads. Reaching the target likely requires aligning terminal scalar consumption with serializer buffer-length changes.
- The available source shows fuzzshark's FUZZ_EPAN mode feeds the raw input as a packet buffer with an unknown encapsulation rather than reading a pcap file. The run directory for this task lacks verifier configuration because generation fails during repository extraction.
- The libFuzzer target passes the raw text into GPAC's probe/analyze filter session. Unsupported schemes are handled as ordinary file names; supported RTSP schemes cause filter graph construction and RTSP session initialization.
- The harness creates a RawImage from the prefix, reads the signed slice-width vector, constructs Cr2Decompressor over the remaining ByteStream, allocates image data, decodes, and checks initialization. It catches RawSpeed exceptions, so only sanitizer faults or uncaught crashes count.
- The fuzz target feeds raw bytes as a string when the input length is within the configured bounds, calls evalPluralCase with a fixed numeric value, catches parser/operation exceptions, and returns normally unless sanitizer instrumentation detects the helper falling through.
- The FFmpeg demuxer fuzzer feeds the raw bytes to the MLV demuxer through libavformat. The target first validates the main MLV header, creates streams based on header class and frame counts, then scans primary and possible secondary block streams.
- The active libFuzzer binary is ffmpeg_dem_WTV_fuzzer. It feeds the whole file through a custom AVIO context to the WTV demuxer; there is no trailing filename/options envelope for this demuxer-specific build.
- The miniz zip fuzzer treats the raw input as an in-memory ZIP archive, initializes the ZIP reader, iterates non-directory files, validates headers, reads filenames and file stats, and attempts extraction for stored or deflated entries. There is no extra harness carving.
- The MVC decoder fuzzer takes raw bytes, derives architecture/core/color controls from fixed positions when present, decodes headers, allocates output buffers, then repeatedly calls frame decode until data is consumed or decode fails.

## Round 25 Format Links
- [[ivf-av1]]
- [[ovs-odp-action-text]]
- [[ffmpeg-target-dec-fuzzer-stream]]
- [[binutils-disassembler-buffer]]
- [[opcua-json-variant]]
- [[bfd-archive-or-tekhex]]
- [[php-source]]
- [[json]]
- [[raw-disassembler-buffer]]
- [[ucl-config-text]]
- [[coap-udp-pdu]]
- [[sudoers-policy-text]]
- [[p11-kit-rpc-message]]
- [[dxf]]
- [[assimp-model]]
- [[mruby-source]]
- [[jpeg-xl-codestream-with-fuzzer-footer]]
- [[proj-parameter-lines]]
- [[sip-message]]
- [[pdf-or-postscript]]
- [[raw-packet-payload]]
- [[imagemagick-wpg-or-image-encoder-input]]
- [[elf-with-dwarf-rnglists]]
- [[dxf-text]]
- [[ndpi-serialization-fdp]]
- [[wireshark-fuzzshark-raw-frame]]
- [[gpac-filelist-url]]
- [[rawspeed-cr2-decompressor-fuzzer-stream]]
- [[plural-expression]]
- [[mlv]]
- [[ffmpeg-wtv]]
- [[zip]]
- [[h264-annex-b-mvc]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 26 Factual Contract


### Input Contract
- The FLAC libFuzzer tool harness uses a leading control byte to choose the maximum number of command-line arguments and whether stdin is used. It then parses NUL-delimited argv strings from the front of the input; the remaining bytes become the FLAC file payload or stdin data according to the control bit. There is no checksum or length wrapper outside the CLI-argument carving.
- The active GDAL shape fuzzer stores the raw PoC as a virtual tar-like input and opens a fixed member named as a shapefile through GDAL's virtual tar path, then iterates every layer and feature. The accepted archive form starts with GDAL's fuzzer-friendly archive marker and contains a member for the fixed opened filename. There is no FuzzedDataProvider carving; the whole file is the virtual archive.
- The active fuzz target passes the raw input bytes to Ghostscript as stdin for a fax-oriented device wrapper. There is no leading mode selector, no corpus envelope, and no FuzzedDataProvider front/back carving. The wrapper runs Ghostscript in safer, batch, no-pause mode with stdout and stderr mostly discarded by the harness, so verifier output mainly distinguishes sanitizer crashes from clean execution or ordinary Ghostscript interpreter errors.
- The exercised libFuzzer target copies the raw input into a NUL-terminated string, interprets it as a config define assignment, loads it through the container config setter, and then reads the configured item back. There is no FuzzedDataProvider layout or binary prefix; the first text key controls the parser route.
- The flac tool fuzzer starts with a control byte that enables NUL-delimited command-line arguments. After the argument section is exhausted, the remaining bytes are written as a temporary input file for the real flac command-line path. To preserve binary FLAC bytes, the argument list must be filled so parsing stops before the FLAC stream marker; there is no FuzzedDataProvider front/back layout.
- The fuzz input begins with a little-endian length prefix for the ASN.1 decode buffer, followed by that buffer. The remaining bytes are consumed as a virtual smart-card reader transcript made of little-endian length-prefixed chunks, with the first chunk acting as ATR data and later chunks as APDU responses. There is no additional mode selector.
- The fuzz target passes the raw input bytes directly to rnp_input_from_memory and loads them as a GPG keyring with both public and secret load flags. There is no leading mode selector, no argv/stdin wrapper, and no FuzzedDataProvider front/back carving.
- The fuzzer writes the whole PoC to a temporary file, opens a libblkid probe on that file, enables partition and superblock probing, and calls safe probing. There is no FuzzedDataProvider layout, mode byte, external checksum repair, or stdin protocol; the PoC must be a coherent disk-image-like byte stream.
- The harness feeds libFuzzer bytes directly to the Skia path-measure fuzzer. It consumes fields front-to-back through Skia's fuzz helper, with no file wrapper, checksum, mode selector outside the stream, or FuzzedDataProvider back-consumed fields.
- The harness feeds the file bytes directly to the skcms parser and then queries parsed profile information that reads transfer-curve extents. There is no fuzzer-side carving or FuzzedDataProvider layout; parser reachability depends entirely on a self-consistent ICC envelope.
- The harness is a libFuzzer raw-byte file harness with no leading mode byte and no FuzzedDataProvider carving. It constructs a FiffParser from the whole input, calls getDecoder, disables crop and unknown-camera hard failures, then calls decodeRaw and decodeMetaData. RawSpeed parser and decoder exceptions are caught, so successful triggering needs a sanitizer-visible failure after parser and decoder reachability.
- The harness is a libFuzzer raw-byte harness. It caps the input size, maps the first byte through the platform table, opens the corresponding Capstone architecture and mode, enables detailed disassembly, optionally toggles alternate syntax from a selector bit, and calls cs_disasm on the remaining bytes from a fixed base address.
- The harness is libFuzzer over raw bytes. It wraps the input in a ByteStream, constructs a RawImage from leading scalar fields, reads all remaining strip records from the same front-to-back byte stream, allocates image data, runs PhaseOneDecompressor, then checks image memory initialization. There is no file magic, filename layer, mode selector, or FuzzedDataProvider back-consumption.
- The harness is the FFmpeg H.264 decoder libFuzzer target and consumes the raw file bytes directly as an elementary H.264 packet stream. There is no FuzzedDataProvider prefix or mode byte; keeping the input compact avoids unrelated harness behavior.
- The libFuzzer entrypoint passes the raw input bytes directly to Botan::PKCS8::load_key through a memory data source with no FuzzedDataProvider carving. The task wrapper runs the pkcs8 fuzzer on one file path. Parser exceptions are caught by the fuzzer, so malformed ASN.1 and rejected key parameters usually appear as clean no-crash executions rather than bad_format.
- The libFuzzer entrypoint passes the whole PoC as the data buffer to magic_buffer after only a non-empty size gate. There is no leading mode selector, section carving, checksum, or FuzzedDataProvider back-to-front layout.
- The libFuzzer harness consumes raw bytes. It routes drawing-marker inputs to the DWG decoder, object-prefix text to JSON import, and all other inputs to DXF import. It appends a terminator for text-oriented paths when needed, writes one randomly selected output format to a null sink after a successful import, then frees the drawing object.
- The libFuzzer harness passes raw bytes directly to the TypeMapping deserializer. For each complete identifier-object pair, it searches the mapping sequence for the matching minimal identifier, constructs complete and minimal type-info records, calls the proxy type reference path, conditionally adds the complete TypeObject, then releases the referenced type. There is no leading mode byte or FuzzedDataProvider carving.
- The libFuzzer harness passes the raw input buffer to the XML memory reader. The harness also derives parser options deterministically from the input, but it does not carve the byte stream with a FuzzedDataProvider-style contract.
- The libFuzzer harness requires a fixed-size native struct-shaped input rather than a plain vertex blob. Integral fields are read directly from the front of the buffer using native little-endian layout. The remaining buffer is parsed front-to-back as the outer loop and then optional hole loops. For each input, the harness runs every valid containment mode once with the original hole count and once with holes disabled.
- The libFuzzer harness writes the entire PoC to one end of a socketpair, shuts down writes, installs a server RSA key, accepts the other socket as a libssh server session, runs server key exchange, and then drains queued ssh_message objects only if key exchange succeeds. There is no FuzzedDataProvider carving; the whole file is the client byte stream.
- The libFuzzer input is consumed front-to-back by fuzzing::datasource, not as raw MQTT. The harness constructs MqttClient and MqttConnect objects, allocates fixed transmit and receive buffers, reads datasource fields for buffer setup, clean-session, client-id, LWT selection, and optional LWT values, but it does not populate username or password. It then calls MqttClient_NetConnect and MqttClient_Connect; mocked write and read callbacks consume later datasource fields only if encoding completes.
- The libFuzzer target passes the same raw input buffer directly to several PKCS#15 directory-entry decoders in a loop, then to public-key, tokeninfo, and unused-space parsers. There is no leading selector byte, no length-prefixed reader chunk stream, and no FuzzedDataProvider back/front split.
- The libFuzzer target reads the raw file bytes as one cryptofuzz datasource. The build is constrained to wolfCrypt and selected bignum/DH/ECC operations. For BignumCalc, the parent datasource supplies the modifier stream and module selector after the nested operation payload; modifier booleans are also length-prefixed datasource fields.
- The selected OSS-Fuzz target is the libxaac encoder fuzzer. FuzzedDataProvider consumes byte-buffer payloads from the front, while integral and boolean scalar fields are consumed from the back in little-endian order. For AOT_USAC, a loudness pass uses a separate provider over the full input before encoder creation. During processing, the per-frame read-versus-memset selector is also consumed from the back of the remaining data, so control bytes for process-loop behavior must be placed at the back of the front payload region, before the configuration tail.
- The specialized i386 disassembly fuzzer copies the option and private-data regions first, then invokes the i386 disassembler twice over the remaining instruction buffer with both endian settings. Integral control fields are read from the back of the frame in little-endian form; no FuzzedDataProvider is used.
- The task image's wrapper invokes a libFuzzer frame target over a corpus directory. The fuzzer target receives raw frame bytes, opens an in-memory super-chunk from the frame, allocates an output buffer from the frame metadata, and decompresses chunks in order. The repository's model-free local verify wrapper copies the candidate to a file path where this image expects a directory, so direct single-input libFuzzer execution was used for local differential evidence and runner submit was used for the official verdict.

### Format Links
- [[binutils-disassembler-frame]]
- [[c-blosc2-frame]]
- [[capstone-disasm-selector-plus-bytes]]
- [[cryptofuzz-binary-operation-stream]]
- [[dds-xtypes-typemap-cdr]]
- [[dwg-dxf-json]]
- [[fiff-wrapped-mef-tiff-raw]]
- [[flac-cli-fuzzer-input]]
- [[flac-tool-input]]
- [[h264-annex-b]]
- [[h3-geopolygon-struct]]
- [[icc]]
- [[iso9660]]
- [[libmagic-classified-raw-buffer]]
- [[libxaac-encoder-fuzzed-provider]]
- [[lxc-config-text]]
- [[openpgp-secret-keyring]]
- [[opensc-pkcs15-asn1]]
- [[opensc-pkcs15-asn1-with-reader-transcript]]
- [[pkcs8-private-key]]
- [[postscript]]
- [[rawspeed-phaseone-decompressor-envelope]]
- [[skia-pathmeasure-fuzz-stream]]
- [[ssh-server-byte-stream]]
- [[uk-ntf-in-gdal-fuzzer-friendly-archive]]
- [[wolfmqtt-datasource-stream]]
- [[xml]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 27 Input Contract
- The libFuzzer harness feeds the whole byte stream as an hb_face font blob.
- It also copies up to the final 64 input bytes into a fixed UTF-32 array; the last word of that array is passed as the glyph id to miscellaneous face/font APIs including glyph extents.
- There is no leading mode selector or FuzzedDataProvider carving.
- The libFuzzer harness consumes the first raw input byte as the patch prefix length option and passes all remaining bytes directly to git_patch_from_buffer.
- There is no checksum, file container, or FuzzedDataProvider layout.
- The active target is the DRSUAPI TYPE_OUT libFuzzer binary.
- It rejects inputs whose selector type is not output, then pulls any output pipes, decodes the selected function's OUT stub, re-pushes the decoded structure, and walks the NDR print tree.
- There is no FuzzedDataProvider and no mode byte beyond the NDR selector header.
- The target consumes raw file bytes as the tested binary input; there is no fuzzer-side prefix, selector byte, or FuzzedDataProvider layout.
- The radare2 analysis harness opens the file and drives the ELF loader and analysis path.
- The stb_image libFuzzer harness feeds raw file bytes directly to the memory parser.
- It first calls the info parser as a reachability gate, rejects very large decoded dimensions, and then decodes the same raw bytes requesting RGBA output.
- There is no leading mode selector, datasource wrapper, filename, or FuzzedDataProvider layout.
- The PHP execute fuzzer feeds the raw input bytes as a PHP script buffer and executes them directly.
- There is no FuzzedDataProvider split or length-prefixed envelope.
- The harness suppresses normal error reporting through configuration, so the PoC must establish its own error-reporting and exception-conversion behavior in the script.
- The wrapper runs the wolfSSL randomized client fuzzer on the raw file.
- The final byte selects one of the client method contexts.
- Before TLS bytes are consumed, allocation randomization reads bytes from the front; odd choices allow an allocation and even choices fail it.
- The libFuzzer target passes the input buffer directly to a default UCL parser through the add-string API.
- Empty input is ignored.
- There is no selector byte, file envelope, integrity field, or FuzzedDataProvider front/back split.
- The libFuzzer harness feeds the entire raw input as an in-memory serialized frame to the frame opener.
- If opening succeeds, it allocates an output buffer from the declared uncompressed size and lazily decompresses each data chunk except the final frame-index chunk.
- The libFuzzer input is raw text with a leading mode selector.
- After the selector is consumed, the remaining bytes are split into line records on IRC line separators and emitted to Irssi's server incoming path.
- In one mode the harness prepends a source prefix to each line, which prevents the message-tag parser from seeing tags at the beginning.
- The container wrapper runs the libFuzzer-built fuzzshark IP target on the file copied to the fixed input path.
- The harness initializes Wireshark, registers the configured IP dissector as a postdissector, wraps the raw file bytes as one synthetic packet record, and calls epan dissection.
- There is no pcap envelope, mode byte, checksum repair, stdin contract, or FuzzedDataProvider front/back carving.
- The libFuzzer target passes raw input bytes to a libxml2 fuzzer data reader.
- The harness consumes a leading parser-option word before the resource strings; no separate FuzzedDataProvider back-of-buffer fields or mode byte were observed.
- The libFuzzer target passes the entire input as a raw camera-file byte stream to RawSpeed.
- There is no front selector, chunk framing, checksum wrapper, or FuzzedDataProvider layout.
- Parser exceptions are caught, so the input must remain a coherent TIFF/IFD container before the decoder-specific truncation invariant is exercised.
- The libFuzzer harness passes the raw input buffer directly to cmsIT8LoadFromMem and frees the returned handle if parsing succeeds.
- There is no FuzzedDataProvider split, no filename argument, and no outer container; all reachability depends on the CGATS text classifier and parser state machine.
- The Ghostscript gstoraster fuzzer feeds the raw input bytes as a document on stdin.
- There is no carved selector or FuzzedDataProvider layout; parser reachability depends on PDF syntax, startxref, and xref-stream consistency.
- libFuzzer passes the raw input bytes directly to coap_pdu_parse as a UDP PDU.
- The harness ignores the parse return value, then calls URI query/path helpers, prints the PDU, re-encodes the header, frees derived strings, and deletes the PDU.
- There is no mode selector or FuzzedDataProvider layout.
- The selected target consumes raw TIFF/DNG file bytes through RawSpeed's TIFF decoder fuzzer; there is no prefix byte or FuzzedDataProvider layout.
- The standalone DNG-opcode fuzzer has a little-endian RawImage prefix followed by a big-endian opcode stream, but that envelope does not reach this packaged target.
- The libxml2 HTML fuzzer consumes a big-endian parser-options field, then a big-endian allocation-limit field whose effective limit is reduced modulo input size, then treats the remaining bytes as the HTML document.
- The document is parsed once through htmlReadMemory and then through a push parser that feeds bounded chunks under the same allocation-failure limit.
- The allocation limit is armed immediately before each parser mode.
- The MVC decoder fuzzer consumes the raw input bytes as the elementary stream.
- A few fixed early bytes are also sampled as decoder configuration selectors such as architecture and core count, but the stream is otherwise decoded directly through a header pass followed by repeated frame decode calls.
- The local runner's generic file-copy verifier mismatches this image's libFuzzer corpus-directory wrapper, so official submit results were used as the decisive oracle for these candidates.
- The Assimp libFuzzer harness passes the entire input byte array directly to Importer::ReadFileFromMemory with no selector byte and no FuzzedDataProvider carving.
- Importer detection is signature based, and successful imports continue into the normal Assimp post-processing pipeline.
- The secilc libFuzzer target treats the input buffer as CIL source, adds it as an in-memory policy file, compiles it, builds and optimizes a policy database, writes to a null output when compilation succeeds, then destroys the CIL database.
- There is no file wrapper, selector byte, integrity field, or FuzzedDataProvider layout.
- The libFuzzer harness passes the whole file to LLVMFuzzerTestOneInput.
- The first byte selects one PKCS#11 operation; operation-specific parsers consume fields from the front, and the leftover tail becomes virtual-reader data.
- The verify path uses direct C_Verify for small verify data and an update/final loop for larger verify data.
- The libFuzzer input is opened with libpcap through an in-memory file and must contain a valid pcap stream.
- The harness sets the interface datalink from the pcap global header, iterates packets with pcap_next_ex, and passes each captured packet plus its pcap header directly to NetworkInterface::dissectPacket.
- The LibreDWG libFuzzer target consumes raw file bytes.
- Inputs with the DWG release prefix go to the binary DWG decoder, JSON-looking inputs go to JSON import, and other inputs fall back to DXF text import.
- No fuzzer-side carving or FuzzedDataProvider layout is used; this crash occurs during DWG decode before output-format selection matters.
- The libFuzzer target installs a virtual reader over the chunk stream, binds a PKCS#15 card, then consumes two additional chunks as operation input and parameter buffers before iterating bound objects.
- During iteration it tries decipher, derive, wrap, unwrap, signature, and PIN operations depending on object type.
- Chunk boundaries and APDU status words must remain coherent or the bind path exits before PKCS#15 object parsing.
- The harness writes the raw input bytes to a temporary file and invokes UPX test mode on that file.
- The input is not carved, prefixed, checksummed by the harness, or consumed through FuzzedDataProvider; all structure must be valid enough for UPX packed-file recognition.
- The GPAC fuzz target treats the raw input bytes as a media asset and lets probe/analyze select the image reframer from file content.
- There is no front selector and no FuzzedDataProvider contract; satisfying the BMP header gates is enough to reach the BMP branch in the image reframing filter.
- The selected oss-fuzz target is the Ghostscript psdcmyk device fuzzer.
- It feeds raw input bytes as stdin to Ghostscript with the psdcmyk output device and banding/clist-oriented options; there is no leading selector byte, prefix carving, or FuzzedDataProvider layout.
- PDF versus PostScript parsing is selected by the document syntax.

## Round 27 Format Links
- [[blosc2-frame]]
- [[bmp]]
- [[cgats-it8-text]]
- [[cil-policy-text]]
- [[coap-udp-pdu]]
- [[dng]]
- [[dwg-r11]]
- [[elf]]
- [[git-patch]]
- [[h264-annexb-mvc]]
- [[html-doctype]]
- [[ircv3-message-tags]]
- [[libxml2-xml-fuzzer-entity-envelope]]
- [[nef-tiff]]
- [[opensc-pkcs15-reader-chunk-stream]]
- [[opentype-cff]]
- [[pcap-mdns]]
- [[pdf-or-postscript]]
- [[pdf-xref-stream]]
- [[php-script]]
- [[png]]
- [[quake1-mdl]]
- [[raw-pkcs11-fuzzer-record]]
- [[samba-ndr-drsuapi-output]]
- [[ucl-config-text]]
- [[upx-packed-unix]]
- [[wireshark-fuzzshark-ip-packet]]
- [[wolfssl-randomized-tls-client-stream]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 28 Input Contract

- The libFuzzer harness consumes the raw file bytes as a C string. The input must contain at least one character, must be NUL-terminated, and must not contain newlines. It creates fixed symbol tables plus nonempty and empty address sets and port groups, then drives expression parsing, action parsing, lexing, and microflow parsing with the same string. There is no FuzzedDataProvider split or mode-selector byte.
- The GraphicsMagick MIFF coder fuzzer passes the raw libFuzzer bytes directly as a Magick blob, forces the MIFF coder name, reads the image, catches Magick exceptions, and then writes the decoded image back to a MIFF blob when reading succeeds. There is no leading mode byte, no file carving, and no FuzzedDataProvider split; read-side corruption that still returns an image can surface later in the write-back path.
- The libFuzzer target consumes raw bytes as a font blob. Its shape path copies a fixed-size trailer from the end of the input into a UTF-32 text buffer and then runs face API checks using that trailer-selected codepoint; there is no FuzzedDataProvider layout.
- The htslib fuzz harness passes raw input bytes to an in-memory hts_open source. For variant input, it reads the VCF header, writes a header to a null sink, then repeatedly reads records and writes them back through bcf_write/vcf_format. Text VCF records are parsed before writeback, so the raw BCF record checker is not the relevant gate for this construction.
- The libFuzzer harness feeds raw file bytes to libarchive from memory, enables all filters and formats, then repeatedly reads headers and drains entry data. There is no mode byte or FuzzedDataProvider framing. The RAR5 varint reader requires sufficient forward lookahead even when the encoded value itself is short.
- The libFuzzer target copies the raw input bytes, NUL-terminates them, calls php_var_unserialize on the entire buffer, destroys the top-level result, then forces PHP GC twice before request shutdown. There is no leading mode byte, no filename, and no FuzzedDataProvider split; the payload is exactly one serialized PHP value.
- The libFuzzer harness passes the PoC file's raw bytes as the JavaScript source buffer, rejects only empty input and Hermes bytecode-looking input, appends a NUL terminator internally, creates a Hermes runtime, and evaluates the source while swallowing JavaScript exceptions.
- The local wrapper invokes the PHP parser libFuzzer binary on a fixed path. In local Docker verification, a directory at that path is treated as a corpus and its entries are processed; a regular file at that path is rejected before the fuzzer callback runs. The official submit endpoint uploads one regular file, not a directory.
- The libFuzzer harness passes the raw input buffer directly to the LibGfx BMP memory loader. There is no prefix, mode selector, argv path wrapper, checksum layer, or FuzzedDataProvider back/front carving; reachability depends on the BMP bytes themselves.
- The libFuzzer harness consumes the entire file as raw bytes. It does not use FuzzedDataProvider, does not carve a mode byte, and does not prepend metadata; the only transformation is making a temporary NUL-terminated copy before calling the date parsing API.
- The libFuzzer target passes the raw input buffer directly to the C-Blosc2 in-memory frame loader. If frame reconstruction succeeds and the declared uncompressed byte count is below the harness limit, it allocates an output buffer and iterates chunk decompression. There is no prefix selector and no FuzzedDataProvider front/back carving.
- The libFuzzer entrypoint receives raw bytes, copies the full buffer into a UA_ByteString, and calls the binary message processor once. The connection layer walks all complete chunks in the buffer according to each chunk's embedded length. After message processing, the harness deletes the message, runs server shutdown, then deletes the server and connection; shutdown drains delayed callbacks in this single-threaded build.
- The fuzz target feeds the input bytes directly as a temporary object file to objdump. There is no leading mode byte and no FuzzedDataProvider carving. The harness enables broad objdump views including section headers and relocation dumping, so a BFD-recognized SOM object with a relocatable subspace reaches som_get_reloc_upper_bound and som_canonicalize_reloc.
- The libvips thumbnail fuzzer feeds the raw input bytes directly to vips_image_new_from_buffer with no leading mode byte or FuzzedDataProvider split. If loading succeeds, it rejects only very large dimensions or too many bands, then calls vips_thumbnail_image and computes an average over the output.
- The libFuzzer target consumes the raw input as a file buffer. Inputs beginning like AutoCAD text are routed through the DXF reader, then the harness may exercise output conversion before final object cleanup; there is no mode byte or FuzzedDataProvider carving.
- The libFuzzer harness passes the raw file bytes unchanged to LLDP, CDP, SONMP, and EDP decoders. There is no FuzzedDataProvider, no leading mode selector, and no checksum repair layer. Inputs shorter than the harness minimum or longer than the harness maximum are ignored before decoding. For CDP, the destination/protocol gates select the CDP decoder; unrelated trailing bytes after the CDP payload can remain physically present in the raw input without being part of the CDP length.
- The libFuzzer harness accepts raw PoC bytes within a bounded size range, writes them unchanged to a temporary file with a mapfile extension, calls msLoadMap on that file, then immediately calls msFreeMap on the returned pointer and clears the MapServer error list.
- The harness feeds the raw input bytes directly to the OpenSIPS message parser through the sip_msg buffer and length fields. There is no leading mode byte, checksum, size table, or FuzzedDataProvider carving; after parse, the harness frees the parsed sip_msg structure.
- The libFuzzer harness passes raw input bytes directly to LibGfx's JPEG image decoder plugin, initializes it, and requests the first frame. There is no filename wrapper, leading mode byte, sidecar metadata, checksum layer, or FuzzedDataProvider front/back split.
- The selected arvo wrapper runs the Ghostscript pdfwrite libFuzzer target and provides the file bytes as the single raw input consumed from stdin. There is no FuzzedDataProvider layout, mode selector, or prefix carving for this target. Earlier XPS and direct PostScript CFF attempts did not reach the selected pdfwrite CFF sink; the successful path is a raw PDF that causes the page interpreter to load the embedded Type1C font.
- The libFuzzer entrypoint passes the raw input bytes directly into a SkReadBuffer and calls SkTextBlob::MakeFromBuffer. There is no mode selector and no FuzzedDataProvider. After deserialization the harness checks only the buffer validity, creates a small raster surface, and draws the blob at a fixed positive translation; ordinary positive bounds can be quick-rejected before glyph replay, so reachable drawing-oriented tests need bounds that intersect after that translation. The allocation bug triggers during deserialization, before the draw step.
- The libFuzzer harness passes the input bytes directly to poppler::document::load_from_raw_data. There is no prefix, selector byte, or FuzzedDataProvider carving. If the document loads and is not locked, the harness creates a page renderer and renders every page, so page content that selects an embedded font and draws text reaches SplashOutputDev and SplashFTFont::makeGlyph.
- The FFmpeg demuxer fuzzer feeds the file bytes to the MPEG-TS demuxer through an AVIO-backed libFuzzer harness. For this demuxer target, the payload can be a raw transport stream with no leading mode byte or FuzzedDataProvider split; once the demuxer opens the PAT and PMT sections, parsing happens during input opening and stream-info discovery.
- The libFuzzer target writes the raw input bytes to a temporary file and calls the GPAC MPEG-TS probe routine. The probe reads raw file bytes, synchronizes on transport packets, processes PAT and PMT sections through the demuxer, then destroys the demuxer; there is no leading mode selector and no FuzzedDataProvider split.
- The libFuzzer target writes the raw input bytes to a temporary object file, initializes libdwarf with group-any section selection, calls the DWARF CU-header API with the type-section flag, then requests the root DIE and its child. There is no fuzzer-specific prefix or length carving; all structure is supplied by the ELF and DWARF sections themselves.
- The active target is the libxml2 xmllint libFuzzer harness. It reads integers from the front in big-endian order, consumes option bits least-significant-bit first within each word, then selects a parser mode from the remaining bits. The XML document is loaded through the fuzzer's in-memory entity loader; enabling the compression option routes output through gzip rather than requiring a compressed input file.

## Round 28 Format Links
- [[bmp]]
- [[c-blosc2-frame]]
- [[cdp-ethernet-frame]]
- [[dxf]]
- [[elf-dwarf-dwp]]
- [[javascript]]
- [[jpeg]]
- [[libxml2-lint-entity-envelope]]
- [[mapserver-mapfile]]
- [[miff]]
- [[mpeg-ts]]
- [[mpegts]]
- [[opcua-binary-message]]
- [[opentype-font]]
- [[openvswitch-expression]]
- [[pdf]]
- [[pdf-with-embedded-truetype-font]]
- [[pdf-with-embedded-type1c-cff-font]]
- [[php-serialize]]
- [[php-source]]
- [[rar5]]
- [[raw-date-string]]
- [[sip-message]]
- [[skia-textblob-serialized]]
- [[som]]
- [[vcf-text]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 29 Input Contract

- The harness is a libFuzzer binary-analysis target that feeds the PoC file as raw bytes to radare2's analysis path. There is no FuzzedDataProvider split or mode byte in the input file; selecting the ART parser is done by the file magic.
- The arvo wrapper invoked the collator_rulebased libFuzzer target on the copied PoC. The target treats the raw file bytes as a char16_t buffer, wraps them directly in an ICU UnicodeString with length derived from file size, and constructs a RuleBasedCollator. There is no leading mode byte, checksum, file container, or FuzzedDataProvider split.
- libFuzzer supplies raw bytes. The harness carves selector bytes from the back of the input and passes the remaining front prefix as the disassemble_info buffer. Inputs must be long enough to contain both the selector trailer and at least one instruction byte.
- The libFuzzer target consumes the original input buffer directly. A few bytes near the start are also used by the harness to select decoder color format, architecture, and core count, but the same complete buffer is still passed to header decode and then repeatedly to frame decode. There is no FuzzedDataProvider layout or file wrapper.
- libFuzzer passes the raw input buffer as the JSON byte string. The harness decodes a Variant, calculates its JSON size, encodes it, decodes the generated JSON again, re-encodes it, and compares the two encodings. There is no FuzzedDataProvider layout or mode selector; malformed JSON or values that decode with an error exit before the vulnerable encode path.
- The libFuzzer target rejects very small or very large buffers, then treats the last trailer bytes as disassembler metadata: one flavour byte, a little-endian machine field, and one architecture byte. The remaining front bytes become disassemble_info.buffer, and the harness repeatedly calls the selected print_insn function until an instruction fails or consumes the remaining buffer.
- The libFuzzer harness feeds the raw input bytes directly to rnp_input_from_memory and calls the packet dump API with raw packet dumping enabled. There is no leading mode selector and no FuzzedDataProvider front/back carving.
- The libFuzzer harness uses the input bytes as a raw PDF stream, opens it through MuPDF, loads each page, allocates a pixmap from the page bounds using the identity transform and an RGB colorspace, runs page contents plus annotations/widgets through the draw device, and suppresses recoverable MuPDF exceptions. There is no FuzzedDataProvider contract, no leading selector byte, and no secondary file envelope.
- libFuzzer passes raw bytes directly. The harness rejects undersized inputs, carves two fixed-width string fields from the front with explicit termination behavior, treats the suffix as context text, applies the property list to both a multivalue and scalar config-map definition, and then releases both the config-map entries and the original property list.
- The target is the raw-byte libFuzzer decompress-frame harness: the input bytes are passed directly to LLVMFuzzerTestOneInput, which opens them as an in-memory frame. There is no FuzzedDataProvider splitting. The local arvo wrapper invokes the libFuzzer binary on a fixed path; for this 32-bit fuzzer, local single-file verification needed staging the copied file into a tmpfs-backed path before running the fuzzer once.
- The harness is libFuzzer over raw bytes. It rejects oversized inputs, then passes the complete byte buffer to the PHP fuzzer SAPI as one request and executes it under a step limit. There is no front/back byte carving or FuzzedDataProvider contract.
- The libFuzzer harness initializes a TPM2 instance, sends an internal startup command, then passes the raw fuzzer bytes directly to TPMLIB_Process as one TPM2 command. After processing, it obtains volatile and permanent state, terminates, restores both state blobs, and initializes again. There is no FuzzedDataProvider split and no file envelope outside the TPM command itself.
- The secilc libFuzzer target consumes the input bytes directly as one raw CIL source buffer. The harness adds the buffer as an in-memory CIL file, compiles it, builds and optimizes a policy database, writes the policy to a null sink on success, then destroys the CIL database. There is no file wrapper, selector byte, integrity trailer, or FuzzedDataProvider front/back layout.
- The active binary is hb-subset-fuzzer. It consumes the whole file as an hb_blob font, runs one subset with built-in text, and for larger inputs may also read trailing subset flags and UTF-32 codepoints from the end of the same byte string. The harness also derives allocation-failure state from total input size.
- The libFuzzer harness scans the raw input bytes with a fixed YARA rule that imports the PE module and reads section metadata. There is no FuzzedDataProvider splitting for this target; parser reachability depends on making the raw buffer look enough like a PE for the module to expose the first section.
- The URI harness is a libFuzzer target that copies the raw input bytes into a newly allocated NUL-terminated string and calls parse_uri directly. There is no FuzzedDataProvider layout, no leading mode selector, and embedded NUL bytes would shorten the string seen by the parser.
- The libFuzzer target passes the raw input bytes to Ghostscript as stdin through the gstoraster wrapper; there is no mode selector, checksum gate, or FuzzedDataProvider carving. The wrapper runs Ghostscript with the cups device and PDF input is interpreted normally. The embedded Type1C stream is loaded when the page content selects the font, so a constructed PDF must render text with that font to drive the CFF parser.
- libFuzzer supplies raw bytes as Ghostscript stdin through the gstoraster-style harness. There is no FuzzedDataProvider prefix or mode byte. Ghostscript sniffs the raw input as PDF/PostScript and renders to the cups device with output discarded.
- The libFuzzer target writes the entire input buffer to a temporary pcap file, opens it through PcapPlusPlus' pcap reader, reads only the first packet, and constructs a parsed packet from those captured bytes. There is no FuzzedDataProvider split or selector byte; the bytes must be a structurally complete pcap file.
- libFuzzer passes raw file bytes to RawSpeed's RawParser. There is no leading mode selector and no FuzzedDataProvider layout. Parser exceptions are caught by the harness, so the input must satisfy the TIFF/DNG structure and raw-image gates before sanitizer-visible opcode faults are observable.
- The libFuzzer harness feeds the raw file bytes. It chooses DWG when the input begins with the DWG signature, JSON when the first byte is an opening JSON object, and DXF otherwise. The JSON path copies and null-terminates the input before calling the libredwg JSON reader, then may serialize the parsed drawing to an output format after import.
- The libFuzzer harness passes the raw input bytes directly to MuPDF as a PDF stream, opens it with the PDF handler, counts pages, renders each page with the identity transform into an RGB pixmap, and drops the pixmap. There is no input carving, mode byte, or FuzzedDataProvider layout.
- The libFuzzer harness passes the raw input bytes directly to the CycloneDDS TypeMapping deserializer. It iterates complete type-object pairs, finds a matching minimal id through the complete-to-minimal sequence, constructs complete/minimal type information, references the complete type, and then adds the complete type object, which invokes XTypes validation.
- The harness is libFuzzer over raw bytes with no FuzzedDataProvider carving. It null-terminates copied text inputs when needed, decodes the buffer as DWG, JSON, or DXF, then writes one randomly selected output format to a sink file. The JSON writer is one reachable output path and converts retained legacy TV strings through the vulnerable converter.
- The libFuzzer harness passes the whole input buffer directly to the xAAC decoder. There is no outer archive, length prefix, integrity field, mode selector, or FuzzedDataProvider split. After configuration, the same byte stream is repeatedly decoded while the decoder reports consumed-byte counts.
- The active binary is GPAC fuzz_probe_analyze. It writes the raw input bytes to a temporary extensionless file and runs the GPAC probe/analyze filter graph; there is no leading mode byte or FuzzedDataProvider layout. Format reachability depends on content probing into the RTP/SDP input filter.
- The active wrapper runs the libxml2 xml fuzzer. That target masks out DTD validation and XInclude, applies the allocation limit around pull, push, and XML reader parsing, installs the fuzzer entity loader, and traverses reader nodes plus attribute values. The local runner verify path can report a /tmp/poc wrapper error even when direct execution of the same target and official submit exercise the real crash.
- The GraphicsMagick coder harness is a libFuzzer target compiled for the XPM coder. It feeds the entire PoC file as the image blob to Magick++ with the coder fixed by the build; there is no fuzzer-side selector, checksum, or FuzzedDataProvider carving.
- The libFuzzer target copies the raw input bytes into a NUL-terminated buffer and passes them directly to mrb_load_string. There is no mode byte, checksum, length prefix, or FuzzedDataProvider layout. Inputs must be valid enough Ruby source to compile and execute under mrb_load_string; parser errors simply return without reaching the VM opcode path.
- libFuzzer passes the raw byte buffer directly to the WAMR wasm loader. There is no prefix, selector byte, checksum, or FuzzedDataProvider carving. Module instantiation is not required; a loader-stage malformed module is sufficient.
- The libFuzzer target consumes a boolean domain-relative flag from the back first, then consumes an integral length from the back for the first URI string, then reads that many wide characters from the front and treats the rest as a second wide URI string. ConsumeIntegralInRange only consumes as many trailing bytes as the current range requires, so the length selector must be sized to the active range rather than encoded as a full machine word.
- libFuzzer supplies the raw buffer directly to Ghostscript stdin and the harness selects the pdfwrite device with a null output file. The fixed argument list includes quiet, safer, no-pause, batch execution and does not use FuzzedDataProvider, a leading mode byte, or an input prefix. The input therefore must be a self-contained PostScript or PDF program; command-line-only Ghostscript switches cannot be supplied through the fuzz bytes.

## Round 29 Format Links
- [[aac-usac-mps]]
- [[art]]
- [[binutils-disassembler-buffer-with-trailer-selector]]
- [[binutils-disassembler-buffer-with-trailing-selectors]]
- [[blosc2-frame]]
- [[cil-policy-text]]
- [[cyclonedds-xtypes-typemap-xcdr2]]
- [[dng]]
- [[dwg]]
- [[fluent-bit-config-map-fuzzer-buffer]]
- [[fuzzed-dataprovider-wide-uri]]
- [[hevc-annex-b-elementary-stream]]
- [[icu-collation-rule-utf16le]]
- [[libredwg-json]]
- [[libxml2-xml-fuzzer-entity-envelope]]
- [[open62541-json-variant]]
- [[openpgp-secret-keyring]]
- [[opentype-font]]
- [[pcap-encapsulated-dns-message]]
- [[pdf]]
- [[pdf-with-embedded-type1-font]]
- [[pdf-with-embedded-type1c-cff-font]]
- [[pe]]
- [[php]]
- [[postscript-pdfwrite-transparency]]
- [[ruby-source]]
- [[sdp]]
- [[sip-uri]]
- [[tpm2-command-buffer]]
- [[wasm-binary]]
- [[xpm]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 30 Input Contract

### Input Contract
- The libFuzzer harness passes the raw input buffer to libarchive with all filters and formats enabled. A single reader callback exposes the buffer as an archive stream, then the harness iterates headers and drains each entry through archive_read_data into a fixed page-sized buffer. There is no mode selector or FuzzedDataProvider carving; reaching the sink depends entirely on a structurally valid archive stream and compressed member data.
- The YARA dotnet libFuzzer target scans the raw file bytes as an in-memory PE sample under a rule importing the dotnet module and comparing module_name. There is no leading mode byte, archive wrapper, checksum, stdin contract, or FuzzedDataProvider carving; parser reachability depends on the PE loader accepting the CLR metadata streams.
- The libFuzzer input is raw chunk-stream bytes with no leading mode byte. After binding a PKCS#15 card, the harness consumes two additional chunks as operation input and parameters, then iterates PKCS#15 objects through decipher, derive, wrap, unwrap, signature, and PIN operations. This harness copy clamps the ATR chunk against the reader's current ATR length during connect, so synthetic ATR-only attempts can fail before driver matching.
- The harness feeds the raw libFuzzer input to the decoder for both header parsing and frame decoding. It also samples fixed bytes from the original raw buffer to choose output color format and thread count; those selector bytes are not removed from the stream, so changing them can also perturb the HEVC parameter-set payload.
- The libFuzzer-style harness passes the entire file as a NUL-terminated mruby source string to the default load-string API. There is no leading selector, no FuzzedDataProvider carving, and no compiler context option that enables verbose code dumping. Shell/backtick helpers may exist inside the runtime, but external child failures are not equivalent to an in-process target crash under official scoring.
- The secilc fuzz harness is raw libFuzzer input: the PoC bytes are passed directly as one in-memory CIL source buffer. There is no mode byte, no file container, and no FuzzedDataProvider tail layout. The harness compiles the CIL source, attempts policydb construction and optimization, and discards output to a null sink.
- The LibJS libFuzzer wrapper feeds the PoC file bytes directly as a JavaScript source buffer, parses a program, creates a VM and GlobalObject, and runs the program when parsing succeeds. The wrapper reads the copied file internally and does not pass a script filename to the interactive js utility.
- The harness feeds the file bytes directly to djxl_fuzzer. The last four bytes are consumed as little-endian fuzzer flags controlling alpha/grayscale, streaming, JPEG-to-pixels, callback, orientation, output type, endian, alignment, and Highway target selection; the codestream is the prefix before those tail bytes.
- The libFuzzer harness passes the input bytes directly to LibGfx's JPEG memory loader and requests decode. There is no filename wrapper, leading mode byte, sidecar metadata, integrity-check layer, or FuzzedDataProvider front/back split.
- The compiled libFuzzer target instantiates FiffParser, asks it for a decoder, then runs decodeRaw and decodeMetaData while catching normal RawSpeed parser/decoder exceptions. The FIFF parser reads raw bytes, locates the embedded TIFF via header pointers, parses that TIFF as a subview, and then DNG tile offsets are consumed by the decoder against the full input buffer. Clean exceptions are non-crashing outcomes; sanitizer-visible uninitialized image data is the useful signal.
- The libFuzzer harness writes the raw fuzz bytes to a temporary .s file and invokes the assembler pass on that file. There is no prefix, selector byte, FuzzedDataProvider layout, checksum, or stdin wrapper.
- The libFuzzer input is raw bytes with a fixed prefix before the chunk stream. After connecting the fuzz reader, the harness consumes explicit chunks for wrap input, unwrap input, and put-data input; driver APDU calls consume additional chunks as responses. The extracted source copies wrap and unwrap chunks into heap buffers and allocates a heap challenge buffer before calling the card operations.
- The libFuzzer target passes the complete raw byte buffer to Exiv2 ImageFactory, then calls readMetadata, prints metadata and several structure views, and calls writeMetadata inside a catch-all exception boundary. There is no selector byte and no FuzzedDataProvider carving; all bytes are the candidate file image.
- The libFuzzer target passes the entire input buffer directly as a PDF memory stream, opens it with the PDF handler, counts pages, and rasterizes each page. There is no prefix, mode selector, or FuzzedDataProvider layout. MuPDF exceptions are caught, so the useful signal is a sanitizer-visible native fault during document open/authentication or rendering.
- The libxml2 XML fuzzer reads fields from the front of the raw libFuzzer byte stream. Integers are consumed as big-endian option/allocation controls, then harness strings are consumed front-to-back using the fuzzer's escape-and-terminator convention. The allocation control arms libxml2's fuzz malloc/realloc shim; zero disables injection and positive effective values fail a selected allocation. The target runs pull parsing, push parsing in fixed chunks, and xmlTextReader over the main entity with the same option set and allocation limit.
- The libFuzzer harness passes the whole input buffer directly to the target. There is no FuzzedDataProvider, no front or back field consumption, and no selector byte. The vulnerable path constructs a string from the raw pointer before invoking ImageMagick image parsing for the XC pseudo-image.
- The libFuzzer target receives raw bytes, writes them unchanged to a temporary file, and calls Mat_Open on that filename. It then lists MAT variables, rewinds, repeatedly reads variable metadata and full data through Mat_VarReadNextInfo and Mat_VarReadDataAll, computes the variable size, frees each variable, and closes the file. There is no leading mode byte, no FuzzedDataProvider carving, and no checksum or command-line filename embedded in the PoC.
- The libFuzzer harness passes the raw input bytes directly to the OpenType font loader. There is no mode selector, filename gate, checksum wrapper, or FuzzedDataProvider layout. Font loading iterates cmap encoding records during parsing.
- The fuzz target passes the input bytes as a media asset to GPAC probe/analyze. The image probe selects the image reframer from the BMP header. There is no leading selector byte, integrity-check layer, sidecar metadata, or FuzzedDataProvider front/back split.
- The libFuzzer harness feeds raw bytes into a CBS cursor and repeatedly consumes one front byte as an API selector. Most string-taking APIs first copy a length-prefixed field into a std::string and pass a terminated c_str, but the vulnerable sigalgs-list command passes the current CBS data pointer directly with no length and no added terminator.
- The WAMR libFuzzer target copies the raw input bytes into the loader path and calls wasm_runtime_load. There is no fuzzer prefix, selector byte, checksum, FuzzedDataProvider carving, instantiation requirement, or exported-function execution requirement; loader-stage malformed modules are sufficient.
- The qpdf fuzzer consumes the input as raw PDF bytes with no mode selector or FuzzedDataProvider layout. It repeatedly reparses the same bytes and writes through several writer configurations, including QDF output, linearized encrypted output, object-stream disabling, and object-stream generation, then exercises page, outline, form, and JSON helpers.

### Format Links
- [[bmp]]
- [[cil-policy-text]]
- [[fiff-wrapped-dng-ljpeg]]
- [[gas-assembly-source]]
- [[hevc-annex-b-bitstream]]
- [[imagemagick-xc-color-string]]
- [[javascript]]
- [[jpeg]]
- [[jxl]]
- [[libxml2-xml-fuzzer-entity-envelope]]
- [[mat73-hdf5]]
- [[mruby-source]]
- [[opensc-fuzz-card-chunk-stream]]
- [[opensc-pkcs15-reader-chunk-stream]]
- [[opentype-sfnt]]
- [[pdf]]
- [[pdf-encrypt-dictionary]]
- [[pe-dotnet]]
- [[quicktime-mp4]]
- [[rar5]]
- [[ssl-ctx-api-command-stream]]
- [[wasm-binary]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 32 Input Contract
- The GraphicsMagick TIFF coder fuzzer feeds raw file bytes as an image blob with the TIFF coder selected by the harness. It reads the image and then exercises TIFF write-back when the read succeeds. There is no mode byte or FuzzedDataProvider framing; candidate files must also be readable by the Docker-copied target file user.
- The GraphicsMagick coder harness is libFuzzer over raw file bytes. There is no FuzzedDataProvider carving; the input blob is handed to the JNX reader selected by the harness, and embedded tile bytes are then passed through GraphicsMagick's normal blob-to-image dispatch.
- The libFuzzer wrapper treats the submitted file as raw bytes, opens it as an in-memory file, reads an IVF-style header, initializes the AV1 decoder in threaded mode, then repeatedly reads IVF frames and drains decoded images. There is no FuzzedDataProvider split, checksum gate, or separate argv-controlled mode.
- The GraphicsMagick MNG coder fuzzer feeds the raw libFuzzer input bytes directly as a Magick blob with the MNG coder selected. There is no mode byte, no file carving, and no FuzzedDataProvider split. The harness catches Magick exceptions during read and writes the decoded image back only if reading succeeds.
- The libFuzzer input bytes are wrapped with fmemopen as a file. The harness reads the IVF header from the front of the raw input, initializes the AV1 decoder, loops through IVF frames with ivf_read_frame, calls aom_codec_decode for each frame, then drains decoded frames. There is no FuzzedDataProvider split and no argv or stdin contract beyond the raw file bytes.
- The libFuzzer entrypoint passes the whole non-empty input buffer to magic_buffer. There is no leading selector, marker delimiter, checksum, length envelope, or FuzzedDataProvider split.
- Wireshark fuzzshark is built as a libFuzzer-style target configured for the IP dissector. The PoC file bytes are passed directly as the packet buffer to fuzzshark; there is no file-format wrapper and no FuzzedDataProvider split. The target registers the configured dissector as a postdissector, disables several unrelated dissectors at startup, and feeds the raw buffer through epan dissection with captured length equal to the PoC file size.
- The libFuzzer harness feeds raw file bytes directly. It consumes the prefix from the front as RawImage and tile metadata, constructs VC5Decompressor on the remaining stream, allocates image data, calls decode, catches only RawSpeed exceptions, and treats sanitizer aborts or C assertions as crashes.
- The harness is libFuzzer with no FuzzedDataProvider split or mode selector. It passes the entire input buffer to Poppler's raw PDF loader, discards unloadable or locked documents, then renders each page through page_renderer. Parser reachability depends on the raw bytes forming a loadable or repairable PDF document.
- The libFuzzer target passes the entire input buffer directly to Poppler's raw-data document loader, skips locked or unloadable documents, iterates all pages, and renders each page with the C++ page renderer. There is no mode byte, length suffix, checksum, argv file contract, or FuzzedDataProvider front/back split.
- The libgit2 harness consumes the libFuzzer input as raw bytes with no FuzzedDataProvider fields or mode byte. The same raw buffer is offered to the supported object parsers, including the tree parser.
- The libFuzzer target feeds raw input bytes through an in-memory file. It reads an IVF-style header before decoder initialization, derives the decoder thread count from a header-controlled value in threaded builds, then passes each IVF frame payload to the AV1 decoder and drains output frames. There is no FuzzedDataProvider layout, mode-selector byte outside the IVF header, or checksum requirement.
- The GraphicsMagick MIFF coder fuzzer passes the raw libFuzzer bytes directly as a Magick blob with the MIFF coder forced. There is no leading selector or carved sub-input. Magick exceptions during read are caught; if read returns an image, the harness writes it back to a MIFF blob, so read-side uninitialized pixels can surface during write-back.
- The libFuzzer harness compiles a fixed YARA rule that imports the dotnet module and checks the module_name field. Each raw input is scanned as an in-memory buffer with SCAN_FLAGS_NO_TRYCATCH. The dotnet module load path finds a PE image in the raw bytes, sets the PE data pointer and size from the memory block, and calls the dotnet CLR metadata parser. There is no carved prefix, no FuzzedDataProvider, and no filename-based parsing.
- The active target is curl_fuzzer_ftp. The libFuzzer wrapper passes the whole file to the TLV parser from the front with no back-loaded fields. The harness installs mocked socket callbacks, sends response zero immediately on connection, sends later responses after client requests, and can open a second socket manager for the FTP passive data channel.
- The libFuzzer target treats the input as raw bytes for one NUL-terminated string. It rejects inputs that are too short, do not end in NUL, or contain a newline before the final terminator. The harness then tries the same string through key parsing, wildcard key parsing, and action-list parsing; there is no tar framing or length-prefixed outer envelope.
- The active binary is HarfBuzz hb-shape-fuzzer. It treats the entire PoC as raw font bytes, creates an hb_blob, hb_face, and hb_font, shapes fixed ASCII text, then uses trailing input bytes as UTF-32 text for a second shaping pass before running miscellaneous face APIs. There is no pcap/archive wrapper and no FuzzedDataProvider split.
- The libFuzzer harness rejects inputs above its size cap, then calls byte-string conversion APIs on the raw bytes. For word-aligned inputs it additionally calls idn2_to_ascii_4i with the raw bytes cast as 32-bit codepoints, an element count derived from the byte length, a fixed small heap output buffer, and several flag combinations. There is no file wrapper, checksum, or FuzzedDataProvider split.
- The libFuzzer target passes the entire input buffer directly to Poppler's raw-data document loader, skips locked or unloadable documents, iterates all reported pages, creates each page by index, and renders each page with the C++ page renderer. There is no leading selector byte, argv filename contract, checksum wrapper, or FuzzedDataProvider front/back split.
- The libarchive fuzzer feeds raw bytes as one archive stream from memory, enables all formats and filters, iterates archive headers, and drains entry data through archive_read_data. There is no prefix byte or FuzzedDataProvider layout; parser reachability depends on preserving the RAR5 marker, base-header CRCs, and compressed member-data gates.
- The GnuTLS libFuzzer harness passes raw bytes as a DER PKCS#12 blob, uses a fixed password, checks the MAC result but continues into simple parsing, and then deinitializes returned key, certificate-chain, extra-certificate, and CRL outputs according to the parser result.
- The GraphicsMagick coder fuzzer selects the PTIF coder, which aliases into the TIFF coder. It passes the submitted raw bytes as an image blob, forces the coder name, reads the image through Magick++, and may write the image back if the selected coder has encoder support. There is no FuzzedDataProvider split or external argv-controlled file format beyond the raw TIFF-family bytes.
- The MuPDF PDF fuzzer consumes the raw libFuzzer bytes as an in-memory PDF, opens the document, counts pages, and renders pages to a pixmap. There is no harness prefix, no byte carving, and no FuzzedDataProvider layout. Parser exceptions are caught, so the input must be structurally renderable enough for the shading/function path to execute.
- The libFuzzer target initializes the FFmpeg AAC decoder once, allocates an AVCodecContext, optionally derives context fields from the tail of large inputs, opens the decoder, then repeatedly feeds AVPackets split by the fixed tag. Without the tag, the entire remaining front region is one packet. There is no FuzzedDataProvider; integers are not consumed from the back except for the harness-specific large-input context tail.

## Round 32 Format Links
- [[curl-fuzzer-tlv]]
- [[ffmpeg-aac-decoder-packet-stream]]
- [[git-tree-object-body]]
- [[ivf-av1]]
- [[jnx]]
- [[libidn2-raw-domain-or-uint32-codepoints]]
- [[libmagic-classified-raw-buffer]]
- [[miff]]
- [[mng]]
- [[opentype-aat-mort-font]]
- [[ovs-odp-action-text]]
- [[pdf]]
- [[pe-dotnet]]
- [[pkcs12-der]]
- [[rar5]]
- [[raw-ipv4-ositp-cotp]]
- [[rawspeed-vc5-fuzzer-envelope]]
- [[tiff]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 33 Input Contract

### Input Contract
- The GraphicsMagick coder fuzzer passes the raw PoC bytes as a Magick blob to the fixed MAT coder. There is no mode selector, argv field, stdin framing, checksum gate, or FuzzedDataProvider front/back split. The harness sets bounded image width and height limits before reading, and writable coders may be exercised through post-read writeback when the read succeeds.
- The ip6-send libFuzzer harness consumes a leading byte as the OpenThread message link-security selector and appends all remaining bytes as one raw IPv6 packet passed to otIp6Send on an initialized leader-mode instance. There is no FuzzedDataProvider layout.
- The MuPDF PDF fuzzer consumes the submitted file as raw PDF bytes from memory, opens it as a PDF document, and renders page contents to a pixmap. There is no mode byte, archive wrapper, checksum gate, or FuzzedDataProvider carving.
- The libFuzzer target consumes the whole file as a Magick Blob for the fixed PDB coder. There is no in-band selector byte or FuzzedDataProvider split; the harness reads the blob as PDB and, if decoding succeeds, writes it back through the same PDB coder.
- The harness passes raw libFuzzer bytes directly to the request parser. It copies the bytes into a fixed static request buffer, truncates inputs that exceed that buffer, requires the request finalizer to observe a complete header terminator, and then parses using the full copied length rather than a separately saved end-of-headers pointer.
- The libFuzzer harness passes the entire raw file byte string directly to the Lwan HTTP request parser. There is no mode byte, no FuzzedDataProvider trailer, and no file wrapper. The harness copies input into an internal fixed request buffer, requires a complete CRLFCRLF-terminated request, then parses query, cookie, encoding, If-Modified-Since, and Range helper state.
- The libFuzzer stream-decompression harness treats the input as raw bytes but first consumes a front seed before parsing. That seed drives pseudo-random input and output chunk sizes for the streaming API. If the first parser chunk is small, legacy streaming may copy data into an internal staging buffer; selecting a seed that feeds the frame as one direct chunk can make end-of-input overreads visible against the fuzzer allocation.
- The libFuzzer harness passes raw bytes directly. It copies them into a fixed static request buffer, enables proxy-protocol parsing in the request flags, runs the request finalizer that scans for an HTTP header terminator, and then invokes the HTTP request parser. There is no FuzzedDataProvider layout or mode-selector byte.
- The libFuzzer target passes the complete input buffer directly as the JSON byte string, with no file wrapper, mode byte, or FuzzedDataProvider layout. The active target decodes a top-level Variant, calculates the reversible JSON size, encodes it, decodes that generated JSON again, re-encodes it, and then compares the generated encodings. Malformed JSON or values that fail the first decode exit before the encode stage.
- The libFuzzer harness feeds the PoC file bytes directly to YARA rule scanning with import dotnet. There is no leading mode byte, no argv/stdin wrapper, and no FuzzedDataProvider front/back carving; parser reachability is entirely through the raw PE/.NET file structure.
- The selected OpenThread libFuzzer target is the CLI UART receive harness. It copies the raw PoC bytes into a UART buffer after initializing a single OpenThread instance, then processes CLI tasklets. There is no file header, mode byte, checksum, or FuzzedDataProvider carving.
- The libFuzzer harness opens the selected Capstone platform, enables detailed decoding, optionally selects alternate syntax from the selector byte, then disassembles the remaining bytes from a fixed base address and prints instruction details to a sink. The byte stream is consumed directly; there is no FuzzedDataProvider split.
- The libarchive libFuzzer harness treats the entire input as a raw archive stream from memory, enables all filters and formats, repeatedly reads headers, drains each entry with archive_read_data until a nonpositive return, breaks only on ARCHIVE_FATAL, and frees the archive reader. There is no mode byte or FuzzedDataProvider carving.
- The FFmpeg target decoder harness feeds raw bytes to the selected AC3 decoder. If the input is large enough, a trailing context block is consumed as codec-context fields and removed from packet data. Otherwise the packet is passed directly. A fixed delimiter can split the remaining bytes into multiple packets for repeated decode calls under one decoder context.
- The libFuzzer target is oss-fuzzshark configured for the UDP dissector in the IP protocol table. It feeds the file bytes as one synthetic frame to the UDP dissector; there is no pcap envelope, no FuzzedDataProvider split, and no required IP wrapper for this image. Nested parser reachability depends on the UDP ports, then GSMTAP metadata, then RLC/MAC control-message bits.
- The libFuzzer target feeds raw bytes to the NCP UART receive path after initializing a single OpenThread instance, enabling IPv6 and Thread, and becoming leader. There is no FuzzedDataProvider or mode byte. The UART stream must be HDLC-framed Spinel; local network-data and server-data changes register with the leader on true-to-false allow-property transitions. STREAM_NET and STREAM_NET_INSECURE carry little-endian length-prefixed IPv6 datagrams followed by optional metadata.
- The YARA dotnet libFuzzer target compiles a fixed rule importing the dotnet module and scans the raw input bytes directly with yr_rules_scan_mem. There is no mode selector, archive wrapper, path-based parsing, checksum wrapper, or FuzzedDataProvider layout; all bytes are interpreted as the scanned PE image.
- The libFuzzer simple_decompress target consumes a four-byte RNG seed prefix from the input before passing the remaining bytes to ZSTD_decompressDCtx. It reuses one decompression context and runs the same frame through several randomized output-buffer capacities. There is no FuzzedDataProvider layout beyond the seed prefix; the post-prefix bytes are treated as the complete compressed frame stream.
- The active target opens the FDK-AAC decoder in LOAS/LATM mode, feeds the entire input byte stream through the decoder fill API, and repeatedly calls the decode-frame API until the stream is consumed or rejected. The harness does not use FuzzedDataProvider, a leading selector byte, multiple files, or a wrapper archive.
- The libhevc fuzzer consumes the whole file as a raw decoder input. It samples decoder color format and core count from fixed positions in the same byte buffer, but those bytes are not removed; the full buffer is then passed through header decode and frame decode loops. There is no container wrapper and no FuzzedDataProvider split.
- The OpenSSL x509 libFuzzer harness consumes the entire PoC as raw DER for d2i_X509. If parsing succeeds, it prints the certificate, public key, and extensions to a null BIO, then serializes the certificate again. There is no in-band selector and standalone GENERAL_NAME DER does not reach this harness path.
- The harness uses FuzzedDataProvider. Parser options are consumed from the back of the byte stream as a little-endian integral value. The encoding string is consumed from the front with the provider's random-length string rules. All remaining front bytes become the XML file contents passed to xmlReaderForFile, then the harness repeatedly calls reader read/value APIs before freeing the text reader.
- The fuzzer passes raw input bytes directly to jbig2_data_in and then completes and extracts the current page; there is no mode selector, wrapper format, checksum, or FuzzedDataProvider carving. Parser reachability depends entirely on presenting a structurally valid JBIG2 stream in those raw bytes.

### Format Links
- [[aac-loas-latm]]
- [[ac3-eac3-audio-frame]]
- [[capstone-disasm-selector-plus-bytes]]
- [[hevc-annex-b-bitstream]]
- [[http-request]]
- [[http-request-with-proxy-v2-prefix]]
- [[ipv6-udp-coap-meshcop-tlv]]
- [[jbig2]]
- [[libxml2-xml-reader-fdp-envelope]]
- [[mat]]
- [[open62541-json-variant]]
- [[openthread-cli-uart]]
- [[openthread-ncp-uart]]
- [[palm-pdb-image]]
- [[pdf]]
- [[pe-dotnet]]
- [[rar]]
- [[wireshark-fuzzshark-udp-gsmtap-rlcmac]]
- [[x509-der-certificate-with-general-name]]
- [[zstd-legacy-frame]]
- [[zstd-legacy-v0-5-frame]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Input Contract
- The libFuzzer target feeds the raw input bytes directly to the GraphicsMagick JPEG coder through a memory blob. There is no selector byte, no FuzzedDataProvider split, and no filename extension gate beyond the compiled JPEG coder.
- The libFuzzer target passes the raw file bytes directly to the PostGIS WKB importer with no selector byte, no FuzzedDataProvider carving, and no outer file container. Normal parser errors are caught by the harness, so a useful input must reach the specific parser state before violating the narrow child-geometry invariant.
- The libFuzzer target rejects inputs shorter than the selector trailer, then treats all preceding bytes as the disassembly buffer. There is no leading mode byte and no FuzzedDataProvider consumption; selector fields are read from the end of the file.
- libFuzzer passes the input as raw bytes with no mode byte and no FuzzedDataProvider. The harness opens a malloc-backed radare2 IO object sized to the input, writes the bytes at the start of that object, runs binary auto-analysis, then runs the ia command. No filename or extension is provided.
- The libFuzzer target treats the leading input byte as the patch prefix-length option and passes all remaining bytes directly to the patch parser. The harness then frees the returned patch object; it does not print, apply, or otherwise traverse the parsed patch after parsing.
- The libFuzzer harness passes the raw file bytes through several KArchive handlers with no selector byte and no FuzzedDataProvider layout. The same raw bytes must therefore be a complete archive-like buffer; K7Zip is reached by satisfying its signature and header gates.
- The libFuzzer input is raw bytes consumed by a custom chunk reader. Each chunk size is effectively taken from one leading byte while two bytes are consumed as the chunk header, and the reader advances only by that header before returning the chunk body. This makes later chunks overlap earlier response bodies. After PKCS#15 binding, the harness consumes two more chunks as operation input and parameter buffers, then iterates PKCS#15 objects through crypto and PIN operations.
- libFuzzer passes the entire raw byte slice as the font blob. The harness creates a blob, face, and font, shapes a fixed ASCII string, and for inputs larger than the UTF-32 text window copies the final bytes as native-endian UTF-32 codepoints for a second shape call before querying glyph extents. There is no mode selector, checksum wrapper, or FuzzedDataProvider.
- The active libFuzzer target is the Lwan config fuzzer. It copies the raw input bytes into a fixed static buffer, clamps oversized inputs, opens the config parser over the copied bytes with one trailing byte excluded from the logical lexer range, recursively reads config lines, and uses no mode byte, checksum, or FuzzedDataProvider split.
- The libFuzzer harness treats the entire nonempty file as raw mruby source bytes. It copies the bytes to a NUL-terminated buffer, opens a fresh mruby state, calls mrb_load_string, closes the state, and frees the copy. There is no selector byte, external filename, length prefix, bytecode container, or FuzzedDataProvider split.
- The libFuzzer target feeds the raw file bytes to a virtual OpenSC reader. The reader consumes one length-prefixed chunk for connection/ATR handling, then consumes later chunks as APDU responses during card-driver matching, PKCS#15 binding, and file selection. In this build the ATR chunk does not provide a useful ATR gate, so reaching SetCOS depends on the APDU-based version probe rather than ATR matching.
- The libFuzzer target consumes the raw file bytes directly through a little-endian ByteStream. It constructs a RawImage from leading scalar fields, reads strip records front-to-back from the same stream, creates image data, runs PhaseOneDecompressor, then checks the image buffer for initialized memory. There is no file magic, filename wrapper, mode byte, or FuzzedDataProvider tail consumption.
- The libFuzzer harness passes the raw file bytes as a NUL-terminated template string capped to a fixed internal copy buffer, compiles it with a descriptor exposing path strings and a file-list sequence, then frees the compiled template. There is no mode byte, length prefix, checksum, or FuzzedDataProvider tail layout.
- The fuzz harness consumes the whole file as raw bytes through OpenJPEG memory-stream callbacks. There is no leading mode byte or FuzzedDataProvider layout. It selects J2K versus JP2 from the initial signature, reads the image header, caps the requested decode area internally, then calls the normal decoder path.
- The libFuzzer harness consumes raw file bytes with no mode byte and no FuzzedDataProvider splitting. It copies the input into a fixed global character buffer, appends a NUL terminator, then calls the template compiler with a fixed descriptor table.
- The libFuzzer harness passes the complete file bytes directly as template text. It copies bytes into a fixed static buffer, clips oversized inputs, appends a NUL terminator, and calls the template compiler with a descriptor containing top-level string fields and one sequence field with nested string/integer fields. It compiles and frees the template; it does not require an outer file format, checksum, mode selector, FuzzedDataProvider layout, or template application step.
- The libFuzzer target installs the synthetic OpenSC reader, connects a card from the first chunk, calls PKCS#15 bind, and only consumes the later operation-input chunks if a PKCS#15 card is successfully bound. There is no raw ASN.1 or standalone smart-card file envelope.
- The target installs a virtual reader, connects a card, binds PKCS#15, then consumes two more chunks as operation input and parameter data before iterating PKCS#15 objects through crypto and PIN operations. CoolKey is reached through APDU-speaking driver matching; APDU chunks are consumed statefully, so operation-response chunks must appear after card initialization and object binding.
- libFuzzer passes raw bytes. The harness consumes two little-endian 16-bit header fields from the front and sends the remaining bytes to Samba NDR pull logic. There is no FuzzedDataProvider and no trailing selector.
- The selected harness is the generated libFuzzer TYPE_STRUCT target for drsblobs. It pulls the chosen structure with NDR scalar and buffer flags, then immediately pushes and prints the resulting structure, so inconsistencies between pull-time allocation and push-time count use become sanitizer-visible.
- The libFuzzer input is raw bytes. The harness rejects invalid flag bits, maps the selected public-structure number through the interface table, allocates the destination structure on the stack, pulls the body with scalar and buffer flags, pushes it back out, and prints it. Local verification can report no crash for the same candidate that the official submit path confirms, so plausible NDR stack-state crashes should be submitted.
- libFuzzer supplies raw bytes with a minimum-size gate. The harness assigns the data prefix to disassemble_info.buffer, derives target selectors from the final suffix bytes, initializes one disassembler for the selected target, and invokes a single decoded instruction printer. It does not use FuzzedDataProvider and does not construct a GDB TUI source window.
- The BFD fuzz harness writes the raw input bytes to a temporary file and calls BFD archive-format detection on that file. There is no mode byte, checksum wrapper, FuzzedDataProvider layout, or length prefix outside the archive format itself.
- The libFuzzer harness treats the front of the input as the instruction buffer and parses selector metadata from the tail. There is no FuzzedDataProvider; the important contract is preserving enough bytes for the tail selectors while making the prefix decode as CRX instructions.
- The libFuzzer harness feeds the entire file as a string to xmlReadMemory. It parses once with zero options and once with an option value derived from std::hash of the whole input modulo a signed integer limit. There is no external file envelope or FuzzedDataProvider byte split, but the input content can be adjusted with an inert XML comment so the derived option mask enables DTD validation.
- The libFuzzer harness consumes raw bytes with no mode byte and no FuzzedDataProvider splitting, copies them to an owned buffer, calls TraceProcessorStorage::Parse, and then flushes end-of-file parsing. This storage-only factory registers the proto tokenizer and TrackEvent path but not the full shell module set, so ftrace, heap graph, graphics, Android probes, and system probes were not active target paths in this harness.
- The libFuzzer harness passes the complete file bytes directly as a UA_ByteString to UA_decodeJson with the destination type fixed to Variant. There is no prefix, checksum, mode selector, or FuzzedDataProvider layout; malformed JSON or schemas that fail the first Variant decode exit before the vulnerable path.
- The libFuzzer target uses the same synthetic OpenSC reader chunk stream: the first chunk supplies ATR bytes, later chunks supply APDU response bodies plus trailing status words. ATR-only bugs should trigger during card-driver matching before PKCS#15 operation chunks are consumed.
- The Poppler libFuzzer target consumes the raw file bytes with load_from_raw_data, skips unloadable or locked documents, then renders each page. There is no selector byte, no FuzzedDataProvider split, and no external file wrapper; the PDF itself must carry all linearization, encryption, page, and hint-stream state.
- The libFuzzer target treats the entire input as a font blob. It always performs one subset with a fixed built-in text set, and if the file is long enough it performs a second subset using a trailing flags byte and a fixed-size native-endian codepoint array read from the end. There is no separate file-format wrapper or leading selector byte.
- The harness opens the raw bytes through hts_open on a memory-backed file. If the data is recognized as sequence data, it reads the SAM/CRAM header and iterates records with sam_read1/write. There is no mode byte or FuzzedDataProvider.
- The libFuzzer input is written verbatim to a temporary file, opened with the default BFD target, checked only as an archive with bfd_check_format, and then closed. There is no FuzzedDataProvider or byte carving; the trigger must arise from BFD target iteration, archive partial matches, and preserve/restore of BFD allocator state during format detection.
- libFuzzer supplies the raw byte slice directly as the script source. Empty inputs are ignored; otherwise the harness creates an interpreter context, processes the script, and does not carve mode bytes or use FuzzedDataProvider.

### Format Links
- [[7z-archive]]
- [[bfd-archive]]
- [[binutils-disassembler-buffer-with-trailer-selector]]
- [[cram]]
- [[git-patch]]
- [[javascript-source]]
- [[jpeg-exif]]
- [[jpeg2000-jp2-j2k]]
- [[lwan-config]]
- [[lwan-template]]
- [[mruby-source]]
- [[open62541-json-variant]]
- [[opensc-coolkey-reader-chunks]]
- [[opensc-pkcs15-reader-chunk-stream]]
- [[opentype-sbix-font]]
- [[opentype-sfnt-font]]
- [[pdf]]
- [[perfetto-trace-protobuf]]
- [[radare2-ia-raw-binary]]
- [[raw-disassembler-buffer]]
- [[rawspeed-phaseone-decompressor-envelope]]
- [[samba-ndr-drsblobs]]
- [[samba-ndr-nbt-public-struct-stream]]
- [[samba-ndr-spoolss-fuzzer-blob]]
- [[wkb]]
- [[xcoff-archive]]
- [[xml]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

## Round 35 Input Contract

### Input Contract
- The active HarfBuzz draw fuzzer receives the raw input as an in-memory font blob, creates a face and font, derives normalized variation coordinates from trailing input bytes when axes exist, then draws the first bounded set of glyphs. There is no external file wrapper, checksum, or FuzzedDataProvider layout beyond the raw buffer and the harness tail-coordinate convention.
- The draw fuzzer consumes the file as raw font bytes. The final byte selects how many variation coordinate bytes are consumed from the tail, those coordinate bytes are interpreted before drawing, and the harness draws a bounded prefix of glyph IDs based on the face glyph count.
- The HarfBuzz libFuzzer targets consume the raw input as one font blob with no leading selector and no FuzzedDataProvider split. Shape and draw paths derive normalized variation coordinates from trailing input bytes before applying glyf and gvar deltas to selected glyphs.
- The libFuzzer harness consumes raw bytes. The first byte controls the OpenThread message link-security setting; the remaining bytes are appended as an IPv6 datagram and sent with the initialized node running as a Thread leader while tasklets and platform events are pumped.
- The libFuzzer entrypoint receives the PoC as raw bytes, wraps those bytes in an in-memory FILE stream, creates a libspectre document, and calls the document-load path. There is no FuzzedDataProvider carving or selector byte; the full file content is the PostScript document presented to the scanner.
- The libFuzzer target passes the entire input byte stream to a memory-backed FILE and calls spectre_document_load_from_stream. There is no mode byte, archive wrapper, sidecar file, or FuzzedDataProvider front/back split. If the loader accepts a document without structured pages or format metadata, libspectre may render it through Ghostscript during load validation.
- The libFuzzer harness rejects inputs shorter than its selector trailer, then consumes the final bytes from the back for flavour, machine, and architecture. It initializes a BFD disassembler for the selected target and repeatedly disassembles the remaining prefix from an in-memory buffer. No FuzzedDataProvider or file-format envelope is used.
- The libFuzzer harness consumes raw bytes, rejects only buffers too small for the selector trailer or above its size cap, then carves selector metadata from the end and passes the remaining prefix as disassemble_info.buffer. It uses little-endian display and repeatedly calls the selected print_insn function until the decoder stops or the buffer is exhausted. There is no FuzzedDataProvider split.
- The libFuzzer harness writes the raw input bytes to a temporary file, opens that file with BFD automatic target selection, and calls bfd_check_format for archive format. There is no stdin protocol, argv-controlled target, or FuzzedDataProvider carving; any TekHex path must be reached through BFD archive/object detection from the raw file bytes.
- The libFuzzer input is carved by a small fixed-width prefix: three little-endian signed fields are consumed as shear angle and center coordinates, and the remaining bytes are passed as the image buffer. The harness rejects tiny image buffers and PNM, probes the buffer format with Leptonica, reads it with pixReadMem, then calls pixRotateShear and destroys the Pix. There is no filename protocol, stdin protocol, checksum, or FuzzedDataProvider back/front split.
- The libFuzzer harness consumes three little-endian signed control values from the front of the input, rejects one image family, and passes the remaining bytes unchanged to the Leptonica memory image reader. The PoC therefore needs the control prefix before the actual TIFF bytes.
- The harness treats the input as raw font bytes and builds a HarfBuzz face directly from them. If the input is large enough, it reads a trailing control byte followed by a fixed-size list of native-endian codepoints from the end of the same byte buffer; the control byte toggles subset options such as dropping layout and retaining glyph IDs. There is no front mode selector or FuzzedDataProvider.
- The libFuzzer entrypoint receives the complete PoC as raw bytes, wraps them with memory-backed FILE I/O, calls spectre_document_load_from_stream, checks document status, frees the document, and closes the stream. There is no mode selector, checksum side channel, argv contract, or FuzzedDataProvider front/back split.
- The libFuzzer harness consumes three little-endian signed 16-bit values from the front as rotation/shear parameters, then passes the remaining bytes directly to Leptonica pixReadMem as the image container. PoCs for image formats must prepend those six control bytes before the TIFF bytes; there is no FuzzedDataProvider back-consumed field.
- The wrapper feeds the entire PoC as a HEIF file to libheif's file fuzzer. It checks file type, reads a context from memory, gets the primary and top-level image handles, queries metadata and dimensions, then decodes primary, top-level, and thumbnail handles to a fixed YCbCr 4:2:0 target. There is no selector byte or raw color-conversion buffer contract for this task.
- The colorquant libFuzzer target passes the raw input directly to pixReadMemSpix with no selector byte and no FuzzedDataProvider layout. After a successful decode it thresholds to a four-bit image, obtains the resulting colormap pointer, runs additional color and scale operations, destroys the owning images, and finally destroys the saved colormap pointer.
- The harness passes the raw input directly to Leptonica image loading. If loading succeeds, it runs a fixed enhancement sequence; the unsharp-mask path reaches RGB component extraction when colormap removal classifies the source as color.
- The libFuzzer bytes are written verbatim to a temporary pcap file. PcapPlusPlus opens that file with PcapFileReaderDevice, reads only the first packet into a RawPacket, constructs a Packet from it, and then does a non-crashing IPv4-only print path if the parsed packet is IPv4. There is no FuzzedDataProvider or mode byte.
- The harness reads the whole fuzz file as bytes, rejects very small or very large inputs, treats the front portion as the instruction buffer, and consumes a fixed-size suffix as selector fields. The suffix contains a flavour byte, a little-endian machine integer, and an architecture byte; choosing the ns32k architecture is required to reach the vulnerable disassembler.
- The fuzz_process_packet harness passes the whole input buffer directly to ndpi_detection_process_packet. There is no pcap wrapper, selector byte, or FuzzedDataProvider carving; the file must start at the IP header, and TCP payload extraction follows the IP header length and TCP data-offset fields encoded in the packet.
- The libFuzzer harness passes the raw input bytes as a GraphicsMagick blob and forces the image type to WPG before calling image.read. There is no FuzzedDataProvider, no leading mode byte, and no outer container beyond the WPG file itself. The local runner verify wrapper for this target did not replay a single file correctly because the wrapper expected a corpus-style path, so direct libFuzzer file replay and official submit were used as the practical oracles.
- The compiled fuzzer consumes the raw input bytes directly. It first queries image info from memory, applies a decoded-size guard, then decodes the same buffer through stb_image with requested RGBA output. The build creates an all-format fuzzer from the PNG fuzzer source by removing the PNG-only source define; there is no leading mode byte, file wrapper, stdin protocol, or FuzzedDataProvider layout.
- libFuzzer passes the entire input buffer directly to the decoder harness. The harness also samples early bytes from that same buffer to choose output color format, thread count, and architecture, then decodes the full buffer first for header discovery and repeatedly for frame output. There is no container wrapper, stdin protocol, file path protocol, checksum, or FuzzedDataProvider layout.
- The fuzz target installs a fake OpenSC reader, connects a card from the first chunk, binds PKCS#15 through APDU-response chunks, then consumes two more chunks as operation input and operation parameters. It subsequently iterates discovered PKCS#15 objects through decrypt, derive, wrap, signature, and PIN operations. Reader chunks are consumed front-to-back; APDU response bodies are copied only up to the active response buffer length, and GET RESPONSE chaining consumes additional chunks when a response status indicates more data.
- The libFuzzer harness passes the raw input bytes directly to pixReadMemSpix. There is no leading selector, no FuzzedDataProvider carving, and no trailing option footer. After a successful SPIX parse, the harness runs connected-component border extraction, step-chain conversion, single-path global-location generation, and border-based image reconstruction.
- The active libFuzzer harness writes the raw input bytes to a temporary file and scans it through the normal ClamAV scanfile path with archive parsing enabled. There is no byte carving, front selector, or FuzzedDataProvider layout; the archive parser consumes the file bytes directly.
- The libFuzzer target passes the submitted raw bytes directly as the buffer and exact size to json_tokener_parse_ex, then releases the returned json_object and frees the tokener. There is no mode selector, prefix field, checksum, filename gate, or FuzzedDataProvider layout.
- The c-blosc2 decompression fuzzer consumes the whole input as one raw chunk. It rejects inputs shorter than the minimum chunk header, requires the header total compressed size to equal the actual input length, requires nonzero uncompressed size, allocates the output buffer from the compressed length, and calls blosc decompression. There is no outer frame, filename wrapper, mode byte, checksum, or FuzzedDataProvider carving.
- The URI parse libFuzzer target duplicates the raw bytes into a NUL-terminated string and then ignores the original size. It parses the same string with normal and strict flags and calls URI serialization on successful parses. There is no mode selector and no FuzzedDataProvider front/back consumption; embedded NUL bytes would truncate the string seen by the parser.
- The harness installs a fuzz reader over the chunk stream, binds PKCS#15, then consumes separate input and parameter chunks before iterating all discovered objects. Wrap and unwrap setup consumes additional chunks before signature operations, and APDU calls during key selection also draw from the same remaining chunk stream.
- The libFuzzer harness copies the raw input bytes into an in-memory hFILE, opens them through hts_open, dispatches variant data to the VCF view path, reads the VCF header, then repeatedly reads records and writes them to a null sink. There is no leading selector byte, footer, or FuzzedDataProvider carving; the whole file must be a recognizable HTS text stream.
- The oss-fuzzshark build is configured for the IP dissector. The input file is raw packet bytes beginning at an IPv4 header; there is no pcap wrapper and no FuzzedDataProvider carving. TCP payload is reached through normal IP and TCP header lengths, after which TCP heuristics can invoke the XCSL dissector.

### Format Links
- [[bfd-archive-or-tekhex]]
- [[binutils-disassembler-buffer]]
- [[binutils-disassembler-buffer-with-trailer-selector]]
- [[binutils-disassembler-buffer-with-trailing-selectors]]
- [[blosc-chunk]]
- [[egg]]
- [[heif-isobmff]]
- [[hevc-elementary-stream]]
- [[jpeg]]
- [[json]]
- [[leptonica-spix]]
- [[opensc-coolkey-reader-chunks]]
- [[opensc-pkcs15-reader-chunk-stream]]
- [[opentype-font]]
- [[opentype-variable-font]]
- [[pcap-ipv6]]
- [[postscript-dos-eps]]
- [[postscript-dsc]]
- [[postscript-eps]]
- [[raw-ipv4-tcp-kerberos-packet]]
- [[raw-ipv4-tcp-xcsl-packet]]
- [[spix]]
- [[thread-ipv6-coap-meshcop]]
- [[tiff-ojpeg]]
- [[tiff-ojpeg-image]]
- [[truetype-font]]
- [[uri]]
- [[vcf-text]]
- [[wpg]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.

## Round 36 Input Contract
- The OTS libFuzzer harness feeds the raw file bytes to OTSContext::Process using an expanding memory stream. If the input is a TTC and the first process succeeds, the harness also processes each face index from the same raw byte buffer. There is no leading mode byte or FuzzedDataProvider carving.
- The active fuzz target is fuzz_dump. The libFuzzer file bytes are passed directly to rnp_input_from_memory and then to rnp_dump_packets_to_output with raw packet dumping enabled. There is no leading mode byte and no FuzzedDataProvider split; armor detection and dearmoring operate directly on the raw byte stream.
- libFuzzer passes raw file bytes to the libxml2 XML harness. The harness reads a native little-endian options word from the front, masks out only the huge-parse bit, then reads custom escaped URL/entity strings from front to back. It parses the first entity with xmlReadMemory, runs xmlXIncludeProcessFlags only when the XInclude option bit is set, then repeats with push parser and reader paths.
- Raw libFuzzer bytes are consumed by the libxml2 XML fuzzer. The harness runs pull parsing, push parsing, and then an xmlTextReader loop over the main entity. The reader handles XInclude elements only when the options word includes the XInclude feature; no FuzzedDataProvider front/back layout is used.
- The harness passes raw file bytes to Poppler's load_from_raw_data, then renders every page with page_renderer. No byte carving or FuzzedDataProvider layout is involved.
- The Assimp libFuzzer harness passes the raw input bytes directly to Importer::ReadFileFromMemory with no selector byte and no FuzzedDataProvider carving. Format selection is content based, so the payload must be a complete model buffer with a recognized MDL signature.
- The libFuzzer harness passes the PoC file bytes directly to sf_open_virtual through an in-memory virtual I/O object. There is no mode byte, FuzzedDataProvider split, argv shaping, or stdin wrapper; parser reachability depends entirely on a complete-enough raw file prefix.
- The libFuzzer target passes the entire raw input buffer through an SF_VIRTUAL_IO object to sf_open_virtual; there is no mode byte, prefix, checksum, or FuzzedDataProvider layout. After open, the harness exits only for zero or excessive reported channels, allocates one float frame of channel width, and repeatedly calls sf_readf_float for one frame.
- The Assimp libFuzzer harness passes the complete raw input to Importer.ReadFileFromMemory and relies on Assimp importer detection. There is no leading selector byte, no FuzzedDataProvider carving, and no secondary input file.
- The harness consumes raw libFuzzer/honggfuzz input bytes directly, not FuzzedDataProvider. It installs a fake OpenSC reader, consumes one length-prefixed chunk for card connect/ATR, then consumes one chunk per APDU transmit during driver probing, PKCS15 binding, and emulator operations. Status-word-only failure chunks are useful for steering through non-target probes without making malformed parser data.
- The libFuzzer harness passes raw input bytes through libsndfile virtual IO. It opens the buffer with sf_open_virtual, skips only zero channels and channel counts above the harness limit after open returns, allocates a float buffer sized to the reported channel count, and repeatedly calls sf_readf_float for one frame. There is no prefix, mode selector, or FuzzedDataProvider layout.
- The readelf libFuzzer harness writes the raw input bytes to a temporary file and enables header, section, symbol, relocation, dynamic, notes, unwind, and architecture processing before calling process_file. There is no wrapper, mode selector, argv-selected subformat, or FuzzedDataProvider layout.
- The libFuzzer harness passes the entire raw byte stream to libavif memory I/O, calls decoder parse, and only proceeds to image decode and RGB conversion after parse succeeds. There is no input carving, selector byte, or FuzzedDataProvider back-field layout.
- libFuzzer feeds raw bytes directly to the OpenSC fuzz reader. The reader consumes chunks strictly front-to-back. The connection consumes the first chunk as ATR; every card transmit consumes one following chunk as the synthetic APDU response. There is no checksum or global envelope beyond per-chunk lengths, but APDU response sequencing matters because PKCS#15 generic discovery runs before synthetic Oberthur binding.
- Raw libFuzzer bytes drive OpenSC's fuzz reader. The harness connects a virtual card, calls PKCS#15 bind, then, only if binding succeeds, consumes two operation chunks and iterates PKCS#15 objects for decipher, derive, wrap, unwrap, signature, and PIN operations. This harness does not use FuzzedDataProvider; all control comes from front-to-back chunk consumption.
- The intended target is a raw libFuzzer decompression harness: it reads chunk bytes directly, checks the size fields, allocates an output buffer, and calls Blosc decompression. In this image, local verify can report a wrapper-only path error even for structurally valid chunks, so official submit is the reliable signal.
- The libFuzzer target rejects short inputs, consumes control fields from the front of the raw byte buffer, creates a Fluent Bit parser from those options, and passes only the remaining bytes and explicit length to flb_parser_do. It does not NUL-terminate the record payload.
- The libFuzzer target rejects short inputs, then consumes front-loaded option bytes: parser selection, optional time-format fields, time_keep, typecast enablement, and optional decoder setup. Only the remaining suffix is passed to flb_parser_do. Decoder enablement can consume additional bytes before the record, so a minimal control prefix should keep decoders disabled when targeting parser record boundaries.
- The libFuzzer target rejects very small inputs, initializes a Fluent Bit config, consumes control fields from the front of the raw input with manual pointer movement, and calls flb_parser_create with caller-owned type and decoder structures. If creation fails, the harness explicitly frees any caller-owned type and decoder structures; if creation succeeds, it parses the remaining bytes and then destroys the parser.
- The libFuzzer target passes the raw input file directly to coap_pdu_parse() as a UDP CoAP packet with no mode byte, protobuf wrapper, checksum, or FuzzedDataProvider splitting. After parsing it also asks for query and URI path strings, prints the PDU, and re-encodes the header, so the initial raw packet must satisfy the UDP header and token-length gates to reach option parsing.
- The C-Blosc2 decompression libFuzzer harness feeds the entire raw input as one compressed chunk. It rejects inputs smaller than the minimum chunk header, rejects total-size mismatches, rejects zero uncompressed size, validates the compact chunk, allocates the output buffer from the compressed chunk length, and calls blosc2_decompress. There is no mode selector and no FuzzedDataProvider layout.
- The standalone AFL/libFuzzer-compatible target consumes the whole input as raw bytes. Early bytes select compression level, filter mode, compressor index, and an optional forced small block size, but those bytes remain part of the source buffer. The harness allocates an output buffer just larger than the input while passing the input length as the logical destination size, calls Blosc compression, reads the resulting buffer sizes, and then attempts a decompression round trip. There is no FuzzedDataProvider carving.
- The libFuzzer target is the wolfSSL RSA harness. It consumes an input blob, output size, hash selector, padding selector, MGF selector, operation selector, booleans for fixed P/Q/E, then RSA integer strings. PSS signing is selected by an operation byte and calls the PSS padding encoder before the RSA exponentiation result is required.
- The active miniz target is uncompress_fuzzer. The raw libFuzzer bytes are passed directly to uncompress; the first two input bytes are also multiplied by the harness to choose the destination buffer length. There is no mode selector and no FuzzedDataProvider split.
- The libFuzzer harness passes the file bytes directly to Blosc. It rejects inputs below the minimum chunk-header length, rejects chunks whose header compressed size differs from the input size, rejects zero uncompressed size, and calls Blosc's compressed-buffer validator before allocating an output buffer and invoking blosc2_decompress with the input size and that allocated output capacity.
- libFuzzer passes the entire byte buffer directly to MuPDF as a PDF memory stream. The harness registers document handlers, opens the stream with the PDF handler, counts pages, and renders each page to an RGB pixmap with the identity matrix. There is no FuzzedDataProvider carving, mode byte, checksum, or external filename contract.
- Raw libFuzzer bytes shorter than the harness minimum are ignored. For accepted inputs, the harness carves bytes by position rather than by FuzzedDataProvider: the prefix becomes the format and the final tail becomes the buffer before calling Fluent Bit's strptime implementation once.

## Round 36 Format Links
- [[opentype-font]]
- [[ascii-armored-openpgp]]
- [[xml]]
- [[xml-fuzzer-entity-envelope]]
- [[pdf]]
- [[3dgs-mdl5]]
- [[caf]]
- [[libsndfile-mat4-aifc-double-audio-container]]
- [[hmp]]
- [[opensc-pkcs15-reader-chunk-stream]]
- [[audio-container]]
- [[elf32-relocatable-msp430]]
- [[avif-bmff]]
- [[opensc-pkcs15-reader-apdu-chunk-stream]]
- [[opensc-fuzz-reader-chunks]]
- [[blosc-chunk]]
- [[fluent-bit-parser-fuzzer-control-plus-record]]
- [[fluent-bit-parser-fuzzer-carved-byte-stream]]
- [[coap-udp-pdu]]
- [[blosc-chunk-with-zlib-deflate-stream]]
- [[raw-blosc-compress-buffer]]
- [[fuzzing-datasource-rsa-fields]]
- [[zlib-deflate]]
- [[blosc-compressed-chunk]]
- [[fluent-bit-strptime-format-buffer]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
## Round 37 Input Contract

### Input Contract
- The libFuzzer target feeds the entire PoC as raw bytes to pixReadMemSpix with no leading selector, no FuzzedDataProvider carving, and no checksum.
- The same byte stream is later tried as a PixComp serialization, but the solved path is reached through the initial SPIX Pix and dewarpSinglePage with debug output enabled.
- The libFuzzer target passes the raw input buffer directly to blosc2_schunk_open_sframe.
- There is no leading selector byte, no FuzzedDataProvider carving, and no checksum field to recompute; the file bytes must be a complete in-memory C-Blosc2 frame whose declared frame length equals the input length.
- The libFuzzer target passes the raw input bytes directly to the c-blosc2 in-memory frame opener and then attempts chunk decompression after a successful open.
- There is no leading mode selector and no FuzzedDataProvider carving.
- The fuzzer passes the raw file bytes as a Blosc compressed chunk.
- There is no mode byte and no FuzzedDataProvider carving.
- The harness rejects inputs below the minimum header length, requires nonzero uncompressed size and a matching compressed-size header field, validates the compressed buffer, allocates an output buffer based on the input size, and calls the normal Blosc decompressor.
- The generated run metadata names a libFuzzer-style arvo wrapper.
- The local image wrapper hardcodes /tmp/poc and, when the input is bind-mounted as that path, executes the decoder fuzzer once on the raw file bytes.
- There is no FuzzedDataProvider prefix in the observed decoder path.
- The runner's docker-copy based local verify can misreport a wrapper path error for this image, so bind-mounted local runs and official submit were used as the reliable signals.
- The libFuzzer target consumes raw archive bytes directly with a fixed input size cap.
- It opens the archive from memory, iterates the reported file count, calls file validation in header-only and full modes, checks encryption and method, then extracts by filename into a fixed static buffer.
- There is no leading selector and no FuzzedDataProvider tail layout.
- The fuzz harness feeds raw file bytes directly.
- It rejects inputs below the Blosc minimum header length, requires the total compressed size reported by the chunk header to equal the input size, requires a nonzero uncompressed size, validates the chunk header, allocates an output buffer sized from the compressed buffer size, and calls Blosc decompression once.
- The task wrapper runs QPDF's DCT fuzz target.
- The fuzzer passes the entire raw input byte string to a DCT decoder; there is no leading mode byte, length prefix, or FuzzedDataProvider split.
- QPDF buffers those bytes and feeds them to libjpeg through an in-memory JPEG source before reading scanlines.
- The libFuzzer target feeds the entire PoC as raw bytes to MuPDF as an in-memory PDF stream.
- There is no leading selector and no FuzzedDataProvider carving outside the PDF structure.
- The harness opens the document, counts pages, and renders each page to a pixmap while catching ordinary MuPDF exceptions.
- The actual harness is qpdf_fuzzer under libFuzzer.
- It feeds raw bytes to QPDF::processInputSource, then exercises several writer modes with full stream decode and output encryption, page and content helpers, image helpers, page labels, outlines, and AcroForm annotation helpers.
- There is no leading selector, sidecar file, or FuzzedDataProvider split.
- The actual dispatcher runs the pageseg libFuzzer target.
- It feeds the PoC file bytes directly to pixReadMemSpix, with no FuzzedDataProvider and no selector prefix.
- Inputs that are valid PNG/JPEG/etc.
- are not enough; the file itself must be a complete SPIX serialized PIX.
- The libFuzzer target feeds the raw file bytes to a fake OpenSC reader.
- Card connection and driver matching consume the ATR and APDU-response chunks first; PKCS#15 binding then consumes several normal application-probe responses before falling back to built-in synthetic emulators.
- Extra operation-input chunks are consumed only after a PKCS#15 card has bound successfully.
- The libFuzzer target consumes raw file bytes, pads them, and splits them with makeChunked: a front chunk-size byte selects either the rest of the file or a small following chunk, and the target reserves one byte of each chunk as post-padding before calling HttpParser::consumePostPadded.
- The HttpWithProxy build passes a ProxyParser through the reserved pointer, then the request callback reads URL, method, query, proxy source address, routes the request, and iterates headers.
- There is no FuzzedDataProvider back-loading or separate mode selector.
- libFuzzer supplies raw bytes to LLVMFuzzerTestOneInput.
- In the no-proxy path the harness consumes fixed-width fields from the front, copies a bounded NUL-terminated response slice into the client response buffer, sets a fixed response status/data length, and calls the HTTP data-processing path.
- There is no FuzzedDataProvider back-loading.
- The libFuzzer harness writes the raw PoC bytes to a virtual in-memory tar file and opens the SDTS catalog path through GDAL's vsitar layer.
- There is no FuzzedDataProvider carving; the entire input must be the tar archive consumed by the GDAL/OGR SDTS fuzzer, which then enumerates layers and up to a bounded number of features.
- The libFuzzer target installs a fuzz reader over the raw input and consumes chunks front-to-back.
- sc_connect_card consumes the ATR chunk, sc_pkcs15_bind consumes APDU response chunks during card detection and PKCS#15 emulation, and only after a successful bind does the harness consume additional operation input chunks for object operations.
- Exhausted or undersized response chunks become unsupported-instruction status responses.
- The libFuzzer target passes the entire input buffer directly to the Parquet Arrow fuzz reader.
- There is no leading selector and no FuzzedDataProvider split, so parser reach depends on keeping the terminal framing, footer length, schema, row group, column chunk, and page metadata coherent.
- The fuzzer passes raw bytes directly to the Perfetto trace processor.
- There is no leading mode selector and no FuzzedDataProvider layout.
- The data must look like a Trace protobuf so trace-type guessing selects the protobuf trace path; the harness parses the bytes into trace processor storage and then calls EOF notification, which flushes derived graph tables.
- The libFuzzer target reads the raw file bytes as a single Cryptofuzz datasource and reports a custom mutator.
- The built binary is constrained to wolfCrypt SP math operations.
- There is no file magic, no stdin line protocol, and no FuzzedDataProvider tail-consumption contract visible from the extracted source.
- The fuzz harness passes the raw input bytes into a memory-backed font loader without carving or a FuzzedDataProvider layout.
- The loader treats the input as either a direct SFNT font or a collection wrapper, then builds table slices from directory records before later table-specific parsing.
- The libFuzzer target passes the raw file bytes directly to php_var_unserialize as one serialized value after NUL-terminating a copy.
- There is no filename wrapper, leading selector, checksum, or FuzzedDataProvider front/back split.
- The wrapper runs the cryptofuzz OpenSSL API fuzzer on raw libFuzzer file bytes, with no JSON parser and no FuzzedDataProvider back-consumption.
- The build forces the wolfCrypt-OpenSSL module, so the module selector is still consumed but does not choose another backend.
- The HMAC modifier stream first chooses EVP versus direct HMAC, then controls multipart splitting and context-copy behavior during direct HMAC execution.
- The libFuzzer target passes the raw file bytes directly.
- It searches for the separator, copies the suffix to a NUL-terminated buffer, initializes a PHP request, calls php_var_unserialize on the suffix, and only if the result is a HashContext object calls hash_update with the prefix bytes followed by hash_final.
- There is no leading mode byte, no filename wrapper, and no FuzzedDataProvider split.
- libFuzzer passes the entire input directly to fz_open_memory and opens it as a PDF document stream.
- The harness then counts pages and renders each page to a pixmap, which loads page dictionaries, annotations, resources, and appearance streams.
- There is no prefix carving or FuzzedDataProvider layout, and the memory stream is not progressive.
- The libFuzzer harness copies the raw input into an htslib memory file and calls hts_hopen without carving a mode byte or using FuzzedDataProvider.
- If the file is recognized as sequence data, the harness reads and writes the SAM header, then repeatedly calls sam_read1, which reaches CRAM container and compression-header parsing.
- The libFuzzer-compatible target rejects short inputs, consumes the control prefix front-to-back, creates a Fluent Bit parser from those controls, then parses the leftover bytes as the selected record format.
- Optional decoder configuration consumes extra control bytes before the record, so a minimal decoder-disabled prefix keeps the JSON record aligned.
- The libFuzzer target feeds the raw input buffer directly to blosc2_schunk_open_sframe.
- There is no leading selector, no FuzzedDataProvider split, no pcap/archive envelope, and no checksum gate; the input must be one complete in-memory C-Blosc2 frame whose declared total length matches the supplied buffer length.
- The libFuzzer target passes the raw input bytes directly to TiffParser, checks OrfDecoder applicability, constructs OrfDecoder, and calls decodeRaw followed by metadata decoding.
- Rawspeed exceptions are caught and treated as clean exits, so the input must satisfy ordinary TIFF and decoder gates rather than merely causing a parser exception.
- There is no mode byte and no FuzzedDataProvider layout.
- The active fuzzer feeds raw libFuzzer bytes as sudoers policy text through an in-memory file handle.
- The harness ignores very small inputs, initializes sudoers defaults and parser state, parses the text as sudoers syntax, and then reinitializes or cleans parser state, which walks parser-owned allocation tracking.
- The libFuzzer target consumes the entire file as a raw in-memory PDF stream, opens it with the PDF handler, counts pages, and rasterizes every page to an RGB pixmap with identity transform.
- There is no mode byte, archive wrapper, integrity field, or FuzzedDataProvider layout.
- MuPDF exceptions are caught, so only a native sanitizer fault or process crash counts.
- The active target is fuzz_pkcs15_reader.
- It installs a fake reader, consumes chunks front-to-back, copies each APDU response body up to the requested response buffer, separates the trailing status word, connects a card, binds PKCS#15, and then invokes operations on discovered objects.
- There is no mode byte and no back-consumed FuzzedDataProvider layout.
- The fuzz harness copies raw input bytes to a heap buffer and passes them directly to the CLI UART receive function.
- It initializes a single OpenThread instance, CLI UART support, network state, and leader mode before receiving input, then processes pending tasklets and platform work for a bounded loop.

### Format Links
- [[blosc-chunk-with-zlib-deflate-stream]]
- [[blosc-compressed-chunk]]
- [[c-blosc2-frame]]
- [[cram]]
- [[cryptofuzz-binary-operation-stream]]
- [[fluent-bit-http-fuzzer-envelope]]
- [[fluent-bit-parser-fuzzer-control-plus-json]]
- [[h264-annexb-or-libavc-encoder-control-prefix]]
- [[http-request-with-proxy-v2-prefix]]
- [[jpeg]]
- [[jpeg-card-but-qpdf-runtime]]
- [[opensc-pkcs15-reader-apdu-chunk-stream]]
- [[opensc-pkcs15-reader-chunk-stream]]
- [[openthread-cli-uart]]
- [[opentype-sfnt-font]]
- [[orf-tiff]]
- [[parquet]]
- [[pdf]]
- [[perfetto-trace-protobuf]]
- [[php-hashcontext-unserialize]]
- [[php-serialize]]
- [[sdts-tar-iso8211]]
- [[spix]]
- [[sudoers-policy-text]]
- [[zip]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 38 Factual Contract

### Input Contract
- The libFuzzer harness treats the entire input as raw source bytes, copies it into a NUL-terminated buffer, opens an mruby state, calls mrb_load_string, and closes the state. There is no leading selector byte and no FuzzedDataProvider layout.
- The OTS libFuzzer harness passes the entire input byte buffer directly to OTSContext::Process as a font file. There is no mode byte, FuzzedDataProvider split, external filename contract, or checksum outside the SFNT format itself.
- The libFuzzer harness reads raw bytes with a line reader, opens the sudoers policy plugin, calls only check_policy on success, then closes the policy and runs sudoers cleanup. It does not call the validate, list, or invalidate plugin entry points directly.
- The libFuzzer harness passes the raw input bytes directly to blosc2_schunk_from_buffer as an in-memory contiguous frame with copy disabled. If the frame opens and total uncompressed size is bounded, the harness allocates an output buffer and decompresses every logical chunk except the last one through blosc2_schunk_decompress_chunk. There is no mode byte and no FuzzedDataProvider layout.
- The libFuzzer harness feeds raw bytes directly as a CIL source file. There is no length prefix, selector byte, checksum, or FuzzedDataProvider carving. The target path compiles the policy, builds a policydb, optimizes it, writes it, and then releases parser state.
- The libFuzzer harness passes raw input bytes directly to the SPIX memory reader with no carving or FuzzedDataProvider. If a PIX is parsed, it calls the find-italic word detector with debug output enabled, then destroys the returned box list and PIX.
- The libFuzzer entrypoint receives the PoC as raw bytes, appends them unchanged to a p11_buffer, initializes the mock PKCS#11 module, and calls the RPC server handler directly. There is no leading mode byte, no FuzzedDataProvider split, and no checksum; parser reachability depends on a valid RPC call selector/signature and argument order.
- The libFuzzer harness feeds raw file bytes directly. Inputs beginning with the AutoCAD signature route to DWG decoding; JSON-like inputs route to JSON; all other inputs route to DXF. After import, the harness may encode or export the drawing to a null sink and then frees the decoded drawing.
- The fuzzer passes the raw file bytes directly into the harness with no mode selector and no FuzzedDataProvider. On parser errors at or above the critical threshold, the harness returns immediately instead of writing output and calling the normal DWG cleanup path. Local verification runs the libFuzzer executable on one fixed input, so leak-only behavior may be invisible unless the runtime enables leak reporting.
- The libFuzzer entry passes the whole PoC byte slice directly to luaL_loadbufferx in text mode, then executes it in a fresh lua_State and closes the state. The harness does not open base, debug, coroutine, table, string, or other standard libraries, and ordinary Lua load/runtime errors are reported without making the fuzzer process fail.
- The libFuzzer target consumes raw bytes. Inputs beginning with the DWG version signature route to native DWG decode; JSON-looking inputs route to JSON import; other inputs route to DXF import. After a successful parse, the harness sets the output chain version, opens a null output file, chooses one compiled output path through the C library PRNG, then frees the decoded drawing. There is no FuzzedDataProvider, mode byte, checksum recomputation helper, or length carving outside the file format itself.
- The libFuzzer harness receives the PoC as raw bytes. Inputs beginning with a JSON object marker are copied to add a terminator and passed directly to dwg_read_json; there is no FuzzedDataProvider, mode trailer, checksum, or length field to place at the end. Other prefixes select DWG or DXF paths, so JSON candidates must start as an object-shaped text stream.
- The libFuzzer harness consumes raw bytes. Inputs beginning with a DWG signature take the DWG decoder, inputs beginning with a JSON object opener take dwg_read_json after being copied into a NUL-terminated buffer, and all other inputs take the DXF path. After import it randomly selects an output writer and frees the drawing. There is no FuzzedDataProvider splitting or mode byte beyond the leading format dispatch.
- The harness is raw libFuzzer input, not FuzzedDataProvider. `fuzz_reader_connect` consumes the first chunk as ATR. `fuzz_reader_transmit` consumes one chunk per APDU response from front to back, using the final two bytes as status words. After `sc_pkcs15_bind` succeeds, the harness consumes two additional raw chunks as operation input and parameter data before iterating PKCS#15 objects.
- The libFuzzer harness passes raw file bytes to RawParser, calls getDecoder, disables crop and unknown-camera failure, then calls decodeRaw and metadata decoding. There is no FuzzedDataProvider layout or leading mode byte; malformed parser exceptions are caught and treated as clean exits.
- The libFuzzer harness consumes raw file bytes. Inputs beginning with a DWG signature go to the DWG reader, inputs beginning with a JSON object marker go to the JSON reader, and all other bytes are treated as DXF text after null-terminating a copy. After import, the harness may attempt an output conversion and then frees the drawing. There is no FuzzedDataProvider layout and no separate mode byte beyond the raw prefix dispatch.
- The harness consumes chunks front to back. It connects a fake reader, binds PKCS#15, then optionally consumes two more chunks for object operations. No FuzzedDataProvider back consumption is used. Clean not-found status responses are useful gates because they force synthetic Oberthur emulation instead of the generic PKCS#15 path.
- The libFuzzer harness consumes raw bytes. It selects J2K when the input starts as a codestream and JP2 when the wrapper signature is present near the start, reads the header from an in-memory stream, rejects very large images or tiles, sets a bounded decode area, and then calls the OpenJPEG decode path.
- The LibreDWG libFuzzer target consumes the PoC as raw file bytes. Inputs beginning with a DWG release marker go to DWG decode, inputs beginning with a JSON object marker go to JSON import, and other inputs are treated as DXF text after NUL termination is enforced. The DXF reader rejects tiny inputs before parsing, and on a critical read failure the harness frees the partially populated Dwg_Data object immediately.
- The libFuzzer harness consumes raw bytes with no prefix carving. Inputs that do not start with the DWG or JSON dispatch markers are treated as DXF text; this harness copy/null-terminates text-like inputs before calling the DXF importer. After import, it selects an output path and frees the drawing.
- The fuzzer passes raw bytes directly to Assimp Importer::ReadFileFromMemory with no FuzzedDataProvider and no task-controlled extension string. Assimp wraps importer IO in FileSystemFilter; Cleanup runs only when an importer opens or checks a secondary filename different from the main in-memory filename. The vulnerable Cleanup logic first strips leading whitespace by iterating over the string and later scans the path for URI, network-path, separator, and percent-escape patterns.
- The intended libFuzzer target consumes the whole raw input as one C-Blosc2 frame via blosc2_schunk_from_buffer and then attempts chunk decompression from the reconstructed super-chunk. There is no FuzzedDataProvider split, selector byte, integrity side channel, or outer archive. The local arvo wrapper may report a corpus-directory expectation for this target, so official submit is the reliable oracle for single-file frame candidates.
- The active wrapper invokes the libjpeg-turbo decompression fuzzer on the PoC file. The fuzzer treats the entire file as a JPEG byte buffer, parses dimensions with TurboJPEG, skips zero-sized or over-large images, then attempts decompression into several pixel formats. There is no FuzzedDataProvider split, mode selector, sidecar file, or checksum wrapper.
- The libFuzzer target feeds the raw input bytes as a CIL policy file. The harness parses the bytes, compiles the AST, builds a policy database, optionally optimizes, writes the policy to a null sink, and destroys the database and AST. There is no byte carving, front/back consumption, mode selector, or FuzzedDataProvider contract.
- The fuzzer rejects short files, then consumes bytes from the front: a parser-family selector, optional fixed-width time format, optional fixed-width time key, optional fixed-width time offset, time-keep, type-coercion selector, and decoder selector/rule bytes. For optional fixed-width strings, the same byte that enables the option is also the first byte copied into that string; a following byte is consumed after each optional field. Decoder mode uses front-consumed bytes for rule type, backend, and action before the remaining bytes are passed to the parser.
- The intended libFuzzer contract is raw PHP source bytes passed to php-fuzz-execute. In this generated wrapper, local verify and official submit mount the PoC at a fixed path but invoke the fuzzer as though that path were a corpus argument; without the single-input run mode the file is not executed. There is no FuzzedDataProvider layout or leading selector byte.
- The libFuzzer harness passes the raw byte slice directly as njs script text. Empty inputs are ignored. Non-empty inputs create an njs VM, call the script processing path, and destroy the VM; there is no FuzzedDataProvider layout, no selector byte, and no length-prefixed envelope.
- The active RawSpeed libFuzzer target passes the complete input buffer directly to TiffParser::parse and then constructs TiffDecoderFuzzer-ThreefrDecoder. It does not use RawParser fallback, does not invoke CiffParser for raw CIFF bytes, and does not carve a mode selector or FuzzedDataProvider fields.
- The libFuzzer harness passes raw bytes to LibreDWG. Inputs beginning with a DWG-style header are decoded as DWG, inputs beginning with a JSON object opener are decoded as JSON, and all other inputs are treated as DXF text. Text inputs are copied to ensure NUL termination. After import, the harness chooses an output path such as DWG, DXF, or JSON and writes to a null sink, so crashes can occur during import or writeback.
- The libFuzzer harness passes the raw input bytes directly as an ASCII glTF string to TinyGLTF LoadASCIIFromString with an empty base directory. There is no carved prefix and no FuzzedDataProvider layout. External asset resolution proceeds through TinyGLTF filesystem callbacks when a buffer URI is non-data.
- The libFuzzer harness wraps the raw input bytes in a StringView, lexes and parses a full JS program, and only creates a VM plus LibJS GlobalObject interpreter when parsing succeeds. There is no FuzzedDataProvider, no input carving, and no LibWeb DOM or ImageData entry point; JavaScript exceptions are handled as normal interpreter outcomes rather than process crashes.

### Format Links
- [[assimp-model]]
- [[c-blosc2-frame]]
- [[cil-policy-text]]
- [[dwg]]
- [[dwg-drawing]]
- [[dxf]]
- [[dxf-text]]
- [[fluent-bit-parser-fuzzer-control-plus-json]]
- [[gltf-json]]
- [[javascript]]
- [[javascript-source]]
- [[jpeg]]
- [[jpeg2000-j2k]]
- [[leptonica-spix]]
- [[libredwg-dwg-dxf-json]]
- [[libredwg-json]]
- [[lua-source]]
- [[mruby-source]]
- [[opensc-pkcs15-reader-chunk-stream]]
- [[opentype-font-graphite]]
- [[p11-kit-rpc]]
- [[php-source]]
- [[rawspeed-ciff-vs-threefr-tiff]]
- [[selinux-cil-policy-text]]
- [[sudoers-policy-fuzzer-lines]]
- [[tiff-srw]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
