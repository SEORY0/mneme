---
type: harness
title: "Afl Libfuzzer"
harness_convention: afl-libfuzzer
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Afl Libfuzzer

## Input Contract
- For `heif-isobmff`, The kimgio HEIF AFL-compatible wrapper feeds the whole PoC as QBuffer data to the Qt image handler. The handler peeks at the header through canRead, then reads all remaining bytes and passes the memory buffer to libheif. There is no front selector.
- For `dng-tiff-rawspeed-camera-file`, The selected RawSpeed parser wrapper consumes raw bytes as a camera file, constructs a RawParser, gets a decoder, disables crop/unknown-camera hard failures, then calls decodeRaw and decodeMetaData. C++ RawSpeed exceptions are caught; sanitizer faults are the relevant signal.
- For `dpx-image`, The GraphicsMagick DPX AFL-compatible wrapper consumes the entire PoC as a DPX image file through the coder_DPX_fuzzer target. There is no front selector; parser reachability depends on a valid DPX header and element metadata.
