"""Offline test for the OpenAI gpt-5.5 main-agent backend.

NO network, NO docker. A fake OpenAI client returns canned tool-call responses
and verify_core.run is monkeypatched to a stub. Drives the sequence:
read_file -> write_poc(hex) -> verify_run(high) -> finish.
"""
from __future__ import annotations

import types

import pytest

from mneme import agent_openai, verify_core
from mneme.verify_core import RuntimeVerdict


# ---------------------------------------------------------------------------
# Fake OpenAI client primitives
# ---------------------------------------------------------------------------
def _tool_call(call_id, name, arguments):
    return types.SimpleNamespace(
        id=call_id,
        type="function",
        function=types.SimpleNamespace(name=name, arguments=arguments),
    )


def _response(*, content=None, tool_calls=None):
    msg = types.SimpleNamespace(content=content, tool_calls=tool_calls)
    choice = types.SimpleNamespace(message=msg, finish_reason="stop")
    return types.SimpleNamespace(choices=[choice])


class FakeCompletions:
    def __init__(self, scripted):
        self._scripted = list(scripted)
        self.calls = []  # captured kwargs per create()

    def create(self, **kw):
        self.calls.append(kw)
        return self._scripted.pop(0)


class FakeChat:
    def __init__(self, scripted):
        self.completions = FakeCompletions(scripted)


class FakeClient:
    def __init__(self, scripted):
        self.chat = FakeChat(scripted)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------
def _build_run_dir(tmp_path):
    run_dir = tmp_path / "run"
    task = run_dir / "task"
    task.mkdir(parents=True)
    (task / "card.md").write_text("# Task\nHeap overflow in parse().\n", encoding="utf-8")
    (task / "src").mkdir()
    (task / "src" / "main.c").write_text("int main(){return 0;}\n", encoding="utf-8")
    return run_dir


def _config():
    return {
        "vul_image": "n132/arvo:10400-vul",
        "fix_image": "n132/arvo:10400-fix",
        "run_cmd": "/bin/arvo",
        "timeout_s": 30,
        "description": "heap-buffer-overflow in parse",
    }


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
def test_solve_loop_writes_candidate_and_terminates(tmp_path, monkeypatch):
    run_dir = _build_run_dir(tmp_path)

    # Stub verify_core.run so NO docker is touched; report a high-likelihood crash.
    verify_calls = []

    def fake_run(candidate_path, **kw):
        verify_calls.append((candidate_path, kw))
        return RuntimeVerdict(
            failure_class="generic_crash",
            crash_type="heap-buffer-overflow",
            sink_fn="parse",
            sink_loc="main.c:1",
            parser_reached=True,
            target_likelihood="high",
            output_excerpt="SUMMARY: AddressSanitizer: heap-buffer-overflow",
        )

    monkeypatch.setattr(verify_core, "run", fake_run)

    poc_hex = b"DEADBEEF".hex()
    scripted = [
        _response(tool_calls=[_tool_call("c1", "read_file", '{"path": "task/src/main.c"}')]),
        _response(tool_calls=[_tool_call("c2", "write_poc", '{"data_hex": "%s"}' % poc_hex)]),
        _response(tool_calls=[_tool_call("c3", "verify_run", "{}")]),
        # (should not be reached — loop stops on target_high)
        _response(content="done"),
    ]
    client = FakeClient(scripted)

    result = agent_openai.solve(
        tmp_path / "task_dir",
        run_dir,
        model="gpt-5.5",
        config=_config(),
        client=client,
    )

    # Candidate written under run_dir/candidate/
    candidate = run_dir / "candidate" / "poc"
    assert candidate.is_file()
    assert candidate.read_bytes() == b"DEADBEEF"

    # Returned dict shape + terminal stop reason
    assert result["candidate_path"] == str(candidate)
    assert result["stop_reason"] == "target_high"
    assert result["iters"] == 3
    assert "transcript_path" in result
    assert result["cost"] == 0.0

    # verify_run actually invoked the stub with the candidate path + config
    assert len(verify_calls) == 1
    cand_arg, kw = verify_calls[0]
    assert str(cand_arg) == str(candidate)
    assert kw["vul_image"] == "n132/arvo:10400-vul"

    # Transcript exists and contains no API key material
    transcript = (run_dir / "transcript_openai.txt").read_text()
    assert "verify_run" in transcript

    # Reasoning params set on every create call; sampling params omitted.
    for kw in client.chat.completions.calls:
        assert kw["reasoning_effort"] == "low"
        assert kw["max_completion_tokens"] >= 4000
        assert "temperature" not in kw
        assert "top_p" not in kw


def test_file_tool_rejects_path_outside_run_dir(tmp_path, monkeypatch):
    run_dir = _build_run_dir(tmp_path)
    monkeypatch.setattr(verify_core, "run", lambda *a, **k: None)

    # Model tries to read /etc/passwd via an escaping relative path, then stops.
    scripted = [
        _response(tool_calls=[_tool_call("c1", "read_file", '{"path": "../../../etc/passwd"}')]),
        _response(content="giving up"),
    ]
    client = FakeClient(scripted)

    result = agent_openai.solve(
        tmp_path / "task_dir",
        run_dir,
        model="gpt-5.5",
        config=_config(),
        client=client,
    )

    # Loop terminated cleanly; no candidate written.
    assert result["candidate_path"] is None
    assert result["stop_reason"] == "model_stopped"

    # The escaping read was rejected — transcript records the error, not file content.
    transcript = (run_dir / "transcript_openai.txt").read_text()
    assert "escapes run_dir" in transcript


def test_empty_response_retries_then_stops(tmp_path, monkeypatch):
    run_dir = _build_run_dir(tmp_path)
    monkeypatch.setattr(verify_core, "run", lambda *a, **k: None)

    # Two empty responses in a row (initial + retry) → stop_reason empty_response.
    scripted = [
        _response(content=None, tool_calls=None),
        _response(content=None, tool_calls=None),
    ]
    client = FakeClient(scripted)

    result = agent_openai.solve(
        tmp_path / "task_dir",
        run_dir,
        model="gpt-5.5",
        config=_config(),
        client=client,
    )

    assert result["stop_reason"] == "empty_response"
    assert result["candidate_path"] is None
    # The retry used a larger completion budget.
    assert client.chat.completions.calls[1]["max_completion_tokens"] > \
        client.chat.completions.calls[0]["max_completion_tokens"]
