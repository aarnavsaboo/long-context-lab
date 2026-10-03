import re

from .retrieval import tokenize


def sentences(text: str) -> list[str]:
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+",text) if x.strip()]


def compress(text: str, query: str, max_chars: int) -> str:
    q = set(tokenize(query))
    scored = []
    for i,sentence in enumerate(sentences(text)):
        words = set(tokenize(sentence))
        overlap = len(q & words)
        density = overlap/max(1,len(words))
        scored.append((overlap,density,-i,sentence))
    ranked = [x[-1] for x in sorted(scored,reverse=True)]
    selected = []
    used = 0
    for sentence in ranked:
        block = sentence + " "
        if used + len(block) > max_chars:
            continue
        selected.append(sentence)
        used += len(block)
    return " ".join(selected)
