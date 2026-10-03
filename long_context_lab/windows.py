def windows(text: str, size: int, overlap: int) -> list[str]:
    if size <= 0 or overlap < 0 or overlap >= size:
        raise ValueError("require size > overlap >= 0")
    out = []
    step = size - overlap
    for start in range(0, len(text), step):
        part = text[start:start + size]
        if part:
            out.append(part)
        if start + size >= len(text):
            break
    return out


def locate(text: str, fragment: str) -> float:
    index = text.find(fragment)
    if index < 0:
        return -1.0
    return index / max(1, len(text) - len(fragment))
