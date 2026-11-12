import re, json, sys, pathlib
from bs4 import BeautifulSoup, NavigableString
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

OUT = pathlib.Path('output/datetrace')

def norm(t):
    return re.sub(r'\s+', ' ', t).strip()

def options_of(ctrl_html):
    """Extract option labels from raw <select> markup (handles unclosed tags)."""
    opts = []
    for m in re.finditer(r'<option\b[^>]*>([^<]*)', ctrl_html):
        t = norm(m.group(1))
        if t and 'sélectionner' not in t.lower() and '— sélectionner' not in t:
            opts.append(t)
    # dedupe preserving order
    seen = set(); out = []
    for o in opts:
        if o not in seen:
            seen.add(o); out.append(o)
    return out

def extract(path):
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    scope = soup.find('form') or soup.body or soup
    fields = []
    for lab in scope.find_all('label'):
        lt = norm(lab.get_text(' ', strip=True))
        if not lt:
            continue
        # next control or next label, whichever comes first in doc order
        nxt_ctrl = lab.find_next(['input', 'select', 'textarea'])
        nxt_lab = lab.find_next('label')
        if nxt_lab and nxt_lab.sourceline and nxt_ctrl and nxt_ctrl.sourceline \
           and nxt_lab.sourceline < nxt_ctrl.sourceline:
            ctrl = None
        else:
            ctrl = nxt_ctrl
        if ctrl is None:
            continue
        if ctrl.name == 'input':
            kind = ctrl.get('type', 'text')
            if kind == 'checkbox':
                kind = 'checkbox'
        elif ctrl.name == 'textarea':
            kind = 'textarea'
        else:
            kind = 'select'
        req = ctrl.has_attr('required') or '*' in lt
        ph = ctrl.get('placeholder', '') or ''
        opts = options_of(str(ctrl)) if ctrl.name == 'select' else []
        fields.append({'label': lt, 'type': kind, 'required': req,
                       'placeholder': ph, 'options': opts})
    # dedupe identical labels
    seen = set(); out = []
    for d in fields:
        key = (d['label'], d['type'])
        if key not in seen:
            seen.add(key); out.append(d)
    return out

report = {}
for f in sorted(OUT.glob('*--form.html')):
    mod = f.name.replace('--form.html', '')
    report[mod] = extract(f)
    print('=' * 15, mod)
    for d in report[mod]:
        print('  ', json.dumps(d, ensure_ascii=False))

pathlib.Path('fields.json').write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
