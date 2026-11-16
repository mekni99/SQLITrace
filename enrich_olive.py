# Enrich OliveTrace pages with realistic demo data (clone existing DOM rows/cards)
import re, sys, os

THERMO_SVG = '<svg xmlns=http://www.w3.org/2000/svg width=24 height=24 viewBox="0 0 24 24" fill=none stroke=currentColor stroke-width=2 stroke-linecap=round stroke-linejoin=round class="lucide lucide-thermometer w-5 h-5 text-sky-600"><path d="M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z"></path></svg>'
FILE_SVG = '<svg xmlns=http://www.w3.org/2000/svg width=24 height=24 viewBox="0 0 24 24" fill=none stroke=currentColor stroke-width=2 stroke-linecap=round stroke-linejoin=round class="lucide lucide-file-text w-4 h-4 text-blue-600"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path><path d="M14 2v4a2 2 0 0 0 2 2h4"></path><path d="M10 9H8"></path><path d="M16 13H8"></path><path d="M16 17H8"></path></svg>'

warn = []

def sub(s, pairs, ctx):
    for old, new in pairs:
        s2, n = re.subn(old, new, s, count=1)
        if n == 0:
            warn.append(f"{ctx}: pattern NOT FOUND: {old[:60]!r}")
        s = s2
    return s

def div_end(h, start):
    depth, pos = 0, start
    while True:
        o = h.find('<div', pos); c = h.find('</div', pos)
        if o != -1 and (c == -1 or o < c):
            depth += 1; pos = o + 4
        elif c != -1:
            depth -= 1; pos = c + 6
            if depth == 0: return pos
        else:
            raise ValueError('unbalanced div')

def add_rows(h, rows, ctx):
    """Clone the FIRST <tr> in <tbody> for each entry. rows = list of (tpl_idx, subs)."""
    tb = h.find('<tbody')
    end = h.find('</table', tb)
    parts = h[tb:end].split('<tr')
    out = ''
    for tpl_idx, pairs in rows:
        tpl = '<tr' + parts[1 + tpl_idx]
        out += sub(tpl, pairs, ctx)
    return h[:end] + out + h[end:]

def add_cards(h, wrap, marker, cards, ctx):
    """Clone the card div that CONTAINS `marker`, once per entry."""
    tpl = None; end = -1
    pos = 0
    while True:
        i = h.find(marker, pos)
        if i == -1: break
        w = h.rfind(wrap, 0, i)
        s = h.rfind('<div', 0, w) if w != -1 else -1
        if s != -1:
            try:
                e = div_end(h, s)
            except ValueError:
                e = -1
            if e > i:
                tpl = h[s:e]; end = e; break
        pos = i + len(marker)
    if tpl is None:
        warn.append(f"{ctx}: card wrapper NOT FOUND for {marker!r}"); return h
    # insert after the LAST sibling card of the same wrap
    last_end = end
    while True:
        nw = h.find(wrap, last_end)
        if nw == -1: break
        nd = h.rfind('<div', 0, nw)
        if nd == last_end:
            last_end = div_end(h, nd)
        else:
            break
    out = ''
    for pairs in cards:
        out += sub(tpl, pairs, ctx)
    return h[:last_end] + out + h[last_end:]

def setcount(h, old, new, ctx):
    h2, n = re.subn(re.escape(old), new, h, count=1)
    if n == 0: warn.append(f"{ctx}: count NOT FOUND: {old!r}")
    return h2

def set_stat(h, label, pat, new, ctx, fwd=False):
    """Replace the stat value adjacent to `label`. fwd=True when value comes AFTER the label."""
    pos = 0
    while True:
        i = h.find(label, pos)
        if i == -1:
            warn.append(f"{ctx}: label NOT FOUND: {label!r}"); return h
        if fwd:
            seg = h[i:i+400]
            m = re.search(pat, seg)
            if m:
                return h[:i] + seg[:m.start()] + new + seg[m.end():] + h[i+400:]
        else:
            seg = h[max(0, i-600):i]
            ms = list(re.finditer(pat, seg))
            if ms:
                m = ms[-1]
                return h[:max(0, i-600)] + seg[:m.start()] + new + seg[m.end():] + h[i:]
        pos = i + len(label)

def fill_empty(h, empty_marker, new_html, ctx):
    i = h.find(empty_marker)
    if i == -1:
        warn.append(f"{ctx}: empty marker NOT FOUND: {empty_marker[:40]!r}"); return h
    start = h.rfind('<div', 0, i)
    end = div_end(h, start)
    return h[:start] + new_html + h[end:]

CARD = 'relative group bg-white rounded-2xl'

def process(path):
    h = open(path, encoding='utf-8').read()
    o = h
    f = os.path.basename(path)
    ctx = f

    if f == 'producteurs.html':
        cards = [
            [('#7','#8'),('Sami Ben Amor','Mohamed Trabelsi'),('Nabeul','Sfax'),('Moulin Ennour','Moulin El Baraka'),('>2<','>3<'),(r'4.{0,3}200','6 800')],
            [('#7','#9'),('Sami Ben Amor','Fatma Gharbi'),('Nabeul','Kairouan'),('>2<','>2<'),(r'4.{0,3}200','3 900')],
            [('#7','#10'),('Sami Ben Amor','Ali Ben Salah'),('Nabeul','Béja'),('Moulin Ennour','Moulin Errim'),('>2<','>4<'),(r'4.{0,3}200','7 100')],
            [('#7','#11'),('Sami Ben Amor','Leïla Mansour'),('Nabeul','Zaghouan'),('Moulin Ennour','Huilerie El Amel'),('>2<','>1<'),(r'4.{0,3}200','2 300')],
        ]
        h = add_cards(h, CARD, 'Sami Ben Amor', cards, ctx)
        h = setcount(h, '2 producers registered', '6 producers registered', ctx)

    elif f == 'parcelles.html':
        rows = [
            (0, [('Henchir el Ain','Ferme El Wafa'),('Sami Ben','Mohamed Trabelsi'),('Chemlali','Chetoui'),('8.00 ha','12.50 ha'),('>2<','>3<'),(r'4.{0,3}200 kg','6 800 kg')]),
            (0, [('Henchir el Ain','Dar Essalem'),('Sami Ben','Fatma Gharbi'),('8.00 ha','6.00 ha'),('>2<','>2<'),(r'4.{0,3}200 kg','3 900 kg'),('biologique','conventionnel')]),
            (0, [('Henchir el Ain','Les Oliviers du Nord'),('Sami Ben','Ali Ben Salah'),('Chemlali','Oueslati'),('8.00 ha','15.00 ha'),('>2<','>4<'),(r'4.{0,3}200 kg','7 100 kg')]),
            (0, [('Henchir el Ain','Henchir Bouzid'),('Sami Ben','Leïla Mansour'),('Chemlali','Arbequina'),('8.00 ha','4.50 ha'),('>2<','>1<'),(r'4.{0,3}200 kg','2 300 kg'),('biologique','en conversion')]),
        ]
        h = add_rows(h, rows, ctx)
        h = setcount(h, '2 plots registered', '6 plots registered', ctx)

    elif f == 'recoltes.html':
        # rows: 0='03/10/2026 producteur1hd ... Pressed', 3='30/09/2026 ... Pending'
        rows = [
            (0, [('03/10/2026','15/10/2026'),('producteur1hd','Mohamed Trabelsi'),('parcelle n1 beja','Ferme El Wafa'),('Chemlali','Chetoui'),(r'1.{0,3}500','2 400'),('Half-ripe','Ripe')]),
            (0, [('03/10/2026','12/10/2026'),('producteur1hd','Fatma Gharbi'),('parcelle n1 beja','Dar Essalem'),(r'1.{0,3}500','1 800'),('Hand picking','Mixed')]),
            (0, [('03/10/2026','08/10/2026'),('producteur1hd','Ali Ben Salah'),('parcelle n1 beja','Les Oliviers du Nord'),('Chemlali','Oueslati'),(r'1.{0,3}500','3 200'),('Half-ripe','Ripe'),('Hand picking','Mechanical')]),
            (3, [('30/09/2026','05/10/2026'),('producteur1hd','Leïla Mansour'),('parcelle n1 beja','Henchir Bouzid'),('Chemlali','Arbequina'),(r'1.{0,3}000','1 100'),('Veraison','Half-ripe')]),
            (0, [('03/10/2026','28/09/2026'),('producteur1hd','Mohamed Trabelsi'),('parcelle n1 beja','Ferme El Wafa'),('Chemlali','Chetoui'),(r'1.{0,3}500','2 100'),('Half-ripe','Veraison'),('Hand picking','Mixed')]),
        ]
        h = add_rows(h, rows, ctx)
        h = setcount(h, '4 harvests recorded', '9 harvests recorded', ctx)

    elif f == 'pressages.html':
        rows = [
            (0, [('02/10/2026','15/10/2026'),('Sami Ben','Mohamed Trabelsi'),('Henchir el Ain','Ferme El Wafa'),('Chemlali','Chetoui'),('Moulin Ennour','Moulin El Baraka'),(r'3.{0,3}000','2 400'),('>570<','>480<'),('19.00%','20.00%')]),
            (0, [('02/10/2026','12/10/2026'),('Sami Ben','Fatma Gharbi'),('Henchir el Ain','Dar Essalem'),(r'3.{0,3}000','1 800'),('>570<','>360<'),('19.00%','20.00%')]),
            (0, [('02/10/2026','08/10/2026'),('Sami Ben','Ali Ben Salah'),('Henchir el Ain','Les Oliviers du Nord'),('Chemlali','Oueslati'),('Moulin Ennour','Moulin Errim'),(r'3.{0,3}000','3 200'),('>570<','>610<'),('19.00%','19.06%')]),
            (0, [('02/10/2026','28/09/2026'),('Sami Ben','Mohamed Trabelsi'),('Henchir el Ain','Ferme El Wafa'),('Chemlali','Chetoui'),('Moulin Ennour','Moulin El Baraka'),(r'3.{0,3}000','2 100'),('>570<','>400<'),('19.00%','19.05%')]),
        ]
        h = add_rows(h, rows, ctx)
        h = setcount(h, '2 pressings recorded', '6 pressings recorded', ctx)

    elif f == 'moulins.html':
        cards = [
            [('moulin1hd','Moulin El Baraka'),('benarous','sfax'),('Pression traditionnelle','Centrifugation — 3 phases'),(r'>1(</div><div[^>]*>pressings)',r'>5\1'),(r'>[^<]{1,8}L(</div><div[^>]*>oil produced)',r'>1 240 L\1'),(r'>10.00 T/j(</div><div[^>]*>capacity)',r'>8.00 T/j\1')],
            [('moulin1hd','Moulin Errim'),('benarous','béja'),(r'>1(</div><div[^>]*>pressings)',r'>3\1'),(r'>[^<]{1,8}L(</div><div[^>]*>oil produced)',r'>640 L\1'),(r'>10.00 T/j(</div><div[^>]*>capacity)',r'>5.00 T/j\1')],
            [('moulin1hd','Huilerie El Amel'),('benarous','zaghouan'),('Pression traditionnelle','Centrifugation — 2 phases'),(r'>1(</div><div[^>]*>pressings)',r'>4\1'),(r'>[^<]{1,8}L(</div><div[^>]*>oil produced)',r'>980 L\1'),(r'>10.00 T/j(</div><div[^>]*>capacity)',r'>10.00 T/j\1')],
        ]
        h = add_cards(h, CARD, 'moulin1hd', cards, ctx)
        h = setcount(h, '2 mills registered', '5 mills registered', ctx)

    elif f == 'laboratoires.html':
        cards = [
            [('laboratoir1hd','Onagri Laboratoire Central'),('1 analyses performed','3 analyses performed')],
            [('laboratoir1hd','SGS Tunisia Lab'),('1 analyses performed','2 analyses performed')],
        ]
        h = add_cards(h, CARD, 'laboratoir1hd', cards, ctx)
        h = setcount(h, '2 laboratories', '4 laboratories', ctx)

    elif f == 'analyses.html':
        cards = [
            [('10/10/2026','18/10/2026'),('laboratoir1hd','Onagri Tunis'),('producteur1hd','Mohamed Trabelsi'),('Chemlali','Chetoui'),('moulin1hd','Moulin El Baraka'),('0.601%','0.320%'),('20.00','8.20'),('0.199','0.142'),('2.499','1.780'),('54.001%','63.200%'),('4.000%','3.100%')],
            [('10/10/2026','05/10/2026'),('laboratoir1hd','SGS Tunisia Lab'),('producteur1hd','Ali Ben Salah'),('Chemlali','Oueslati'),('moulin1hd','Moulin Errim'),('0.601%','0.890%'),('20.00','14.50'),('0.199','0.218'),('2.499','2.640'),('54.001%','57.400%'),('4.000%','3.900%')],
        ]
        h = add_cards(h, '<div class="bg-white rounded-2xl border border-slate-100 p-5">', '10/10/2026', cards, ctx)

    elif f == 'conditionneurs.html':
        cards = [
            [('conditionneur1hd','Société Méditerranée Emballage'),('beja','tunis'),(r'>0(</div><div[^>]*>operations)',r'>2\1'),(r'>0 L(</div><div[^>]*>packed)',r'>1 800 L\1')],
            [('conditionneur1hd','Huile Prestige Packing'),('beja','sousse'),(r'>0(</div><div[^>]*>operations)',r'>1\1'),(r'>0 L(</div><div[^>]*>packed)',r'>720 L\1')],
        ]
        h = add_cards(h, CARD, 'conditionneur1hd', cards, ctx)
        h = setcount(h, '2 packers', '4 packers', ctx)

    elif f == 'operations.html':
        rows = [
            (0, [('OLV-2026-0001','OLV-2026-0002'),('Sami Ben','Mohamed Trabelsi'),('El Amel Conditionnement','Société Méditerranée Emballage'),('Glass bottle 0.5L','Glass bottle 0.75L'),(r'560 L','1 200 L'),('6de84f52','a91f3d07')]),
            (0, [('OLV-2026-0001','OLV-2026-0003'),('Sami Ben','Ali Ben Salah'),('El Amel Conditionnement','Huile Prestige Packing'),('Glass bottle 0.5L','Can 5L'),(r'560 L','720 L'),('30/04/2028','31/05/2028'),('6de84f52','f4c2b891')]),
            (0, [('OLV-2026-0001','OLV-2026-0004'),('Sami Ben','Fatma Gharbi'),('Glass bottle 0.5L','Glass bottle 1L'),(r'560 L','600 L'),('30/04/2028','30/06/2028'),('6de84f52','7e3d5a02')]),
        ]
        h = add_rows(h, rows, ctx)
        h = setcount(h, '1 packed lots', '4 packed lots', ctx)

    elif f == 'exportateurs.html':
        cards = [
            [('export1hd','Méditerranée Trading'),('France','italie'),(r'>0(</div><div[^>]*>exports)',r'>1\1'),(r'>0 L(</div><div[^>]*>exported)',r'>1 200 L\1')],
            [('export1hd','Atlas Olive Export'),('France','france'),(r'>0(</div><div[^>]*>exports)',r'>1\1'),(r'>0 L(</div><div[^>]*>exported)',r'>720 L\1')],
        ]
        h = add_cards(h, CARD, 'export1hd', cards, ctx)
        h = setcount(h, '2 exporters', '4 exporters', ctx)

    elif f == 'exports.html':
        WRAP = '<div class="bg-white rounded-2xl border border-slate-100 p-4 flex items-center gap-4">'
        cards = [
            [('OLV-2026-0001','OLV-2026-0002'),('El Amel export','Méditerranée Trading'),('France','Italie'),(r'560 L','1 200 L'),('DE-2026-9105','DE-2026-9211'),('04/10/2026','16/10/2026'),('8c92a2b552','b3e91f4a'),('In progress','Shipped')],
            [('OLV-2026-0001','OLV-2026-0003'),('El Amel export','Atlas Olive Export'),(r'560 L','720 L'),('Port of Sfax','Port de Radès'),('DE-2026-9105','DE-2026-9345'),('04/10/2026','20/10/2026'),('8c92a2b552','c7d2a815')],
        ]
        h = add_cards(h, WRAP, 'OLV-2026-0001', cards, ctx)
        h = setcount(h, '1 exports', '3 exports', ctx)

    elif f == 'dossiers.html':
        WRAP = '<div class="bg-white rounded-2xl border border-slate-100 overflow-hidden">'
        cards = [
            [('OLV-2026-0001','OLV-2026-0002'),('France','Italie'),('El Amel export','Méditerranée Trading'),('5/10 docs','6/10 docs'),('50%','60%')],
        ]
        h = add_cards(h, WRAP, 'Export file OLV-2026-0001', cards, ctx)

    elif f == 'certifications.html':
        cards = [
            [('Organic','HACCP'),('Ecocert','SGS Tunisia'),('TN-BIO-2026-0457','CERT-HACCP-2026-089'),('Producer','Packer'),('Sami Ben Amor','El Amel Conditionnement'),('Expires 14/01/2027','Expires 02/03/2027')],
            [('TN-BIO-2026-0457','TN-BIO-2026-0521'),('Sami Ben Amor','Mohamed Trabelsi'),('Expires 14/01/2027','Expires 20/09/2027')],
        ]
        h = add_cards(h, '<div class="bg-white rounded-2xl border p-5 cursor-pointer hover:shadow-sm transition-shadow border-slate-100">', 'TN-BIO-2026-0457', cards, ctx)

    elif f == 'iot.html':
        rows = ''
        pts = [('Chambre froide — quai de chargement','Sfax · capteur TNEnergy SN-2201','-2.4 °C'),
               ('Cuve de stockage huile','Moulin Ennour · SN-2202','18.2 °C'),
               ('Salle de trituration','Moulin Ennour · SN-2203','24.7 °C'),
               ('Entrepôt conditionnement','El Amel Conditionnement · SN-2204','19.8 °C'),
               ('Camion frigorifique export','Route Sfax–Radès · SN-2205','3.1 °C')]
        for name, loc, val in pts:
            rows += f'<div class="bg-white rounded-2xl border border-slate-100 p-4 flex items-center gap-4"><div class="w-10 h-10 bg-sky-50 rounded-xl flex items-center justify-center flex-shrink-0">{THERMO_SVG}</div><div class="flex-1 min-w-0"><div class="font-semibold text-slate-800 text-sm">{name}</div><div class="text-xs text-slate-400">{loc}</div></div><div class="text-right"><div class="text-sm font-bold text-slate-800">{val}</div><div class="text-xs text-emerald-600">En ligne · il y a 2 min</div></div></div>'
        h = fill_empty(h, 'No monitoring point configured', rows, ctx)
        h = setcount(h, '0 monitoring points', '5 monitoring points', ctx)

    elif f == 'documents.html':
        docs = ''
        items = [('Certificat d\'analyse IOC — OLV-2026-0001.pdf','Olea analyses sfax · 03/10/2026 · 1.2 MB'),
                 ('Certificat biologique Ecocert — Sami Ben Amor.pdf','Sami Ben Amor · 14/01/2026 · 0.8 MB'),
                 ('Déclaration douanière DE-2026-9105.pdf','El Amel export · 04/10/2026 · 0.6 MB'),
                 ('Fiche technique huile d\'olive extra vierge.pdf','Huilerie El Amel · 01/10/2026 · 0.4 MB')]
        for name, meta in items:
            docs += f'<div class="bg-white rounded-2xl border border-slate-100 p-4"><div class="flex items-center gap-3"><div class="w-9 h-9 bg-blue-50 rounded-lg flex items-center justify-center flex-shrink-0">{FILE_SVG}</div><div class="min-w-0"><p class="text-sm font-medium text-slate-800 truncate">{name}</p><p class="text-xs text-slate-400">{meta}</p></div></div></div>'
        h = fill_empty(h, 'No document', docs, ctx)
        h = setcount(h, '0 documents', '4 documents', ctx)

    elif f == 'carbone.html':
        lots = '<div class="divide-y divide-slate-50">'
        for lot, kg in [('OLV-2026-0001','412 kg CO₂e'),('OLV-2026-0002','688 kg CO₂e'),('OLV-2026-0003','356 kg CO₂e')]:
            lots += f'<button class="w-full px-4 py-2.5 flex items-center justify-between hover:bg-slate-50 text-left"><span class="font-mono text-xs text-slate-700">{lot}</span><span class="text-xs font-medium text-slate-500">{kg}</span></button>'
        lots += '</div>'
        h = fill_empty(h, 'Aucun lot', lots, ctx)
        h = set_stat(h, 'Batches calculated', r'>\d+<', '>3<', ctx, fwd=True)
        h = set_stat(h, 'Company total', r'>[^<]{1,15}kg CO', '>1 456 kg CO', ctx, fwd=True)

    elif f == 'iso22000.html':
        h = set_stat(h, 'mt-0.5">Procedures', r'>\d+<', '>4<', ctx)
        h = set_stat(h, 'mt-0.5">HACCP hazards', r'>\d+<', '>6<', ctx)
        h = set_stat(h, 'mt-0.5">Audits', r'>\d+<', '>2<', ctx)
        h = set_stat(h, 'mt-0.5">CAPA', r'>\d+<', '>1<', ctx)

    elif f == 'index.html':
        h = set_stat(h, 'mt-0.5">Producers', r'>\d+<', '>6<', ctx)
        h = set_stat(h, 'mt-0.5">Harvests', r'>[^<]{1,15}kg<', '>16 200 kg<', ctx)
        h = set_stat(h, 'mt-0.5">Oil produced', r'>[^<]{1,15}L<', '>2 620 L<', ctx)
        h = set_stat(h, 'mt-0.5">Packed lots', r'>\d+<', '>4<', ctx)
        h = set_stat(h, 'mt-0.5">Compliant analyses', r'>\d+<', '>4<', ctx)
        h = set_stat(h, 'mt-0.5">Exports completed', r'>\d+<', '>3<', ctx)
        h = set_stat(h, 'mt-0.5">Blockchain blocks', r'>\d+<', '>68<', ctx)
        h = set_stat(h, 'compliance rate', r'>\d+%<', '>100%<', ctx, fwd=True)
        h = set_stat(h, 'compliance rate', r'width:\d+%', 'width:100%', ctx, fwd=True)
        h = set_stat(h, 'Total harvested', r'>[^<]{1,15}kg<', '>16 200 kg<', ctx, fwd=True)
        h = set_stat(h, 'Total oil produced', r'>[^<]{1,15}L<', '>2 620 L<', ctx, fwd=True)
        h = set_stat(h, 'Total exported', r'>[^<]{1,15}L<', '>2 480 L<', ctx, fwd=True)

    if h != o:
        open(path, 'w', encoding='utf-8').write(h)
        print(f'ENRICHED {path}')
    else:
        print(f'-- no change {f}')

for root in ['output/olivetrace']:
    if not os.path.isdir(root):
        continue
    for fn in sorted(os.listdir(root)):
        if fn.endswith('.html') and '--' not in fn and '404' not in fn:
            process(os.path.join(root, fn))

print('\n'.join(warn) if warn else 'NO WARNINGS')
