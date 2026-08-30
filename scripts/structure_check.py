#!/usr/bin/env python3
"""Validate the minimum structure of the RO/DRO skill package."""
from pathlib import Path
import sys

REQUIRED = [
    'SKILL.md', 'CORE_PRINCIPLES.md',
    'references/notation_conventions.md',
    'references/source_hierarchy.md',
    'references/dro_canonical_map.md',
    'tasks/reformulate.md', 'tasks/finite_sample.md',
    'auditor/VETO_POLICY.md',
    'auditor/reformulation_auditor.md',
    'auditor/equivalence_object_auditor.md',
    'auditor/statistical_auditor.md',
    'auditor/multistage_statistical_auditor.md',
    'auditor/statistical_computational_composition_auditor.md',
    'auditor/internal_consistency_auditor.md',
    'auditor/oracle_quantity_auditor.md',
    'auditor/deviation_regime_auditor.md',
    'auditor/process_law_auditor.md',
    'auditor/sufficiency_compression_auditor.md',
    'templates/reformulation_ledger.md',
    'templates/randomness_map.md',
    'templates/multistage_randomness_map.md',
    'templates/rate_anatomy.md',
    'templates/deviation_regime_ledger.md',
    'templates/process_randomness_map.md',
    'references/dependent_process_statistics.md',
]

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
    failures = []
    for rel in REQUIRED:
        if not (root / rel).is_file(): failures.append(f'missing: {rel}')
    skill = root / 'SKILL.md'
    if skill.is_file():
        text = skill.read_text(errors='replace')
        if not text.startswith('---\n'): failures.append('SKILL.md: missing YAML frontmatter')
        if 'name: ro-dro-research' not in text[:1000]: failures.append('SKILL.md: unexpected/missing name')
        if 'Auditor' not in text or 'veto' not in text.lower(): failures.append('SKILL.md: veto-powered audit rule not found')
    manifest = root / 'manifest.txt'
    if manifest.is_file():
        listed = [x.strip() for x in manifest.read_text().splitlines() if x.strip()]
        actual = sorted(str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.name != 'manifest.txt')
        if sorted(listed) != actual: failures.append('manifest.txt does not match package files')
    if failures:
        print('structure_check: FAIL')
        for f in failures: print(' -', f)
        return 1
    print('structure_check: PASS'); return 0

if __name__ == '__main__': raise SystemExit(main())
