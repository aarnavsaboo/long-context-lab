# long-context-lab

Utilities for testing what actually happens as prompts get long on local language models.

The repository builds synthetic "needle" tasks with controlled answer positions, creates prompt-length sweeps, and records accuracy together with latency. It is useful for comparing full-context prompting against sliding windows, retrieval and compact summaries without relying on one anecdotal long prompt.

## Questions this lab is meant to answer

- does answer accuracy change when the relevant passage moves from the start to the middle or end?
- when does a larger context window become slower than retrieval plus a smaller prompt?
- how much repeated filler changes latency on a local runtime?
- do sliding windows recover facts that a single long prompt misses?
- when does compression remove the evidence needed to answer?

```bash
python -m long_context_lab make --tokens 8192 --position 0.5
```

The generated tasks are synthetic by design. They are diagnostics for context handling, not claims about general reasoning ability.

Maintained by **Aarnav Saboo**.
