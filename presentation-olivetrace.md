# OliveTrace — Présentation & Guide experts

**Récit central** : *« Un litre d'huile d'olive. Une histoire vérifiable de la parcelle à la bouteille. »*

Deux experts consultés :
- **Houssem Eddine Sassi** — Qualité & contrôle (Solivera/COGIA, ISO 9001, IFS, BRCGS, HACCP)
- **Bassem Harrathi** — Ingénieur production huile d'olive (huilerie Ali Sfar, COGIA, achats/coupage)

> Objectif de la réunion : leur faire **comprendre le système**, leur montrer **où leur expertise est indispensable**, et repartir avec des **missions concrètes**.

---

# PARTIE 1 — LE SLIDE DECK (14 slides)

*Style visuel recommandé pour tous les slides : fond sombre premium (navy/noir), accent or/olive, photos réelles d'oliveraies tunisiennes, schémas épurés, une idée par slide.*

---

## Slide 1 — Titre

**Contenu** :
- Titre : **OLIVETRACE**
- Sous-titre : *Traçabilité nationale de la filière huile d'olive — de la parcelle à la bouteille*
- Badge : `Démo interactive — système fonctionnel`
- Logo/visuel : bouteille d'huile + QR code stylisé + feuille d'olivier

**Notes orateur** : « Bonjour. Avant de vous montrer quoi que ce soit, laissez-moi vous poser une question : quand vous achetez une bouteille d'huile d'olive, savez-vous vraiment d'où elle vient ? » *(Transition : on passe au constat.)*

**Prompt Gemini** :
```
Crée un slide de titre premium, style sombre (fond navy profond #0a1628), accent doré. 
Titre géant "OLIVETRACE" en blanc avec "OLIVE" en doré. Sous-titre : "Traçabilité nationale de la filière huile d'olive — de la parcelle à la bouteille". 
À droite : composition photoréaliste d'une bouteille d'huile d'olive, une feuille d'olivier et un QR code lumineux flottant. 
Badge discret "Démo interactive". Style : keynote Apple/Stripe, espaces généreux, aucune surcharge.
```

---

## Slide 2 — Le constat : une filière en silos

**Contenu** :
- Titre : *La filière fonctionne — mais chaque acteur est isolé*
- 5 silos isolés : **Producteur** (papier/WhatsApp) → **Moulin** (bons de mouture) → **Labo** (analyses PDF isolées) → **Conditionneur** (Excel) → **Exportateur** (dossier manuel)
- Chaque flèche entre silos = **une rupture** : pas de preuve partagée, pas de lien entre les étapes, pas de remontée possible
- Chiffres-clés : dossier d'export = jours de paperasse ; un rappel = impossible de cibler les lots concernés

**Notes orateur** : « Regardez la filière : chaque acteur fait bien son travail — producteur, moulin, labo, conditionneur, exportateur. Mais les informations sont éparpillées : le labo a ses PDF, le moulin ses bons de mouture, l'exportateur son Excel. Personne ne peut répondre à 'cette bouteille vient de quelle parcelle ?' » *(Transition : on passe à la solution.)*

**Prompt Gemini** :
```
Crée un slide "problème" sur fond sombre. Titre : "La filière fonctionne — mais chaque acteur est isolé".
Diagramme horizontal de 5 blocs isolés (Producteur, Moulin, Laboratoire, Conditionneur, Exportateur),
chacun dans une "bulle" grise avec icône, séparés par des flèches brisées rouges.
Sous chaque bloc : petit texte "papier", "PDF isolé", "Excel", "manuel".
Style : épuré, un seul message visuel — la chaîne est cassée. Accent rouge pour les ruptures.
```

---

## Slide 3 — La promesse : un litre, une histoire

**Contenu** :
- Titre : *Un litre d'huile = une histoire vérifiable*
- Le concept en 3 mots : **CHAÎNE** (toutes les étapes reliées) · **PREUVE** (SHA-256, infalsifiable) · **ACCÈS** (QR code public)
- Visuel : une bouteille au centre, des lignes qui remontent vers la parcelle (scan satellite/oliveraie)
- Phrase choc : *« Scannez le QR → toute la chaîne s'affiche. Pas de confiance requise — une preuve cryptographique. »*
- ⚠️ **Note honnêteté** : ne PAS dire « première solution blockchain pour l'huile » — ça existe. Notre angle : **première plateforme nationale complète** pour la filière tunisienne.

**Notes orateur** : « C'est exactement pour ça qu'on a construit OliveTrace. L'idée est simple : chaque étape de la chaîne est reliée à la précédente, et chaque étape génère une preuve cryptographique. Un litre d'huile = une histoire vérifiable. » *(Transition : montrons concrètement le parcours.)*

**Prompt Gemini** :
```
Crée un slide "solution" sur fond sombre avec photo subtile d'oliveraie tunisienne en arrière-plan (très foncée).
Centre : une bouteille d'huile d'olive en verre transparent avec lumière dorée à l'intérieur.
Autour : lignes lumineuses fines qui remontent de la bouteille vers une parcelle vue du ciel,
avec des nœuds (QR codes) le long du chemin.
Titre : "Un litre d'huile = une histoire vérifiable".
3 badges en bas : CHAÎNE / PREUVE / ACCÈS.
Style : épuré, premium, message unique.
```

---

## Slide 4 — Le voyage du lot (slide clé)

**Contenu** :
- Titre : *Voici le parcours d'un lot — chaque étape scellée*
- Schéma vertical/linéaire des 7 étapes avec icônes :
  1. **Parcelle** — superficie, variété, producteur
  2. **Récolte** — date, quantité d'olives, bulletin
  3. **Moulin/Pressage** — température, temps, rendement
  4. **Analyse labo** — 17 paramètres IOC/UE, verdict
  5. **Conditionnement** — lot OLV-2026-XXXX, bouteille
  6. **Export** — destination, transport, documents
  7. **Dossier douanier** — RASFF, EUR.1, phytosanitaire, DUM…
- Chaque étape = un QR + un hash blockchain

**Notes orateur** : « Voilà concrètement ce que ça donne : sept étapes, de la parcelle jusqu'au dossier douanier. Chaque étape alimente la suivante — et chaque étape est scellée. Si quelqu'un modifie une donnée en cours de route, la preuve ne correspond plus. » *(Transition : passons à la démo — montrons que ça existe vraiment.)*

**Prompt Gemini** :
```
Crée un slide "architecture métier" sur fond sombre navy.
Titre : "Le parcours d'un lot — chaque étape scellée".
Diagramme horizontal de 7 étapes reliées par une ligne lumineuse dorée :
Parcelle → Récolte → Moulin → Analyse → Conditionnement → Export → Dossier.
Sous chaque étape : icône simple + 2-3 mots-clés (ex: "17 paramètres IOC", "rendement", "EUR.1").
Au-dessus de chaque étape : petit cadenas ou QR stylisé.
Style : flowchart premium, lisible, pas de surcharge textuelle.
```

---

## Slide 5 — Démo live : la traçabilité

**Contenu** :
- Titre : *Regardez — c'est en direct*
- Capture d'écran de `tracabilite.html` avec le lot **OLV-2026-0001**
- Annotations : la chaîne complète s'affiche → parcelle → exportateur → documents
- Call-to-action : *« Essayez vous-mêmes : tapez n'importe quel lot »*

**Notes orateur** : « Plutôt que de vous le décrire, je vais vous le montrer. Je tape un numéro de lot — OLV-2026-0001 — et regardez ce qui s'affiche : toute la chaîne, de la parcelle à l'exportateur. » *(Transition : montrer les modules métier.)*

**Prompt Gemini** :
```
Crée un slide "démo" sur fond sombre. Titre : "Regardez — c'est en direct".
Au centre : mockup d'une interface web sombre montrant une timeline verticale de traçabilité
(7 étapes avec dates et statuts colorés : vert=validé, or=en cours).
À gauche du mockup : une main qui tape "OLV-2026-0001" dans une barre de recherche.
Flèches d'annotation : "Parcelle d'origine", "Analyses IOC", "Export France".
Style : screenshot stylisé, pas de texte parasite.
```

---

## Slide 6 — Qualité & conformité (slide Sassi)

**Contenu** :
- Titre : *La qualité n'est plus une opinion — c'est une règle*
- Module Analyses : **17 paramètres IOC / Règlement CE 2568/91** par lot
- Verdict automatique : ✅ conforme / ⚠️ attention / ❌ non-conforme
- Module ISO 22000 : **HACCP par étape**, audits internes, **CAPA**
- Certifications : Ecocert bio, ISO 22000, ISO 17025, IFS, BRCGS — avec alertes d'expiration

**Notes orateur** : « Approfondissons la qualité. Chaque analyse est attachée au lot, avec 17 paramètres vérifiés automatiquement contre les seuils CE 2568/91 — et un verdict : conforme, attention, ou non-conforme. En parallèle, le module ISO 22000 gère les procédures, le plan HACCP et les actions correctives. » *(Transition : et pour l'export ?)*

**Prompt Gemini** :
```
Crée un slide "qualité" sur fond sombre. Titre : "La qualité n'est plus une opinion — c'est une règle".
Layout en 3 colonnes :
1. "17 paramètres IOC" — icône balance, liste abrégée (acidité, peroxyde, K232, K270, stérols)
2. "ISO 22000 / HACCP" — icône bouclier, points de contrôle par étape
3. "Certifications" — badges Empilés (Ecocert, ISO 22000, IFS, BRCGS)
Accent : or pour les badges certifiés, vert pour "conforme".
Style : professionnel, certifiant.
```

---

## Slide 7 — Export & certifications (slide Sassi)

**Contenu** :
- Titre : *L'export n'est plus un cauchemar de paperasse*
- Dossier d'export **généré automatiquement** selon la destination :
  - 🇪🇺 UE : RASFF, certificat d'analyse IOC, EUR.1, phytosanitaire ONPV
  - 🇺🇸 USA : FDA prior notice, certificat organique si bio
  - 🌍 Autres : documents spécifiques
- Avancement : 5/10 documents → alerte si manquant
- Chaque document lié à sa source (analyse, certificat, transport)

**Notes orateur** : « Et quand vient l'export — le moment où tout se joue — le système génère automatiquement le dossier douanier depuis les données du lot : certificat d'analyse, EUR.1, phytosanitaire, connaissement. Selon la destination, les documents changent — UE, USA, autres. Plus d'oubli, plus de relance. » *(Transition : mais comment on prouve que ces données n'ont pas été trafiquées ?)*

**Prompt Gemini** :
```
Crée un slide "export" sur fond sombre. Titre : "L'export n'est plus un cauchemar de paperasse".
Centre : un dossier bleu avec des documents qui se remplissent automatiquement (animation suggérée).
Autour : 3 destinations (UE, USA, Autres) avec leurs documents respectifs listés brièvement.
Progress bar : "5/10 documents — 50%".
Badge : "Généré automatiquement depuis les données du lot".
Style : administratif mais moderne, tons bleus/or.
```

---

## Slide 8 — Blockchain & QR : la preuve

**Contenu** :
- Titre : *Pas de confiance requise — une preuve*
- Chaque lot = **empreinte SHA-256** ancrée sur blockchain
- Le QR code sur la bouteille → page publique de vérification
- Si quelqu'un modifie une donnée → le hash ne correspond plus → **preuve d'altération**
- Visuel : chaîne de blocs + QR code scanné par un smartphone

**Notes orateur** : « La question que vous vous posez sûrement : 'et si quelqu'un modifie les données ?' C'est là que la blockchain entre en jeu. Chaque lot a une empreinte SHA-256 ancrée sur la chaîne — et le QR code sur la bouteille mène à une page de vérification publique. Modifiez une donnée, le hash ne correspond plus : c'est mathématiquement détectable. » *(Transition : positionnement honnête — qu'est-ce qui existe déjà ?)*

**Prompt Gemini** :
```
Crée un slide "blockchain" sur fond sombre. Titre : "Pas de confiance requise — une preuve".
Centre : une chaîne de blocs stylisée (cubes 3D reliés) avec un QR code lumineux au centre.
À droite : un smartphone qui scanne le QR, affichant une page de vérification verte.
Texte clé : "SHA-256 — toute modification est détectable".
Style : tech premium, tons cyan/or sur fond sombre.
```

---

## Slide 9 — Positionnement : ce qui existe vs OliveTrace

**Contenu** :
- Titre : *La traçabilité existe — mais pas pour la filière olive oil tunisienne*
- Tableau comparatif honnête :

| Existant | OliveTrace |
|---|---|
| QR code sur la bouteille (claim marketing) | Chaîne complète parcelle → export, **vérifiable** |
| Blockchain générique (registre, pas de métier) | **Modèle métier olive oil** : 17 paramètres IOC, CE 2568/91 |
| Outil par entreprise (silo) | **Plateforme multi-acteurs** : producteur, moulin, labo, conditionneur, exportateur |
| Traçabilité seule | Traçabilité **+ conformité + ISO 22000 + export + carbone** |
| Anglophone / générique | **Conçu pour la réglementation et la filière tunisiennes** |

- Message : *« On ne réinvente pas la blockchain — on construit la plateforme métier qui manquait. »*

**Notes orateur** : « Soyons honnêtes une minute : des QR codes et des blockchains existent déjà dans l'alimentaire. Mais ce sont des briques génériques — ils ne savent pas ce qu'est une trituration, un K232, ou un EUR.1. OliveTrace intègre la connaissance métier de la filière dans le système. On ne réinvente pas la blockchain — on construit la plateforme métier qui manquait. » *(Transition : et où va-t-on ?)*

**Prompt Gemini** :
```
Crée un slide "positionnement" sur fond sombre. Titre : "La traçabilité existe — mais pas pour la filière olive oil tunisienne".
Tableau comparatif 2 colonnes : "Existant" (gris) vs "OliveTrace" (or).
Lignes : QR simple vs chaîne vérifiable / Blockchain générique vs modèle métier IOC / Outil silo vs plateforme multi-acteurs / Traçabilité seule vs traçabilité + conformité + export.
En bas : badge "On ne réinvente pas la blockchain — on construit la plateforme métier".
Style : honnête, différenciant, pas agressif.
```

---

## Slide 10 — Vision & feuille de route

**Contenu** :
- Titre : *Ce que nous voulons construire ensemble*
- **Aujourd'hui** : démo fonctionnelle, données réalistes, 15 modules
- **Demain** : 
  - Données réelles d'une huilerie pilote (anonymisées)
  - Application mobile pour les producteurs (saisie récolte sur le terrain)
  - API pour connecter les balances, capteurs IoT
  - Déploiement national progressif par gouvernorat
- **Impact** : export plus facile, bio crédible, rappels ciblés, transparence totale

**Notes orateur** : « Ce que vous voyez aujourd'hui, c'est la base. La suite : brancher le système sur une vraie huilerie avec des données réelles, une application mobile pour les producteurs sur le terrain, et à terme un déploiement national par gouvernorat. L'objectif : que l'huile d'olive tunisienne soit reconnue comme la meilleure — et prouvée. » *(Transition : votre rôle à vous.)*

**Prompt Gemini** :
```
Crée un slide "roadmap" sur fond sombre. Titre : "Ce que nous voulons construire ensemble".
Timeline horizontale en 3 phases :
1. "Aujourd'hui" — démo fonctionnelle (icône laptop)
2. "Pilote" — huilerie réelle + données terrain (icône usine)
3. "National" — déploiement par gouvernorat (icône Tunisie)
En bas : 3 badges impact (Export +, Bio +, Rappels ciblés).
Style : aspirationnel, tons dorés.
```

---

## Slide 11 — Mission : Pr. Sassi (Qualité & Labo)

**Contenu** — un seul slide, un tableau :

| # | Mission | Zone du système | Ce qu'on attend de vous |
|---|---|---|---|
| 1 | **Valider les seuils IOC** | Module Analyses | Corriger les 17 paramètres et leurs limites (acidité, peroxyde, K232, K270, stérols…) selon votre pratique labo réelle |
| 2 | **Plan d'échantillonnage** | Module Analyses | Confirmer si le plan ISO (taille échantillon, fréquence, critères) doit être dans le dossier du lot |
| 3 | **HACCP / CAPA** | Module ISO 22000 | Comparer notre plan HACCP avec votre pratique IFS/BRCGS — identifier les dangers manquants (filtration, azote, hygrométrie) |
| 4 | **Dossier d'export** | Module Dossiers | Vérifier la complétude des documents générés pour l'UE / USA / ONH (RASFF, EUR.1, phytosanitaire, DUM…) |
| 5 | **Certifications** | Module Certifications | Valider la couverture (Ecocert, ISO 22000, ISO 17025, IFS, BRCGS) et l'utilité des alertes d'expiration |
| 6 | **Analyse réelle** | Démo | Fournir une analyse anonymisée d'un vrai lot pour rendre la démo crédible |

- Titre slide : *« Pr. Sassi — votre expertise qualité rend le système exact »*
- Bas de slide : *« On a la structure — vous avez le terrain »*

**Notes orateur** : « Et maintenant, parlons de vous — Pr. Sassi. On a modélisé la qualité avec nos hypothèses. Vous, vous faites ces analyses tous les jours. Voici les 6 missions où votre expertise est indispensable : corriger les seuils IOC, valider le plan d'échantillonnage, comparer notre HACCP à votre pratique IFS/BRCGS, vérifier le dossier d'export, valider les certifications — et si possible nous donner une vraie analyse anonymisée pour la démo. » *(Transition : même logique pour la production.)*

**Prompt Gemini** :
```
Crée un slide "mission" sur fond sombre navy, accent doré. 
Titre : "Pr. Sassi — votre expertise qualité rend le système exact".
Un tableau propre à 4 colonnes (# / Mission / Zone / Ce qu'on attend) avec 6 lignes :
1 Valider les seuils IOC / Analyses / Corriger les 17 paramètres
2 Plan d'échantillonnage / Analyses / Confirmer le plan ISO dans le dossier lot
3 HACCP / CAPA / Comparer avec IFS/BRCGS, dangers manquants
4 Dossier d'export / Dossiers / Vérifier complétude UE/USA/ONH
5 Certifications / Certifications / Valider couverture + alertes
6 Analyse réelle / Démo / Fournir une analyse anonymisée
Bas de slide : "On a la structure — vous avez le terrain".
Style : tableau lisible, icônes discrètes par ligne, une seule idée : collaboration experte.
```

---

## Slide 12 — Mission : M. Harrathi (Production & Moulin)

**Contexte** : Bassem ne voit pas la démo live → ce slide doit être **autonome**. Il explique d'abord ce que le système fait déjà côté production, puis ce qu'on lui demande.

**Contenu** — un seul slide, deux blocs :

**Bloc A — Ce que le système fait déjà (à gauche, plus petit)** :
- **Moulins** : 5 moulins enregistrés (nom, capacité, certification)
- **Pressages** : chaque trituration tracée — date, quantité d'olives, huile produite, rendement, paramètres (température, temps)
- **Lots** : assemblage olives → huile → conditionnement, numérotation OLV-2026-XXXX
- **Dashboard** : volumes produits, rendement global, alertes

**Bloc B — Les 6 missions (à droite, tableau principal)** :

| # | Mission | Ce qu'on attend de vous |
|---|---|---|
| 1 | **Valider le pressage** | Confirmer que les paramètres capturés (température, temps de malaxation, rendement) correspondent à une vraie trituration — et nous dire ce qui manque : humidité du fruit, variétés, maturité, rendement théorique vs réel |
| 2 | **Le coupage de lots** | Vous faisiez des assemblages de lots pour atteindre une qualité cible — est-ce que le système doit tracer le **mélange** comme un événement à part (avec les ratios, les lots sources, le lot résultant) ? |
| 3 | **Rendement par parcelle** | Le dashboard calcule le rendement global — est-ce que le calculer **par producteur/parcelle** (kg olives → L huile) vous aurait aidé à comparer les fournisseurs et négocier les achats ? |
| 4 | **Saisie à la source** | Faut-il que le producteur saisisse lui-même sa récolte (mobile, terrain), ou tout doit passer par le moulin/conditionneur ? Quel est le bon niveau de digitalisation pour un petit oléiculteur tunisien ? |
| 5 | **Données terrain** | Dans une vraie huilerie, quelles données existent déjà — registre papier, cahier de traçabilité, Excel, tickets de balance ? Qu'est-ce qu'on digitalise en premier pour que ce soit utile immédiatement ? |
| 6 | **Scénario pilote** | Co-construire avec nous comment le système tournerait pendant **une vraie campagne de trituration** : qui saisit quoi, à quel moment, quels KPIs suivre |

- Titre slide : *« M. Harrathi — votre expérience huilerie rend le système terrain »*
- Bas de slide : *« On a la structure — vous avez le terrain »*

**Notes orateur** : « Vous n'avez pas vu la démo, alors laissez-moi vous décrire ce qui existe côté production : le système enregistre chaque moulin, chaque trituration avec ses paramètres, chaque lot assemblé. Mais ce qui compte, c'est votre réalité — est-ce que ces champs sont les bons ? Est-ce que le coupage doit être tracé ? Quel est le bon niveau de saisie pour un petit producteur ? Et si on faisait un pilote sur une vraie campagne ? » *(Transition : ce que chacun repart avec.)*

**Prompt Gemini** :
```
Crée un slide "mission expert" sur fond sombre navy, accent cyan/olive, style industriel.
Titre : "M. Harrathi — votre expérience huilerie rend le système terrain".
Layout en 2 zones :
- Gauche (30%) : bloc "Ce que le système fait déjà" avec 4 mini-cartes : Moulins (capacité, certification), Pressages (paramètres, rendement), Lots (OLV-2026-XXXX), Dashboard (KPIs).
- Droite (70%) : tableau "6 missions" à 3 colonnes (Mission / Ce qu'on attend / Priorité) :
  1 Valider pressage — paramètres réels + humidité/maturité
  2 Coupage de lots — assemblage tracé avec ratios
  3 Rendement par parcelle — KPI achat
  4 Saisie à la source — producteur mobile ou centralisé
  5 Données terrain — inventaire paperasse existante
  6 Scénario pilote — campagne réelle
Bas de slide : "On a la structure — vous avez le terrain".
Style : dense mais lisible, icônes industrielles, ton expert-terrain.
```

---

## Slide 13 — Ce que nous vous rapportons (récapitulatif)

**Contenu** :
- Titre : *Ce que vous repartez avec*
- Pour **Sassi** : validation des seuils + plan d'échantillonnage + un cas d'usage concret pour ses audits
- Pour **Harrathi** : validation des paramètres moulin + un scénario de rendement par parcelle
- Pour les deux : une démo qu'ils peuvent montrer à leurs équipes, et un contact pour la suite

**Notes orateur** : « Pour résumer ce que chacun repart avec : Pr. Sassi, des seuils validés et un module prêt pour ses audits ; M. Harrathi, des paramètres trituration exacts et un scénario pilote. Et pour vous deux : une démo à montrer à vos équipes, et un contact pour la suite. » *(Transition : on ouvre les questions.)*

**Prompt Gemini** :
```
Crée un slide "récap" sur fond sombre. Titre : "Ce que vous repartez avec".
Deux colonnes avec checkmarks verts :
- "Pr. Sassi" : seuils IOC validés, plan d'échantillonnage intégré, audit-ready
- "M. Harrathi" : paramètres trituration validés, rendement par parcelle, scénario pilote
En bas : "Une démo à montrer + un contact pour la suite".
Style : gratifiant, clair.
```

---

## Slide 14 — Merci / Questions ouvertes

**Contenu** :
- Titre : *Merci — à vos questions*
- Contact : [votre nom], [email], [lien démo]
- QR code vers la démo live : `http://127.0.0.1:8765/olivetrace/` (ou GitHub Pages)
- Phrase finale : *« La traçabilité n'est pas un luxe — c'est la clé pour que l'huile d'olive tunisienne soit reconnue comme la meilleure au monde. »*

**Notes orateur** : « Merci pour votre temps et votre expertise. Ce qu'on a besoin de vous, c'est votre regard critique — ce qui est faux, ce qui manque, ce qui vous ferait gagner du temps. Et si vous avez des données réelles à partager, anonymisées, on les intègre pour la suite. » *(Fin — laisser la place aux questions.)*

**Prompt Gemini** :
```
Crée un slide de clôture sur fond sombre avec photo panoramique d'oliveraie tunisienne au coucher du soleil (très subtile).
Titre centré : "Merci — à vos questions".
En bas : QR code stylisé + "Scannez pour voir la démo".
Phrase finale en italique : "La traçabilité n'est pas un luxe — c'est la clé pour que l'huile d'olive tunisienne soit reconnue comme la meilleure au monde."
Style : émotif, mémorable.
```

---

# PARTIE 2 — NOTES ORALES (PAR EXPERT)

> Les missions sont sur les **slides 11 et 12** (une slide par expert, format tableau).
> Cette partie = ce que vous **dites** pendant ces slides + les questions pour lancer la discussion.
> **Principe** : ne pas les interroger — leur demander **ce qu'ils peuvent nous apporter** pour que le système soit exact.

---

## 🎓 Pr. Houssem Eddine Sassi — Slide 11
*Qualité & Contrôle — Solivera / COGIA · Laboratoire, analyses, ISO 9001/IFS/BRCGS/HACCP, export*

**Ce que vous dites** (30 sec) :
> « Voici votre slide. On a modélisé la qualité avec nos hypothèses — vous, vous faites ces analyses tous les jours. Les 6 missions : corriger les seuils IOC, valider le plan d'échantillonnage, comparer notre HACCP à votre pratique IFS/BRCGS, vérifier le dossier d'export, valider les certifications, et si possible nous donner une vraie analyse anonymisée pour la démo. »

**Questions pour lancer** :
- « Quand vous recevez une huile, comment faites-vous le lien entre l'analyse et le lot précis ? »
- « Si le système vérifiait les seuils automatiquement avant même que vous ouvriez le rapport, feriez-vous confiance au verdict ? »
- « Pour IFS/BRCGS, la traçabilité lot-par-lot suffit, ou il faut tracer aussi les paramètres de process ? »
- « À quel point la traçabilité est-elle un problème dans votre quotidien — qu'est-ce qui vous frustre le plus ? »

---

## 🔧 M. Bassem Harrathi — Slide 12
*Ingénieur Production Huile d'Olive — Ali Sfar / COGIA · Huilerie, trituration, achats/coupage, rendement*

**Ce que vous dites** (30 sec) :
> « Vous avez monté une huilerie et piloté des campagnes de trituration — vous savez ce qui se passe vraiment sur le terrain. Les 6 missions : valider les paramètres de pressage, nous dire si le coupage de lots doit être tracé, valider le rendement par parcelle, trancher qui saisit les données (producteur ou centralisé), inventorier les données existantes à digitaliser, et co-construire un scénario pilote sur une vraie campagne. »

**Questions pour lancer** :
- « Quand vous pilotiez une trituration, qu'est-ce que vous mesuriez vraiment à chaud — température, temps, humidité, rendement ? »
- « Vos 'coupages' pour atteindre une qualité cible — si le système modélisait le mélange comme un événement tracé, ça clarifierait votre gestion ? »
- « Vous achetiez chez les huileries avec dégustation — quelles données de l'origine étaient vraiment décisives pour accepter un lot ? »
- « Si vous ne deviez choisir qu'une seule chose — traçabilité, qualité, rendement ou achats — ce serait quoi ? »

---

## 🔄 Questions communes (pour les deux ensemble)

À poser en fin de réunion, quand les deux sont présents :

1. **Parcours** : « Est-ce que le chemin parcelle → export que j'ai modélisé correspond à la réalité, ou il y a des étapes oubliées (filtration, assemblage, stockage, transport) ? »
2. **Champs manquants** : « Dans les formulaires, est-ce qu'il manque des champs que vous renseigneriez obligatoirement au quotidien ? »
3. **Seuils** : « Les limites que j'ai mises (acidité, peroxyde, K232…) sont-elles correctes, ou vous appliquez des seuils différents en pratique ? »
4. **Données** : « Qui devrait nourrir le système — le producteur, le moulin, le labo, l'exportateur ? Ou une plateforme centrale pour tous ? »
5. **Valeur** : « Sur une échelle de 1 à 10, à quel point ce système résoudrait-il un **vrai problème** que vous rencontrez — et qu'est-ce qui vous manque pour y croire ? »

---

# PARTIE 3 — CHECKLIST DE LA RÉUNION

## Avant
- [ ] Tester la démo sur `http://127.0.0.1:8765/olivetrace/` (ou GitHub Pages)
- [ ] Préparer le lot `OLV-2026-0001` pour la traçabilité
- [ ] Imprimer `rapports/02-olivetrace-entites-champs.md` (liste des champs)
- [ ] Préparer une fiche IOC des seuils
- [ ] Tester le QR code si vous en avez un

## Pendant
- [ ] Slides 1-4 : contexte et promesse (5 min)
- [ ] Slides 5-8 : démo live (7 min)
- [ ] Slide 9 : positionnement vs existant (2 min) — **important : être honnête, pas claim "premier"**
- [ ] Slide 10 : vision (1 min)
- [ ] Slides 11-12 : **une slide par expert** — présenter le tableau des missions, laisser réagir (5 min)
- [ ] Slide 13 : récap (1 min)
- [ ] Slide 14 + questions ouvertes : laisser parler (10 min)

## Après
- [ ] Noter les corrections de seuils et champs manquants
- [ ] Demander les analyses réelles anonymisées (Sassi) et les paramètres moulin (Harrathi)
- [ ] Proposer un pilote sur une vraie campagne
- [ ] Remercier et envoyer le document de synthèse
