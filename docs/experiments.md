# Suggested experiments

A useful matrix varies prompt size and evidence position separately. Repeating each cell with different filler text avoids accidentally measuring one phrase pattern.

Compare at least four modes:

- one full prompt;
- sliding windows with a fixed overlap;
- retrieval of the most similar windows;
- an extractive summary followed by generation.

Record answer accuracy, wall-clock latency, input tokens and output tokens for every attempt. Local runtimes can show large warm/cold differences, so record model load separately where possible.

"Supports 32k context" is a capacity statement, not an accuracy statement. The aim of this lab is to make that distinction visible.
