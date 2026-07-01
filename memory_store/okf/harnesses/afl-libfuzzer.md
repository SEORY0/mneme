---
type: harness
title: "Afl Libfuzzer"
access_scope: generate
confidence: medium
tags: ["afl-libfuzzer", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
okf_support: 2
---
# Afl Libfuzzer

## Round 13 Facts
- The kimgio HEIF AFL-compatible wrapper feeds the whole PoC as QBuffer data to the Qt image handler. The handler peeks at the header through canRead, then reads all remaining bytes and passes the memory buffer to libheif. There is no front selector.
- The selected RawSpeed parser wrapper consumes raw bytes as a camera file, constructs a RawParser, gets a decoder, disables crop/unknown-camera hard failures, then calls decodeRaw and decodeMetaData. C++ RawSpeed exceptions are caught; sanitizer faults are the relevant signal.
- The GraphicsMagick DPX AFL-compatible wrapper consumes the entire PoC as a DPX image file through the coder_DPX_fuzzer target. There is no front selector; parser reachability depends on a valid DPX header and element metadata.

## Round 19 Input Contract

- The selected GraphicsMagick target is the raw MVG coder fuzzer. The entire input is consumed as MVG bytes; there is no selector byte, archive wrapper, checksum, or FuzzedDataProvider split.
- Format link: [[mvg]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 23 Input Contract
- The libxml2 XML fuzzer reads the option word, builds the entity map, parses the main entity through pull parsing, push parsing, and reader parsing, and runs XInclude processing after pull/push parses when the XInclude option is enabled. The reader path may also invoke XInclude processing on nodes. There is no raw XML-only input; missing the entity envelope prevents the main document from being parsed.

## Round 23 Format Links
- [[libxml2-entity-stream]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 32 Input Contract
- The first input byte selects the OpenFlow flow-mod command by modulo arithmetic. The remaining bytes are passed as one NUL-terminated C string; newlines and interior NULs are rejected before parsing. The harness parses the flow string, chooses a usable protocol, encodes the flow mod, and frees the resulting buffers.

## Round 32 Format Links
- [[openvswitch-flow]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 33 Input Contract

### Input Contract
- The active fuzz target reads raw bytes, uses the final byte as the datalink type for pcap_open_dead with a fixed snap length, copies all bytes into the filter buffer, terminates the filter at the final byte, and invokes pcap_compile with optimization enabled. There is no pcap file envelope, no packet records, no mode prefix, and no FuzzedDataProvider layout.

### Format Links
- [[pcap-filter-expression]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 35 Input Contract

### Input Contract
- The active AFL/libFuzzer-compatible harness reads the raw PoC bytes from a file. It treats the leading little-endian settings word as feature bits for CharReaderBuilder and passes the remaining bytes directly as the JSON document; there is no FuzzedDataProvider layout or checksum.

### Format Links
- [[json]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.

## Round 36 Input Contract
- The libsndfile fuzzer feeds the whole raw input through virtual file I/O into the normal open path, then allocates a frame buffer based on the reported channel count and repeatedly reads floating-point frames. There is no selector byte or FuzzedDataProvider carving; RIFF chunk sizes and the selected subtype determine whether the ADPCM decoder is reached.

## Round 36 Format Links
- [[wav-ms-adpcm]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
