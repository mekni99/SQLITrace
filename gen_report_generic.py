# -*- coding: utf-8 -*-
"""Génère rapports/NN-<produit>-entites-champs.md depuis fields_<produit>.json"""
import json, pathlib, sys, datetime
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TITLES = {
    'datetrace':   ('DateTrace', 'datetrace',  '01'),
    'olivetrace':  ('OliveTrace', 'olivetrace', '02'),
    'aquatrace':   ('AquaTrace', 'aquatrace',  '03'),
    'medtrace':    ('MedTrace', 'medtrace',    '04'),
    'medtrace':    ('MedTrace', 'medtrace',    '04'),
    'machine':     ('TNMachine', 'machine',     '05'),
}
TYPES = {
    'text': 'Texte', 'number': 'Nombre', 'date': 'Date', 'datetime-local': 'Date + heure',
    'email': 'Email', 'password': 'Mot de passe', 'select': 'Liste déroulante',
    'textarea': 'Zone de texte', 'checkbox': 'Case à cocher', 'file': 'Fichier',
    'boutons': 'Sélecteur à boutons',
}
# ordre = navigation de l'app ; (clé json, nom entité, écran, déclencheur)
META = {
'datetrace': [
    ('lots', 'Lots', 'lots.html', 'Nouveau Lot'),
    ('producteurs', 'Producteurs', 'producteurs.html', 'Ajouter Producteur'),
    ('etapes', 'Étapes de production', 'etapes.html', 'Ajouter Étape'),
    ('chaine-froid', 'Chaîne du froid', 'chaine-froid.html', 'Nouveau segment'),
    ('certifications', 'Certifications', 'certifications.html', 'Nouvelle Certification'),
    ('audits', 'Audits', 'audits.html', 'Nouvel Audit'),
    ('capa', 'CAPA (actions)', 'capa.html', 'Nouvelle Action'),
    ('evaluations-fournisseurs', 'Évaluations fournisseurs', 'evaluations-fournisseurs.html', 'Nouvelle Évaluation'),
    ('ia', 'Analyses IA (pesticides)', 'ia.html', 'Nouvelle Analyse IA'),
    ('iot', 'Lieux / capteurs IoT', 'iot.html', 'Nouveau lieu'),
    ('users', 'Utilisateurs', 'users.html', 'Nouvel utilisateur'),
],
'olivetrace': [
    ('producteurs', 'Producteurs', 'producteurs.html', 'New producer'),
    ('parcelles', 'Parcelles oléicoles', 'parcelles.html', 'New plot'),
    ('recoltes', 'Récoltes', 'recoltes.html', 'New harvest'),
    ('moulins', 'Moulins', 'moulins.html', 'New mill'),
    ('pressages', 'Pressages', 'pressages.html', 'New pressing'),
    ('laboratoires', 'Laboratoires', 'laboratoires.html', 'New laboratory'),
    ('analyses', 'Analyses', 'analyses.html', 'New analysis'),
    ('conditionneurs', 'Conditionneurs', 'conditionneurs.html', 'New'),
    ('operations', 'Opérations', 'operations.html', 'New operation'),
    ('exportateurs', 'Exportateurs', 'exportateurs.html', 'New exporter'),
    ('exports', 'Exports', 'exports.html', 'New export'),
    ('certifications', 'Certifications', 'certifications.html', 'New certification'),
    ('conformite', 'Conformité IOC', 'conformite.html', 'Manual check'),
    ('dossiers', 'Dossiers export', 'dossiers.html', 'Manual file'),
    ('iot', 'Points IoT / température', 'iot.html', 'New point'),
    ('iso22000-procedure', 'ISO 22000 — Procédures', 'iso22000.html', 'Procedures'),
    ('iso22000-haccp', 'ISO 22000 — HACCP', 'iso22000.html', 'HACCP'),
    ('iso22000-audit', 'ISO 22000 — Audits internes', 'iso22000.html', 'Internal audits'),
    ('iso22000-capa', 'ISO 22000 — Actions correctives', 'iso22000.html', 'Corrective actions'),
    ('documents', 'Documents', 'documents.html', 'New document'),
],
'medtrace': [
    ('medicaments', 'Médicaments', 'medicaments.html', 'Nouveau médicament'),
    ('lots', 'Lots & sérialisation', 'lots.html', 'Nouveau lot'),
    ('unites', 'Unités sérialisées', 'unites.html', '—'),
    ('distributions', 'Distributions', 'distributions.html', 'Nouvelle distribution'),
    ('pharmacies', 'Pharmacies', 'pharmacies.html', 'Nouvelle pharmacie'),
    ('laboratoires', 'Laboratoires', 'laboratoires.html', 'Nouveau laboratoire'),
    ('hopitaux', 'Hôpitaux / établissements', 'hopitaux.html', 'Nouvel établissement'),
    ('rappels', 'Rappels', 'rappels.html', '—'),
    ('corrections', 'Corrections', 'corrections.html', '—'),
    ('stupefiants', 'Stupéfiants', 'stupefiants.html', 'Nouvelle dispensation'),
    ('temperature', 'Chaîne du froid (DPM)', 'temperature.html', 'Ajouter mesure'),
    ('conformite', 'Conformité', 'conformite.html', '—'),
    ('ia', 'IA & prédictions', 'ia.html', '—'),
    ('inspections', 'Inspections DPM', 'inspections.html', 'Nouvelle inspection'),
    ('utilisateurs', 'Utilisateurs', 'utilisateurs.html', 'Nouvel utilisateur'),
],
}

def esc(t):
    return t.replace('|', chr(92) + '|')

prod = sys.argv[1]
fields = json.loads(pathlib.Path(f'fields_{prod}.json').read_text(encoding='utf-8'))
title, folder, num = TITLES[prod]
meta = {k for k, *_ in META[prod]}

lines = [f'# {title} — Inventaire des entités et champs de formulaires', '',
         f"*Rapport généré le {datetime.date.today().isoformat()} — extraction automatique des formulaires capturés "
         f"(`output/{folder}/*--*.html`).*", '']
lines += ['## Vue d\'ensemble', '', '| # | Entité | Écran | Formulaire | Champs |', '|---|--------|-------|------------|--------|']
n = 0; total = 0; rows = []
for key, name, screen, btn in META[prod]:
    flds = fields.get(key, {}).get('fields', [])
    rows.append((key, name, screen, btn, flds))
missing = []
for key, name, screen, btn, flds in rows:
    if not flds:
        missing.append(name); continue
    n += 1; total += len(flds)
    lines.append(f'| {n} | {name} | `{screen}` | {btn} | {len(flds)} |')
lines.append(f'| | **Total** | | | **{total}** |')
lines.append('')
if missing:
    lines.append('Entités sans formulaire capturé : ' + ', '.join(missing) + '.')
    lines.append('')
extra = [k for k in fields if k not in meta]
if extra:
    lines.append('Entités supplémentaires extraites : ' + ', '.join(f'`{k}`' for k in extra) + '.')
    lines.append('')
for key, name, screen, btn, flds in rows:
    if not flds: continue
    lines.append(f'## {name}')
    lines.append('')
    lines.append(f"- **Écran :** `{screen}` — formulaire « {btn} » (`{fields[key]['file']}`)")
    lines.append('')
    lines.append('| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |')
    lines.append('|-------|------|-------------|-------------------|---------------|')
    for d in flds:
        if d['type'] == 'select':
            typ, opts = 'Liste déroulante', '<br>'.join(esc(o) for o in d['options']) or '—'
        else:
            typ, opts = TYPES.get(d['type'], d['type']), '—'
        req = 'Oui' if d['required'] else 'Non'
        ph = esc(d['placeholder']) if d['placeholder'] else '—'
        lines.append(f"| {esc(d['label'])} | {typ} | {req} | {opts} | {ph} |")
    lines.append('')

out = pathlib.Path('rapports'); out.mkdir(exist_ok=True)
p = out / f'{num}-{prod}-entites-champs.md'
p.write_text('\n'.join(lines), encoding='utf-8')
print('written:', p, '|', total, 'champs,', n, 'entités')
