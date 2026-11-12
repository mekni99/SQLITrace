#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — Clone statique multi-produits des dashboards TNtrace.

Usage :
    python scripts/build.py

Entrées :
    pages/home/index.html           Export SingleFile de https://tntrace.tn/ (hub)
    pages/<produit>/*.html          Exports SingleFile d'un produit
                                    (pages/datetrace/, pages/olivetrace/…)
    pages/<produit>/<route>--<variante>.html
                                    Variante d'écran (modale ouverte, vue détail)

Sorties :
    output/index.html               Page d'accueil hub
    output/<produit>/*.html         Pages du produit (liens réécrits en local)
    output/<produit>/404-local.html Page d'attente (chrome du produit)
    output/404-local.html           Page d'attente globale (produit non capturé)
    output/manifest.json            Inventaire produits/routes

Config :
    scripts/data_map.<produit>.json Remplacements littéraux par produit
                                    (données fictives).
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "pages"
OUT_DIR = ROOT / "output"
SCRIPTS_DIR = Path(__file__).resolve().parent

NOT_FOUND_PAGE = "404-local.html"

# Sous-domaine TNtrace -> nom du dossier produit local
KNOWN_PRODUCTS = {
    "date": "datetrace",
    "olivetrace": "olivetrace",
    "aquatrace": "aquatrace",
    "machine": "machine",
    "conservetrace": "conservetrace",
    "berrytrace": "berrytrace",
    "milktrace": "milktrace",
    "medtrace": "medtrace",
    "waterjuicetrace": "waterjuicetrace",
    "energy": "energy",
    "tnsupply": "tnsupply",
    "tnfleet": "tnfleet",
    "tnfret": "tnfret",
}

# --------------------------------------------------------------------------
# Routeur de boutons par produit (nav.js)
#   page -> [ (sous-chaîne OU regex 're:…', cible) ]  premier match gagnant
# --------------------------------------------------------------------------

BTN_ROUTES = {
    "datetrace": {
        "index.html": [
            ("Voir tout", "lots.html"),
            ("Lots ", "lots.html"),
            ("Producteurs", "producteurs.html"),
            ("IoT", "iot.html"),
            ("Certifications", "certifications.html"),
            ("Blockchain", "blockchain.html"),
            ("IA Pesticides", "ia.html"),
            ("QR & Traçabilité", "qr-trace.html"),
            ("Assistant IA", "assistant.html"),
        ],
        "lots.html": [
            ("Nouveau Lot", "lots--form.html"),
            ("re:DT-", "lots--selected.html"),
        ],
        "producteurs.html": [("Ajouter Producteur", "producteurs--form.html")],
        "users.html": [("Nouvel utilisateur", "users--form.html")],
        "etapes.html": [("re:DT-\\d", "etapes--selected.html")],
        "etapes--selected.html": [
            ("Ajouter Étape", "etapes--form.html"),
            ("re:DT-\\d", "etapes--selected.html"),
        ],
        "qr-trace.html": [("re:DT-\\d", "qr-trace--selected.html")],
        "qr-trace--selected.html": [("re:DT-\\d", "qr-trace--selected.html")],
        "ia.html": [("Nouvelle Analyse IA", "ia--form.html")],
        "iot.html": [
            ("Nouveau lieu", "iot--form.html"),
            ("Créer un lieu", "iot--form.html"),
        ],
        "certifications.html": [
            ("Nouvelle Certification", "certifications--form.html"),
            ("Ajouter une certification", "certifications--form.html"),
        ],
        "audits.html": [
            ("Nouvel Audit", "audits--form.html"),
            ("Planifier un audit", "audits--form.html"),
        ],
        "capa.html": [
            ("Nouvelle Action", "capa--form.html"),
            ("Créer une action", "capa--form.html"),
        ],
        "evaluations-fournisseurs.html": [
            ("Nouvelle Évaluation", "evaluations-fournisseurs--form.html"),
            ("Évaluer un producteur", "evaluations-fournisseurs--form.html"),
        ],
        "chaine-froid.html": [("Nouveau segment", "chaine-froid--form.html")],
    },
    "olivetrace": {
        "producteurs.html": [("New producer", "producteurs--form.html")],
        "parcelles.html": [("New plot", "parcelles--form.html")],
        "recoltes.html": [("New harvest", "recoltes--form.html")],
        "moulins.html": [("New mill", "moulins--form.html")],
        "pressages.html": [("New pressing", "pressages--form.html")],
        "laboratoires.html": [("New laboratory", "laboratoires--form.html")],
        "analyses.html": [("New analysis", "analyses--form.html")],
        "conditionneurs.html": [("New", "conditionneurs--form.html")],
        "operations.html": [("New operation", "operations--form.html")],
        "exportateurs.html": [("New exporter", "exportateurs--form.html")],
        "exports.html": [("New export", "exports--form.html")],
        "certifications.html": [("New certification", "certifications--form.html")],
        "conformite.html": [("Manual check", "conformite--form.html")],
        "dossiers.html": [("Manual file", "dossiers--form.html")],
        "iot.html": [("New point", "iot--form.html")],
        "documents.html": [
            ("New document", "documents--form.html"),
            ("Sample documents", "documents--samples.html"),
        ],
        "documents--samples.html": [("Company documents", "documents.html")],
        "utilisateurs.html": [("New user", "404-local.html#new-user")],
        # Onglets ISO 22000 (mêmes sur la page et ses 4 variantes)
        "iso22000.html": [
            ("Procedures", "iso22000--procedure.html"),
            ("HACCP", "iso22000--haccp.html"),
            ("Internal audits", "iso22000--audit.html"),
            ("Corrective actions", "iso22000--capa.html"),
        ],
        "iso22000--procedure.html": [
            ("Procedures", "iso22000--procedure.html"),
            ("HACCP", "iso22000--haccp.html"),
            ("Internal audits", "iso22000--audit.html"),
            ("Corrective actions", "iso22000--capa.html"),
        ],
        "iso22000--haccp.html": [
            ("Procedures", "iso22000--procedure.html"),
            ("HACCP", "iso22000--haccp.html"),
            ("Internal audits", "iso22000--audit.html"),
            ("Corrective actions", "iso22000--capa.html"),
        ],
        "iso22000--audit.html": [
            ("Procedures", "iso22000--procedure.html"),
            ("HACCP", "iso22000--haccp.html"),
            ("Internal audits", "iso22000--audit.html"),
            ("Corrective actions", "iso22000--capa.html"),
        ],
        "iso22000--capa.html": [
            ("Procedures", "iso22000--procedure.html"),
            ("HACCP", "iso22000--haccp.html"),
            ("Internal audits", "iso22000--audit.html"),
            ("Corrective actions", "iso22000--capa.html"),
        ],
    },
    "aquatrace": {
        "lots.html": [("Nouveau lot", "lots--form.html")],
        "farms.html": [("Nouvelle ferme", "farms--form.html")],
        "basins.html": [("Nouveau bassin", "basins--form.html")],
        "feeding.html": [("Nouvelle ration", "feeding--form.html")],
        "harvest.html": [("Enregistrer récolte", "harvest--form.html")],
        "health.html": [("Nouvel événement", "health--form.html")],
        "nonconformites.html": [("Signaler", "nonconformites--form.html")],
        "rappels.html": [("Nouveau rappel", "rappels--form.html")],
        "sales.html": [("Nouvelle vente", "sales--form.html")],
        "sensors.html": [("Nouveau capteur", "sensors--form.html")],
        "distributions.html": [("Nouvelle distribution", "distributions--form.html")],
        "utilisateurs.html": [("Nouvel utilisateur", "utilisateurs--form.html")],
    },
    "medtrace": {
        "lots.html": [
            ("Nouveau lot", "lots--form.html"),
            ("icon:eye", "lots--selected.html"),
        ],
        "medicaments.html": [("Nouveau médicament", "medicaments--form.html")],
        "unites.html": [],
        "distributions.html": [("Nouvelle distribution", "distributions--form.html")],
        "pharmacies.html": [("Nouvelle pharmacie", "pharmacies--form.html")],
        "laboratoires.html": [("Nouveau laboratoire", "laboratoires--form.html")],
        "hopitaux.html": [("Nouvel établissement", "hopitaux--form.html")],
        "inspections.html": [("Nouvelle inspection", "inspections--form.html")],
        "stupefiants.html": [("Nouvelle dispensation", "stupefiants--form.html")],
        "temperature.html": [("Ajouter mesure", "temperature--form.html")],
        "utilisateurs.html": [("Nouvel utilisateur", "utilisateurs--form.html")],
    },
    "machine": {
        "machines.html": [("re:▸", "machines--selected.html")],
        "machines--selected.html": [("re:▸", "machines--selected.html")],
        "maintenance.html": [("Créer l'OT", "maintenance--form.html")],
    },
}

# Normalisation des routes par produit
#   ROUTE_STRIP : préfixe retiré de la route ('/app/producteurs' -> '/producteurs')
#   ROUTE_INDEX : route servie comme index.html du produit
ROUTE_STRIP = {"olivetrace": "/app", "aquatrace": "/app", "medtrace": "/app"}
ROUTE_INDEX = {
    "olivetrace": {"/dashboard": "index.html"},
    "aquatrace": {"/dashboard": "index.html"},
    "medtrace": {"/dashboard": "index.html"},
}

# Page de repli des variantes (dérivée automatiquement sinon : x--v -> x.html)
VARIANT_BASE_OVERRIDES = {
    "datetrace": {"etapes--form.html": "etapes--selected.html"},
}

# Menu « Plus » absent du DOM capturé (dropdown React rendu à l'ouverture) :
# rebuild local des items [libellé, fichier] injecté dans nav.js.
PLUS_MENU = {
    "machine": [
        ("🏭 Structure", "structure.html"),
        ("📡 Boîtiers", "boitiers.html"),
        ("👷 Opérateurs", "operateurs.html"),
        ("📚 Historique", "historique.html"),
        ("🔖 Traçabilité", "tracabilite.html"),
        ("📱 QR Codes", "qrcodes.html"),
        ("🔗 Intégration", "integration.html"),
        ("🎛️ Simulateur", "simulateur.html"),
        ("⚙️ Paramètres", "parametres.html"),
    ],
}

NAV_JS_TEMPLATE = """// nav.js — navigation locale du clone statique (aucun accès réseau).
// Généré par scripts/build.py — modifier la config dans build.py, pas ici.
(function () {
  "use strict";

  var PAGE = location.pathname.split("/").pop() || "index.html";
  var ROUTES = __ROUTES__;
  var VARIANT_BASE = __VARIANT_BASE__;
  var PLUS_MENU = __PLUS_MENU__;

  function norm(s) {
    return (s || "").replace(/\\s+/g, " ").trim();
  }

  function closeModal() {
    if (document.referrer &&
        document.referrer.indexOf(location.origin) === 0) {
      history.back();
    } else {
      location.href = VARIANT_BASE[PAGE] || "index.html";
    }
  }

  var CLOSE_RE =
    /annuler|cancel|fermer|close|discard|enregistrer|save|créer|creer|create|planifier|schedule|lancer|confirmer|confirm|valider|validate|soumettre|submit|✅/i;

  // Menu « Plus » : absent du DOM capturé -> rebuild local
  var plusOpen = null;
  function togglePlus(btn) {
    var host = btn.parentElement;
    var menu = host && host.querySelector(".plus-menu-local");
    if (menu) { menu.remove(); plusOpen = null; return; }
    if (plusOpen) { plusOpen.remove(); plusOpen = null; }
    var div = document.createElement("div");
    div.className = "plus-menu-local";
    div.setAttribute(
      "style",
      "position:absolute;right:0;top:100%;margin-top:8px;width:200px;" +
      "background:#fff;border-radius:12px;box-shadow:0 10px 25px rgba(0,0,0,.18);" +
      "border:1px solid #e2e8f0;padding:6px 0;z-index:9999;"
    );
    PLUS_MENU.forEach(function (it) {
      var a = document.createElement("a");
      a.href = it[1];
      a.textContent = it[0];
      a.setAttribute(
        "style",
        "display:block;padding:8px 16px;font-size:14px;color:#1e293b;text-decoration:none;"
      );
      a.onmouseenter = function () { this.style.background = "#f1f5f9"; };
      a.onmouseleave = function () { this.style.background = ""; };
      div.appendChild(a);
    });
    host.style.position = "relative";
    host.appendChild(div);
    plusOpen = div;
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest("button, [role=button], .cursor-pointer, a");
    if (!btn) {
      if (plusOpen) { plusOpen.remove(); plusOpen = null; }
      return;
    }
    var label = norm(btn.textContent);

    // Menu « Plus » du clone
    if (PLUS_MENU.length && /plus|⋯|\.\.\./i.test(label) &&
        !btn.closest(".plus-menu-local")) {
      e.preventDefault();
      togglePlus(btn);
      return;
    }
    if (plusOpen && !btn.closest(".plus-menu-local")) {
      plusOpen.remove(); plusOpen = null;
    }

    var inModal = !!btn.closest("div.fixed.inset-0");
    var isVariant = PAGE.indexOf("--") !== -1;

    if (inModal) {
      // Dans une vraie modale overlay : X/vide ou bouton de clôture -> retour
      if (!label || CLOSE_RE.test(label)) {
        e.preventDefault();
        closeModal();
      }
      return;
    }
    // Sur une page variante (formulaire inline, carte détail) : boutons de
    // clôture, « Retour… » ou flèche ← -> retour ; les autres passent par les règles.
    if (isVariant && (btn.querySelector("svg.lucide-arrow-left") ||
        (label && (/retour|back|←/i.test(label) || CLOSE_RE.test(label))))) {
      e.preventDefault();
      closeModal();
      return;
    }

    var rules = ROUTES[PAGE] || [];
    for (var i = 0; i < rules.length; i++) {
      var pat = rules[i][0], target = rules[i][1];
      var match;
      if (pat.indexOf("icon:") === 0) {
        // Bouton sans texte identifiable par icône lucide (ex. icon:eye)
        match = !!btn.querySelector("svg.lucide-" + pat.slice(5));
      } else {
        match =
          pat.indexOf("re:") === 0
            ? new RegExp(pat.slice(3), "i").test(label)
            : label.toLowerCase().indexOf(pat.toLowerCase()) !== -1;
      }
      if (match) {
        e.preventDefault();
        location.href = target;
        return;
      }
    }

    if (/^actualiser$/i.test(label)) {
      e.preventDefault();
      location.reload();
    }
  });

  // Bouton flottant « ← Hub TNtrace » dans chaque produit + « Déconnexion » -> hub
  (function injectHubBtn() {
    var a = document.createElement("a");
    a.href = "../index.html";
    a.className = "tntrace-hub-back";
    a.innerHTML = "&#8592; Hub TNtrace";
    a.setAttribute(
      "style",
      "position:fixed;bottom:16px;right:16px;z-index:9998;" +
      "display:inline-flex;align-items:center;gap:6px;" +
      "padding:8px 14px;border-radius:999px;" +
      "background:linear-gradient(135deg,#0f172a,#1e3a8a);color:#fff;" +
      "font:600 12.5px/1 Inter,system-ui,sans-serif;text-decoration:none;" +
      "box-shadow:0 8px 24px rgba(15,23,42,.28);border:1px solid rgba(255,255,255,.16);" +
      "transition:transform .15s,box-shadow .15s;"
    );
    a.onmouseenter = function () { this.style.transform = "translateY(-2px)"; };
    a.onmouseleave = function () { this.style.transform = ""; };
    document.body.appendChild(a);

    // Clic sur « Déconnexion / Logout » -> retour au hub
    document.addEventListener("click", function (ev) {
      var b = ev.target.closest("button, a");
      if (!b) return;
      var t = norm(b.textContent);
      if (/^(déconnexion|deconnexion|logout|log out|se déconnecter)$/i.test(t) ||
          b.querySelector("svg.lucide-log-out")) {
        ev.preventDefault();
        location.href = "../index.html";
      }
    });
  })();
})();
"""


# --------------------------------------------------------------------------
# Utilitaires exports SingleFile
# --------------------------------------------------------------------------

SF_URL_RE = re.compile(r"url:\s*(https?://\S+)")


def read_source_url(html: str) -> str | None:
    head = html[:4000]
    if "Page saved with SingleFile" not in head:
        return None
    m = SF_URL_RE.search(head)
    return m.group(1) if m else None


def route_of(url: str) -> str:
    path = re.sub(r"^https?://[^/]+", "", url).split("?")[0].split("#")[0]
    return "/" + path.strip("/") if path.strip("/") else "/"


def slug_for(route: str) -> str:
    return "index.html" if route == "/" else route.strip("/").replace("/", "-") + ".html"


# --------------------------------------------------------------------------
# Nettoyage
# --------------------------------------------------------------------------

SCRIPT_RE = re.compile(r"<script\b[^>]*>.*?</script\s*>", re.S | re.I)
SCRIPT_SELFCLOSED_RE = re.compile(r"<script\b[^>]*/\s*>", re.I)
EVENT_ATTR_RE = re.compile(r"\s+on[a-zA-Z]+\s*=\s*(\"[^\"]*\"|'[^']*'|[^\s>]+)")
META_REFRESH_RE = re.compile(r"<meta\b[^>]*http-equiv\s*=\s*[\"']?refresh[\"']?[^>]*>", re.I)


def clean_html(html: str) -> str:
    html = SCRIPT_RE.sub("", html)
    html = SCRIPT_SELFCLOSED_RE.sub("", html)
    html = META_REFRESH_RE.sub("", html)
    html = EVENT_ATTR_RE.sub("", html)
    return html


# --------------------------------------------------------------------------
# Réécriture des liens (pages produit)
# --------------------------------------------------------------------------

HREF_RE = re.compile(
    r"href\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))",
    re.I,
)


def make_rewriter(site_origin: str, route_map: dict[str, str], not_found: str,
                  strip_prefix: str = ""):
    def rewrite(m: re.Match) -> str:
        raw = m.group(1) or m.group(2) or m.group(3) or ""

        if raw.startswith(("#", "data:", "mailto:", "tel:")):
            return m.group(0)

        if raw.startswith(site_origin):
            path = re.sub(r"^https?://[^/]+", "", raw) or "/"
        elif raw.startswith("http://") or raw.startswith("https://") or raw.startswith("//"):
            return 'href="#" data-external="' + raw + '"'
        elif raw.startswith("/"):
            path = raw
        elif re.fullmatch(r"[A-Za-z0-9_-]+(--[A-Za-z0-9_-]+)?\.html(#[^\s]*)?", raw):
            return m.group(0)  # déjà un fichier local
        else:
            return 'href="#" data-external="' + raw + '"'

        frag = ""
        if "#" in path:
            path, frag = path.split("#", 1)
            frag = "#" + frag
        path = path.split("?")[0]
        route = "/" + path.strip("/") if path.strip("/") else "/"
        if strip_prefix and route.startswith(strip_prefix):
            route = route[len(strip_prefix):] or "/"

        target = route_map.get(route)
        if target:
            return 'href="' + target + frag + '"'
        missing = route.strip("/")
        return 'href="' + not_found + ("#" + missing if missing else "") + '"'

    return rewrite


def rewrite_links(html: str, site_origin: str, route_map: dict[str, str],
                  not_found: str, strip_prefix: str = "") -> str:
    return HREF_RE.sub(
        make_rewriter(site_origin, route_map, not_found, strip_prefix), html
    )


# --------------------------------------------------------------------------
# Réécriture des liens (page d'accueil hub)
# --------------------------------------------------------------------------

def rewrite_home_links(html: str, available: dict[str, str]) -> str:
    """available : dossier produit -> présent dans pages/ (ex. 'datetrace')."""

    def rewrite(m: re.Match) -> str:
        raw = m.group(1) or m.group(2) or m.group(3) or ""
        if raw.startswith(("#", "data:", "mailto:", "tel:")):
            return m.group(0)
        host = re.match(r"https?://([^/]+)", raw)
        if not host:
            return 'href="#" data-external="' + raw + '"'
        host = host.group(1)
        if host == "tntrace.tn":
            return 'href="index.html"'
        sub = host.split(".")[0]
        folder = KNOWN_PRODUCTS.get(sub)
        if not folder:
            return 'href="#" data-external="' + raw + '"'
        if folder in available:
            return f'href="{folder}/index.html"'
        return f'href="{NOT_FOUND_PAGE}#{folder}"'

    return HREF_RE.sub(rewrite, html)


# --------------------------------------------------------------------------
# Pages 404
# --------------------------------------------------------------------------

MAIN_RE = re.compile(r"<main\b.*?</main>", re.S)
TITLE_RE = re.compile(r"<title>.*?</title>", re.S)

NOT_FOUND_MAIN = """<main class="flex-1 overflow-auto">
<div class="min-h-full flex items-center justify-center p-8">
<div class="max-w-md w-full bg-white rounded-2xl shadow-lg border border-gray-100 p-8 text-center">
<div class="w-16 h-16 rounded-2xl bg-berry-100 flex items-center justify-center mx-auto mb-4 text-3xl">🌴</div>
<h1 class="text-xl font-bold text-gray-900 mb-2">Écran non capturé</h1>
<p class="text-sm text-gray-500 mb-1">La page <code id="nf-route" class="bg-gray-100 rounded px-1.5 py-0.5 text-berry-700 font-mono text-xs"></code> n'a pas été exportée.</p>
<p class="text-sm text-gray-400 mb-6">Exportez cet écran avec SingleFile puis relancez <code class="bg-gray-100 rounded px-1 py-0.5 font-mono text-xs">scripts/build.py</code>.</p>
<a href="index.html" class="inline-flex items-center gap-2 bg-berry-700 hover:bg-berry-800 text-white text-sm font-medium px-5 py-2.5 rounded-lg transition-colors">← Retour au Dashboard</a>
</div>
</div>
</main>
<script>
(function () {
    var el = document.getElementById("nf-route");
    if (el) el.textContent = "/" + location.hash.replace(/^#/, "").replace(/^[/]+/, "");
})();
</script>
"""

ROOT_404 = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TNtrace — Produit non capturé</title>
<style>
  body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
       font-family:ui-sans-serif,system-ui,sans-serif;background:#f9fafb;color:#111827}
  .card{max-width:28rem;background:#fff;border:1px solid #e5e7eb;border-radius:1rem;
        padding:2rem;text-align:center;box-shadow:0 10px 25px rgba(0,0,0,.08)}
  h1{font-size:1.25rem;margin:.75rem 0 .5rem}
  p{font-size:.875rem;color:#6b7280;margin:.25rem 0}
  code{background:#f3f4f6;border-radius:.25rem;padding:.15rem .4rem;font-size:.8rem}
  a.btn{display:inline-block;margin-top:1.25rem;background:#7c2d4e;color:#fff;
        font-size:.875rem;font-weight:500;padding:.6rem 1.25rem;border-radius:.5rem;
        text-decoration:none}
</style></head>
<body><div class="card">
  <div style="font-size:2rem">🧭</div>
  <h1>Produit non capturé</h1>
  <p>Le module <code id="nf-route"></code> n'a pas encore été exporté.</p>
  <p>Exportez ses écrans avec SingleFile dans <code>pages/&lt;produit&gt;/</code>
     puis relancez <code>scripts/build.py</code>.</p>
  <a class="btn" href="index.html">← Retour à l'accueil TNtrace</a>
</div>
<script>
(function () {
    var el = document.getElementById("nf-route");
    if (el) el.textContent = location.hash.replace(/^#/, "").replace(/^[/]+/, "") || "?";
})();
</script>
</body></html>
"""


def build_product_404(dashboard_html: str) -> str:
    html = TITLE_RE.sub("<title>Page non capturée</title>", dashboard_html, count=1)
    if MAIN_RE.search(html):
        return MAIN_RE.sub(NOT_FOUND_MAIN, html, count=1)
    return ROOT_404


# --------------------------------------------------------------------------
# Données fictives + nav.js
# --------------------------------------------------------------------------

def apply_data_map(html: str, mapping: dict[str, str]) -> str:
    for old, new in mapping.items():
        html = html.replace(old, new)
    return html


def load_data_map(product: str) -> dict[str, str]:
    f = SCRIPTS_DIR / f"data_map.{product}.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.is_file() else {}


def make_nav_js(product: str, variant_files: set[str]) -> str:
    routes = BTN_ROUTES.get(product, {})
    overrides = VARIANT_BASE_OVERRIDES.get(product, {})
    vbase = {}
    for vf in variant_files:
        base = re.sub(r"--[^.]+\.html$", ".html", vf)
        vbase[vf] = overrides.get(vf, base)
    return (
        NAV_JS_TEMPLATE.replace(
            "__ROUTES__", json.dumps(routes, ensure_ascii=False)
        )
        .replace("__VARIANT_BASE__", json.dumps(vbase, ensure_ascii=False))
        .replace("__PLUS_MENU__", json.dumps(PLUS_MENU.get(product, []), ensure_ascii=False))
    )


def inject_nav(html: str, nav_js: str) -> str:
    tag = "<script>\n" + nav_js + "\n</script>"
    return html.replace("</body>", tag + "</body>", 1) if "</body>" in html else html + tag


# --------------------------------------------------------------------------
# Build d'un produit
# --------------------------------------------------------------------------

def build_product(product: str, src_dir: Path) -> dict:
    out_dir = OUT_DIR / product
    out_dir.mkdir(parents=True, exist_ok=True)

    sources: dict[str, Path] = {}
    variants: list[Path] = []
    origin = None
    for f in sorted(src_dir.glob("*.html")):
        if "--" in f.stem:
            variants.append(f)
            continue
        html = f.read_text(encoding="utf-8", errors="replace")
        url = read_source_url(html)
        if not url:
            continue
        if not origin:
            origin = re.match(r"https?://[^/]+", url).group(0)
        r = route_of(url)
        strip = ROUTE_STRIP.get(product)
        if strip and r.startswith(strip):
            r = r[len(strip):] or "/"
        if r not in sources:
            sources[r] = f

    if not sources:
        return {}

    idx = ROUTE_INDEX.get(product, {})
    route_map = {r: idx.get(r, slug_for(r)) for r in sources}
    data_map = load_data_map(product)
    nav_js = make_nav_js(product, {f.name for f in variants})
    nf = NOT_FOUND_PAGE
    referenced: set[str] = set()

    for route, src in sorted(sources.items()):
        html = src.read_text(encoding="utf-8", errors="replace")
        for m in HREF_RE.finditer(html):
            raw = m.group(1) or m.group(2) or m.group(3) or ""
            if origin and raw.startswith(origin):
                p = re.sub(r"^https?://[^/]+", "", raw).split("?")[0].split("#")[0]
                r = "/" + p.strip("/") if p.strip("/") else "/"
                strip = ROUTE_STRIP.get(product, "")
                if strip and r.startswith(strip):
                    r = r[len(strip):] or "/"
                if r not in route_map:
                    referenced.add(r)
        html = clean_html(html)
        html = rewrite_links(html, origin, route_map, nf, ROUTE_STRIP.get(product, ""))
        if data_map:
            html = apply_data_map(html, data_map)
        html = inject_nav(html, nav_js)
        (out_dir / route_map[route]).write_text(html, encoding="utf-8")
        print(f"   OK  {route:42s} -> {product}/{route_map[route]}")

    for f in variants:
        html = f.read_text(encoding="utf-8", errors="replace")
        html = clean_html(html)
        html = rewrite_links(html, origin, route_map, nf, ROUTE_STRIP.get(product, ""))
        if data_map:
            html = apply_data_map(html, data_map)
        html = inject_nav(html, nav_js)
        (out_dir / f.name).write_text(html, encoding="utf-8")
        print(f"   OK  {'[variante]':42s} -> {product}/{f.name}")

    dash_route = "/" if "/" in sources else sorted(sources)[0]
    dash_html = clean_html(sources[dash_route].read_text(encoding="utf-8", errors="replace"))
    nf_html = build_product_404(dash_html)
    nf_html = rewrite_links(nf_html, origin, route_map, nf, ROUTE_STRIP.get(product, ""))
    if data_map:
        nf_html = apply_data_map(nf_html, data_map)
    nf_html = inject_nav(nf_html, nav_js)
    (out_dir / nf).write_text(nf_html, encoding="utf-8")

    return {
        "origin": origin,
        "captured": {r: route_map[r] for r in sorted(route_map)},
        "variants": sorted(f.name for f in variants),
        "missing_routes": sorted(referenced),
    }


# --------------------------------------------------------------------------
# Hub d'accueil (design propre, sidebar produits)
# --------------------------------------------------------------------------

PRODUCTS_META = {
    "datetrace": {
        "name": "DateTrace", "icon": "🌴", "tag": "Filière dattes",
        "color": "#e11d48", "accent": "#9f1239", "textDark": "#ffe4e6",
        "modules": [
            ("datetrace/lots.html", "📦 Lots & Palmeraies", "Gestion lots Deglet Nour, terroirs & producteurs"),
            ("datetrace/producteurs.html", "👤 Producteurs", "Registre palmiers, certifications & bio"),
            ("datetrace/etapes.html", "🔬 Étapes & Qualité", "Désinfection, tri calibre, IA chimique pesticides"),
            ("datetrace/qr-trace.html", "📱 QR & Traçabilité", "Certificats GS1, scan consommateur & blockchain"),
            ("datetrace/blockchain.html", "⛓️ Ancrage Blockchain", "Registre distribué immuable SHA-256"),
            ("datetrace/iot.html", "📡 Capteurs IoT", "Humidité sol palmeraie, chaîne du froid box"),
            ("datetrace/certifications.html", "🌿 Certifications", "Bio, GlobalG.A.P., BRGM, Tesco TN+"),
            ("datetrace/audits.html", "🛡️ Audits & CAPA", "ISO 9001/22000, plans correctifs actions"),
            ("datetrace/assistant.html", "🤖 Assistant IA", "Requêtes NLP filière et alertes qualité"),
        ],
        "summary": "Traçabilité unitaire de la datte de la palmeraie au supermarché, sécurisée par QR Code et ancrage Blockchain.",
    },
    "olivetrace": {
        "name": "OliveTrace", "icon": "🫒", "tag": "Huile d'olive",
        "color": "#10b981", "accent": "#065f46", "textDark": "#d1fae5",
        "modules": [
            ("olivetrace/index.html", "📊 Tableau de Bord Millésime", "Vue temps réel parcelles, moulins & exports"),
            ("olivetrace/parcelles.html", "🌳 Parcelles Oléicoles", "Géolocalisation SI Oli, densité arbres & rendement"),
            ("olivetrace/recoltes.html", "🧺 Récoltes & Cueillette", "Pesées journalières, mode manuel/effleurage"),
            ("olivetrace/moulins.html", "🏭 Moulins & Pressages", "Suivi malaxage, filtration et rendement litre/arbre"),
            ("olivetrace/laboratoires.html", "🧪 Analyses Labo & Qualité", "Acidité libre, indice peroxyde, empyreumatique"),
            ("olivetrace/iso22000.html", "📋 ISO 22000 & HACCP", "Maîtrise dangers CCP, procédures & actions correctives"),
            ("olivetrace/exports.html", "🚢 Dossiers Export ONH", "Préparation certificats export Tunisie & UE"),
            ("olivetrace/iot.html", "📡 Capteurs IoT Oléicole", "Sonde température cuve, hygrométrie cave"),
            ("olivetrace/documents.html", "📁 Certificats & Factures", "Factures annulantes, attestations douane & COA"),
        ],
        "summary": "Pilotage complet de la chaîne huile d'olive : de la récolte à la bouteille exportée avec conformité ISO 22000.",
    },
    "aquatrace": {
        "name": "AquaTrace", "icon": "🐟", "tag": "Aquaculture",
        "color": "#06b6d4", "accent": "#0e7490", "textDark": "#cffafe",
        "modules": [
            ("aquatrace/index.html", "📊 Tableau de Bord Bassins", "Bilan biomasse, TRS traitement, taux oxygénation"),
            ("aquatrace/lots.html", "🐟 Lots & Poissons", "Tracabilité cycles d'élevage crevette & daurade"),
            ("aquatrace/farms.html", "🏗️ Fermes Aquacoles", "Sites marine & étang, concession ONP & autorisations"),
            ("aquatrace/sensors.html", "📟 Capteurs Eau IoT", "O₂ dissous, pH, T°, turbidité, ammoniac NH₃/NH₄"),
            ("aquatrace/feeding.html", "🌾 Alimentations", "Rations granulés, taux conversion (FCR) & arrêts"),
            ("aquatrace/health.html", "💊 Santé & Pathogènes", "Registre sanitaire, mortalité, antiparasitaires"),
            ("aquatrace/withdrawal.html", "⏳ Délais d'Attente", "Calcul fin traitement avant commercialisation"),
            ("aquatrace/blockchain.html", "⛓️ Preuve Blockchain", "Scellement cryptographique des lots pêchés"),
            ("aquatrace/qrcode.html", "📱 QR Code Marché", "Traçabilité du banc au restaurateur"),
        ],
        "summary": "Maîtrise de la qualité eau, de la santé des cheptels et des délais d'attente pour des produits aqua responsables.",
    },
    "medtrace": {
        "name": "MedTrace", "icon": "💊", "tag": "Pharmaceutique",
        "color": "#3b82f6", "accent": "#1e40af", "textDark": "#dbeafe",
        "modules": [
            ("medtrace/index.html", "📊 Tableau de Bord Santé", "Taux rupture, couverture vaccinale, alertes DPM"),
            ("medtrace/lots.html", "🧬 Lots & DCI", "Traçabilité lots vaccins, sérums, consommables injectables"),
            ("medtrace/stupefiants.html", "🔒 Registre Stupéfiants", "Livres officiels de movements stupéfiants N1-N2"),
            ("medtrace/temperature.html", "🌡️ Chaîne du Froid DPM", "Boîtiers IoT température frigo vaccins (-80°C à +8°C)"),
            ("medtrace/hopitaux.html", "🏥 Établissements Sanitaires", "CHU, Hôpitaux régionaux, centres de santé de base"),
            ("medtrace/laboratoires.html", "🔬 Laboratoires Analyse", "Analyses toxicologiques, PCR, microstérilisation"),
            ("medtrace/inspections.html", "🛡️ Inspections & Sanctions", "Contrôles DPM, suivi non-conformités sanitaires"),
            ("medtrace/ia.html", "🤖 IA Antifalsification", "Détection anomalies prix et ruptures sur chaîne"),
            ("medtrace/pharmacies.html", "🏪 Pharmacies Privées", "Tupiniers, officines de garde, traçabilité délivrance"),
        ],
        "summary": "Sécurisation absolue des circuits pharmaceutiques, vaccines et stupéfiants avec preuve de température infalsifiable.",
    },
    "machine": {
        "name": "TNMachine", "icon": "⚙️", "tag": "Production & Maintenance",
        "color": "#f97316", "accent": "#9a3412", "textDark": "#ffedd5",
        "modules": [
            ("machine/index.html", "📊 Supervision Parc Global", "TRS moyen, disponibilité, OEE consolidé des lignes"),
            ("machine/machines.html", "🏭 Machines & Capteurs", "Remplisseuse, Sertisseuse, Autoclave, Étiqueteuse"),
            ("machine/machines--selected.html", "📟 Analyse Vibrométrique IA", "Vibrations palier, courant moteur, thermique bobine"),
            ("machine/production.html", "📈 Production & TRS / OEE", "Performance horaire, taux de rebut, cadence nominale"),
            ("machine/maintenance.html", "🔧 Maintenance Prédictive", "Ordres de travail (OT), pannes anticipées, pièces"),
            ("machine/jumeau.html", "🧬 Jumeau Numérique 3D", "Simulation temps réel des lignes de conditionnement"),
            ("machine/energie.html", "⚡ Supervision Énergie", "Consommation kWh par poste et coût au kilo produit"),
            ("machine/boitiers.html", "📶 Boîtiers Edge IoT", "Gateway connectées au parc machines sur site"),
            ("machine/simulateur.html", "🧪 Simulateur Charge", "Tests scénarios panne / surchauffe sans risque"),
        ],
        "summary": "Supervision industrielle temps réel avec IoT Edge, calcul OEE/TRS automatisé et jumeau numérique prédictif.",
    },
}

HUB_PAGE = (SCRIPTS_DIR / "hub_template.html").read_text(encoding="utf-8")


def build_hub(manifest: dict, pending: list[str]) -> None:
    """Génère output/index.html — hub clair éditorial (design doux)."""
    platform_cards = []
    all_modules_data = {}
    product_meta_js = {}
    n_routes = n_variants = 0
    num = 0

    for prod, meta in PRODUCTS_META.items():
        if prod not in manifest["products"]:
            continue
        num += 1
        info = manifest["products"][prod]
        nr = len(info["captured"])
        nv = len(info["variants"])
        n_routes += nr
        n_variants += nv

        color = meta["color"]
        tint = meta["textDark"]
        cov = min(98, nr * 4 + nv)

        all_modules_data[prod] = meta["modules"]
        product_meta_js[prod] = {"name": meta["name"], "tag": meta["tag"], "icon": meta["icon"]}

        # Chips : 3 premiers modules, libellé court sans emoji
        def chip_label(m):
            return re.sub(r"^\S+\s*", "", m[1]).split("·")[0].split("&")[0].strip()

        chips = "\n".join(
            f'          <a class="chip" href="{m[0]}">{chip_label(m)}</a>'
            for m in meta["modules"][:3]
        )

        platform_cards.append(
            f'''      <article class="pcard" style="--ac:{color};--tint:{tint}" data-prod="{prod}">
        <div class="pcard-top">
          <div class="pcard-ic">{meta["icon"]}</div>
          <span class="pcard-num">{num:02d} / TN</span>
        </div>
        <div class="pcard-body">
          <h3>{meta["name"]}</h3>
          <div class="tl">{meta["tag"]}</div>
          <p>{meta["summary"]}</p>
          <div class="chips">
{chips}
          </div>
        </div>
        <div class="pcard-foot">
          <div class="pcard-meta"><span>{nr} écrans · {nv} formulaires</span><span>{cov} %</span></div>
          <div class="bar"><i style="--cov:{cov}%"></i></div>
          <div class="pcard-actions">
            <a class="btn-open" href="{prod}/index.html">Explorer la plateforme →</a>
            <button class="btn-mods" onclick="openDrawer('{prod}','{color}','{tint}')">Modules</button>
          </div>
        </div>
      </article>'''
        )

    modules_js = json.dumps(all_modules_data, ensure_ascii=False)
    meta_js = json.dumps(product_meta_js, ensure_ascii=False)

    html = (
        HUB_PAGE
        .replace("__PLATFORM_CARDS__", "\n".join(platform_cards))
        .replace("__MODULES_DATA__", modules_js)
        .replace("__PRODUCT_META__", meta_js)
        .replace("__NPROD__", str(len(manifest["products"])))
        .replace("__NROUTES__", str(n_routes))
        .replace("__NVARIANTS__", str(n_variants))
    )
    (OUT_DIR / "index.html").write_text(html, encoding="utf-8")
    print("=== hub ===")
    print(f"   OK  index.html : {len(manifest['products'])} produits, "
          f"{n_routes} écrans, {n_variants} formulaires")


def main() -> int:
    if not PAGES_DIR.is_dir():
        sys.exit(f"Dossier introuvable : {PAGES_DIR}")

    # output/ est entièrement généré -> on le recrée proprement
    import shutil
    if OUT_DIR.is_dir():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(exist_ok=True)

    # Assets statiques (photos du hub) copiés tels quels dans output/assets/
    assets_dir = ROOT / "assets"
    if assets_dir.is_dir():
        shutil.copytree(assets_dir, OUT_DIR / "assets")

    manifest: dict = {"products": {}, "home": False}
    dirs = sorted(d for d in PAGES_DIR.iterdir() if d.is_dir())

    for d in dirs:
        if d.name == "home":
            continue
        print(f"=== {d.name} ===")
        info = build_product(d.name, d)
        if info:
            manifest["products"][d.name] = info
            print(f"   OK  {d.name} : {len(info['captured'])} routes, {len(info['variants'])} variantes")
        else:
            print("   (aucun export valide)")

    # Landing officielle TNtrace (page produit d'origine, en annexe du hub)
    home_dir = PAGES_DIR / "home"
    if home_dir.is_dir():
        files = list(home_dir.glob("*.html"))
        if files:
            html = files[0].read_text(encoding="utf-8", errors="replace")
            html = clean_html(html)
            available = set(manifest["products"])
            html = rewrite_home_links(html, available)
            (OUT_DIR / "tntrace-landing.html").write_text(html, encoding="utf-8")
            manifest["home"] = True
            print("=== home ===")
            print("   OK  /tntrace.tn -> tntrace-landing.html (landing officielle)")

    missing = [p for d, p in KNOWN_PRODUCTS.items() if p not in manifest["products"]]

    # Hub custom = page d'entrée du clone
    build_hub(manifest, missing)

    # 404 globale (produits non capturés)
    (OUT_DIR / NOT_FOUND_PAGE).write_text(ROOT_404, encoding="utf-8")

    (OUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    if missing:
        print("\nProduits du hub non encore capturés :", ", ".join(missing))
    return 0


if __name__ == "__main__":
    sys.exit(main())
