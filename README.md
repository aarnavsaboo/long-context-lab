# long-context-lab

Local-model experiments for understanding what changes as prompts become long.

The repository builds controlled synthetic tasks where a required fact appears at a known position inside a growing prompt. It then runs the same task through several input strategies—full prompt, sliding windows, simple retrieval and extractive compression—and records both answer accuracy and runtime behaviour.

The goal is not to produce a single "maximum context" number. Capacity, latency and useful evidence use are different measurements.

## Experiment matrix

Typical sweeps vary:

- approximate prompt tokens
- evidence position
- local model
- generation budget
- full-prompt vs retrieval mode
- sliding-window size and overlap
- number of retrieved windows
- repeated trials
- warm/cold model state

## Strategies

### Full prompt

Send the entire synthetic document to the local model.

### Sliding windows

Split the document into overlapping windows and run the question against each selected window.

### Lexical retrieval

Rank windows using a small local BM25 implementation and send only the top windows.

### Extractive compression

Select sentences with the strongest lexical relation to the question until a character budget is reached.

None of these strategies is assumed to win. The point is to locate where additional prompt capacity stops being useful for a particular local model.

## Workflow

```text
experiment.json
      |
      v
task generator
      |
      +--> length
      +--> evidence position
      +--> randomized filler
      |
      v
strategy builder
      |
      +--> full
      +--> windows
      +--> retrieval
      +--> compression
      |
      v
local runtime
      |
      +--> answer
      +--> token counts
      +--> latency
      |
      v
raw JSONL
      |
      v
length x position report
```

## Example

```bash
python -m long_context_lab plan configs/sweep.example.json > runs/plan.jsonl

python -m long_context_lab run \
  runs/plan.jsonl \
  --model qwen3:4b \
  --out runs/results.jsonl

python -m long_context_lab report runs/results.jsonl
```

## Useful outputs

The report groups by strategy, target prompt size and evidence position. This makes "lost in the middle" style failures visible without averaging positions together.

Per-run records preserve the generated answer and exact expected code, so scoring can be regenerated later.

## Repository layout

- `needles.py` — deterministic synthetic tasks
- `windows.py` — overlapping input windows
- `retrieval.py` — local lexical window ranking
- `compression.py` — extractive budget reduction
- `planner.py` — experiment matrix
- `ollama.py` — local generation adapter
- `runner.py` — strategy execution
- `report.py` — length/position summaries
- `configs/` — sweep manifests
- `tests/` — deterministic tests

Maintained by **Aarnav Saboo**.
