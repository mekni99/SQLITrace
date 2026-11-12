# -*- coding: utf-8 -*-
import json, pathlib, sys, datetime
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

fields = json.loads(pathlib.Path('fields.json').read_text(encoding='utf-8'))

# Corrections : champs à boutons (pas d'input/select dans le HTML capturé)
BUTTONS = {
    ('users', 'Rôle *'): ['admin', 'superviseur', 'operateur'],
    ('iot', 'Type *'): ['Entrepôt', 'Chambre froide', 'Conditionnement', 'Centre de distribution'],
    ('etapes', "Type d'exécution"): ['Initial', 'Retravail', 'Contrôle'],
}

META = {
    'lots':                      ('Lots',                    'Nouveau Lot',                'lots.html'),
    'producteurs':               ('Producteurs',             'Ajouter Producteur',         'producteurs.html'),
    'etapes':                    ('Étapes de production',    'Ajouter Étape',              'etapes.html'),
    'chaine-froid':              ('Chaîne du froid',         'Nouveau segment',            'chaine-froid.html'),
    'certifications':            ('Certifications',          'Nouvelle Certification',     'certifications.html'),
    'audits':                    ('Audits',                  'Nouvel Audit',               'audits.html'),
    'capa':                      ('CAPA (actions)',          'Nouvelle Action',            'capa.html'),
    'evaluations-fournisseurs':  ('Évaluations fournisseurs','Nouvelle Évaluation',       'evaluations-fournisseurs.html'),
    'ia':                        ('Analyses IA (pesticides)', 'Nouvelle Analyse IA',        'ia.html'),
    'iot':                       ('Lieux / capteurs IoT',    'Nouveau lieu',               'iot.html'),
    'users':                     ('Utilisateurs',            'Nouvel utilisateur',         'users.html'),
}

TYPES = {
    'text': 'Texte', 'number': 'Nombre', 'date': 'Date', 'datetime-local': 'Date + heure',
    'email': 'Email', 'password': 'Mot de passe', 'select': 'Liste déroulante',
    'textarea': 'Zone de texte', 'checkbox': 'Case à cocher',
}

def ftype(d):
    return 'Sélecteur à boutons' if (d['label'], d.get('key')) else TYPES.get(d['type'], d['type'])

def esc(t):
    return t.replace('|', chr(92)+'|')

lines = []
lines.append('# DateTrace — Inventaire des entités et champs de formulaires')
lines.append('')
lines.append(f"*Rapport généré le {datetime.date.today().isoformat()} — extraction automatique des formulaires capturés "
             f"(`output/datetrace/*--form.html`).*")
lines.append('')
lines.append('## Vue d\'ensemble')
lines.append('')
lines.append('| # | Entité | Écran | Formulaire | Champs |')
lines.append('|---|--------|-------|------------|--------|')
n = 0; total = 0
for mod in META:
    flds = fields.get(mod, [])
    n += 1
    name, btn, screen = META.get(mod, (mod, '—', mod + '.html'))
    total += len(flds)
    lines.append(f'| {n} | {name} | `{screen}` | {btn} | {len(flds)} |')
lines.append(f'| | **Total** | | | **{total}** |')
lines.append('')
lines.append('Modules sans formulaire capturé : Dashboard, Blockchain, PRP, QR & Traçabilité, Assistant IA.')
lines.append('')

for mod in META:
    flds = fields.get(mod, [])
    name, btn, screen = META.get(mod, (mod, '—', mod + '.html'))
    lines.append(f'## {name}')
    lines.append('')
    lines.append(f"- **Écran :** `{screen}` — formulaire « {btn} » (`{mod}--form.html`)")
    lines.append('')
    lines.append('| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |')
    lines.append('|-------|------|-------------|-------------------|---------------|')
    for d in flds:
        key = (mod, d['label'])
        if key in BUTTONS:
            typ = 'Sélecteur à boutons'
            opts = ', '.join(BUTTONS[key])
        elif d['type'] == 'select':
            typ = 'Liste déroulante'
            opts = '<br>'.join(esc(o) for o in d['options']) or '—'
        elif d['type'] == 'checkbox':
            typ = 'Case à cocher'
            opts = '—'
        else:
            typ = TYPES.get(d['type'], d['type'])
            opts = '—'
        req = 'Oui' if d['required'] else 'Non'
        ph = '—' if key in BUTTONS else (esc(d['placeholder']) if d['placeholder'] else '—')
        lines.append(f"| {esc(d['label'])} | {typ} | {req} | {opts} | {ph} |")
    lines.append('')

out = pathlib.Path('rapports')
out.mkdir(exist_ok=True)
p = out / '01-datetrace-entites-champs.md'
p.write_text('\n'.join(lines), encoding='utf-8')
print('written:', p, len(lines), 'lines')
