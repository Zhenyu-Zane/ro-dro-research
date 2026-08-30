#!/usr/bin/env python3
"""Conservative notation linter for RO/DRO LaTeX manuscripts.

This script only flags suspicious patterns. It never edits the source and does not
attempt to infer whether a plain symbol is a scalar or vector.
"""
from pathlib import Path
import re, sys

RULES = [
    (r'\\mathbf\s*\{', "Use \\bm{...} for vectors/matrices under the binding notation."),
    (r'\\boldsymbol\s*\{', "Use \\bm{...} for vectors/matrices under the binding notation."),
    (r'P_0\s*\(', "Probability-law space should normally be \\mathcal{M}(...) under the binding notation."),
    (r'\\mathcal\{P\}_0\s*\(', "Probability-law space should normally be \\mathcal{M}(...) under the binding notation."),
    (r'\\mathbb\{E\}\s*\[', "Expectation normally needs a distribution subscript, e.g. \\mathbb{E}_{\\mathbb{P}}[...]."),
]

def main():
    if len(sys.argv) != 2:
        print('usage: notation_lint.py manuscript.tex', file=sys.stderr)
        return 2
    p = Path(sys.argv[1])
    text = p.read_text(errors='replace')
    lines = text.splitlines()
    n = 0
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith('%'):
            continue
        for pat, msg in RULES:
            if re.search(pat, line):
                n += 1
                print(f'{p}:{i}: WARNING: {msg}\n    {line.strip()}')
    print(f'notation_lint: {n} warning(s)')
    return 1 if n else 0

if __name__ == '__main__':
    raise SystemExit(main())
