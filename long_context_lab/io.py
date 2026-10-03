from pathlib import Path
import json

from .planner import Job


def read_jobs(path:str)->list[Job]:
    return [Job(**json.loads(x)) for x in Path(path).read_text().splitlines() if x.strip()]


def read_rows(path:str)->list[dict]:
    return [json.loads(x) for x in Path(path).read_text().splitlines() if x.strip()]


def write_rows(path:str,rows:list[dict]):
    target=Path(path)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text("".join(json.dumps(x,sort_keys=True)+"\n" for x in rows),encoding="utf-8")
