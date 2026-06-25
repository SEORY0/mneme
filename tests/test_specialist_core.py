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
