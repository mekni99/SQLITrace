# TNtrace — Clone statique multi-produits

Clone front-end **100 % hors-ligne** des dashboards de traçabilité TNtrace,
reconstruit à partir d'exports SingleFile réalisés en session authentifiée.

## Lancer le projet

**Option 1 — directement :** ouvrir `output/index.html` dans un navigateur.

**Option 2 — serveur local (recommandé) :**

```bash
cd output
python -m http.server 8765
# puis ouvrir http://127.0.0.1:8765/index.html
```

Aucune connexion internet, aucun backend, aucune authentification requis.

## Structure

```
aquatrace_files/
├── pages/                  # Exports SingleFile bruts (sources — ne pas éditer)
│   ├── home/index.html     #   tntrace.tn — page d'accueil hub
│   ├── datetrace/*.html    #   DateTrace (dattes) — 16 écrans + 13 variantes
│   ├── olivetrace/*.html   #   OliveTrace (huile d'olive) — 24 écrans + 21 variantes
│   ├── aquatrace/*.html    #   AquaTrace (aquaculture) — 22 écrans + 12 variantes
│   ├── medtrace/*.html     #   MedTrace (pharma) — 17 écrans + 11 variantes
│   └── machine/*.html      #   MachineTrace (TNMachine) — 15 écrans + 2 variantes
├── output/                 # ★ LE CLONE — pages liées, prêtes à l'emploi
│   ├── index.html          #   ★ Hub custom (sidebar + cartes produits)
│   ├── tntrace-landing.html#   Landing officielle tntrace.tn (annexe)
│   ├── datetrace/          #   clone dattes
│   ├── olivetrace/         #   clone huile d'olive
│   ├── aquatrace/         #   clone aquaculture
│   ├── 404-local.html      #   page d'attente (produit non capturé)
│   └── manifest.json       #   inventaire routes/variantes
├── scripts/
│   ├── build.py            # Génère output/ depuis pages/ (multi-produits)
│   ├── data_map.datetrace.json      # Données fictives dattes
│   ├── data_map.olivetrace.json     # Données fictives huile d'olive
│   ├── data_map.aquatrace.json      # Données fictives aquaculture
│   └── data_map.medtrace.json       # Données fictives pharma
│   ├── capture.mjs         # Capture auto des écrans via CDP + single-file
│   └── sf.mjs              # Wrapper polyfill pour single-file-cli (Node)
├── verification/           # verify.js, verify-clicks.js, captures *.png
├── README.md
└── RAPPORT.md              # Audit détaillé, choix techniques, limites
```

## Produits

| Produit | Écrans | Variantes | État |
|---|---|---|---|
| DateTrace (`date.tntrace.tn`) | 16/16 routes | 13 | ✅ complet |
| OliveTrace (`olivetrace.tntrace.tn`) | 24 routes* | 21 | ✅ complet |
| AquaTrace (`aquatrace.tntrace.tn`) | 22/22 routes | 12 | ✅ complet |
| MedTrace (`medtrace.tntrace.tn`) | 17/17 routes | 11 | ✅ complet |
| MachineTrace (`machine.tntrace.tn`) | 15/15 routes | 2 | ✅ complet |
| MachineTrace (`machine.tntrace.tn`) | — | — | ⏳ à capturer |

\* 2 routes du menu OliveTrace non capturées (`Security log`, `Client companies`)
→ mènent vers `olivetrace/404-local.html`. Le hub liste aussi 9 autres produits
non capturés (berrytrace, milktrace…) → `404-local.html#<produit>`.

## Écrans couverts — DateTrace (16/16)

Dashboard · Lots · Producteurs · Étapes · QR & Traçabilité · IA Pesticides ·
Blockchain · IoT & Capteurs · Certifications · PRP · Audits ISO · CAPA ·
Éval. Fournisseurs · Assistant IA · Chaîne de Froid · Utilisateurs

## Écrans couverts — OliveTrace (24/24)

Dashboard · Traceability · Mass balance · Carbon footprint · Blockchain ·
Producers · Plots · Harvests · Mills · Pressing · Laboratories · Analyses ·
Packers · Operations · Exporters · Exports · Certifications · IOC compliance ·
Export files · ISO 22000/HACCP · Temperature & IoT · Documents · AI assistant ·
Users

## Variantes interactives

Chaque produit a ses `<route>--<variante>.html` : formulaires « New … »
(OliveTrace : 17 formulaires inline + 4 onglets ISO 22000 + documents samples),
vues détail (datetrace : étapes du lot, QR affiché).

## Interactions actives (nav.js inliné, ~60 lignes, 100 % local)

- Boutons « Nouveau… / New… » → ouvrent la variante capturée
- « Annuler / Cancel / X / Créer / Create / Enregistrer… » → retour arrière
- Onglets (ISO 22000, Documents samples) → navigation entre variantes
- Cartes du Dashboard dattes → modules ; lignes de lot → vues détail
- « Actualiser » → recharge la page

Le reste (recherche, filtres, sous-boutons de formulaire, chat IA,
« Déconnexion ») reste visuel mais inerte — le JS applicatif n'existe pas
dans un export statique.

## Modifier les données affichées

Les données sont figées dans le HTML. Pour les changer **sans toucher aux pages**,
éditez `scripts/data_map.<produit>.json` (remplacements littéraux appliqués) :

```json
// scripts/data_map.datetrace.json
{ "Ahmed Ben Salah": "Nouveau Nom" }
```

Puis relancez `python scripts/build.py`.

## Ajouter / mettre à jour un écran

1. Exportez la page avec SingleFile (connecté au site) → fichier `.html`.
2. Déposez-le dans `pages/<produit>/` (n'importe quel nom — l'URL d'origine
   est lue dans l'en-tête du fichier).
3. `python scripts/build.py` → la page apparaît, les liens sont branchés
   automatiquement (une route non capturée → `404-local.html` du produit).

### Ajouter un état (modale/formulaire ouvert, vue détail…)

1. Sur le site réel, ouvrez la modale/vue voulue, **puis** exportez SingleFile.
2. Renommez le fichier `<route>--<variante>.html` dans `pages/<produit>/`.
3. Déclarez le déclencheur dans `BTN_ROUTES` de `scripts/build.py`
   (texte du bouton → fichier variante ; préfixe `re:` = regex).
4. `python scripts/build.py`.

## Vérification

```bash
cd output && python -m http.server 8765        # terminal 1
cd verification && node verify.js              # terminal 2 (nécessite npm i playwright)
cd verification && node verify-clicks.js       # interactions (chemins datetrace)
```

## Limites connues

- Les formulaires s'ouvrent et se ferment, mais **ne sauvegardent rien**
  (soumettre = retour arrière) — pas de backend dans un clone statique.
- Recherche, tris, filtres et chat IA : visuels uniquement.
- Le QR code (image) encode l'ancien identifiant réel ; le texte affiché
  est fictif.
- Le rendu reflète l'état des données au moment de la capture.
