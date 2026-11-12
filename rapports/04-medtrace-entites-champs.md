# MedTrace — Inventaire des entités et champs de formulaires

*Rapport généré le 2026-11-11 — extraction automatique des formulaires capturés (`output/medtrace/*--*.html`).*

## Vue d'ensemble

| # | Entité | Écran | Formulaire | Champs |
|---|--------|-------|------------|--------|
| 1 | Médicaments | `medicaments.html` | Nouveau médicament | 11 |
| 2 | Lots & sérialisation | `lots.html` | Nouveau lot | 6 |
| 3 | Distributions | `distributions.html` | Nouvelle distribution | 4 |
| 4 | Pharmacies | `pharmacies.html` | Nouvelle pharmacie | 6 |
| 5 | Laboratoires | `laboratoires.html` | Nouveau laboratoire | 7 |
| 6 | Hôpitaux / établissements | `hopitaux.html` | Nouvel établissement | 7 |
| 7 | Stupéfiants | `stupefiants.html` | Nouvelle dispensation | 3 |
| 8 | Chaîne du froid (DPM) | `temperature.html` | Ajouter mesure | 3 |
| 9 | Inspections DPM | `inspections.html` | Nouvelle inspection | 7 |
| 10 | Utilisateurs | `utilisateurs.html` | Nouvel utilisateur | 5 |
| | **Total** | | | **59** |

Entités sans formulaire capturé : Unités sérialisées, Rappels, Corrections, Conformité, IA & prédictions.

## Médicaments

- **Écran :** `medicaments.html` — formulaire « Nouveau médicament » (`medicaments--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Nom commercial * | Texte | Oui | — | — |
| Nom générique | Texte | Non | — | — |
| DCI * | Texte | Oui | — | — |
| Forme | Texte | Non | — | — |
| Dosage | Texte | Non | — | — |
| Fabricant | Texte | Non | — | — |
| Pays origine | Texte | Non | — | — |
| N° AMM | Texte | Non | — | — |
| Classe thérapeutique | Texte | Non | — | — |
| Stupéfiant | Case à cocher | Non | — | — |
| Prescription obligatoire | Case à cocher | Non | — | — |

## Lots & sérialisation

- **Écran :** `lots.html` — formulaire « Nouveau lot » (`lots--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Médicament * | Liste déroulante | Oui | Amoxicilline 500mg — 500mg<br>Morfine 10mg — 10mg/ml<br>Paracétamol 1g — 1000mg | — |
| Numéro de lot * | Texte | Oui | — | — |
| Date fabrication * | Date | Oui | — | — |
| Date péremption * | Date | Oui | — | — |
| Quantité produite * | Nombre | Oui | — | — |
| Température stockage | Texte | Non | — | — |

## Distributions

- **Écran :** `distributions.html` — formulaire « Nouvelle distribution » (`distributions--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Lot * | Liste déroulante | Oui | Amoxicilline 500mg — Lot lot-2026-001 (100 dispo) | — |
| Pharmacie * | Liste déroulante | Oui | Pharmacie Centrale Tunis — Tunis<br>Pharmacie El Amal — Sfax<br>Pharmacie Ibn Sina — Sousse | — |
| Quantité * | Nombre | Oui | — | — |
| Notes | Texte | Non | — | — |

## Pharmacies

- **Écran :** `pharmacies.html` — formulaire « Nouvelle pharmacie » (`pharmacies--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Nom * | Texte | Oui | — | — |
| Adresse | Texte | Non | — | — |
| Ville * | Texte | Oui | — | — |
| Téléphone | Texte | Non | — | — |
| Email | Texte | Non | — | — |
| N° Autorisation | Texte | Non | — | — |

## Laboratoires

- **Écran :** `laboratoires.html` — formulaire « Nouveau laboratoire » (`laboratoires--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Nom du laboratoire * | Texte | Oui | — | — |
| Pays | Texte | Non | — | — |
| Licence de fabrication | Texte | Non | — | LF-TN-... |
| Email | Email | Non | — | — |
| Téléphone | Texte | Non | — | — |
| Adresse | Texte | Non | — | — |
| Site web | Texte | Non | — | https://... |

## Hôpitaux / établissements

- **Écran :** `hopitaux.html` — formulaire « Nouvel établissement » (`hopitaux--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Nom de l'établissement * | Texte | Oui | — | — |
| Type | Liste déroulante | Non | Hôpital public<br>Clinique privée<br>Polyclinique<br>Centre de santé<br>Hôpital universitaire | — |
| Ville | Texte | Non | — | — |
| Téléphone | Texte | Non | — | — |
| Email | Email | Non | — | — |
| N° autorisation | Texte | Non | — | — |
| Adresse | Texte | Non | — | — |

## Stupéfiants

- **Écran :** `stupefiants.html` — formulaire « Nouvelle dispensation » (`stupefiants--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Pharmacie * | Liste déroulante | Oui | Pharmacie Centrale Tunis<br>Pharmacie El Amal<br>Pharmacie Ibn Sina | — |
| Référence ordonnance * | Texte | Oui | — | — |
| Votre mot de passe (1ère signature) * | Mot de passe | Oui | — | — |

## Chaîne du froid (DPM)

- **Écran :** `temperature.html` — formulaire « Ajouter mesure » (`temperature--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Lot concerné * | Liste déroulante | Oui | Amoxicilline 500mg — Lot lot-2026-001 | — |
| Température (°C) * | Nombre | Oui | — | — |
| Humidité (%) | Nombre | Non | — | — |

## Inspections DPM

- **Écran :** `inspections.html` — formulaire « Nouvelle inspection » (`inspections--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Date d'inspection * | Date | Oui | — | — |
| Type * | Liste déroulante | Oui | ANMPS<br>OMS / BPF<br>FMD<br>Interne<br>Douane<br>Autre | — |
| Organisme inspecteur | Texte | Non | — | ANMPS, Inspecteur OMS... |
| Statut initial | Liste déroulante | Non | En cours<br>Conforme<br>Non conforme | — |
| Lots inspectés (numéros, séparés par virgule) | Texte | Non | — | LOT-2024-001, LOT-2024-002... |
| Observations | Zone de texte | Non | — | — |
| Recommandations | Zone de texte | Non | — | — |

## Utilisateurs

- **Écran :** `utilisateurs.html` — formulaire « Nouvel utilisateur » (`utilisateurs--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Nom * | Texte | Oui | — | — |
| Prénom * | Texte | Oui | — | — |
| Email * | Email | Oui | — | — |
| Mot de passe * | Mot de passe | Oui | — | — |
| Type d'accès * | Liste déroulante | Oui | Administrateur<br>Laboratoire<br>Pharmacie<br>Inspecteur<br>Hôpital | — |
