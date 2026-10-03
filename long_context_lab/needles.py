from dataclasses import dataclass
from hashlib import sha1


@dataclass(frozen=True)
class NeedleTask:
    prompt: str
    answer: str
    position: float
    target_chars: int


def _filler(index: int) -> str:
    return f"Background note {index}: the archive contains ordinary descriptive text with no target answer. "


def make_task(target_chars: int, position: float, seed: str = "0") -> NeedleTask:
    if target_chars < 256:
        raise ValueError("target_chars must be at least 256")
    if not 0 <= position <= 1:
        raise ValueError("position must be between 0 and 1")
    answer = "NX-" + sha1(seed.encode()).hexdigest()[:10].upper()
    needle = f"Important record: the calibration code is {answer}. Remember this exact code. "
    filler = ""
    i = 0
    while len(filler) < target_chars:
        filler += _filler(i)
        i += 1
    index = int(min(len(filler), max(0, position * len(filler))))
    prompt = (
        filler[:index] + needle + filler[index:] +
        "\n\nQuestion: What is the exact calibration code? Reply with only the code."
    )
    return NeedleTask(prompt=prompt, answer=answer, position=position, target_chars=target_chars)


def exact_score(output: str, answer: str) -> float:
    return float(output.strip() == answer.strip())
