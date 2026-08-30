#!/usr/bin/env python3
"""Extract theorem-like/high-risk claims from LaTeX. Diagnostic only."""
from pathlib import Path
import re, sys

ENV_RE = re.compile(r'\\begin\{(theorem|proposition|lemma|corollary)\}(.*?)\\end\{\1\}', re.I | re.S)
RISK = [
    ('equivalence', re.compile(r'\b(equivalent|equivalently|exact reformulation|if and only if)\b', re.I)),
    ('duality', re.compile(r'\b(strong duality|zero duality gap|dualiz)\w*', re.I)),
    ('minimax', re.compile(r'\b(minimax|interchange|swap(?:ping)? (?:the )?(?:inf|sup|max|min))\b', re.I)),
    ('finite-sample', re.compile(r'\b(finite[- ]sample|with probability|confidence bound|coverage guarantee|out[- ]of[- ]sample)\b', re.I)),
    ('asymptotic', re.compile(r'\b(asymptotic|consistent|consistency|almost surely|converges? in probability)\b', re.I)),
    ('tractability', re.compile(r'\b(tractable|polynomial time|second[- ]order cone|semidefinite|mixed[- ]integer|conic reformulation)\b', re.I)),
]

def clean(s):
    s = re.sub(r'%.*', '', s)
    return re.sub(r'\s+', ' ', s).strip()

def main():
    if len(sys.argv) != 2:
        print('usage: claim_inventory.py manuscript.tex', file=sys.stderr); return 2
    p = Path(sys.argv[1]); text = p.read_text(errors='replace'); claims = []
    for m in ENV_RE.finditer(text):
        body = clean(m.group(2)); line = text.count('\n', 0, m.start()) + 1
        tags = [name for name, rgx in RISK if rgx.search(body)]
        claims.append((line, m.group(1).lower(), tags, body[:500]))
    print(f'# Claim inventory: {p.name}')
    for line, kind, tags, body in claims:
        print(f'\n- line {line} [{kind}] risk={",".join(tags) if tags else "general"}\n  {body}')
    print(f'\nTotal theorem-like environments: {len(claims)}'); return 0

if __name__ == '__main__': raise SystemExit(main())
