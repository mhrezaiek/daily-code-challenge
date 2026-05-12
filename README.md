# Daily Code Challenge

Daily algorithm practice that doubles as steady GitHub contribution-graph activity.

## How it works

Each day at 9:00 the scheduled task runs `scripts/daily_pick.py`, which:

1. Seeds Python's RNG with the date so the day's picks are reproducible.
2. With ~10% probability, declares a **rest day** and writes nothing — this keeps
   the graph looking organic instead of suspiciously uniform.
3. Otherwise picks 1–4 problems from `questions.json -> active_pool`.
4. Writes `solutions/YYYY-MM-DD/README.md` listing the day's prompts.
5. Removes the chosen questions from `active_pool` and refills it from `replenish_pool`.

Solutions themselves are written into `solutions/YYYY-MM-DD/<problem>.py`,
each with assertion-based tests at the bottom. Run any file directly
(`python3 maximum_subarray.py`) to verify.

## Layout

```
daily-code-challenge/
├── README.md                   # this file
├── questions.json              # active_pool + replenish_pool (state)
├── scripts/
│   ├── daily_pick.py           # picks today's problems, rotates the pool
│   └── push_to_github.sh       # commits today's folder and pushes
└── solutions/
    └── 2026-05-12/
        ├── README.md
        ├── maximum_subarray.py
        └── coin_change.py
```

## One-time GitHub setup

The sandbox where the scheduled task runs has **no git credentials**, so it
can't push to your account on its own. Do this once on your own machine,
then point the schedule at the clone:

```bash
# 1. Create a private repo on GitHub, e.g. `daily-code-challenge`.
# 2. Clone it somewhere persistent and copy this project's contents into it:
git clone git@github.com:<your-username>/daily-code-challenge.git
cp -R /path/to/this/folder/* daily-code-challenge/
cd daily-code-challenge
git add . && git commit -m "Initial pool + 2026-05-12 solutions" && git push

# 3. Make sure `git push` works from cron / launchd without prompting:
#    - Use an SSH key with no passphrase loaded into ssh-agent at login, OR
#    - Use a Personal Access Token stored via `git credential-helper osxkeychain`.
```

After that, future scheduled runs only need to:
1. Re-run `scripts/daily_pick.py` (already done — it persists state in-place).
2. Add the new files and `git commit && git push`.

`scripts/push_to_github.sh` does steps 1 and 2 in one shot.

## Tuning

Edit constants at the top of `scripts/daily_pick.py`:

- `DAILY_RANGE = (1, 4)` — min/max problems per active day.
- `REST_DAY_PROB = 0.10` — fraction of days that skip entirely.

To make the graph **more** active, raise the upper bound and lower the rest probability.
To make it **less** active, do the opposite.

## Notes from today's run (2026-05-12)

- This sandbox has no GitHub credentials, so today's solutions were only written
  to disk — not pushed. After completing the one-time setup above, run
  `scripts/push_to_github.sh 2026-05-12` to retroactively push today's commit.
- Picked: **Maximum Subarray** (Kadane's) and **Coin Change** (bottom-up DP).
- Both files include built-in assertion tests; `python3 <file>.py` exits 0 on success.
