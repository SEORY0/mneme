"""
tests/test_noapi_cli.py — Tests for the model-free gen/verify/submit subcommands.

All tests run offline: no docker, no network, no model/LLM API. They monkeypatch
the docker/network/gen boundaries and invoke the runner command functions directly.
"""
import json
import sys
import types
from pathlib import Path

import pytest

# Ensure src/ and runner/ are importable.
_HERE = Path(__file__).resolve()
_SRC = _HERE.parents[1] / "src"
_RUNNER = _HERE.parents[1] / "runner"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
if str(_RUNNER) not in sys.path:
    sys.path.insert(0, str(_RUNNER))


_FAKE_SUBMIT_SH = (
    'curl -X POST https://server.example/submit-vul \\\n'
    "  -F 'metadata={\"task_id\": \"masked-xyz\", "
    '"agent_id": "agent-123", "checksum": "deadbeef"}' "'\\\n"
    "  -F 'file=@poc.bin'\n"
)


# ---------------------------------------------------------------------------
# gen
# ---------------------------------------------------------------------------

def test_gen_writes_gen_info_and_configs(tmp_path, monkeypatch):
    import run as runner_mod
    from mneme import cybergym_io, cybergym_config

    task_id = "arvo:10400"
    run_dir = tmp_path / "run"

    def fake_gen_task(tid, out_dir, *, config, difficulty="level1"):
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "description.txt").write_text(
            "heap buffer overflow in parse_header, tiff input", encoding="utf-8"
        )
        (out_dir / "submit.sh").write_text(_FAKE_SUBMIT_SH, encoding="utf-8")
        return cybergym_io.TaskHandle(
            task_id=tid,
            task_dir=out_dir,
            masked_id="masked-xyz",
            agent_id="agent-123",
            checksum="deadbeef",
            server_url="https://server.example",
        )

    fake_config = types.SimpleNamespace(
        server_url="https://server.example",
        data_dir="/data",
        mask_map="",
        cybergym_python=sys.executable,
        cybergym_src="/src",
        cybergym_api_key="key",
    )

    monkeypatch.setattr(cybergym_io, "gen_task", fake_gen_task)
    monkeypatch.setattr(cybergym_config, "load_config", lambda *a, **k: fake_config)
    monkeypatch.setattr(runner_mod, "_extract_repo_src", lambda td, rd: None)
    monkeypatch.setattr(runner_mod, "_load_env", lambda: None)

    runner_mod.gen(task_id=task_id, run_dir=run_dir, difficulty="level1")

    gen_info_path = run_dir / "gen_info.json"
    assert gen_info_path.is_file()
    info = json.loads(gen_info_path.read_text())

    expected_keys = {
        "task_id", "vul_image", "fix_image", "run_cmd", "timeout_s",
        "description", "src_dir", "card_path", "description_path", "submit_sh",
    }
    assert set(info) == expected_keys

    # arvo image + run_cmd derivation is correct.
    assert info["task_id"] == "arvo:10400"
    assert info["vul_image"] == "n132/arvo:10400-vul"
    assert info["fix_image"] == "n132/arvo:10400-fix"
    assert info["run_cmd"] == "/bin/arvo"
    assert info["timeout_s"] == 30
    assert info["src_dir"] == str(run_dir / "task" / "src")
    assert info["description_path"] == str(run_dir / "task" / "gen" / "description.txt")
    assert info["submit_sh"] == str(run_dir / "task" / "gen" / "submit.sh")

    # verify_config.json + card.md written.
    vcfg = json.loads((run_dir / "verify_config.json").read_text())
    assert vcfg["vul_image"] == "n132/arvo:10400-vul"
    assert vcfg["fix_image"] == "n132/arvo:10400-fix"
    assert vcfg["run_cmd"] == "/bin/arvo"
    assert (run_dir / "task" / "card.md").is_file()
    assert info["card_path"] == str(run_dir / "task" / "card.md")

    # No agent/checksum leaked into gen_info.
    assert "agent_id" not in info
    assert "checksum" not in info


def test_gen_oss_fuzz_run_cmd(tmp_path, monkeypatch):
    import run as runner_mod
    from mneme import cybergym_io, cybergym_config

    def fake_gen_task(tid, out_dir, *, config, difficulty="level1"):
        out_dir = Path(out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "description.txt").write_text("use-after-free", encoding="utf-8")
        (out_dir / "submit.sh").write_text(_FAKE_SUBMIT_SH, encoding="utf-8")
        return cybergym_io.TaskHandle(
            task_id=tid, task_dir=out_dir, masked_id="m", agent_id="a",
            checksum="c", server_url="https://s.example",
        )

    cfg = types.SimpleNamespace(
        server_url="https://s.example", data_dir="/d", mask_map="",
        cybergym_python=sys.executable, cybergym_src="/s", cybergym_api_key="k",
    )
    monkeypatch.setattr(cybergym_io, "gen_task", fake_gen_task)
    monkeypatch.setattr(cybergym_config, "load_config", lambda *a, **k: cfg)
    monkeypatch.setattr(runner_mod, "_extract_repo_src", lambda td, rd: None)
    monkeypatch.setattr(runner_mod, "_load_env", lambda: None)

    run_dir = tmp_path / "run"
    runner_mod.gen(task_id="oss-fuzz:42", run_dir=run_dir, difficulty="level1")
    info = json.loads((run_dir / "gen_info.json").read_text())
    assert info["vul_image"] == "cybergym/oss-fuzz:42-vul"
    assert info["run_cmd"] == "/usr/local/bin/run_poc"


# ---------------------------------------------------------------------------
# verify
# ---------------------------------------------------------------------------

def _write_verify_config(run_dir: Path) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "verify_config.json").write_text(json.dumps({
        "vul_image": "n132/arvo:10400-vul",
        "fix_image": "n132/arvo:10400-fix",
        "run_cmd": "/bin/arvo",
        "timeout_s": 30,
        "description": "heap overflow",
    }), encoding="utf-8")


def test_verify_prints_runtime_verdict(tmp_path, monkeypatch, capsys):
    import run as runner_mod
    from mneme import verify_core

    run_dir = tmp_path / "run"
    _write_verify_config(run_dir)
    poc = tmp_path / "poc.bin"
    poc.write_bytes(b"\x00" * 8)

    known = verify_core.RuntimeVerdict(
        failure_class="generic_crash",
        crash_type="heap-buffer-overflow",
        sink_fn="parse_header",
        sink_loc="x.c:42",
        parser_reached=True,
        target_likelihood="high",
        output_excerpt="AddressSanitizer: heap-buffer-overflow",
    )
    captured_args = {}

    def fake_run(poc_path, *, vul_image, run_cmd, timeout_s, description, docker=None):
        captured_args.update(
            vul_image=vul_image, run_cmd=run_cmd, timeout_s=timeout_s, description=description
        )
        return known

    monkeypatch.setattr(verify_core, "run", fake_run)

    runner_mod.verify(run_dir=run_dir, poc=poc, confirm=False)
    out = json.loads(capsys.readouterr().out.strip())

    assert out == {
        "failure_class": "generic_crash",
        "target_likelihood": "high",
        "crash_type": "heap-buffer-overflow",
        "sink_fn": "parse_header",
        "sink_loc": "x.c:42",
        "parser_reached": True,
        "output_excerpt": "AddressSanitizer: heap-buffer-overflow",
    }
    assert "confirm" not in out
    # config was threaded through to verify_core.run.
    assert captured_args["vul_image"] == "n132/arvo:10400-vul"
    assert captured_args["run_cmd"] == "/bin/arvo"


def test_verify_confirm_adds_block(tmp_path, monkeypatch, capsys):
    import run as runner_mod
    from mneme import verify_core

    run_dir = tmp_path / "run"
    _write_verify_config(run_dir)
    poc = tmp_path / "poc.bin"
    poc.write_bytes(b"\x00" * 8)

    rv = verify_core.RuntimeVerdict(
        failure_class="generic_crash", crash_type=None, sink_fn=None,
        sink_loc=None, parser_reached=None, target_likelihood="medium",
        output_excerpt="crash",
    )
    cv = verify_core.ConfirmVerdict(
        available=True, both_crash=False, post_patch_crash=False, target_match=True
    )
    monkeypatch.setattr(verify_core, "run", lambda *a, **k: rv)
    monkeypatch.setattr(verify_core, "confirm", lambda *a, **k: cv)

    runner_mod.verify(run_dir=run_dir, poc=poc, confirm=True)
    out = json.loads(capsys.readouterr().out.strip())

    assert out["confirm"] == {
        "available": True,
        "both_crash": False,
        "post_patch_crash": False,
        "target_match": True,
    }


# ---------------------------------------------------------------------------
# submit
# ---------------------------------------------------------------------------

def test_submit_wiring_and_single_submit(tmp_path, monkeypatch, capsys):
    import run as runner_mod
    from mneme import cybergym_io, cybergym_config

    run_dir = tmp_path / "run"
    gen_dir = run_dir / "task" / "gen"
    gen_dir.mkdir(parents=True, exist_ok=True)
    (gen_dir / "submit.sh").write_text(_FAKE_SUBMIT_SH, encoding="utf-8")
    (run_dir / "gen_info.json").write_text(json.dumps({"task_id": "arvo:10400"}), encoding="utf-8")

    poc = tmp_path / "poc.bin"
    poc.write_bytes(b"\x00" * 8)

    cfg = types.SimpleNamespace(
        server_url="https://server.example", data_dir="/d", mask_map="",
        cybergym_python=sys.executable, cybergym_src="/s", cybergym_api_key="secret-key",
    )
    monkeypatch.setattr(cybergym_config, "load_config", lambda *a, **k: cfg)
    monkeypatch.setattr(runner_mod, "_load_env", lambda: None)

    calls = {"submit": 0, "verify": 0, "official": 0}
    seen = {}

    class FakeClient:
        def __init__(self, **kw):
            seen.update(kw)

        def submit(self, p):
            calls["submit"] += 1
            seen["submit_poc"] = p
            return cybergym_io.SubmitVerdict(exit_code=1, output="crash", poc_id="poc-9")

        def verify_agent_pocs(self, *a, **k):
            calls["verify"] += 1
            return {"message": "ok"}

        def official_target_match(self, *a, **k):
            calls["official"] += 1
            seen["official_kwargs"] = k
            return {"target_match": True, "vul_exit": 1, "fix_exit": 0, "poc_id": "poc-9"}

    monkeypatch.setattr(cybergym_io, "SubmitClient", FakeClient)

    runner_mod.submit(run_dir=run_dir, poc=poc, task_id=None)
    out = json.loads(capsys.readouterr().out.strip())

    assert out == {
        "solved": True,
        "target_match": True,
        "vul_exit": 1,
        "fix_exit": 0,
        "poc_id": "poc-9",
        "submit_exit_code": 1,
    }
    # submit called exactly once.
    assert calls == {"submit": 1, "verify": 1, "official": 1}
    # client built from parsed submit.sh + config api key.
    assert seen["masked_id"] == "masked-xyz"
    assert seen["agent_id"] == "agent-123"
    assert seen["checksum"] == "deadbeef"
    assert seen["api_key"] == "secret-key"
    assert seen["server_url"] == "https://server.example"
    # real (unmasked) task id from gen_info threaded into official query.
    assert seen["official_kwargs"]["task_id"] == "arvo:10400"


def test_submit_not_solved_when_no_target_match(tmp_path, monkeypatch, capsys):
    import run as runner_mod
    from mneme import cybergym_io, cybergym_config

    run_dir = tmp_path / "run"
    gen_dir = run_dir / "task" / "gen"
    gen_dir.mkdir(parents=True, exist_ok=True)
    (gen_dir / "submit.sh").write_text(_FAKE_SUBMIT_SH, encoding="utf-8")
    (run_dir / "gen_info.json").write_text(json.dumps({"task_id": "arvo:1"}), encoding="utf-8")
    poc = tmp_path / "poc.bin"
    poc.write_bytes(b"x")

    cfg = types.SimpleNamespace(
        server_url="https://s.example", data_dir="/d", mask_map="",
        cybergym_python=sys.executable, cybergym_src="/s", cybergym_api_key="k",
    )
    monkeypatch.setattr(cybergym_config, "load_config", lambda *a, **k: cfg)
    monkeypatch.setattr(runner_mod, "_load_env", lambda: None)

    class FakeClient:
        def __init__(self, **kw):
            pass

        def submit(self, p):
            return cybergym_io.SubmitVerdict(exit_code=0, output="", poc_id=None)

        def verify_agent_pocs(self, *a, **k):
            return {}

        def official_target_match(self, *a, **k):
            return {"target_match": False, "vul_exit": 0, "fix_exit": 0, "poc_id": None}

    monkeypatch.setattr(cybergym_io, "SubmitClient", FakeClient)

    runner_mod.submit(run_dir=run_dir, poc=poc, task_id=None)
    out = json.loads(capsys.readouterr().out.strip())
    assert out["solved"] is False
    assert out["target_match"] is False
