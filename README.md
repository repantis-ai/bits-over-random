# Bits-over-Random

Small Python utilities for chance-corrected retrieval evaluation.

Based on the ICLR 2026 Blog Poster Track paper:

**The 99% Success Paradox: When Near-Perfect Retrieval Equals Random Selection**

![Poster](poster.png)

[Blog](https://iclr-blogposts.github.io/2026/blog/2026/bits-over-random/) |
[Poster](https://iclr.cc/virtual/2026/poster/10012083)

## Why this exists

Raw retrieval metrics such as Success@K and Recall@K can look strong when random selection would also succeed.

Bits-over-Random compares observed success against the success expected from a blind draw over the same corpus.

Each bit is one doubling over random chance.

## What BoR measures

For a corpus of N items with R relevant items, and a retrieval depth K, random selection has its own success rate.

BoR asks:

> How many bits better than random was the observed retrieval result?

- BoR = log2(P_observed / P_random)
- BoR = 0: no better than random
- BoR = 1: 2x better than random
- BoR = 3: 8x better than random
- BoR < 0: worse than random

## Install locally

Before using, install:

```bash
pip install -e .
```

## Quick example

```python
from bor import random_success_at_least_one, bits_over_random

N = 400_000
R = 20_000  # 5% of the corpus
K = 100

p_rand = random_success_at_least_one(N=N, R=R, K=K)
bor = bits_over_random(observed=1.0, random_baseline=p_rand)

print(p_rand)  # about 0.994
print(bor)     # near zero bits
```

## Command line

```bash
bor --N 400000 --R 20000 --K 100 --observed 1.0
```

Example output:

```bash
Random baseline: 0.9941
Bits-over-Random: 0.0086
lambda: 5.0000
warning: random baseline is already near 1.0
warning: lambda is in the collapse zone
```

## Examples

```bash
python examples/case2_lottery.py
python examples/tool_selection_58.py
```

## Intuition

Retrieval systems are often evaluated by whether at least one relevant item appears in the top K. That is useful, but it does not ask how hard the task was.

If relevant items are common, or K is large, a blind draw can also succeed. BoR asks how far above that random baseline the system actually is.

## Citation

If you use this code, please cite:

```bibtex
Repantis et al., "The 99% Success Paradox: When Near-Perfect Retrieval Equals Random Selection," ICLR Blogposts, 2026.
```

BibTeX citation:

```bibtex
@inproceedings{repantis2026the99success,
  author = {Repantis, Vyzantinos and Singh, Harshvardhan and Joseph, Tony and Zhang, Cien and Vishwakarma, Akash and Karslioglu, Svetlana and Thot, Michael Wyatt and Gawde, Ameya},
  title = {The 99% Success Paradox: When Near-Perfect Retrieval Equals Random Selection},
  abstract = {For most of the history of information retrieval (IR), search results were designed for human consumers who could scan, filter, and discard irrelevant information on their own. This shaped retrieval systems to optimize for finding and ranking more relevant documents, but not keeping results clean and minimal, as the human was the final filter. However, LLMs have changed that by lacking this filtering ability. To address this, we introduce Bits-over-Random (BoR), a chance-corrected measure of retrieval selectivity that reveals when high success rates mask random-level performance.},
  booktitle = {ICLR Blogposts 2026},
  year = {2026},
  date = {April 27, 2026},
  note = {https://iclr-blogposts.github.io/2026/blog/2026/bits-over-random/},
  url  = {https://iclr-blogposts.github.io/2026/blog/2026/bits-over-random/}
}
```
