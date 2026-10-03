from collections import defaultdict
from statistics import median


def summarize(rows:list[dict])->list[dict]:
    groups=defaultdict(list)
    for row in rows:
        groups[(row["strategy"],row["target_tokens"],row["position"])].append(row)
    output=[]
    for (strategy,tokens,position),group in sorted(groups.items()):
        output.append({
            "strategy":strategy,
            "target_tokens":tokens,
            "position":position,
            "runs":len(group),
            "accuracy":sum(float(x["score"]) for x in group)/len(group),
            "median_latency_s":median(float(x["elapsed_seconds"]) for x in group),
            "median_sent_chars":median(int(x["sent_chars"]) for x in group),
            "median_prompt_tokens":median(
                [int(x["prompt_tokens"]) for x in group if x.get("prompt_tokens") is not None]
            ) if any(x.get("prompt_tokens") is not None for x in group) else None,
        })
    return output
