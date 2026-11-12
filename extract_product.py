# -*- coding: utf-8 -*-
"""Extrait tous les champs de formulaires d'un produit du clone (pages --form
et variantes iso22000--* qui contiennent un <form>). Usage: python extract_product.py <produit>"""
import re, json, sys, pathlib
from bs4 import BeautifulSoup
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

prod = sys.argv[1]
OUT = pathlib.Path('output') / prod

def norm(t):
    return re.sub(r'\s+', ' ', t).strip()

def options_of(ctrl_html):
    opts, seen = [], set()
    for m in re.finditer(r'<option\b[^>]*>([^<]*)', ctrl_html):
        t = norm(m.group(1))
        if t and 'sélectionner' not in t.lower() and t.lower() != 'select...' and t not in seen:
            seen.add(t); opts.append(t)
    return opts

def extract_fields(scope):
    fields = []
    for lab in scope.find_all('label'):
        lt = norm(lab.get_text(' ', strip=True))
        if not lt:
            continue
        nxt_ctrl = lab.find_next(['input', 'select', 'textarea'])
        nxt_lab = lab.find_next('label')
        if nxt_lab is not None and nxt_ctrl is not None:
            # si un autre label arrive avant le prochain contrôle -> champ sans input (boutons)
            try:
                if nxt_lab < nxt_ctrl:
                    nxt_ctrl = None
            except Exception:
                pass
        if nxt_ctrl is None:
            fields.append({'label': lt, 'type': 'boutons', 'required': '*' in lt,
                           'placeholder': '', 'options': []})
            continue
        if nxt_ctrl.name == 'input':
            kind = nxt_ctrl.get('type', 'text')
        elif nxt_ctrl.name == 'textarea':
            kind = 'textarea'
        else:
            kind = 'select'
        fields.append({'label': lt, 'type': kind,
                       'required': nxt_ctrl.has_attr('required') or '*' in lt,
                       'placeholder': nxt_ctrl.get('placeholder', '') or '',
                       'options': options_of(str(nxt_ctrl)) if nxt_ctrl.name == 'select' else []})
    seen, out = set(), []
    for d in fields:
        key = (d['label'], d['type'])
        if key not in seen:
            seen.add(key); out.append(d)
    return out

report = {}
for f in sorted(OUT.glob('*.html')):
    if '--' not in f.name:
        continue
    soup = BeautifulSoup(f.read_text(encoding='utf-8'), 'html.parser')
    for fi, form in enumerate(soup.find_all('form')):
        flds = extract_fields(form)
        if not flds:
            continue
        mod = f.name.split('--')[0]
        suffix = '' if fi == 0 else f'#{fi+1}'
        if f.name.startswith('iso22000--'):
            tab = f.name.replace('iso22000--', '').replace('.html', '')
            key = f'iso22000-{tab}'
        else:
            key = f.name.replace('--form.html', '').replace('--', '-')
        report.setdefault(key, {'file': f.name, 'fields': []})['fields'].extend(flds)
    if soup.find_all('label') and not soup.find('form'):
        # formulaire sans <form> (modale en div) : on tente sur tout le body
        flds = extract_fields(soup.body) if soup.body else []
        if flds:
            report.setdefault(f.name.replace('--form.html','').replace('--','-'),
                              {'file': f.name, 'fields': []})['fields'].extend(flds)

pathlib.Path(f'fields_{prod}.json').write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
print(prod, '->', len(report), 'entités')
for k, v in report.items():
    print(f"  {k:35s} {v['file']:35s} {len(v['fields'])} champs")
