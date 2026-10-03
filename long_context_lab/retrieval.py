from collections import Counter
from math import log
import re

from .windows import windows


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+", text.casefold())


def rank_windows(text: str, query: str, size: int, overlap: int, top_k: int) -> list[str]:
    parts = windows(text,size,overlap)
    counts = [Counter(tokenize(x)) for x in parts]
    lengths = [sum(c.values()) for c in counts]
    avg = sum(lengths)/max(1,len(lengths))
    df = Counter(term for c in counts for term in c)
    idf = {term:log(1+(len(parts)-freq+.5)/(freq+.5)) for term,freq in df.items()}
    terms = set(tokenize(query))
    scored = []
    for i,(part,c,length) in enumerate(zip(parts,counts,lengths)):
        score = 0.0
        for term in terms:
            tf = c.get(term,0)
            if tf:
                score += idf.get(term,0)*tf*2.5/(tf+1.5*(.25+.75*length/max(avg,1e-9)))
        scored.append((i,score,part))
    return [part for _,score,part in sorted(scored,key=lambda x:(-x[1],x[0]))[:top_k] if score>0]
