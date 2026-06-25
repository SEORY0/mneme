"""Offline tests for the real CyberGym cybergym_io API.

No live server, no docker, no real gen_task: subprocess.run and the SubmitClient
HTTP calls are mocked.
"""
import json
from pathlib import Path
from unittest import mock

import pytest

from mneme import cybergym_io
from mneme.cybergym_config import Config


SUBMIT_SH = (
    "#!/bin/bash\n"
    "curl -X POST http://127.0.0.1:8666/submit-vul \\\n"
    "  -F 'metadata={\"task_id\": \"7fa395d7dac0\", "
    "\"agent_id\": \"d73b8c9300494876b08dfb02677a3b8c\", "
    "\"checksum\": \"287694847bdafca5e949b6c934f365379b\", "
    "\"require_flag\": false}' \\\n"
    "  -F \"file=@${POC_FILE}\"\n"
)


def _fake_config() -> Config:
    return Config(
        server_url="http://127.0.0.1:8666",
        data_dir="/data/cybergym_data/data",
        mask_map="/some/mask_map.json",
        cybergym_python="/usr/bin/python3",
        cybergym_src="/some/cybergym/src",
        cybergym_api_key="cybergym-test-key",
    )


# ---------------------------------------------------------------------------
# gen_task: mock subprocess.run, parse submit.sh, redact in repr
# ---------------------------------------------------------------------------

def test_gen_task_parses_submit_sh_and_redacts(tmp_path):
    out_dir = tmp_path / "task"

    def fake_run(cmd, capture_output, text, env):
        # gen_task is supposed to write submit.sh into out_dir (the --out-dir arg).
        idx = cmd.index("--out-dir")
        Path(cmd[idx + 1], "submit.sh").write_text(SUBMIT_SH)
        return mock.Mock(returncode=0, stdout="ok", stderr="")

    with mock.patch("mneme.cybergym_io.subprocess.run", side_effect=fake_run) as m:
        handle = cybergym_io.gen_task("arvo:10400", out_dir, config=_fake_config())

    # parsed metadata
    assert handle.task_id == "arvo:10400"
    assert handle.masked_id == "7fa395d7dac0"
    assert handle.agent_id == "d73b8c9300494876b08dfb02677a3b8c"
    assert handle.checksum.startswith("287694847bda")
    assert handle.server_url == "http://127.0.0.1:8666"

    # --mask-map must be passed (server runs with a mask_map)
    called_cmd = m.call_args.args[0]
    assert "--mask-map" in called_cmd
    assert "--task-id" in called_cmd and "arvo:10400" in called_cmd

    # repr/str redact the sensitive tokens but keep the non-secret task_id/server_url
    r = repr(handle)
    assert "7fa395d7dac0" not in r
    assert "d73b8c9300494876b08dfb02677a3b8c" not in r
    assert "287694847bda" not in r
    assert "[redacted-submit-metadata]" in r
    assert "arvo:10400" in r


def test_gen_task_raises_on_nonzero_exit(tmp_path):
    with mock.patch(
        "mneme.cybergym_io.subprocess.run",
        return_value=mock.Mock(returncode=1, stdout="", stderr="boom"),
    ):
        with pytest.raises(RuntimeError, match="gen_task failed"):
            cybergym_io.gen_task("arvo:10400", tmp_path / "t", config=_fake_config())


# ---------------------------------------------------------------------------
# images_for: arvo -> n132/arvo, oss-fuzz -> cybergym/oss-fuzz
# ---------------------------------------------------------------------------

def test_images_for_arvo():
    imgs = cybergym_io.images_for("arvo:10400")
    assert imgs["vul_image"] == "n132/arvo:10400-vul"
    assert imgs["fix_image"] == "n132/arvo:10400-fix"


def test_images_for_oss_fuzz():
    imgs = cybergym_io.images_for("oss-fuzz:42537730")
    assert imgs["vul_image"] == "cybergym/oss-fuzz:42537730-vul"
    assert imgs["fix_image"] == "cybergym/oss-fuzz:42537730-fix"


def test_images_for_rejects_unknown_subset():
    with pytest.raises(ValueError):
        cybergym_io.images_for("weird:1")
    with pytest.raises(ValueError):
        cybergym_io.images_for("no-colon")


# ---------------------------------------------------------------------------
# SubmitClient.submit: mocked HTTP
# ---------------------------------------------------------------------------

def _client():
    return cybergym_io.SubmitClient(
        server_url="http://127.0.0.1:8666",
        masked_id="7fa395d7dac0",
        agent_id="agent123",
        checksum="cksum123",
        api_key="cybergym-test-key",
    )


def test_submit_posts_metadata_and_file(tmp_path):
    poc = tmp_path / "poc.bin"
    poc.write_bytes(b"A\n")

    resp = mock.Mock()
    resp.json.return_value = {
        "task_id": "7fa395d7dac0",
        "exit_code": 0,
        "output": "no crash",
        "poc_id": "deadbeef",
    }
    resp.raise_for_status.return_value = None

    with mock.patch("mneme.cybergym_io.requests.post", return_value=resp) as m:
        verdict = _client().submit(poc)

    assert verdict.exit_code == 0
    assert verdict.poc_id == "deadbeef"
    assert verdict.output == "no crash"

    # metadata is sent as JSON in the "metadata" form field
    kwargs = m.call_args.kwargs
    meta = json.loads(kwargs["data"]["metadata"])
    assert meta["task_id"] == "7fa395d7dac0"
    assert meta["agent_id"] == "agent123"
    assert meta["checksum"] == "cksum123"
    assert meta["require_flag"] is False
    assert "file" in kwargs["files"]
    assert m.call_args.args[0].endswith("/submit-vul")


def test_submit_client_repr_redacts():
    r = repr(_client())
    assert "7fa395d7dac0" not in r
    assert "agent123" not in r
    assert "cksum123" not in r
    assert "cybergym-test-key" not in r
    assert "[redacted-submit-metadata]" in r


# ---------------------------------------------------------------------------
# verify_agent_pocs + query_pocs: mocked HTTP, correct endpoints + header
# ---------------------------------------------------------------------------

def test_verify_agent_pocs_uses_api_key_header():
    resp = mock.Mock()
    resp.json.return_value = {"message": "ok", "poc_ids": ["p1"]}
    resp.raise_for_status.return_value = None
    with mock.patch("mneme.cybergym_io.requests.post", return_value=resp) as m:
        out = _client().verify_agent_pocs()
    assert out["poc_ids"] == ["p1"]
    kwargs = m.call_args.kwargs
    assert kwargs["headers"]["X-API-Key"] == "cybergym-test-key"
    assert kwargs["json"]["agent_id"] == "agent123"
    assert m.call_args.args[0].endswith("/verify-agent-pocs")


def test_query_pocs_uses_api_key_header():
    resp = mock.Mock()
    resp.json.return_value = [{"poc_id": "p1", "vul_exit_code": 1, "fix_exit_code": 0}]
    resp.raise_for_status.return_value = None
    with mock.patch("mneme.cybergym_io.requests.post", return_value=resp) as m:
        out = _client().query_pocs(agent_id="agent123")
    assert out[0]["poc_id"] == "p1"
    kwargs = m.call_args.kwargs
    assert kwargs["headers"]["X-API-Key"] == "cybergym-test-key"
    assert m.call_args.args[0].endswith("/query-poc")


# ---------------------------------------------------------------------------
# official_target_match: vul!=0 & fix==0 from mocked query records
# ---------------------------------------------------------------------------

def _patch_query(records):
    return mock.patch.object(cybergym_io.SubmitClient, "query_pocs", return_value=records)


def test_official_target_match_true():
    recs = [{"poc_id": "p1", "vul_exit_code": 1, "fix_exit_code": 0}]
    with _patch_query(recs):
        out = _client().official_target_match()
    assert out["target_match"] is True
    assert out["vul_exit"] == 1
    assert out["fix_exit"] == 0
    assert out["poc_id"] == "p1"


def test_official_target_match_false_when_fix_also_crashes():
    recs = [{"poc_id": "p1", "vul_exit_code": 1, "fix_exit_code": 1}]
    with _patch_query(recs):
        out = _client().official_target_match()
    assert out["target_match"] is False
    assert out["vul_exit"] == 1
    assert out["fix_exit"] == 1


def test_official_target_match_false_when_no_vul_crash():
    recs = [{"poc_id": "p1", "vul_exit_code": 0, "fix_exit_code": 0}]
    with _patch_query(recs):
        out = _client().official_target_match()
    assert out["target_match"] is False
    assert out["vul_exit"] == 0


def test_official_target_match_picks_best_record():
    recs = [
        {"poc_id": "p1", "vul_exit_code": 0, "fix_exit_code": 0},
        {"poc_id": "p2", "vul_exit_code": 134, "fix_exit_code": 0},  # the winner
    ]
    with _patch_query(recs):
        out = _client().official_target_match()
    assert out["target_match"] is True
    assert out["poc_id"] == "p2"
    assert out["vul_exit"] == 134


def test_official_target_match_no_records():
    with _patch_query([]):
        out = _client().official_target_match()
    assert out["target_match"] is False
    assert out["vul_exit"] is None
    assert out["fix_exit"] is None
