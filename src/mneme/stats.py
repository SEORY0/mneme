from __future__ import annotations
import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Stats:
    rows: list[dict] = field(default_factory=list)

    @classmethod
    def load(cls, path: Path) -> "Stats":
        p = Path(path)
        if not p.exists():
            return cls()
        rows = [json.loads(line) for line in p.read_text().splitlines() if line.strip()]
        return cls(rows)

    @staticmethod
    def record(path: Path, policy_name: str, *, success: bool) -> None:
        line = json.dumps({"policy": policy_name, "success": bool(success)})
        with Path(path).open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")

    def _for(self, name: str) -> list[dict]:
        return [r for r in self.rows if r.get("policy") == name]

    def success_rate(self, name: str) -> float:
        rs = self._for(name)
        if not rs:
            return 0.0
        return sum(1 for r in rs if r.get("success")) / len(rs)

    def frequency(self, name: str) -> int:
        return len(self._for(name))

    def recency_rank(self, name: str) -> int:
        # Higher = more recently used. Index of last occurrence.
        last = -1
        for i, r in enumerate(self.rows):
            if r.get("policy") == name:
                last = i
        return last
