# Cahier des Charges — OliveTrace
## Plateforme de traçabilité & e-commerce de la filière huile d'olive tunisienne

**Version** : 1.0 — Novembre 2026
**Destinataires** : expert développement & blockchain, encadrant, experts métier (Sassi / Harrathi)
**Statut** : spécification fonctionnelle — démo statique existante, backend à concevoir

---

## 1. Contexte & objectif

### 1.1 Le projet

**OliveTrace** est une plateforme nationale de traçabilité et de commercialisation de la filière huile d'olive tunisienne, inspirée du modèle **OrigoVerro** (Italie) :

- **Côté filière (B2B)** : chaque acteur (producteur, moulin, laboratoire, conditionneur, exportateur) saisit ses données — la traçabilité se construit lot par lot, scellée cryptographiquement.
- **Côté consommateur (B2C)** : chaque produit vendu affiche un **QR code** qui donne accès à sa **fiche traçabilité publique** : parcelle d'origine, dates de récolte et de trituration, analyses laboratoire, certifications — transformant la traçabilité en **argument de vente**.
- **Côté commerce** : une boutique intégrée permet de vendre directement les produits tracés (producteurs → consommateurs, ou exportateurs → acheteurs).

### 1.2 Objectifs

| # | Objectif | Indicateur |
|---|---|---|
| O1 | Tracer 100 % des lots de la parcelle à la bouteille/export | % de lots avec chaîne complète |
| O2 | Rendre la traçabilité infalsifiable | Chaque événement ancré (hash) |
| O3 | Automatiser les dossiers d'export selon la destination | Temps de préparation < 1 h |
| O4 | Transformer la traçabilité en argument commercial | Scans QR par consommateurs |
| O5 | Vendre les produits tracés directement | Boutique en ligne opérationnelle |

### 1.3 Périmètre

- **Inclus** : filière olive oil Tunisie (olives → huile en bouteille ou en vrac → export)
- **Exclus V1** : autres produits (olives de table, margines), multi-pays
- **Vision** : modèle réplicable aux autres filières (dattes — DateTrace, poisson — AquaTrace, médicaments — MedTrace, machines — TNMachine)

---

## 2. Acteurs & rôles

| Acteur | Rôle | Accès |
|---|---|---|
| **Producteur** | Déclare parcelles, récoltes | App mobile (hors ligne possible) |
| **Moulin** | Enregistre triturations, paramètres, rendement | Web |
| **Laboratoire** | Saisit analyses (17 paramètres IOC), échantillonnage | Web |
| **Conditionneur** | Crée les lots commerciaux, mise en bouteille, QR | Web |
| **Exportateur** | Prépare exports, dossiers douaniers, transport | Web |
| **Admin plateforme** | Valide les acteurs, supervise, paramètres seuils | Web admin |
| **Consommateur** | Scanne QR → fiche publique, achète en boutique | Public, sans compte |
| **Acheteur B2B** | Consulte l'historique d'un lot avant achat | Compte léger |

---

## 3. Parcours fonctionnel global

```
PARCELLE → RÉCOLTE → MOULIN/PRESSAGE → ANALYSE LABO → CONDITIONNEMENT (LOT + QR)
                                                              │
                                    ┌─────────────────────────┴──────────────────┐
                                    ▼                                            ▼
                              EXPORT (B2B)                              PRODUIT CONSOMMATEUR (B2C)
                        Dossier douanier auto                    Fiche produit + QR → boutique
                        (UE / USA / ONH…)                      Catalogue OrigoVerro-like
```

Chaque étape : **événement + données + preuve SHA-256** ancrée sur blockchain.

---

## 4. Besoins fonctionnels — B2B (filière)

*Priorités : **M**ust = indispensable, **S**hould = important, **C**ould = souhaitable*

### 4.1 Gestion des acteurs & identités

| ID | Besoin | P. |
|---|---|---|
| F-01 | Créer et gérer les fiches acteurs : producteur, moulin, laboratoire, conditionneur, exportateur | M |
| F-02 | Enregistrer les certifications par acteur (bio, ISO 22000, ISO 17025, IFS, BRCGS…) avec dates d'expiration | M |
| F-03 | Alertes automatiques d'expiration de certification | S |
| F-04 | Validation des acteurs par l'admin avant accès à la plateforme | M |

### 4.2 Amont — parcelles & récoltes

| ID | Besoin | P. |
|---|---|---|
| F-05 | Gérer les parcelles : superficie, variétés, géolocalisation, producteur | M |
| F-06 | Déclarer une récolte : date, quantité d'olives, parcelle source, bulletin | M |
| F-07 | Saisie mobile terrain (hors ligne, synchronisation ultérieure) | S |

### 4.3 Moulin & pressage

| ID | Besoin | P. |
|---|---|---|
| F-08 | Enregistrer une trituration : date, quantité olives, huile produite, paramètres (température malaxation, temps, type d'extraction), rendement calculé | M |
| F-09 | Lier la trituration aux récoltes sources (traçabilité descendante) | M |
| F-10 | **Coupage / assemblage de lots** : mélanger plusieurs lots d'huile avec ratios et qualité cible → nouveau lot tracé | S |
| F-11 | KPI rendement par parcelle/producteur | C |

### 4.4 Laboratoire & analyses

| ID | Besoin | P. |
|---|---|---|
| F-12 | Saisir une analyse par lot : 17 paramètres IOC / CE 2568/91 (acidité, peroxyde, K232, K270, stérols, triglycérides…) | M |
| F-13 | **Verdict automatique** : conforme / attention / non-conforme selon les seuils réglementaires | M |
| F-14 | Joindre le plan d'échantillonnage ISO au dossier du lot | S |
| F-15 | Workflow non-conformité : blocage, tri, déclassage → action corrective (CAPA) | M |
| F-16 | Rapport d'analyse imprimable/signé | S |

### 4.5 Conditionnement & lots

| ID | Besoin | P. |
|---|---|---|
| F-17 | Créer un lot commercial : huile(s) source(s), format (bouteille, vrac), quantité, numéro lot (OLV-AAAA-XXXX) | M |
| F-18 | **Générer le QR code** du lot — lien vers fiche publique | M |
| F-19 | Imprimer étiquettes avec QR | S |
| F-20 | Historiser la chaîne complète du lot (toutes les étapes) | M |

### 4.6 Export & douane

| ID | Besoin | P. |
|---|---|---|
| F-21 | Créer un export : destination, transporteur, quantités | M |
| F-22 | **Générer automatiquement le dossier d'export** selon destination : RASFF, certificat d'analyse IOC, EUR.1, phytosanitaire ONPV, connaissement/LTA, DUM | M |
| F-23 | Avancement du dossier (X/10 documents), alertes sur pièces manquantes | M |
| F-24 | Statuts : en préparation → complet → soumis douanes → validé | M |

### 4.7 Qualité & ISO 22000

| ID | Besoin | P. |
|---|---|---|
| F-25 | Gérer procédures, plan HACCP (dangers par étape), audits internes, CAPA | M |
| F-26 | Check de conformité automatique par lot (check-list réglementaire) | M |
| F-27 | Tableau de bord ISO 22000 : audits planifiés, NC ouvertes | S |

### 4.8 Traçabilité & recherche

| ID | Besoin | P. |
|---|---|---|
| F-28 | Recherche par numéro de lot → chaîne complète visualisée (bidirectionnelle) | M |
| F-29 | Filtrer par acteur, date, statut | S |
| F-30 | Export CSV/PDF de l'historique d'un lot | S |

### 4.9 IoT & environnement

| ID | Besoin | P. |
|---|---|---|
| F-31 | Enregistrer relevés IoT : température, hygrométrie (chambre froide, cuve, camion) | S |
| F-32 | Alertes hors seuil | S |
| F-33 | Bilan carbone par lot et par campagne | C |

---

## 5. Besoins fonctionnels — B2C (consommateur & vente) ⭐

*Volet OrigoVerro : la traçabilité devient argument commercial.*

### 5.1 Fiche produit publique

| ID | Besoin | P. |
|---|---|---|
| F-34 | **Fiche publique par QR** : scan → page web responsive, sans compte | M |
| F-35 | Contenu fiche : nom produit, photo, origine (parcelle, gouvernorat), dates récolte/trituration, analyses clés (acidité, catégorie), certifications, histoire du producteur | M |
| F-36 | Visualisation chronologique du voyage du lot (timeline) | M |
| F-37 | Bouton « vérifier la preuve » → hash blockchain + statut | S |
| F-38 | Multi-langue : arabe / français / anglais | S |

### 5.2 Catalogue & boutique

| ID | Besoin | P. |
|---|---|---|
| F-39 | **Catalogue produits** : toutes les bouteilles en vente, filtrées par origine, catégorie, certification (bio, extra-vierge…) | M |
| F-40 | Fiche produit commerciale : prix, format, stock, fiche technique | M |
| F-41 | **Panier & commande** : paiement (à définir : carte, virement, livraison) | M |
| F-42 | Suivi de commande consommateur | S |
| F-43 | Livraison : choix transporteur, suivi, frais par zone | S |
| F-44 | Compte client : historique commandes, produits scannés, favoris | C |
| F-45 | Notation/avis consommateur sur produits | C |

### 5.3 Vitrine producteur

| ID | Besoin | P. |
|---|---|---|
| F-46 | Page publique par producteur/conditionneur : présentation, parcelles, produits | S |
| F-47 | Statistiques vendeur : ventes, scans QR, avis | C |

---

## 6. Blockchain & preuves

| ID | Besoin | P. |
|---|---|---|
| B-01 | À chaque événement chaîne (récolte, pressage, analyse, lot, export) → **hash SHA-256** du payload | M |
| B-02 | Ancrage du hash sur blockchain (à définir : privée, publique, ou ancrage périodique sur chaîne publique) | M |
| B-03 | Page publique de vérification : afficher hash + statut « conforme / altéré » | M |
| B-04 | Registre des preuves consultable par n° de lot | M |
| B-05 | Horodatage certifié | S |
| B-06 | Signature électronique des acteurs sur les événements critiques | S |

> **Décision architecturale à trancher avec l'expert blockchain** : registre privé (Hyperledger/consortium) vs ancrage sur chaîne publique (Ethereum, Tezos…) — coût, vitesse, confiance publique.

---

## 7. Données principales (entités)

| Entité | Champs clés |
|---|---|
| Producteur | nom, identifiant, contact, gouvernorat, certifications |
| Parcelle | producteur, superficie (ha), variétés, géoloc, irriguée |
| Récolte | parcelle, date, quantité olives (kg), bulletin, opérateur |
| Moulin | nom, capacité, certifications, localisation |
| Pressage | moulin, date, kg olives, L huile, rendement %, paramètres process |
| Laboratoire | nom, accréditation ISO 17025 |
| Analyse | lot, labo, date, 17 paramètres, verdict, plan d'échantillonnage, rapport PDF |
| Conditionneur | nom, format, ligne de conditionnement |
| Lot | numéro OLV, sources (pressages/assemblages), format, quantité, QR, statut |
| Exportateur | nom, destination(s), références |
| Export | lot(s), destination, transporteur, documents, statut |
| Dossier | export, liste documents, avancement, statut |
| Produit (B2C) | lot(s), fiche commerciale, prix, stock, photos, QR |
| Commande | client, produits, montant, paiement, livraison, statut |
| Certification | acteur, organisme, type, n°, dates émission/expiration, statut |
| Événement blockchain | étape, lot, hash, horodatage, émetteur |

---

## 8. Exigences non-fonctionnelles

| ID | Exigence | Cible |
|---|---|---|
| NF-01 | Disponibilité | ≥ 99,5 % (hors maintenance) |
| NF-02 | Temps de réponse | < 2 s (fiche publique, scan QR) |
| NF-03 | Mobile-first | App producteur + fiche QR responsive |
| NF-04 | Hors ligne | Saisie terrain sans connexion, synchro différée |
| NF-05 | Sécurité | HTTPS, RBAC par rôle, audit des accès |
| NF-06 | Données | RGPD-like / loi tunisienne protection données, anonymisation possible |
| NF-07 | Scalabilité | ≥ 100 k lots/an, ≥ 1 M scans QR/an |
| NF-08 | Intégrité | aucune modification silencieuse — tout est versionné |
| NF-09 | Multi-langue | arabe / français / anglais (fiche publique) |
| NF-10 | Interopérabilité | API REST pour capteurs IoT, balances, ERP |
| NF-11 | Sauvegarde | données chiffrées, backup quotidien, RPO < 24 h |

---

## 9. Architecture cible (proposition)

```
┌─────────────────────────────────────────────────────────────┐
│  FRONT : web admin (React/Vue) + app mobile (React Native/    │
│  Flutter) + fiches publiques QR (SSR, SEO-friendly)           │
├─────────────────────────────────────────────────────────────┤
│  API REST / GraphQL — auth JWT, RBAC, audit trail             │
├─────────────────────────────────────────────────────────────┤
│  BACK-END : services métier — Acteurs / Chaîne / Analyses /   │
│  Export / Boutique / Notifications                            │
├─────────────────────────────────────────────────────────────┤
│  DONNÉES : PostgreSQL (métier) + IPFS (docs/photos) +          │
│  blockchain (hashes) + cache Redis                            │
├─────────────────────────────────────────────────────────────┤
│  IoT : MQTT ou API → relevés capteurs → alertes               │
└─────────────────────────────────────────────────────────────┘
```

---

## 10. Phasage (proposition)

| Phase | Contenu | Livrable |
|---|---|---|
| **MVP** | Chaîne parcelle→lot + QR + fiche publique + analyses + hash blockchain | Traçabilité vérifiable |
| **V1** | + Export/dossiers + certifications + ISO 22000 + catalogue boutique | Filiale B2B complète |
| **V2** | + E-commerce (panier, paiement, livraison) + IoT + carbone + coupage | Plateforme commerciale |
| **V3** | + App producteur hors ligne + API ouverte + autres filières (DateTrace…) | Suite nationale |

---

## 11. Questions ouvertes — pour l'expert dev & blockchain

À trancher ensemble avant démarrage :

| # | Question | Enjeu |
|---|---|---|
| 1 | **Quelle blockchain ?** — privée (Hyperledger/consortium) vs ancrage public (Ethereum, Tezos, Polygon…) | Coût par transaction, confiance publique, vitesse |
| 2 | **Granularité des preuves** : hash par événement, par lot, ou Merkle-tree agrégé ? | Coût vs granularité |
| 3 | **Qui signe ?** — comment authentifier l'acteur qui saisit (clé privée, signature électronique, identité tunisienne) ? | Anti-fraude |
| 4 | **Données hors chaîne** : photos, PDF, bulletins → IPFS ? Cloud ? | Stockage, confidentialité |
| 5 | **Stack** : React/Vue + Node/Python/Go + PostgreSQL — ou microservices ? | Maintenabilité, équipe |
| 6 | **Mobile** : React Native, Flutter, ou PWA ? | Terrain hors ligne, iOS+Android |
| 7 | **Paiement e-commerce** : quelle solution pour la Tunisie (Paymee, Konnect, virement) ? | Vente réelle |
| 8 | **QR dynamique ou statique ?** — contenu dans le QR ou juste l'URL ? | Révocabilité, offline |
| 9 | **Intégration IoT** : MQTT vs API REST — quels capteurs, quelle fréquence ? | Données temps réel |
| 10 | **Modèle économique** : SaaS par acteur, commission vente, ou subvention nationale ? | Pérennité |

---

## 12. Références & annexes

- **Démo statique** : `output/olivetrace/` — 15 modules, données réalistes (lot `OLV-2026-0001`)
- **Rapport d'entités** : `rapports/02-olivetrace-entites-champs.md` — tous les champs par formulaire
- **Référence commerciale** : OrigoVerro (IT) — modèle QR + vente + transparence
- **Références réglementaires** : IOC, Règlement CE 2568/91, ISO 22000, ISO 17025, IFS Food, BRCGS, EUR.1, RASFF, ONPV
