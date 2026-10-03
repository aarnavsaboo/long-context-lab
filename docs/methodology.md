# Long-context methodology

The experiments in this repository distinguish nominal context capacity from useful evidence use.

## Task construction

Synthetic documents contain a deterministic target fact at a known relative position. Filler text and target placement are generated from explicit inputs so the same task can be reconstructed across model runs.

The main dimensions are:

- target prompt length
- target evidence position
- model/runtime
- input strategy
- generation budget
- repeated trials

## Strategy boundary

Each strategy receives the same generated task and produces the prompt material that reaches the model.

```text
synthetic task
   |
   +--> full prompt
   +--> sliding windows
   +--> lexical retrieval
   +--> extractive compression
            |
            v
        local model
            |
            v
      answer + timings
```

This keeps prompt-construction effects separate from answer scoring.

## Measurements

A result should retain the target code, generated answer, strategy parameters, approximate prompt size, evidence position and runtime timing data. Reports group by both length and position so middle-of-context failures are not hidden by an overall average.

## Controls

When comparing strategies, keep model, generation parameters and task seed constant. Warm and cold runs should not be mixed into one latency summary.

A successful answer at a long prompt length does not prove stable behavior across positions. Likewise, a retrieval strategy that is faster may fail if the evidence-ranking step misses the relevant window.

## Reproducibility

Model revision, tokenizer/runtime version and machine information matter for context experiments. They should travel with exported results when performance numbers are compared across environments.
