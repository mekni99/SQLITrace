#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_vitrine.py — Génère showcase/olivetrace/vitrine-data.js

Données publiques des lots (vitrine consommateur), empreintes SHA-256
chaînées (recalculables dans le navigateur) et QR codes SVG (GS1 Digital Link).

Usage : python scripts/gen_vitrine.py   (nécessite `pip install segno`)
"""

import hashlib
import io
import json
from pathlib import Path

import segno

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "showcase" / "olivetrace" / "vitrine-data.js"

GTIN = "06191234000017"


def canon(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


LOTS = [
    {
        "id": "OLV-2026-0001",
        "name": "Henchir el Ain",
        "subtitle": "Chemlali biologique · Récolte précoce",
        "category": "Extra vierge",
        "bio": True,
        "format": "Bouteille verre 0,5 L",
        "volume": "0,5 L",
        "price": 29,
        "color": "#4d7c0f",
        "region": "Nabeul",
        "variety": "Chemlali",
        "serial": "000427",
        "bottles": 1120,
        "tasting": {"fruite": 7, "amertume": 4, "piquant": 5},
        "notes": "Amande verte, artichaut et herbe fraîchement coupée ; finale poivrée tout en douceur.",
        "pairings": ["Burrata & tomates anciennes", "Poisson grillé", "Salade méchouia"],
        "producer": {"name": "Sami Ben Amor", "since": 1998, "initials": "SB",
                     "quote": "Nos oliviers ont plus de soixante ans. On récolte tôt, à la main, pour garder le fruité."},
        "carbon": {"total": 412, "per_bottle": 0.37,
                   "split": {"Verger": 38, "Trituration": 17, "Emballage": 21, "Transport": 24}},
        "certs": [["Agriculture biologique", "Ecocert · TN-BIO-2026-0457"],
                  ["ISO 22000", "Moulin Ennour · Bureau Veritas"],
                  ["ISO/IEC 17025", "Olea Analyses Sfax · TUNAC"],
                  ["HACCP", "El Amel Conditionnement · SGS"]],
        "anchor": {"block": 37, "btc": 972670, "date": "23/10/2026"},
        "scans": {"count": 3, "last": "Lyon, France", "status": "normal"},
        "steps": [
            {"k": "parcelle", "title": "Parcelle", "date": "Campagne 2026", "place": "Henchir el Ain · Nabeul",
             "data": {"Producteur": "Sami Ben Amor", "Surface": "8 ha", "Variété": "Chemlali", "Certification": "Biologique (Ecocert)", "GPS": "36.45° N · 10.73° E"}},
            {"k": "recolte", "title": "Récolte", "date": "01/10/2026", "place": "Henchir el Ain",
             "data": {"Quantité": "3 000 kg", "Méthode": "Mixte (main + peigne)", "Maturité": "Mi-mûre", "Délai avant trituration": "< 24 h"}},
            {"k": "trituration", "title": "Trituration", "date": "02/10/2026", "place": "Moulin Ennour · Sfax",
             "data": {"Procédé": "Centrifugation 2 phases", "Entrée": "3 000 kg d'olives", "Huile obtenue": "570 L", "Rendement": "19 %", "Malaxage": "27 °C · 35 min"}},
            {"k": "analyse", "title": "Analyse laboratoire", "date": "02/10/2026", "place": "Olea Analyses Sfax (ISO 17025)",
             "data": {"Catégorie": "Extra vierge", "Acidité libre": 0.38, "Indice de peroxyde": 9.5, "K232": 1.92, "K270": 0.16, "Acide oléique": 61.5}},
            {"k": "conditionnement", "title": "Conditionnement", "date": "03/10/2026", "place": "El Amel Conditionnement",
             "data": {"Contenant": "Bouteille verre 0,5 L", "Quantité": "560 L · 1 120 bouteilles", "DDM": "30/04/2028", "QR": "GS1 Digital Link unique"}},
            {"k": "export", "title": "Export", "date": "04/10/2026", "place": "Port de Sfax → France",
             "data": {"Exportateur": "El Amel Export", "Destination": "France", "Déclaration": "DE-2026-9105", "Statut": "En transit"}},
        ],
    },
    {
        "id": "OLV-2026-0002",
        "name": "Ferme El Wafa",
        "subtitle": "Chetoui biologique · Cueillette manuelle",
        "category": "Vierge",
        "bio": True,
        "format": "Bouteille verre 0,75 L",
        "volume": "0,75 L",
        "price": 34,
        "color": "#166534",
        "region": "Sfax",
        "variety": "Chetoui",
        "serial": "000812",
        "bottles": 1600,
        "tasting": {"fruite": 8, "amertume": 7, "piquant": 7},
        "notes": "Fruité intense, feuille de tomate et poivre noir ; amertume franche typique du Chetoui.",
        "pairings": ["Couscous au poisson", "Légumes rôtis", "Pain tabouna"],
        "producer": {"name": "Mohamed Trabelsi", "since": 2004, "initials": "MT",
                     "quote": "Le Chetoui a du caractère. On le cueille à la main pour respecter le fruit."},
        "carbon": {"total": 688, "per_bottle": 0.43,
                   "split": {"Verger": 34, "Trituration": 19, "Emballage": 22, "Transport": 25}},
        "certs": [["Agriculture biologique", "Ecocert · TN-BIO-2026-0512"],
                  ["ISO/IEC 17025", "ONAGRI Tunis"],
                  ["HACCP", "Société Méditerranée Emballage"]],
        "anchor": {"block": 32, "btc": 972668, "date": "22/10/2026"},
        "scans": {"count": 1, "last": "Milan, Italie", "status": "normal"},
        "steps": [
            {"k": "parcelle", "title": "Parcelle", "date": "Campagne 2026", "place": "Ferme El Wafa · Sfax",
             "data": {"Producteur": "Mohamed Trabelsi", "Surface": "12,5 ha", "Variété": "Chetoui", "Certification": "Biologique (Ecocert)", "GPS": "34.74° N · 10.76° E"}},
            {"k": "recolte", "title": "Récolte", "date": "15/10/2026", "place": "Ferme El Wafa",
             "data": {"Quantité": "2 400 kg", "Méthode": "Cueillette manuelle", "Maturité": "Mûre", "Délai avant trituration": "< 12 h"}},
            {"k": "trituration", "title": "Trituration", "date": "15/10/2026", "place": "Moulin El Baraka · Sfax",
             "data": {"Procédé": "Centrifugation 3 phases", "Entrée": "2 400 kg d'olives", "Huile obtenue": "480 L", "Rendement": "20 %", "Malaxage": "26 °C · 40 min"}},
            {"k": "analyse", "title": "Analyse laboratoire", "date": "18/10/2026", "place": "ONAGRI Tunis",
             "data": {"Catégorie": "Vierge", "Acidité libre": 0.32, "Indice de peroxyde": 8.2, "K232": 1.78, "K270": 0.142, "Acide oléique": 63.2}},
            {"k": "conditionnement", "title": "Conditionnement", "date": "19/10/2026", "place": "Société Méditerranée Emballage",
             "data": {"Contenant": "Bouteille verre 0,75 L", "Quantité": "1 200 L · 1 600 bouteilles", "DDM": "30/04/2028", "QR": "GS1 Digital Link unique"}},
            {"k": "export", "title": "Export", "date": "16/10/2026", "place": "Port de Sfax → Italie",
             "data": {"Exportateur": "Méditerranée Trading", "Destination": "Italie", "Déclaration": "DE-2026-9211", "Statut": "Expédié"}},
        ],
    },
    {
        "id": "OLV-2026-0003",
        "name": "Les Oliviers du Nord",
        "subtitle": "Oueslati biologique · Format famille",
        "category": "Vierge",
        "bio": True,
        "format": "Bidon métal 5 L",
        "volume": "5 L",
        "price": 125,
        "color": "#a16207",
        "region": "Béja",
        "variety": "Oueslati",
        "serial": "000064",
        "bottles": 144,
        "tasting": {"fruite": 6, "amertume": 5, "piquant": 6},
        "notes": "Fruité mûr, notes de pomme et d'amande sèche ; un équilibre rond pour la cuisine de tous les jours.",
        "pairings": ["Cuisson douce", "Tajine", "Pâtisseries à l'huile"],
        "producer": {"name": "Ali Ben Salah", "since": 1987, "initials": "AB",
                     "quote": "Dans le Nord, l'Oueslati pousse lentement. C'est ce qui lui donne sa rondeur."},
        "carbon": {"total": 356, "per_bottle": 2.47,
                   "split": {"Verger": 41, "Trituration": 16, "Emballage": 15, "Transport": 28}},
        "certs": [["Agriculture biologique", "Ecocert · TN-BIO-2026-0388"],
                  ["ISO/IEC 17025", "SGS Tunisia Lab"],
                  ["HACCP", "Huile Prestige Packing"]],
        "anchor": {"block": 27, "btc": 972668, "date": "22/10/2026"},
        "scans": {"count": 2, "last": "Marseille, France", "status": "normal"},
        "steps": [
            {"k": "parcelle", "title": "Parcelle", "date": "Campagne 2026", "place": "Les Oliviers du Nord · Béja",
             "data": {"Producteur": "Ali Ben Salah", "Surface": "15 ha", "Variété": "Oueslati", "Certification": "Biologique (Ecocert)", "GPS": "36.72° N · 9.18° E"}},
            {"k": "recolte", "title": "Récolte", "date": "08/10/2026", "place": "Les Oliviers du Nord",
             "data": {"Quantité": "3 200 kg", "Méthode": "Mécanique (vibreur)", "Maturité": "Mûre", "Délai avant trituration": "< 24 h"}},
            {"k": "trituration", "title": "Trituration", "date": "08/10/2026", "place": "Moulin Errim · Béja",
             "data": {"Procédé": "Pression traditionnelle", "Entrée": "3 200 kg d'olives", "Huile obtenue": "610 L", "Rendement": "19,06 %", "Malaxage": "28 °C · 45 min"}},
            {"k": "analyse", "title": "Analyse laboratoire", "date": "09/10/2026", "place": "SGS Tunisia Lab",
             "data": {"Catégorie": "Vierge", "Acidité libre": 0.89, "Indice de peroxyde": 14.5, "K232": 2.54, "K270": 0.218, "Acide oléique": 57.4}},
            {"k": "conditionnement", "title": "Conditionnement", "date": "12/10/2026", "place": "Huile Prestige Packing",
             "data": {"Contenant": "Bidon métal 5 L", "Quantité": "720 L · 144 bidons", "DDM": "31/05/2028", "QR": "GS1 Digital Link unique"}},
            {"k": "export", "title": "Export", "date": "20/10/2026", "place": "Port de Radès → France",
             "data": {"Exportateur": "Atlas Olive Export", "Destination": "France", "Déclaration": "DE-2026-9345", "Statut": "En transit"}},
        ],
    },
    {
        "id": "OLV-2026-0004",
        "name": "Dar Essalem",
        "subtitle": "Chemlali de Kairouan · Cuvée de table",
        "category": "Extra vierge",
        "bio": False,
        "format": "Bouteille verre 1 L",
        "volume": "1 L",
        "price": 38,
        "color": "#365314",
        "region": "Kairouan",
        "variety": "Chemlali",
        "serial": "000215",
        "bottles": 600,
        "tasting": {"fruite": 6, "amertume": 3, "piquant": 4},
        "notes": "Fruité vert léger, notes d'amande douce et de banane verte ; tout en finesse.",
        "pairings": ["Assaisonnement", "Houmous", "Petit-déjeuner tunisien"],
        "producer": {"name": "Fatma Gharbi", "since": 2011, "initials": "FG",
                     "quote": "J'ai repris le verger de mon père. Chaque bouteille porte notre nom et notre histoire."},
        "carbon": {"total": 268, "per_bottle": 0.45,
                   "split": {"Verger": 44, "Trituration": 18, "Emballage": 24, "Transport": 14}},
        "certs": [["ISO 22000", "Moulin Ennour · Bureau Veritas"],
                  ["ISO/IEC 17025", "Olea Analyses Sfax · TUNAC"],
                  ["HACCP", "El Amel Conditionnement · SGS"]],
        "anchor": {"block": 41, "btc": 972701, "date": "24/10/2026"},
        "scans": {"count": 14, "last": "Tunis · Sfax · Paris · Montréal", "status": "suspect"},
        "steps": [
            {"k": "parcelle", "title": "Parcelle", "date": "Campagne 2026", "place": "Dar Essalem · Kairouan",
             "data": {"Producteur": "Fatma Gharbi", "Surface": "6 ha", "Variété": "Chemlali", "Certification": "Conventionnelle", "GPS": "35.68° N · 10.10° E"}},
            {"k": "recolte", "title": "Récolte", "date": "12/10/2026", "place": "Dar Essalem",
             "data": {"Quantité": "1 800 kg", "Méthode": "Mixte (main + peigne)", "Maturité": "Mi-mûre", "Délai avant trituration": "< 24 h"}},
            {"k": "trituration", "title": "Trituration", "date": "12/10/2026", "place": "Moulin Ennour · Sfax",
             "data": {"Procédé": "Centrifugation 2 phases", "Entrée": "1 800 kg d'olives", "Huile obtenue": "360 L", "Rendement": "20 %", "Malaxage": "27 °C · 30 min"}},
            {"k": "analyse", "title": "Analyse laboratoire", "date": "13/10/2026", "place": "Olea Analyses Sfax (ISO 17025)",
             "data": {"Catégorie": "Extra vierge", "Acidité libre": 0.42, "Indice de peroxyde": 10.1, "K232": 1.98, "K270": 0.17, "Acide oléique": 62.1}},
            {"k": "conditionnement", "title": "Conditionnement", "date": "14/10/2026", "place": "El Amel Conditionnement",
             "data": {"Contenant": "Bouteille verre 1 L", "Quantité": "600 L · 600 bouteilles", "DDM": "30/06/2028", "QR": "GS1 Digital Link unique"}},
            {"k": "export", "title": "Distribution", "date": "16/10/2026", "place": "Marché local · Tunisie",
             "data": {"Distributeur": "El Amel Distribution", "Destination": "Tunisie", "Points de vente": "Tunis · Sousse · Sfax", "Statut": "En rayon"}},
        ],
    },
]


def qr_svg(data: str) -> str:
    q = segno.make(data, error="m")
    buf = io.BytesIO()
    q.save(buf, kind="svg", scale=1, border=0, dark="#0f1f14", light=None,
           xmldecl=False, svgns=True, nl=False, omitsize=True)
    return buf.getvalue().decode("utf-8")


def main() -> None:
    for lot in LOTS:
        prev = "0" * 64
        for st in lot["steps"]:
            st["prev"] = prev
            st["hash"] = sha(prev + canon({"k": st["k"], "date": st["date"], "place": st["place"], "data": st["data"]}))
            prev = st["hash"]
        lot["seal"] = sha(prev + lot["id"])
        lot["url"] = f"https://olivetrace.tntrace.tn/01/{GTIN}/10/{lot['id']}/21/{lot['serial']}"
        lot["qr"] = qr_svg(lot["url"])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        "// Généré par scripts/gen_vitrine.py — ne pas modifier à la main.\n"
        "window.OLIVE_LOTS = " + json.dumps(LOTS, ensure_ascii=False, indent=1) + ";\n",
        encoding="utf-8",
    )
    print(f"OK {OUT} ({len(LOTS)} lots)")


if __name__ == "__main__":
    main()
