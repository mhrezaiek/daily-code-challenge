# Daily Code Challenge

Daily algorithm and data-science practice. Each day's batch lives in
`solutions/YYYY-MM-DD/` with a per-folder README explaining the
approach, complexity, and pitfalls of each problem.

## Stats

- **Total solved:** 8
- **Current streak:** active (latest entry 2026-05-14)
- **Last 7 days bucket coverage:** `dp` ×3, `classic-dsa` ×2, `trees-graphs` ×1, `ml-coding` ×1, `sql` ×1

### Breakdown by bucket

| Bucket                   | Count |
|--------------------------|-------|
| classic-dsa              | 2     |
| dp                       | 3     |
| trees-graphs             | 1     |
| ml-coding                | 1     |
| sql                      | 1     |
| pandas                   | 0     |
| numerical-matrix         | 0     |
| probability-stats        | 0     |
| system-design-adjacent   | 0     |

### Breakdown by difficulty

| Difficulty | Count |
|------------|-------|
| easy       | 1     |
| medium     | 6     |
| hard       | 1     |

## Topic rotation (data-scientist focused)

1. Classic DSA — arrays, strings, two-pointer, sliding window, hashing
2. Trees & graphs — BFS, DFS, topological sort, union-find, shortest paths
3. Dynamic programming — 1D, 2D, knapsack, LIS, interval DP
4. ML-coding — k-means, gradient descent, logistic regression, k-NN, softmax, attention, etc.
5. Numerical / matrix — NumPy puzzles, linear algebra
6. SQL — window functions, joins, aggregations
7. Pandas — group-bys, transformations, time-series
8. Probability & stats — sampling, A/B math, Bayesian puzzles
9. System-design-adjacent — LRU, rate limiter, tokenizer, consistent hashing

## Repo layout

```
daily-code-challenge/
├── README.md             # this file (stats + overview)
├── backlog.md            # researched problems queued for future days
├── solved-index.md       # every problem ever solved (de-dup ledger)
├── questions.json        # legacy curated pool used by scripts/daily_pick.py
├── scripts/
│   ├── daily_pick.py     # random selection over the curated pool
│   └── push_to_github.sh # one-shot commit + push helper
└── solutions/
    └── YYYY-MM-DD/
        ├── README.md                       # day summary + per-problem write-up
        └── <bucket>-<slug>.(py|sql)        # one file per problem
```

## Daily workflow (automated agent)

A scheduled agent runs every morning and:

1. Researches 5–10 new problems across the buckets above, appending to
   `backlog.md`.
2. Selects 3–5 (max 5) for today, biasing toward buckets uncovered in
   the last 5 days and keeping a difficulty mix.
3. Solves each into `solutions/YYYY-MM-DD/<bucket>-<slug>.(py|sql)`
   with tests, complexity notes, and a per-folder README.
4. Updates `solved-index.md`, prunes solved entries from `backlog.md`,
   and refreshes these stats.
5. Commits and pushes to `main`.

All Python solutions ship with an `if __name__ == "__main__":` block
that runs assertion-based tests — `python3 <file>.py` exits 0 on
success.

## Quality bar

- No brute force unless it is genuinely optimal (justified in the
  per-problem README if so).
- Every problem traces to a real source URL — no fabrication.
- No repeats from `solved-index.md`.
- ML-coding solutions are written from scratch in NumPy, with an
  optional cross-check against scikit-learn when applicable.

## Today (2026-05-14)

Buckets covered today: `classic-dsa`, `trees-graphs`, `ml-coding`, `sql`.
See [`solutions/2026-05-14/README.md`](solutions/2026-05-14/README.md)
for the full write-up.
