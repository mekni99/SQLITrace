# OliveTrace — Données métier à valider par l'expert

> **Objet du document** : référentiel des données métier utilisées dans la plateforme OliveTrace
> (traçabilité huile d'olive Tunisie → export). Chaque section contient les valeurs réellement
> utilisées dans la démo + les normes de référence. Merci de **corriger toute valeur, seuil,
> document ou organisme inexact** — les corrections seront reportées dans la plateforme.
>
> Date : 26/11/2026 · Contact : [à compléter]

---

## 1. Chaîne de traçabilité — étapes et codifications

| Étape | Code / format | Exemple réel (démo) | Remarque |
|---|---|---|---|
| Parcelle | déclaration SI Oli | Henchir el Ain (Nabeul) | géoréférencée, surface en ha |
| Récolte | `BV-YYYY-NNNN` (bon de pesée) | BV-2026-0102 | méthode, maturité, statut |
| Pressage | `TM-YYYY-NNNN` (ticket moulin) | TM-2026-0210 | entrée kg → sortie L, rendement |
| Analyse | `RA-YYYY-NNNN` (rapport labo) | RA-2026-0388 | 17 paramètres COI |
| Lot conditionné | `OLV-YYYY-NNNN` | OLV-2026-0001 | scellé blockchain + QR GS1 |
| Déclaration export | `DE-YYYY-NNNN` | DE-2026-9105 | liée à la DUM douane |
| Facture | `FA-YYYY-NNNN` | FA-2026-0417 | commerciale |
| Capteur IoT | `SN-NNNN` | SN-2201 | TNEnergy |

**Question expert** : ces formats internes sont-ils cohérents avec les usages tunisiens
(ONH, douane, moulin) ? Existe-t-il des codes réglementaires obligatoires à afficher ?

---

## 2. Acteurs de la filière (données de démonstration)

### 2.1 Producteurs
| Nom | Région | Parcelles | Récolté | Moulin habituel |
|---|---|---|---|---|
| Sami Ben Amor | Nabeul | 2 | 4 200 kg | Moulin Ennour |
| Mohamed Trabelsi | Sfax | 3 | 6 800 kg | Moulin El Baraka |
| Fatma Gharbi | Kairouan | 2 | 3 900 kg | Moulin Ennour |
| Ali Ben Salah | Béja | 4 | 7 100 kg | Moulin Errim |
| Leïla Mansour | Zaghouan | 1 | 2 300 kg | Huilerie El Amel |

### 2.2 Parcelles
| Parcelle | Producteur | Variété | Surface | Certification |
|---|---|---|---|---|
| Henchir el Ain | Sami Ben | Chemlali | 8,00 ha | biologique |
| Ferme El Wafa | Mohamed Trabelsi | Chetoui | 12,50 ha | biologique |
| Dar Essalem | Fatma Gharbi | Chemlali | 6,00 ha | conventionnel |
| Les Oliviers du Nord | Ali Ben Salah | Oueslati | 15,00 ha | biologique |
| Henchir Bouzid | Leïla Mansour | Arbequina | 4,50 ha | en conversion |

### 2.3 Moulins
| Moulin | Région | Procédé | Capacité | Statut |
|---|---|---|---|---|
| Moulin Ennour | Sfax | Centrifugation 2 phases | 3,00 T/j | bio |
| Moulin El Baraka | Sfax | Centrifugation 3 phases | 8,00 T/j | bio |
| Moulin Errim | Béja | Pression traditionnelle | 5,00 T/j | bio |
| Huilerie El Amel | Zaghouan | Centrifugation 2 phases | 10,00 T/j | bio |

### 2.4 Laboratoires (accès en saisie d'analyses)
- **Olea analyses** — Sfax (accrédité TUNAC, voir §5)
- **ONAGRI — Laboratoire Central** — Tunis
- **SGS Tunisia Lab**
- laboratoire interne moulin (contrôle courant)

### 2.5 Conditionneurs
- El Amel Conditionnement (Sfax) — 560 L
- Société Méditerranée Emballage (Tunis) — 1 800 L
- Huile Prestige Packing (Sousse) — 720 L

### 2.6 Exportateurs
- El Amel Export → France · Méditerranée Trading → Italie · Atlas Olive Export → France

**Questions expert** : faut-il ajouter le n° d'agrément ONH des exportateurs, le n°
d'immatriculation des moulins, le code douane de chaque acteur ? Quels champs
d'identification sont **obligatoires** pour chaque rôle ?

---

## 3. Récoltes et pressages (mesures enregistrées)

| Date | Producteur | Variété | Quantité | Méthode | Maturité | Rendement réel |
|---|---|---|---|---|---|---|
| 01/10/2026 | Sami Ben | Chemlali | 3 000 kg | Mixte | Demi-mûre | 19,0 % (570 L) |
| 08/10/2026 | Ali Ben Salah | Oueslati | 3 200 kg | Mécanique | Mûre | 19,06 % (610 L) |
| 15/10/2026 | Mohamed Trabelsi | Chetoui | 2 400 kg | Manuelle | Mûre | 20,0 % (480 L) |
| 12/10/2026 | Fatma Gharbi | Chemlali | 1 800 kg | Mixte | Demi-mûre | 20,0 % (360 L) |
| 28/09/2026 | Mohamed Trabelsi | Chetoui | 2 100 kg | Mixte | Veraison | 19,05 % (400 L) |

Méthodes retenues : **manuelle / effleurage / mixte / mécanique**.
Maturités : **veraison / demi-mûre / mûre**.

**Questions expert** : rendements plausibles (19–22 %) ? Le suivi « délai
récolte → trituration < 24 h » est-il la bonne exigence qualité ?

---

## 4. Analyses laboratoire — les 17 paramètres COI/IOC

Références : **COI/T.15/NC n°3** (norme commerciale IOC) et **règlement CE 2568/91**
+ amendements (UE 2022/2104) appliqués automatiquement.

### 4.1 Seuils de classification utilisés

| Paramètre | Extra vierge | Vierge | Unité |
|---|---|---|---|
| Acidité libre | ≤ 0,8 % | ≤ 2,0 % | % acide oléique |
| Indice de peroxyde | ≤ 20 | ≤ 20 | meq O₂/kg |
| K232 | ≤ 2,50 | ≤ 2,60 | — |
| K270 | ≤ 0,22 | ≤ 0,25 | — |
| ΔK | ≤ 0,01 | ≤ 0,01 | — |
| Organoleptique — défaut médian (Md) | Md = 0 | Md ≤ 3,5 | — |
| Organoleptique — fruité médian (Mf) | Mf > 0 | Mf > 0 | — |
| Humidité et matières volatiles | ≤ 0,2 % | ≤ 0,2 % | — |
| Impuretés insolubles | ≤ 0,1 % | ≤ 0,1 % | — |

### 4.2 Paramètres de pureté contrôlés

| Paramètre | Limite | Valeur mesurée (lot OLV-2026-0001) |
|---|---|---|
| Acide oléique (C18:1) | 55–83 % | 61,5 % |
| Acide palmitique (C16:0) | 7,5–20 % | 15,9 % |
| Acide stéarique (C18:0) | 0,5–5 % | 2,4 % |
| Acide linoléique (C18:2) | 2,5–21 % | 16,8 % |
| Acide α-linolénique (C18:3) | ≤ 1,0 % | 0,8 % |
| Campestérol | ≤ 4,0 % | 3,4 % |
| β-sitostérol apparent | ≥ 93,0 % | 93,6 % |
| Stérols totaux | ≥ 1 000 mg/kg | 1 620 mg/kg |
| Érythrodiol + uvaol | ≤ 4,5 % | 2,6 % |
| Cires (C40–C46) | ≤ 150 mg/kg | 85 mg/kg |
| Esters éthyliques (FAEEs) | ≤ 35 mg/kg | 14 mg/kg |
| Stigmastadiènes | ≤ 0,05 mg/kg | 0,02 mg/kg |

### 4.3 Exemples d'analyses saisies (démo)

| Date | Labo | Producteur · Variété | Acidité | Peroxyde | K232 | K270 | Oléique | Catégorie |
|---|---|---|---|---|---|---|---|---|
| 02/10/2026 | Olea (Sfax) | Sami Ben · Chemlali | 0,38 % | 9,5 | 1,92 | 0,16 | 61,5 % | Extra vierge |
| 18/10/2026 | ONAGRI | M. Trabelsi · Chetoui | 0,32 % | 8,2 | 1,78 | 0,14 | 63,2 % | Vierge |
| 05/10/2026 | SGS Tunisia | A. Ben Salah · Oueslati | 0,89 % | 14,5 | 2,64 | 0,218 | 57,4 % | Vierge |
| 10/10/2026 | Labo interne | Chemlali | 0,60 % | 20,0 | 2,499 | 0,199 | 54,0 % | Vierge |

> ⚠️ Cas pédagogique intégré : l'analyse SGS du 05/10 (K232 = 2,64) dépasse la limite
> « Vierge » (2,60) → signalée par le contrôle automatique ; le statut « Document »
> déclenche la lecture IA du rapport PDF.

**Questions expert** :
- Le seuil **linoléique 2,5–21 %** est-il correct pour la Tunisie (certaines normes
  admettent jusqu'à 21 % pour huiles à forte teneur en linoléique) ?
- FAEEs : la limite 35 mg/kg s'applique-t-elle à l'extra vierge *et* vierge, ou
  limite différente pour origines particulières ?
- Faut-il intégrer le **2-monopalmitate de glycéryle (≤ 0,9/1,0 %)** et la
  **différence ECN42 (|≤ 0,2|)** dans les 17 paramètres ?
- Les autres acides gras (myristique ≤ 0,03 %, palmitoléique 0,3–3,5 %,
  margarique ≤ 0,4 %, arachidique ≤ 0,6 %, béhénique ≤ 0,2 %, lignocérique ≤ 0,2 %,
  eicosénoïque, heptadécénoïque) — à ajouter en saisie complète ?
- Stérols : cholestérol ≤ 0,5 %, brasicastérol ≤ 0,1 %, stigmastérol < campestérol,
  Δ7-stigmasténol ≤ 0,5 % — à ajouter ?

---

## 5. Certifications et organismes

| Certification | Organisme | Référence (démo) | Détenteur | Expiration |
|---|---|---|---|---|
| Biologique | **Ecocert** | TN-BIO-2026-0457 | Sami Ben Amor (producteur) | 14/01/2027 |
| Biologique | **Ecocert** | TN-BIO-2026-0521 | Mohamed Trabelsi | 20/09/2027 |
| ISO 22000 (SMSA) | Bureau Veritas | Certif TN BV-TN-22K-2025-118 | Moulin Ennour | 09/06/2028 |
| ISO/IEC 17025 (accréditation labo) | **TUNAC** | LAB-TN-0417 | Olea analyses Sfax | 28/02/2029 |
| HACCP | SGS Tunisia | CERT-HACCP-2026-089 | El Amel Conditionnement | 02/03/2027 |

Organismes tunisiens cités : **ONH** (Office National de l'Huile — agrément export),
**ONPV** (certificat phytosanitaire), **TUNAC** (accréditation), **ONAGRI** (contrôle).

**Questions expert** :
- Format des numéros de certificat Ecocert Tunisie — réaliste ?
- Un exporteur doit-il être **agréé ONH** ? Autres agréments obligatoires
  (ONAA, ministère du commerce) ?
- BRCGS / IFS / FDA (FSMA) à prévoir pour d'autres destinations (USA, UK) ?
- Certification ISO 22000 délivrée en Tunisie : quels organismes accrédités ?

---

## 6. Export / Import — documents et procédure

### 6.1 Exports enregistrés (démo)

| Lot | Exportateur | Destination | Volume | Port | Déclaration | Statut |
|---|---|---|---|---|---|---|
| OLV-2026-0001 | El Amel export | France | 560 L | Port de Sfax | DE-2026-9105 | En transit |
| OLV-2026-0002 | Méditerranée Trading | Italie | 1 200 L | Port de Sfax | DE-2026-9211 | Expédié |
| OLV-2026-0003 | Atlas Olive Export | France | 720 L | Port de Radès | DE-2026-9345 | En préparation |

### 6.2 Documents générés automatiquement par dossier (destination UE)

| # | Document | Statut dans la démo | Source |
|---|---|---|---|
| 1 | Déclaration de conformité **RASFF** | Requis — à joindre | Réglementaire |
| 2 | **Certificat d'analyse COI** (règ. CE 2568/91) | ✔ coché auto (scellé blockchain) — RA-2026-0388 | Qualité |
| 3 | **EUR.1** — certificat d'origine préférentielle Tunisie–UE | ✔ coché auto — A_2026-61834 | Origine |
| 4 | **Certificat phytosanitaire ONPV** | Requis — à joindre | Sanitaire |
| 5 | **Connaissement maritime** (B/L) ou LTA | Requis — à joindre | Transport |
| 6 | **Déclaration en douane (DUM)** | ✔ coché auto — DE-2026-9105 | Douane |
| 7 | **Déclaration nutritionnelle** (étiquetage UE 1169/2011) | Requis — à joindre | Étiquetage |
| 8 | **Facture commerciale** | ✔ coché auto — FA-2026-0417 | Commercial |
| 9 | **Packing list** | Requis — à joindre | Logistique |
| 10 | **Certificat biologique** (si applicable) | Optionnel — TN-BIO-2026-0457 | Bio |

Règle métier : *« Cocher un document exige de joindre son fichier — l'IA lit le PDF,
compare aux valeurs saisies et scelle le résultat dans la blockchain. »*

### 6.3 Exigences par destination (à valider)

| Destination | Exigences spécifiques envisagées |
|---|---|
| UE | EUR.1, CE 2568/91 + 1169/2011, RASFF, certificat bio (règ. 2018/848 si bio) |
| USA | FDA prior notice, FSMA, nutrition facts FDA (pas EUR.1) |
| Canada / UK / Golfe | à définir selon marchés |

**Questions expert** :
- La liste des 10 documents est-elle **complète et correcte** pour un export UE ?
  Manque-t-il : attestation de circulation, certificat sanitaire DGCCRF,
  conformité matériaux au contact (1935/2004) ?
- Le **phytosanitaire ONPV** est-il réellement requis pour l'huile d'olive
  (produit transformé) ou seulement pour les olives ? 
- Délai « avant le 22/10 » affiché par dossier — quel délai réglementaire
  réel s'applique ?
- Côté **import** : la plateforme doit-elle aussi tracer l'import de matières
  (bouteilles, capsules, étiquettes, carton) ? Certificats fournisseurs requis ?

---

## 7. Conditionnement — formats et étiquetage

| Format | Lot | Volume total | DLUO / best before |
|---|---|---|---|
| Bouteille verre 0,5 L | OLV-2026-0001 | 560 L | 30/04/2028 |
| Bouteille verre 0,75 L | OLV-2026-0002 | 1 200 L | 30/04/2028 |
| Bidon 5 L | OLV-2026-0003 | 720 L | 31/05/2028 |
| Bouteille verre 1 L | OLV-2026-0004 | 600 L | 30/06/2028 |

Chaque contenant reçoit un **QR unique (GS1 Digital Link)** → page publique de
vérification (voyage du lot + preuve blockchain).

**Questions expert** :
- DLUO typique huile d'olive : 18–24 mois — la règle à appliquer ?
- Mentions obligatoires à l'étiquette UE : origine, catégorie, mode d'extraction
  (« première pression à froid » / « extraction à froid »), lots, allergènes ?
- QR : faut-il un **sérial unique par bouteille** (anti-contrefaçon) ou par lot ?

---

## 8. Valeurs nutritionnelles (déclaration UE — règ. 1169/2011)

Tableau indicatif utilisé pour l'étiquette (par 100 ml d'huile d'olive vierge extra) :

| Nutriment | Pour 100 ml | % VNR* |
|---|---|---|
| Énergie | 3 389 kJ / 824 kcal | 41 % |
| Matières grasses | 91,6 g | 131 % |
| — dont acides gras saturés | 13,8 g | 69 % |
| — dont acides gras mono-insaturés | ~66 g | — |
| — dont acides gras polyinsaturés | ~8,5 g | — |
| Glucides | 0 g | 0 % |
| — dont sucres | 0 g | 0 % |
| Protéines | 0 g | 0 % |
| Sel | 0 g | 0 % |
| Vitamine E | ~14 mg | 117 % |
| Vitamine K | ~60 µg | 80 % |

\* VNR = Valeurs Nutritionnelles de Référence.

**Questions expert** : les valeurs mono/poly-insaturées varient selon la variété
(Chemlali vs Chetoui) — faut-il calculer la déclaration **par lot** depuis le profil
en acides gras mesuré, ou utiliser des valeurs moyennes ? Tolérances UE ?

---

## 9. Blockchain, IoT et carbone

- **Chaîne interne SHA-256** : chaque étape, contrôle IA et correction = un bloc
  chaîné (ex. bloc #37 « lot seal OLV-2026-0001 », hash `1abff53d…`).
- **Ancrage Bitcoin (OpenTimestamps)** : preuve `.ots` publique vérifiable sur
  opentimestamps.org (ex. bloc Bitcoin #972670).
- **Vérification IA des documents** : lecture PDF → comparaison valeurs → scellé
  (~0,01 $/page).
- **IoT TNEnergy** : chambre froide quai Sfax (−2,4 °C), cuve stockage (18,2 °C),
  salle de trituration (24,7 °C), entrepôt conditionnement (19,8 °C), camion
  frigorifique Sfax–Radès (3,1 °C).
- **Empreinte carbone** : méthode ISO 14067 simplifiée, facteurs ADEME/Agribalyse —
  OLV-2026-0001 : 412 kg CO₂e · OLV-2026-0002 : 688 kg · OLV-2026-0003 : 356 kg
  (répartition : verger 38 %, trituration 18 %, emballage 20 %, transport 24 %).

**Questions expert** : plage de température réglementaire pour stockage huile en cuve
(≈ 15–20 °C ?) — les seuils d'alerte IoT sont-ils justes ? Répartition carbone
réaliste pour la filière ?

---

## 10. ISO 22000 / HACCP intégré

- Procédures documentées (code, version, type)
- **HACCP** : dangers par étape (biologique/chimique/physique/allergène), sévérité,
  points critiques CCP avec limites critiques, surveillance, actions correctives
- Audits internes + **CAPA** (référence, source, causes, actions)

**Question expert** : quels **CCP réels** de la filière huile d'olive faut-il
pré-remplir (trituration, filtration, stockage cuve, mise en bouteille) ?

---

## 11. Points ouverts soumis à correction

1. **Codifications** (OLV/TM/BV/DE/RA/FA) : formats acceptables ou normalisation imposée ?
2. **17 paramètres COI** : la liste est-elle complète/exacte pour un contrôle qualité
   tunisien + export UE (ajouter ECN42, 2-MG, tous acides gras, tous stérols) ?
3. **Seuils** : vérifier chaque valeur du tableau §4 (virgin/extra virgin + pureté).
4. **Documents export UE** : liste complète ? ONPV requis pour huile ? RASFF statement ?
5. **ONH** : rôle exact à intégrer (agrément exportateur, contrôle qualité pré-export,
   certificat de qualité) ?
6. **Nutrition** : calcul par lot vs moyenne — tolérances légales ?
7. **Étiquette** : mentions obligatoires UE + Tunisie ; QR par bouteille ou par lot ?
8. **CCP HACCP** : liste de référence de la filière ?
9. **Carbone** : facteurs et périmètre (cultivation → port destination ? livraison client ?)
10. **Marchés hors UE** (USA, Golfe, Asie) : exigences documentaires spécifiques ?

---

*Document généré depuis les données réelles de la démo OliveTrace — chaque
correction de l'expert sera reportée dans les écrans de la plateforme.*
