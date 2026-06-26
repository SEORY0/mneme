---
type: index
title: CyberGym OKF knowledge bundle
okf_version: "0.1"
---

# CyberGym PoC Knowledge (OKF)

Task-agnostic, distilled patterns. Abstract only — no task ids, no concrete offsets.

## vuln-classes
- [global-buffer-overflow-read](vuln-classes/global-buffer-overflow-read.md)
- [global-buffer-overflow-write](vuln-classes/global-buffer-overflow-write.md)
- [heap-buffer-overflow-read](vuln-classes/heap-buffer-overflow-read.md)
- [heap-buffer-overflow-write](vuln-classes/heap-buffer-overflow-write.md)
- [heap-double-free](vuln-classes/heap-double-free.md)
- [heap-use-after-free-read](vuln-classes/heap-use-after-free-read.md)
- [stack-buffer-overflow-read](vuln-classes/stack-buffer-overflow-read.md)
- [use-after-poison-read](vuln-classes/use-after-poison-read.md)
- [use-of-uninitialized-value](vuln-classes/use-of-uninitialized-value.md)

## formats
- [cff2-font](formats/cff2-font.md)
- [chunked-image](formats/chunked-image.md)
- [config](formats/config.md)
- [elf](formats/elf.md)
- [executable](formats/executable.md)
- [file-magic](formats/file-magic.md)
- [isobmff](formats/isobmff.md)
- [json](formats/json.md)
- [md3-model](formats/md3-model.md)
- [media-container](formats/media-container.md)
- [mvg](formats/mvg.md)
- [pcap](formats/pcap.md)
- [pdf](formats/pdf.md)
- [sip-text](formats/sip-text.md)
- [text-expr](formats/text-expr.md)
- [tiff](formats/tiff.md)
- [xml](formats/xml.md)
- [yara-rules](formats/yara-rules.md)

- [flatbuffers-monster-json](formats/flatbuffers-monster-json.md)
- [mruby-script](formats/mruby-script.md)
- [postscript](formats/postscript.md)
- [proj-params](formats/proj-params.md)
- [ucl](formats/ucl.md)

## strategies
- [construct](strategies/construct.md)
- [fuzzer](strategies/fuzzer.md)
- [hint-literal](strategies/hint-literal.md)
- [seed-mutate](strategies/seed-mutate.md)
- [seed-sweep](strategies/seed-sweep.md)
- [tiny-probe](strategies/tiny-probe.md)

## causal-policies
- [flatbuffers-json-escape-boundary](causal-policies/flatbuffers-json-escape-boundary.md)
- [generic-crash-official-clean-negative-memory](causal-policies/generic-crash-official-clean-negative-memory.md)
- [mruby-bigint-base-range](causal-policies/mruby-bigint-base-range.md)
- [mvg-text-attribute-key-buffer](causal-policies/mvg-text-attribute-key-buffer.md)
- [no-crash-format-recognition-negative-memory](causal-policies/no-crash-format-recognition-negative-memory.md)
- [no-crash-parser-reached-clean-negative-memory](causal-policies/no-crash-parser-reached-clean-negative-memory.md)
- [no-crash-parser-reached-no-sink-negative-memory](causal-policies/no-crash-parser-reached-no-sink-negative-memory.md)
- [no-crash-specialized-clean-exit-negative-memory](causal-policies/no-crash-specialized-clean-exit-negative-memory.md)
- [no-crash-target-path-not-reached-negative-memory](causal-policies/no-crash-target-path-not-reached-negative-memory.md)
- [no-crash-wrapper-surface-mismatch-negative-memory](causal-policies/no-crash-wrapper-surface-mismatch-negative-memory.md)
- [postscript-nul-filename-stream](causal-policies/postscript-nul-filename-stream.md)
- [proj-grid-selector-buffer](causal-policies/proj-grid-selector-buffer.md)
- [ucl-multiline-string-boundary](causal-policies/ucl-multiline-string-boundary.md)
