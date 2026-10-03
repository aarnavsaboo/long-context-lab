from dataclasses import asdict, dataclass
from hashlib import sha1
from itertools import product
import json


@dataclass(frozen=True)
class Job:
    id: str
    target_tokens: int
    position: float
    strategy: str
    repeat: int
    window_chars: int
    overlap_chars: int
    top_k: int
    evidence_budget_chars: int

    def to_dict(self):
        return asdict(self)


def expand(config: dict) -> list[Job]:
    rows = []
    for tokens,position,strategy,repeat in product(
        config["target_tokens"],
        config["positions"],
        config["strategies"],
        range(int(config.get("repeats",3))),
    ):
        payload = {
            "target_tokens":int(tokens),
            "position":float(position),
            "strategy":str(strategy),
            "repeat":repeat,
            "window_chars":int(config.get("window_chars",4000)),
            "overlap_chars":int(config.get("overlap_chars",400)),
            "top_k":int(config.get("top_k",3)),
            "evidence_budget_chars":int(config.get("evidence_budget_chars",12000)),
        }
        ident = sha1(json.dumps(payload,sort_keys=True).encode()).hexdigest()[:16]
        rows.append(Job(id=ident,**payload))
    return rows
