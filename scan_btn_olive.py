import re, sys, pathlib
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
for f in sorted(pathlib.Path('output/olivetrace').glob('*.html')):
    if '--' not in f.name: continue
    s = f.read_text(encoding='utf-8')
    for m in re.finditer(r'<label[^>]*>(.*?)</label>(.{0,120}?)<div class="[^"]*grid[^"]*"><button', s, re.S):
        print(f.name, '->', re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',m.group(1))).strip()[:60])
