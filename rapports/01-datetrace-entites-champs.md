# DateTrace — Inventaire des entités et champs de formulaires

*Rapport généré le 2026-11-11 — extraction automatique des formulaires capturés (`output/datetrace/*--form.html`).*

## Vue d'ensemble

| # | Entité | Écran | Formulaire | Champs |
|---|--------|-------|------------|--------|
| 1 | Lots | `lots.html` | Nouveau Lot | 11 |
| 2 | Producteurs | `producteurs.html` | Ajouter Producteur | 10 |
| 3 | Étapes de production | `etapes.html` | Ajouter Étape | 9 |
| 4 | Chaîne du froid | `chaine-froid.html` | Nouveau segment | 16 |
| 5 | Certifications | `certifications.html` | Nouvelle Certification | 6 |
| 6 | Audits | `audits.html` | Nouvel Audit | 5 |
| 7 | CAPA (actions) | `capa.html` | Nouvelle Action | 8 |
| 8 | Évaluations fournisseurs | `evaluations-fournisseurs.html` | Nouvelle Évaluation | 10 |
| 9 | Analyses IA (pesticides) | `ia.html` | Nouvelle Analyse IA | 7 |
| 10 | Lieux / capteurs IoT | `iot.html` | Nouveau lieu | 11 |
| 11 | Utilisateurs | `users.html` | Nouvel utilisateur | 5 |
| | **Total** | | | **98** |

Modules sans formulaire capturé : Dashboard, Blockchain, PRP, QR & Traçabilité, Assistant IA.

## Lots

- **Écran :** `lots.html` — formulaire « Nouveau Lot » (`lots--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Producteur * | Liste déroulante | Oui | Ahmed Ben Salah — Nabeul | — |
| Variété * | Liste déroulante | Oui | Datte — Allig<br>Datte — Boufeggous<br>Datte — Deglet Nour<br>Datte — Kenta<br>Datte — Kentichi<br>Datte — Khouat Allig | — |
| Date Récolte | Date | Non | — | — |
| Date Conditionnement | Date | Non | — | — |
| Date Expiration | Date | Non | — | — |
| Quantité (kg) | Nombre | Non | — | Ex: 1500 |
| Nb. Boîtes | Nombre | Non | — | Ex: 3000 |
| Parcelle | Texte | Non | — | Ex: Parcelle Nord B3 |
| Pays Destination | Texte | Non | — | Ex: France, Allemagne |
| Supermarché cible | Texte | Non | — | Ex: Géant, Tesco |
| Remarques | Zone de texte | Non | — | — |

## Producteurs

- **Écran :** `producteurs.html` — formulaire « Ajouter Producteur » (`producteurs--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Nom * | Texte | Oui | — | — |
| Gouvernorat | Liste déroulante | Non | Ariana<br>Nabeul<br>Ben Arous<br>Bizerte<br>Gabès<br>Gafsa<br>Jendouba<br>Kairouan<br>Kasserine<br>Kébili<br>Kef<br>Mahdia<br>Manouba<br>Médenine<br>Monastir<br>Sfax<br>Sidi Bouzid<br>Siliana<br>Sousse<br>Tataouine<br>Tozeur<br>Tunis<br>Zaghouan | — |
| Région / Délégation | Texte | Non | — | — |
| Superficie (ha) | Nombre | Non | — | — |
| GlobalG.A.P. | Case à cocher | Non | — | — |
| Certification Bio | Case à cocher | Non | — | — |
| Tesco TN+ | Case à cocher | Non | — | — |
| Contact | Texte | Non | — | Nom |
| Tél | Texte | Non | — | +216... |
| Email | Email | Non | — | — |

## Étapes de production

- **Écran :** `etapes.html` — formulaire « Ajouter Étape » (`etapes--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Type d'étape * | Liste déroulante | Oui | 🌴 Récolte (régime de dattes, stade Tamr)<br>⚖️ Tri &amp; Calibrage<br>💧 Lavage / Désinfection<br>☀️ Séchage (naturel ou contrôlé)<br>🔥 Traitement thermique / Pasteurisation<br>📦 Conditionnement (vrac, boîtes, barquettes)<br>❄️ Stockage frigorifique<br>🔬 Contrôle Qualité (résidus, microbiologie)<br>🌬️ Fumigation phytosanitaire export<br>✅ Certification Biologique (Ecocert/INNORPI)<br>🚛 Expédition export | — |
| Type d'exécution | Sélecteur à boutons | Non | Initial, Retravail, Contrôle | — |
| Date début | Date + heure | Non | — | — |
| Date fin | Date + heure | Non | — | — |
| Lieu | Liste déroulante | Non | — | — |
| Temp (°C) | Nombre | Non | — | auto |
| Humidité (%) | Nombre | Non | — | auto |
| Score qualité | Nombre | Non | — | — |
| Notes | Zone de texte | Non | — | — |

## Chaîne du froid

- **Écran :** `chaine-froid.html` — formulaire « Nouveau segment » (`chaine-froid--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Lot * | Liste déroulante | Oui | — | — |
| Phase * | Liste déroulante | Oui | Pré-refroidissement<br>Chambre froide<br>Transport refrigere<br>Distribution<br>Livraison | — |
| Lieu | Texte | Non | — | Entrepôt, camion... |
| Responsable | Texte | Non | — | Nom du responsable |
| Temp. cible (°C) | Nombre | Non | — | — |
| Min autorisé (°C) | Nombre | Non | — | — |
| Max autorisé (°C) | Nombre | Non | — | — |
| Temp. min obs. (°C) | Nombre | Non | — | ex: 1.2 |
| Temp. max obs. (°C) | Nombre | Non | — | ex: 3.8 |
| Temp. moyenne obs. (°C) | Nombre | Non | — | ex: 2.5 |
| Humidité moyenne (%) | Nombre | Non | — | ex: 90 |
| Score intégrité (%) | Nombre | Non | — | 0-100 |
| Statut | Liste déroulante | Non | En cours<br>Conforme<br>Rupture<br>Avertissement<br>Termine | — |
| Date début | Date + heure | Non | — | — |
| Date fin | Date + heure | Non | — | — |
| Notes | Zone de texte | Non | — | Observations... |

## Certifications

- **Écran :** `certifications.html` — formulaire « Nouvelle Certification » (`certifications--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Lot * | Liste déroulante | Oui | DT-2026-0001-AB7F — Deglet Nour (Ahmed Ben Salah) | — |
| Type de certification * | Liste déroulante | Oui | ✅ GlobalG.A.P.<br>🌿 Certification Bio<br>🏪 Tesco TN+<br>🔬 Phytosanitaire<br>📋 ISO 22000<br>🏆 BRC Food<br>🇪🇺 IFS Food<br>⚙️ HACCP<br>🇪🇺 export_UE<br>🌍 export_GCC<br>📄 Autre | — |
| Numéro | Texte | Non | — | Ex: TN-0012-2026 |
| Organisme | Texte | Non | — | Ex: Control Union |
| Date d'émission | Date | Non | — | — |
| Date d'expiration | Date | Non | — | — |

## Audits

- **Écran :** `audits.html` — formulaire « Nouvel Audit » (`audits--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Référence * | Texte | Oui | — | — |
| Type d'audit | Liste déroulante | Non | Interne<br>Externe<br>Certification<br>Suivi | — |
| Date planifiée * | Date | Oui | — | — |
| Périmètre (scope) | Zone de texte | Non | — | — |
| Auditeur | Texte | Non | — | — |

## CAPA (actions)

- **Écran :** `capa.html` — formulaire « Nouvelle Action » (`capa--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Référence * | Texte | Oui | — | — |
| Titre * | Texte | Oui | — | — |
| Type | Liste déroulante | Non | Corrective<br>Préventive | — |
| Priorité | Liste déroulante | Non | Basse<br>Normale<br>Haute<br>Critique | — |
| Description | Zone de texte | Non | — | — |
| Source | Texte | Non | — | Ex: audit, NC, PRP |
| Responsable | Texte | Non | — | — |
| Date d'échéance | Date | Non | — | — |

## Évaluations fournisseurs

- **Écran :** `evaluations-fournisseurs.html` — formulaire « Nouvelle Évaluation » (`evaluations-fournisseurs--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Producteur * | Liste déroulante | Oui | Ahmed Ben Salah (PROD-2026-01) | — |
| Date d'évaluation * | Date | Oui | — | — |
| Score Qualité (0-100) | Nombre | Non | — | — |
| Score Délais (0-100) | Nombre | Non | — | — |
| Score Conformité (0-100) | Nombre | Non | — | — |
| Score Documentation (0-100) | Nombre | Non | — | — |
| Statut d'approbation | Liste déroulante | Non | Approuvé<br>Sous surveillance<br>Refusé | — |
| Certifications vérifiées | Texte | Non | — | Ex: Bio, GlobalG.A.P. |
| Observations | Zone de texte | Non | — | — |
| Prochaine évaluation | Date | Non | — | — |

## Analyses IA (pesticides)

- **Écran :** `ia.html` — formulaire « Nouvelle Analyse IA » (`ia--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Lot à analyser * | Liste déroulante | Oui | 🌴 DT-2026-0001-AB7F — Deglet Nour (Ahmed Ben Salah) | — |
| Laboratoire | Texte | Non | — | Labo National Sfax |
| Méthode | Texte | Non | — | — |
| Chlorpyrifos | Nombre | Non | — | 0.000 |
| Imidaclopride | Nombre | Non | — | 0.000 |
| Azoxystrobine | Nombre | Non | — | 0.000 |
| Boscalide | Nombre | Non | — | 0.000 |

## Lieux / capteurs IoT

- **Écran :** `iot.html` — formulaire « Nouveau lieu » (`iot--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Nom du lieu * | Texte | Oui | — | Ex: Chambre Froide Nord — Grombalia |
| Type * | Sélecteur à boutons | Oui | Entrepôt, Chambre froide, Conditionnement, Centre de distribution | — |
| Région | Texte | Non | — | Ex: Nabeul |
| Gouvernorat | Texte | Non | — | Ex: Nabeul |
| Adresse | Texte | Non | — | Adresse complète |
| Responsable | Texte | Non | — | Nom du responsable |
| Tél. contact | Texte | Non | — | +216 XX XXX XXX |
| Temp. min cible (°C) | Nombre | Non | — | — |
| Temp. max cible (°C) | Nombre | Non | — | — |
| Capacité (kg) | Nombre | Non | — | Ex: 5000 |
| Notes | Zone de texte | Non | — | Informations complémentaires... |

## Utilisateurs

- **Écran :** `users.html` — formulaire « Nouvel utilisateur » (`users--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Nom * | Texte | Oui | — | Ben Salem |
| Prénom | Texte | Non | — | Ahmed |
| Email * | Email | Oui | — | ahmed@datetrace.tn |
| Rôle * | Sélecteur à boutons | Oui | admin, superviseur, operateur | — |
| Mot de passe * | Mot de passe | Oui | — | Min. 8 caractères |
