# OliveTrace — Inventaire des entités et champs de formulaires

*Rapport généré le 2026-11-11 — extraction automatique des formulaires capturés (`output/olivetrace/*--*.html`).*

## Vue d'ensemble

| # | Entité | Écran | Formulaire | Champs |
|---|--------|-------|------------|--------|
| 1 | Producteurs | `producteurs.html` | New producer | 9 |
| 2 | Parcelles oléicoles | `parcelles.html` | New plot | 7 |
| 3 | Récoltes | `recoltes.html` | New harvest | 10 |
| 4 | Moulins | `moulins.html` | New mill | 8 |
| 5 | Pressages | `pressages.html` | New pressing | 10 |
| 6 | Laboratoires | `laboratoires.html` | New laboratory | 5 |
| 7 | Conditionneurs | `conditionneurs.html` | New | 6 |
| 8 | Opérations | `operations.html` | New operation | 12 |
| 9 | Exportateurs | `exportateurs.html` | New exporter | 6 |
| 10 | Exports | `exports.html` | New export | 12 |
| 11 | Certifications | `certifications.html` | New certification | 11 |
| 12 | Conformité IOC | `conformite.html` | Manual check | 4 |
| 13 | Dossiers export | `dossiers.html` | Manual file | 4 |
| 14 | Points IoT / température | `iot.html` | New point | 5 |
| 15 | ISO 22000 — Procédures | `iso22000.html` | Procedures | 8 |
| 16 | ISO 22000 — HACCP | `iso22000.html` | HACCP | 10 |
| 17 | ISO 22000 — Audits internes | `iso22000.html` | Internal audits | 9 |
| 18 | ISO 22000 — Actions correctives | `iso22000.html` | Corrective actions | 10 |
| 19 | Documents | `documents.html` | New document | 4 |
| | **Total** | | | **150** |

Entités sans formulaire capturé : Analyses.

## Producteurs

- **Écran :** `producteurs.html` — formulaire « New producer » (`producteurs--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Name * | Texte | Oui | — | — |
| First name | Texte | Non | — | — |
| CIN | Texte | Non | — | — |
| Phone | Texte | Non | — | — |
| Email | Texte | Non | — | — |
| Address | Texte | Non | — | — |
| Governorate | Liste déroulante | Non | Tunis<br>Ariana<br>Ben Arous<br>Manouba<br>Nabeul<br>Zaghouan<br>Bizerte<br>Béja<br>Jendouba<br>Le Kef<br>Siliana<br>Sousse<br>Monastir<br>Mahdia<br>Sfax<br>Kairouan<br>Kasserine<br>Sidi Bouzid<br>Gabès<br>Médenine<br>Tataouine<br>Gafsa<br>Tozeur<br>Kébili | — |
| Delegation | Texte | Non | — | — |
| Usual mill | Liste déroulante | Non | None (delivers to any mill)<br>moulin1hd<br>Moulin Ennour | — |

## Parcelles oléicoles

- **Écran :** `parcelles.html` — formulaire « New plot » (`parcelles--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Producer * | Liste déroulante | Oui | Sami Ben Amor<br>producteur1hd p1 | — |
| Plot name * | Texte | Oui | — | — |
| Area (ha) | Texte | Non | — | — |
| Location | Texte | Non | — | — |
| Planting year | Texte | Non | — | — |
| Certification | Texte | Non | — | — |
| Olive variety | Liste déroulante | Non | Chemlali<br>Chetoui<br>Oueslati<br>Zalmati<br>Arbequina<br>Picholine<br>Other | — |

## Récoltes

- **Écran :** `recoltes.html` — formulaire « New harvest » (`recoltes--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Producer * | Liste déroulante | Oui | Sami Ben Amor<br>producteur1hd p1 | — |
| Plot * | Liste déroulante | Oui | Henchir el Ain<br>parcelle n1 beja | — |
| Weighing slip no. | Texte | Non | — | BP-2026-... |
| Harvest date * | Date | Oui | — | — |
| Quantity (kg) * | Nombre | Oui | — | — |
| Harvesting method | Liste déroulante | Non | Hand picking<br>Comb<br>Net<br>Mechanical shaking<br>Mixed | — |
| Ripeness index | Liste déroulante | Non | Green (early)<br>Half-ripe<br>Veraison<br>Advanced ripeness | — |
| Remarks | Zone de texte | Non | — | — |
| Weighing slip (PDF or photo) | Fichier | Non | — | — |
| Attach the document | Fichier | Non | — | — |

## Moulins

- **Écran :** `moulins.html` — formulaire « New mill » (`moulins--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Mill name * | Texte | Oui | — | — |
| Governorate | Texte | Non | — | — |
| Phone | Texte | Non | — | — |
| Email | Texte | Non | — | — |
| Capacity (t/day) | Texte | Non | — | — |
| Certification | Texte | Non | — | — |
| Extraction type | Liste déroulante | Non | 2-phase centrifugation<br>3-phase centrifugation<br>Traditional press<br>Supercritical | — |
| Address | Texte | Non | — | — |

## Pressages

- **Écran :** `pressages.html` — formulaire « New pressing » (`pressages--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Harvest * | Liste déroulante | Oui | Select a harvest to press...<br>BP-2026-0502 · Sami Ben · Henchir el Ain · 02/10/2026 · 1 200 kg left / 1 200 kg<br>BP-2026-1 · producteur1hd · parcelle n1 beja · 30/09/2026 · 1 000 kg left / 1 000 kg | — |
| Pressing date * | Date | Oui | — | — |
| Mill * | Liste déroulante | Oui | moulin1hd<br>Moulin Ennour | — |
| Mill ticket no. | Texte | Non | — | TM-... |
| Olives in (kg) * | Nombre | Oui | — | — |
| Oil produced (L) * | Nombre | Oui | — | — |
| Temperature (°C) | Nombre | Non | — | — |
| Malaxing time (min) | Nombre | Non | — | — |
| Mill ticket (PDF or photo) | Fichier | Non | — | — |
| Attach the document | Fichier | Non | — | — |

## Laboratoires

- **Écran :** `laboratoires.html` — formulaire « New laboratory » (`laboratoires--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Name * | Texte | Oui | — | — |
| Phone | Texte | Non | — | — |
| Email | Texte | Non | — | — |
| Accreditation (e.g. ISO 17025) | Texte | Non | — | — |
| Address | Texte | Non | — | — |

## Conditionneurs

- **Écran :** `conditionneurs.html` — formulaire « New » (`conditionneurs--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Name * | Texte | Oui | — | — |
| Governorate | Texte | Non | — | — |
| Phone | Texte | Non | — | — |
| Email | Texte | Non | — | — |
| Capacity (L/day) | Texte | Non | — | — |
| Container types | Texte | Non | — | — |

## Opérations

- **Écran :** `operations.html` — formulaire « New operation » (`operations--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Source pressing * | Liste déroulante | Oui | Select a pressing...<br>Ticket TM-2026-0210 · Sami Ben · Moulin Ennour · 02/10/2026 · 10 L left / 570 L<br>Ticket TM-2026-1 · producteur1hd · moulin1hd · 30/09/2026 · 200 L left / 200 L | — |
| Packer * | Liste déroulante | Oui | conditionneur1hd<br>El Amel Conditionnement | — |
| Lot number * | Texte | Oui | — | LOT-OL-2025-... |
| Container type * | Liste déroulante | Oui | Glass bottle 0.5L<br>Glass bottle 0.75L<br>Glass bottle 1L<br>Plastic jerrycan 2L<br>Plastic jerrycan 5L<br>Tin 3L<br>Tin 5L<br>Demijohn 10L<br>Bulk 200L | — |
| Category on the label | Liste déroulante | Non | Extra virgin<br>Virgin<br>Ordinary virgin<br>Lampante (not edible) | — |
| Total quantity (L) * | Nombre | Oui | — | — |
| Container volume (L) | Nombre | Non | — | — |
| Number of units | Nombre | Non | — | — |
| Storage point (tank/warehouse) | Liste déroulante | Non | None / not monitored | — |
| Expiry date | Date | Non | — | — |
| Bottling sheet (PDF or photo) | Fichier | Non | — | — |
| Attach the document | Fichier | Non | — | — |

## Exportateurs

- **Écran :** `exportateurs.html` — formulaire « New exporter » (`exportateurs--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Company name * | Texte | Oui | — | — |
| Country | Texte | Non | — | — |
| Phone | Texte | Non | — | — |
| Email | Texte | Non | — | — |
| Tax ID | Texte | Non | — | — |
| Destination countries (comma-separated) | Texte | Non | — | — |

## Exports

- **Écran :** `exports.html` — formulaire « New export » (`exports--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Packed lot * | Liste déroulante | Oui | Select a lot... | — |
| Exporter * | Liste déroulante | Oui | export1hd<br>El Amel export | — |
| Destination country * | Texte | Oui | — | — |
| Quantity (L) * | Nombre | Oui | — | — |
| Number of units | Nombre | Non | — | — |
| Customs declaration no. | Texte | Non | — | — |
| Invoice no. | Texte | Non | — | — |
| Certificate of origin no. (EUR.1) | Texte | Non | — | — |
| Carrier | Texte | Non | — | — |
| Port of loading | Liste déroulante | Non | Port of Sfax<br>Port of Tunis-La Goulette<br>Port of Bizerte<br>Port of Sousse<br>Port of Gabès | — |
| Customs declaration (PDF or photo) | Fichier | Non | — | — |
| Attach the document | Fichier | Non | — | — |

## Certifications

- **Écran :** `certifications.html` — formulaire « New certification » (`certifications--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Actor type * | Liste déroulante | Oui | Producer<br>Plot<br>Mill<br>Laboratory<br>Packer<br>Exporter | — |
| Certified actor * | Liste déroulante | Oui | Sami Ben Amor<br>producteur1hd p1 | — |
| Certification body * | Liste déroulante | Oui | Ecocert<br>Certif TN<br>SGS<br>Intertek<br>CCPB<br>IMC<br>CERES<br>Tüv Rheinland<br>AFNOR Certification<br>TUNAC (accreditation)<br>CTAA Tunisia<br>INNORPI<br>Other | — |
| Certification type * | Liste déroulante | Oui | Organic<br>EU organic farming<br>ISO/IEC 17025 (laboratory accreditation)<br>GlobalG.A.P<br>ISO 22000 Food safety<br>ISO 9001 Quality<br>HACCP<br>BRC Food<br>IFS Food<br>Demeter (biodynamic)<br>Fairtrade<br>Rainforest Alliance<br>Halal<br>Kosher<br>DOP / IGP / AOP<br>Other | — |
| Certificate no. | Texte | Non | — | — |
| Issue date | Date | Non | — | — |
| Expiry date | Date | Non | — | — |
| Status | Liste déroulante | Non | Valid<br>Being obtained<br>Suspended<br>Expired | — |
| Certificate (PDF or photo) (PDF or photo) | Fichier | Non | — | — |
| Attach the document | Fichier | Non | — | — |
| Notes | Zone de texte | Non | — | — |

## Conformité IOC

- **Écran :** `conformite.html` — formulaire « Manual check » (`conformite--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Packed lot * | Liste déroulante | Oui | Select a lot...<br>OLV-2026-0001 · Sami Ben | — |
| Standard * | Liste déroulante | Oui | IOC Extra Virgin<br>CE 2568/91<br>Organic | — |
| Check date | Date | Non | — | — |
| Inspector | Texte | Non | — | Inspector's name |

## Dossiers export

- **Écran :** `dossiers.html` — formulaire « Manual file » (`dossiers--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Linked export | Liste déroulante | Non | Unlinked (independent file)<br>OLV-2026-0001 → France | — |
| File title * | Texte | Oui | — | E.g. Export France - Lot LOT-OL-2025-06-AB12 |
| Destination country * | Texte | Oui | — | France, Italy, USA... |
| Exporter | Texte | Non | — | — |

## Points IoT / température

- **Écran :** `iot.html` — formulaire « New point » (`iot--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Name (must match the room name in TNEnergy exactly) * | Texte | Oui | — | — |
| Point type | Liste déroulante | Non | Mill (reception/pressing)<br>Oil storage before packing<br>Warehouse / before export | — |
| Linked entity * | Liste déroulante | Oui | moulin1hd<br>Moulin Ennour | — |
| Min threshold (°C) | Nombre | Non | — | — |
| Max threshold (°C) | Nombre | Non | — | — |

## ISO 22000 — Procédures

- **Écran :** `iso22000.html` — formulaire « Procedures » (`iso22000--procedure.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Code * | Texte | Oui | — | PRC-001 |
| Version | Texte | Non | — | — |
| Title * | Texte | Oui | — | — |
| Type | Liste déroulante | Non | Quality procedure<br>HACCP procedure<br>Work instruction<br>Operating method<br>Inspection procedure<br>Cleaning procedure<br>Traceability procedure<br>Recall procedure | — |
| Owner | Texte | Non | — | — |
| Creation date | Date | Non | — | — |
| Revision date | Date | Non | — | — |
| Description | Zone de texte | Non | — | — |

## ISO 22000 — HACCP

- **Écran :** `iso22000.html` — formulaire « HACCP » (`iso22000--haccp.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Process step * | Texte | Oui | — | E.g. Olive reception |
| Hazard type * | Liste déroulante | Oui | biologique<br>chimique<br>physique<br>allergen<br>radiologique | — |
| Hazard description * | Texte | Oui | — | — |
| Severity | Liste déroulante | Non | low<br>medium<br>high<br>critique | — |
| Critical Control Point (CCP) | Texte | Non | — | — |
| Cause | Texte | Non | — | — |
| Control measure | Texte | Non | — | — |
| Critical limit | Texte | Non | — | — |
| Monitoring frequency | Texte | Non | — | — |
| Corrective action | Texte | Non | — | — |

## ISO 22000 — Audits internes

- **Écran :** `iso22000.html` — formulaire « Internal audits » (`iso22000--audit.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Title * | Texte | Oui | — | — |
| Audit type | Liste déroulante | Non | ISO 22000 system audit<br>HACCP audit<br>BRC/IFS audit<br>Supplier audit<br>Hygiene audit<br>Traceability audit | — |
| Auditor | Texte | Non | — | — |
| Planned date | Date | Non | — | — |
| Completed date | Date | Non | — | — |
| Deviations found | Nombre | Non | — | — |
| Status | Liste déroulante | Non | planned<br>in progress<br>completed<br>cancelled | — |
| Findings | Zone de texte | Non | — | — |
| Conclusions | Zone de texte | Non | — | — |

## ISO 22000 — Actions correctives

- **Écran :** `iso22000.html` — formulaire « Corrective actions » (`iso22000--capa.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Reference * | Texte | Oui | — | CAPA-2025-001 |
| Source | Liste déroulante | Non | Internal audit<br>External audit<br>Customer complaint<br>Analysis non-conformity<br>HACCP deviation<br>Withdrawal/Recall<br>Management review | — |
| Problem description * | Zone de texte | Oui | — | — |
| Root cause | Texte | Non | — | — |
| Immediate action | Texte | Non | — | — |
| Corrective action | Texte | Non | — | — |
| Preventive action | Texte | Non | — | — |
| Owner | Texte | Non | — | — |
| Deadline | Date | Non | — | — |
| Status | Liste déroulante | Non | open<br>in progress<br>closed<br>abandoned | — |

## Documents

- **Écran :** `documents.html` — formulaire « New document » (`documents--form.html`)

| Champ | Type | Obligatoire | Options / valeurs | Exemple / aide |
|-------|------|-------------|-------------------|---------------|
| Title * | Texte | Oui | — | — |
| Document type | Liste déroulante | Non | Certificate of origin<br>IOC analysis<br>Phytosanitary<br>Customs declaration<br>Delivery note<br>Product data sheet<br>Organic certificate<br>Other | — |
| Linked entity | Texte | Non | — | e.g. lot, producer, export... |
| Content / Notes | Zone de texte | Non | — | — |
