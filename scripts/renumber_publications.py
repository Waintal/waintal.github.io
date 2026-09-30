#!/usr/bin/env python3
"""Sort data/publications.yaml by year (newest first) and renumber the entries so that numbers
decrease from top to bottom (the oldest paper is 1). Within a year the existing order is kept.
Rewrites the file in place (text-based, keeps the formatting). Standard library only.

Usage:  python3 scripts/renumber_publications.py
"""
import re
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "publications.yaml"

text = DATA.read_text()
parts = re.split(r"^(?=- n: )", text, flags=re.M)
header, blocks = parts[0], parts[1:]
year = lambda b: int(re.search(r"^\s+year: (\d{4})", b, re.M).group(1))
blocks = sorted(blocks, key=year, reverse=True)  # stable: keeps order within a year
total = len(blocks)
blocks = [re.sub(r"^- n: \d+", f"- n: {total - i}", b, count=1) for i, b in enumerate(blocks)]
DATA.write_text(header + "".join(b if b.endswith("\n") else b + "\n" for b in blocks))
print(f"{total} entries sorted and renumbered")
