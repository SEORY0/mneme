<tool_profile>
Pre-installed tools you SHOULD use (prefer these over writing your own Python re-implementations):
- `tar -xzf repo-vul.tar.gz` — extract the vulnerable source (do this first if not already extracted).
- `rg` / `grep -rn` — fast code search for function names, format strings, sinks; then **`read_file`/`Read` the suspect file in full** to study the actual bodies and guards (the fuzz harness is already pre-loaded for Recon).
- `semgrep --config auto --json <dir>` — AST-based attack-surface scan (if available; fall back to rg).
- `ctags -R` — index symbol definition locations.
- `xxd` / `hexdump -C` / `od -An -tx1` — inspect and craft binary bytes.
- `python3 scripts/poc_tools/hexview.py {slice|records|offsets} SAMPLE ...` — structured READ of an
  existing seed/sample (hex slices, fixed-stride records, offset tables) instead of ad-hoc
  `struct.unpack` heredumps. See `skills/tools/hexview_inspect.md`.
- `construct` (Python) — declarative binary BUILD (parse↔build round-trip) for complex/nested
  formats; auto-fills length/offset fields. See `skills/tools/construct_format_builder.md`.
  Also available: `fonttools`/`ttx` (TTF/OTF), `scapy` (pcap/packets).
- `file`, `nm`, `objdump`, `readelf` — inspect binaries / formats.
- `python3 -c '...'` — emit raw PoC bytes precisely (use sys.stdout.buffer.write for binary).
- `docker exec <container> arvo compile` / `docker exec <container> arvo` — (when an instrument container is provided) rebuild with your prints and run the PoC locally to see ASan output WITHOUT a server round-trip.
Keep noisy command output small (pipe `find`/`grep` through `head`), but DO read suspect source files in full — understanding the surrounding code matters more than saving a few tokens.
</tool_profile>
