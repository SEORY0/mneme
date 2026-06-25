#!/usr/bin/env python3
"""Live plumbing validation for the REAL CyberGym harness (NO model).

Exercises the non-model path end to end against the running server + local docker:
  1. gen_task(arvo:10400) into a temp dir
  2. submit a trivial NON-crashing PoC (b"A\\n") via SubmitClient.submit
  3. verify_agent_pocs + official_target_match (query records)

Prints redacted, coherent output. A trivial PoC almost certainly does NOT trigger
the bug, so target_match is expected False, but vul_exit/fix_exit should be
populated and there should be no errors.
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

_SRC = Path(__file__).resolve().parents[1] / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from mneme import cybergym_config, cybergym_io  # noqa: E402

TASK_ID = "arvo:10400"


def main() -> int:
    config = cybergym_config.load_config()
    print(f"config: {config}")  # api key is redacted by Config.__repr__

    with tempfile.TemporaryDirectory(prefix="mneme_plumbing_") as tmp:
        out_dir = Path(tmp) / "task"

        # 1. gen_task
        handle = cybergym_io.gen_task(TASK_ID, out_dir, config=config)
        print("\n[gen] ok")
        print(f"[gen] handle: {handle}")  # redacted repr
        print(f"[gen] files: {sorted(p.name for p in handle.task_dir.iterdir())}")
        imgs = cybergym_io.images_for(TASK_ID)
        print(f"[gen] images: {imgs}")

        # 2. trivial non-crashing PoC
        poc = Path(tmp) / "poc.bin"
        poc.write_bytes(b"A\n")
        client = cybergym_io.SubmitClient.from_handle(handle, config.cybergym_api_key)
        print(f"\n[submit] client: {client}")  # redacted repr
        verdict = client.submit(poc)
        snippet = (verdict.output or "")[:200].replace("\n", " ")
        print(f"[submit] exit_code={verdict.exit_code} poc_id={verdict.poc_id}")
        print(f"[submit] output[:200]={snippet!r}")

        # 3. official verify + query
        vinfo = client.verify_agent_pocs()
        print(f"\n[verify] message={vinfo.get('message')!r} poc_ids={vinfo.get('poc_ids')}")
        official = client.official_target_match()
        print(
            f"[official] target_match={official['target_match']} "
            f"vul_exit={official['vul_exit']} fix_exit={official['fix_exit']} "
            f"poc_id={official['poc_id']}"
        )

    print("\nPLUMBING OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
