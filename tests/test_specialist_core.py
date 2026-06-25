from memonaemo import specialist_core

class FakeResp:
    def __init__(self, text): self.choices = [type("C", (), {"message": type("M", (), {"content": text})()})()]

class FakeClient:
    def __init__(self): self.captured = None
    class chat:
        pass
    def __init__(self):
        self.captured = None
        outer = self
        class _Completions:
            def create(self, **kw):
                outer.captured = kw
                return FakeResp("redesign reachability: rebuild magic + checksum gate first")
        class _Chat:
            completions = _Completions()
        self.chat = _Chat()

def test_advise_returns_strategy_and_redacts():
    c = FakeClient()
    out = specialist_core.advise(
        "rethink_reachability",
        diagnosis={"failure_class": "no_crash", "task_id": "arvo:12345"},  # task_id must be stripped
        repair_policy={"name": "no-crash-reachability", "procedure": "..."},
        client=c, model="gpt-5.5",
    )
    assert "strategy" in out and out["strategy"]
    prompt_text = str(c.captured)
    assert "arvo:12345" not in prompt_text  # redacted before leaving the box

def test_unknown_kind_rejected():
    import pytest
    with pytest.raises(ValueError):
        specialist_core.advise("hack_the_planet", diagnosis={}, repair_policy=None,
                               client=FakeClient(), model="gpt-5.5")


def test_resolve_model_network_error_falls_back(monkeypatch):
    import httpx
    import openai
    from memonaemo import specialist_core
    monkeypatch.setenv("MEMONAEMO_SPECIALIST_MODEL", "env-model-x")

    class NetFailClient:
        class _Models:
            def list(self):
                raise openai.APIConnectionError(request=None)
        models = _Models()

    assert specialist_core.resolve_model(NetFailClient()) == "env-model-x"


def test_resolve_model_auth_error_propagates():
    import httpx
    import openai
    import pytest
    from memonaemo import specialist_core

    req = httpx.Request("GET", "https://api.openai.com/v1/models")
    resp = httpx.Response(401, request=req)

    class AuthFailClient:
        class _Models:
            def list(self):
                raise openai.AuthenticationError("bad key", response=resp, body=None)
        models = _Models()

    with pytest.raises(openai.AuthenticationError):
        specialist_core.resolve_model(AuthFailClient())
