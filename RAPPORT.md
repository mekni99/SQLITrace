# RAPPORT — Audit & reconstruction du clone DateTrace

Date : 09/11/2026 · Source : `https://date.tntrace.tn/` · 16 exports SingleFile

## 1. Audit des sources

### Fichiers reçus
16 exports SingleFile (un par écran), chacun portant en en-tête
`url: https://date.tntrace.tn/<route>`. Taille 24–67 KB — tout est inliné
(CSS Tailwind, SVG, favicon data-URI).

### Nature de l'application
SPA **React** (Tailwind, icônes lucide, graphiques recharts) — mais le routeur
émet de **vrais `<a href="https://date.tntrace.tn/…">`** rendus côté client.
→ Approche **Cas A** retenue : multi-pages + réécriture des `href` internes,
sans routeur JavaScript (plus robuste, zéro JS ajouté dans les pages métier).

### État des exports (très favorable au hors-ligne)
- `0 <script>`, `0 fetch/XHR/WebSocket`, `0 tracker` — déjà neutralisés à l'export.
- `0` ressource externe (pas d'`<img>`, pas de CSS/font distante, icônes = SVG inline).
- `0` token, cookie, session, email. Seule identité : compte « Admin / admin » (générique).
- 23 SVG recharts inline sur le Dashboard → graphiques figés mais visuellement parfaits.

## 1b. États capturés (2e passe d'export)

13 variantes d'écrans exportées avec modale/état ouvert
(convention `<route>--<variante>.html`) : formulaires « Nouveau … » de lots,
producteurs, users, ia, iot, certifications, audits, capa,
evaluations-fournisseurs, chaine-froid + états sélectionnés (etapes, qr-trace).

**Interactivité restaurée** via `nav.js` (inline, ~60 lignes, aucun réseau) :
le CSP des exports (`script-src 'unsafe-inline'`) interdisant les fichiers
`.js` externes, le routeur est **inliné** dans chaque page. Il branche :
boutons « Nouveau… » → variante modale ; « Annuler/X/Créer/Enregistrer… »
dans une modale (`div.fixed.inset-0`) → `history.back()` ; cartes du
Dashboard → modules ; lignes de lot (boutons ou `div.cursor-pointer`) → vues
détail ; « Actualiser » → reload. Table de routage : `BTN_ROUTES` dans
`scripts/build.py` (sous-chaîne ou `re:` regex, premier match gagnant).

## 2. Pipeline de reconstruction (`scripts/build.py`)

1. **Inventaire** : lit l'URL d'origine de chaque export → table `route → fichier`
   (`/` → `index.html`, `/lots` → `lots.html`, …).
2. **Nettoyage** : supprime `<script>`, attributs `on*`, `<meta refresh>` (par sécurité).
3. **Réécriture des liens** : gère `href=` quoté et non-quoté (SingleFile retire
   les guillemets), absolus `https://date.tntrace.tn/x`, relatifs `/x`, ancres `#`,
   data-URI. Domaine externe → `href="#"`. Route non capturée → `404-local.html#route`.
4. **404 locale** : reconstruite sur le **chrome du Dashboard** (sidebar identique,
   menu fonctionnel) avec remplacement de `<main>` ; affiche la route demandée via
   le hash (seul JS du projet, 6 lignes, local).
5. **Données fictives** : remplacements littéraux depuis `scripts/data_map.json`.

## 3. Données remplacées

| Original | Fictif | Pages |
|---|---|---|
| `DT-1782427976011-090E34` (n° de lot) | `DT-2026-0001-AB7F` | lots, étapes, qr-trace, ia |
| `PROD-614097` (code producteur) | `PROD-2026-01` | producteurs |
| `mohamed` (prénom producteur) | `Ahmed Ben Salah` | producteurs, lots, etapes, qr-trace |

Scan complémentaire : aucun email, téléphone, JWT ou nom propre réel résiduel
(les « numéros » détectés étaient des triplets RGB Tailwind — faux positifs).
« Admin/admin », dates (01/06/2026), région Béja, destination France : conservés
(génériques / nécessaires au réalisme).

## 4. Résultats de vérification (Playwright + Edge headless)

| Test | Résultat |
|---|---|
| Pages servies | 30/30 → HTTP 200 |
| Liens du menu (cliqués) | 16/16 → 200, restent en local |
| Interactions (verify-clicks.js) | 12/12 : modales, retour, cartes, sélections ✅ |
| Requêtes réseau sortantes | **0** |
| Erreurs console / pageerror | **0** |
| Liens externes ou morts | 0 |
| 404-local affiche la route demandée | ✅ (`#lots` → « /lots ») |
| Rendu visuel | identique aux captures (vérifié par screenshots) |

## 5. Limites connues

- Les formulaires s'ouvrent et se ferment, mais **ne sauvegardent rien**
  (soumettre = retour arrière) — pas de backend dans un clone statique.
- Recherche, tri/filtres `<select>`, sous-boutons de modale (choix de rôle,
  type, priorité), chat IA, « Déconnexion » : inertes.
- Non capturés : détail d'un lot depuis /lots, formulaires blockchain/PRP
  (pas de variante fournie), modales d'aide.
- Le QR code (image) encode l'ancien ID réel ; le texte affiché est fictif.
- `aquatrace.html` (autre sous-domaine, sauvegarde navigateur incomplète) :
  **hors périmètre**, non utilisé.

## 6. Couverture des écrans

16/16 routes du menu capturées et reliées. Voir `output/manifest.json`
pour la table complète route → fichier.

---

# Addendum — Multi-produits (TNtrace hub)

## Architecture

- `output/index.html` = page d'accueil `tntrace.tn` (export SingleFile),
  liens produits réécrits vers les dossiers locaux `datetrace/`,
  `olivetrace/`, `aquatrace/`. Produits non capturés → `404-local.html#<produit>`.
- `pages/<produit>/` = exports SingleFile par produit ; `pages/home/` = hub.

## AquaTrace (`aquatrace.tntrace.tn`)

- **22/22 routes capturées** via `scripts/capture.mjs` (automatisation
  CDP + single-file-cli) : dashboard, lots, farms, basins, feeding, health,
  harvest, suivi, sensors, blockchain, qrcode, assistant, documents,
  nonconformites, rappels, distributions, sales, notifications, withdrawal,
  audit, integrations, utilisateurs.
- Routes `/app/*` normalisées → `aquatrace/<page>.html`, dashboard → `index.html`.
- Données fictionalisées (`data_map.aquatrace.json`) : emails
  `*@aquatrace.tn` → `*@aqua-demo.tn`, noms réels → fictifs.
- **12 variantes formulaires capturées** via `scripts/capture-variants.mjs`
  + `scripts/click-create.js` : SingleFile recharge chaque page avec un
  script injecté (`--browser-script`) qui poll le DOM, clique le bouton
  « + Nouveau… » automatiquement, puis capture le DOM modale ouverte ->
  `<page>--form.html`. Couvre : lots, farms, basins, feeding, harvest,
  health, nonconformites, rappels, sales, sensors, distributions,
  utilisateurs. Boutons câblés dans `BTN_ROUTES["aquatrace"]` ; « Annuler »
  / « Créer » / « Enregistrer » referment (CLOSE_RE).
- Capture automatisée : Chrome/CDP port 9222, profil
  `capture-profile-chrome`, login automatique (bouton Connexion →
  Se connecter, champs pré-remplis). `sf.mjs` polyfill `CloseEvent`
  (requis par single-file-cli sous Node 22).

## MedTrace (`medtrace.tntrace.tn`)

- **17/17 routes capturées** via `capture.mjs` : dashboard, medicaments,
  lots, unites, distributions, pharmacies, laboratoires, hopitaux, rappels,
  corrections, stupefiants, temperature, conformite, ia, assistant,
  inspections, utilisateurs.
- **11 variantes** via `capture-variants.mjs` : lots,
  medicaments, distributions, pharmacies, laboratoires, hopitaux
  (« Nouvel établissement »), inspections, stupefiants (« Nouvelle
  dispensation »), temperature (« Ajouter mesure »), utilisateurs —
  + `lots--selected.html` (vue détail lot, icône œil du tableau).
- Données quasi propres : seul `admin@medtrace.tn` → `admin@med-demo.tn`
  (`data_map.medtrace.json`). Identifiants TN-001… génériques.
- Sessions SSO : les cookies `tntrace.tn` sont partagés entre
  sous-domaines — une seule connexion suffit pour tous les produits.

## MachineTrace / TNMachine (`machine.tntrace.tn`)

- **15/15 routes** : accueil, machines, production (TRS/OEE), maintenance,
  jumeau (digital twin), energie + 9 sous-routes du menu **Plus** :
  structure, boitiers, operateurs, historique, tracabilite, qrcodes,
  integration, simulateur, parametres. Routes **sans préfixe /app**.
- Menu « Plus » absent du DOM capturé (dropdown React) -> rebuild local
  dans nav.js via `PLUS_MENU` (9 items injectés, toggle JS, styles inline).
- Login séparé nécessaire (SSO non propagé ce jour-là) ; détecté via le
  bouton « Déconnexion » (`ensureLoggedIn` généralisé).
- **2 variantes** :
  - `machines--selected.html` — clic sur une ligne machine → panneau
    détail (capteurs : vibration, température, courant, tension, puissance).
    Capturé via `scripts/click-row.js` ; déclencheur = règle `re:▸`.
  - `maintenance--form.html` — « Créer l'OT » → modale nouvel ordre de
    travail (machine, priorité, titre).
- App légère (~10-20 Ko/page) : `savePage`/`capture-variants` seuil
  abaissé à 5 Ko.
- Aucune donnée personnelle (noms d'équipements uniquement).
