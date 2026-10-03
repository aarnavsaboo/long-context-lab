from __future__ import annotations

from .compression import compress
from .needles import exact_score, make_task
from .ollama import OllamaRunner
from .planner import Job
from .retrieval import rank_windows
from .windows import windows


QUESTION = "What is the exact calibration code? Reply with only the code."


def build_input(job: Job, source: str) -> str:
    if job.strategy == "full":
        return source
    if job.strategy == "retrieval":
        parts=rank_windows(source,QUESTION,job.window_chars,job.overlap_chars,job.top_k)
        return "\n\n".join(parts)+"\n\nQuestion: "+QUESTION
    if job.strategy == "compression":
        reduced=compress(source,QUESTION,job.evidence_budget_chars)
        return reduced+"\n\nQuestion: "+QUESTION
    if job.strategy == "windows":
        parts=windows(source,job.window_chars,job.overlap_chars)[:job.top_k]
        return "\n\n".join(parts)+"\n\nQuestion: "+QUESTION
    raise ValueError(f"unknown strategy: {job.strategy}")


def execute(job: Job, backend: OllamaRunner) -> dict:
    task=make_task(job.target_tokens*4,job.position,f"{job.id}:{job.repeat}")
    prompt=build_input(job,task.prompt)
    result=backend.generate(prompt)
    return {
        "job_id":job.id,
        "strategy":job.strategy,
        "target_tokens":job.target_tokens,
        "position":job.position,
        "repeat":job.repeat,
        "source_chars":len(task.prompt),
        "sent_chars":len(prompt),
        "answer":task.answer,
        "score":exact_score(result["text"],task.answer),
        **result,
    }
