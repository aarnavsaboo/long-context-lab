# Reading the result table

Do not average evidence position away too early.

A model can score well when the fact is near the beginning and end while missing the same fact in the middle. Grouping by both target length and position keeps that behaviour visible.

Retrieval and compression can lower prompt cost dramatically, but they introduce another failure mode: the evidence may not be selected at all. The final report therefore keeps accuracy and sent prompt size together.
