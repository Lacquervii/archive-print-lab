#!/usr/bin/env python3
# Validate the Archive Print Lab package (generator-agnostic prompt skill).
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
required=[
 'SKILL.md','manifest.json',
 'references/decision-router.md','references/theme-grammar.md','references/graphic-chassis.md','references/rendering-branches.md','references/theme-compiler.md','references/theme-customization-contract.md','references/family-standard.md','references/aspect-ratio-contract.md','references/composition-planner.md','references/prompt-renderer.md','references/poster-mechanics.md','references/structural-scale-ladder.md','references/editorial-imprint.md','references/image2-editorial-adapter.md','references/backend-adapters.md',
 'workflows/adapt-reference.md','workflows/generate-review.md','workflows/optimize-skill.md',
 'schemas/brief.schema.json','schemas/compiled-theme.schema.json','schemas/composition-plan.schema.json','schemas/review.schema.json','schemas/series-contract.schema.json','scripts/validate_skill.py'
]
errors=[]
for rel in required:
 if not (ROOT/rel).is_file(): errors.append('missing: '+rel)
skill=(ROOT/'SKILL.md').read_text(encoding='utf8') if (ROOT/'SKILL.md').exists() else ''
for phrase in ['Archive Print Lab','旧档博物志','9010-derived editorial','Backend-agnostic contract','prompt-renderer.md','surface selection','family roles']:
 if phrase.lower() not in skill.lower(): errors.append('SKILL missing: '+phrase)
if 'Image2-only' in skill: errors.append('SKILL still claims an Image2-only requirement')
if 'archive-print-lab' not in (ROOT/'references'/'editorial-imprint.md').read_text(encoding='utf8'): errors.append('editorial imprint missing')
try:
 m=json.loads((ROOT/'manifest.json').read_text(encoding='utf8'))
 if m.get('name')!='archive-print-lab': errors.append('manifest name mismatch')
 if m.get('display_name')!='Archive Print Lab / 旧档博物志': errors.append('manifest display name mismatch')
 if m.get('version')!='5.1.0': errors.append('manifest version mismatch')
 if m.get('optional_cases'): errors.append('public package retains optional cases')
 if m.get('evidence_sources'): errors.append('public package retains private evidence sources')
 for rel in m.get('core',[]):
  if not (ROOT/rel).is_file(): errors.append('manifest points to missing resource: '+rel)
except Exception as e: errors.append('manifest invalid: '+str(e))
for rel in ['brief.schema.json','compiled-theme.schema.json','composition-plan.schema.json','review.schema.json','series-contract.schema.json']:
 try: json.loads((ROOT/'schemas'/rel).read_text(encoding='utf8'))
 except Exception as e: errors.append('schema invalid '+rel+': '+str(e))
for p in ROOT.rglob('*'):
 if p.is_file() and ('__pycache__' in p.parts or p.suffix=='.pyc'): errors.append('cache artifact: '+str(p.relative_to(ROOT)))
if (ROOT/'references'/'prompt-renderer-image2.md').exists(): errors.append('stale image2-only renderer file remains')
if errors:
 print('FAIL'); print('\n'.join(errors)); raise SystemExit(1)
print('PASS'); print('name=archive-print-lab'); print('display_name=Archive Print Lab / 旧档博物志'); print('version=5.1.0'); print('required_files='+str(len(required)))