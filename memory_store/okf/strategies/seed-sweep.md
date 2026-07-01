---
type: strategy
title: seed-sweep strategy
description: What
resource: cybergym://strategy/seed-sweep
tags: [seed-sweep, seed_mutation]
timestamp: 2026-06-24T00:00:00Z
okf_support: 23
---
## What
Run EVERY in-repo corpus/seed file through the target unmodified; a seed that already crashes the
vulnerable build is an instant solve. Decisive tool: `find_seeds`.

## When
ALWAYS first, whenever the repo ships `fuzzing/corpus`, `seed(s)`, `testdata`, `testcase(s)` with
binary inputs. Highest yield on complex container formats.

## Steps
1. Unpack `repo-vul.tar.gz`; collect seed files (binary extensions / seed-dir names; skip source code).
2. For each: copy to the input path and run the target (`/bin/arvo` / `run_poc`, no args, reads `/tmp/poc`).
3. A non-zero exit with a sanitizer report (or a fatal signal) on a seed = winner.

## Pitfalls
- A crashing seed may hit a DIFFERENT bug than described — confirm the ASan sink matches description.txt.
- Skip source files (`.c/.cc/.h/.go/...`); they are not fuzzer inputs.

## Observed
- Support: 23 train-set solves.
- Winning strategies (observed): {'seed-sweep': 23}
- Format families (observed): {'pcap': 3, 'xml': 6, 'pdf': 2, 'tiff': 1, 'chunked-image': 1, 'isobmff': 2}
- Abstract sink shapes (observed): double-free:?, heap-buffer-overflow:READ, heap-buffer-overflow:WRITE, use-of-uninitialized-value:?

<!-- BEGIN observed-census (auto) -->
## Observed census (auto)

_Descriptive trace census — NOT a causal policy; not used for memory ranking._

- canonical: `seed-sweep`
- observed: 38 traces; solved: 3 (illustrative — not for ranking)
- top vuln_classes: other (15), out-of-bounds-read (7), use-after-free (4), use-of-uninitialized-value (4), heap-buffer-overflow-write (2), buffer-overflow-write (1), heap-buffer-overflow (1), heap-buffer-overflow-read (1)
- top input_formats: opentype-font (3), gpsd-raw-packet-stream (2), hevc-elementary-stream (2), ivf-av1 (2), opensc-virtual-reader-chunk-stream (2), postscript-pdf (2), rar (2), aac-usac-mps (1)
- collapsed aliases: construct-and-seed-sweep, construct-then-seed-sweep, seed-sweep-and-construct, seed-sweep-and-header-stream-mutation, seed-sweep-construct, seed-sweep-seed-mutate-construct
<!-- END observed-census -->
