#!/usr/bin/env python3
"""Write one pigeon startup pitch to /output/entry.txt.

Entry (162 chars, limit 200): a city pigeon's elevator pitch to
investors — traction in tons of crumbs, zero payroll, 40,000 pigeons,
every park bench a pickup point, and the ask: $2M in seed, literally
seed. Pigeon voice, concrete numbers, twist in the last two words.
"""
import os

LINE = "Coo moves 12 tons of crumbs a day with zero payroll \u2014 40,000 pigeons, one app, and every park bench is a pickup point. We are raising $2M in seed. Literally seed."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, limit 200"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars")


if __name__ == "__main__":
    main()
