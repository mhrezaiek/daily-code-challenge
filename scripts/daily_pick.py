#!/usr/bin/env python3
"""
daily_pick.py — pick a random number of questions from the active pool,
write a daily-solutions folder skeleton, then rotate replenish_pool entries
back into active_pool so the pool stays roughly full.

Usage:
    python3 daily_pick.py                # uses today's date
    python3 daily_pick.py 2026-05-12     # backfill for a specific date
"""
from __future__ import annotations
import json
import random
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUESTIONS_FILE = ROOT / "questions.json"
SOLUTIONS_DIR = ROOT / "solutions"

# Realistic-looking range: 1–4 commits per active day, with occasional 5.
# Some days the picker will roll 0 → caller can skip that day (mimics a rest day).
DAILY_RANGE = (1, 4)
REST_DAY_PROB = 0.10  # 10% chance of a "no commits" day


def pick(today: date) -> tuple[list[dict], dict]:
    data = json.loads(QUESTIONS_FILE.read_text())
    rng = random.Random(today.isoformat())  # deterministic per day

    if rng.random() < REST_DAY_PROB:
        return [], data

    active = data["active_pool"]
    replenish = data["replenish_pool"]

    n = rng.randint(*DAILY_RANGE)
    n = min(n, len(active))
    chosen = rng.sample(active, n)

    chosen_ids = {q["id"] for q in chosen}
    remaining = [q for q in active if q["id"] not in chosen_ids]

    # Refill active_pool from replenish_pool to keep it at the original size.
    needed = len(active) - len(remaining)
    take = min(needed, len(replenish))
    refill, replenish_left = replenish[:take], replenish[take:]
    new_active = remaining + refill

    data["active_pool"] = new_active
    data["replenish_pool"] = replenish_left
    return chosen, data


def write_daily_readme(today: date, chosen: list[dict]) -> Path:
    day_dir = SOLUTIONS_DIR / today.isoformat()
    day_dir.mkdir(parents=True, exist_ok=True)
    readme = day_dir / "README.md"
    lines = [f"# Daily Code Challenge — {today.isoformat()}", ""]
    if not chosen:
        lines.append("_Rest day — no problems solved._")
    else:
        lines.append(f"Solved {len(chosen)} problem(s) today:\n")
        for q in chosen:
            lines.append(f"- **{q['title']}** ({q['difficulty']}, {q['topic']}) — `{q['id']}.py`")
        lines.append("")
        lines.append("## Prompts")
        for q in chosen:
            lines.append(f"\n### {q['title']}\n\n> {q['prompt']}")
    readme.write_text("\n".join(lines) + "\n")
    return day_dir


def main() -> int:
    today = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today()
    chosen, new_data = pick(today)
    day_dir = write_daily_readme(today, chosen)

    # Persist updated question pool.
    QUESTIONS_FILE.write_text(json.dumps(new_data, indent=2) + "\n")

    print(f"Date: {today.isoformat()}")
    print(f"Output dir: {day_dir}")
    print(f"Picked {len(chosen)} problem(s):")
    for q in chosen:
        print(f"  - {q['id']} ({q['difficulty']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
