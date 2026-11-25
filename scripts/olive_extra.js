// olive_extra.js — enrichissements démo OliveTrace (injecté après nav.js sur les pages olivetrace).
// Sidebar « Consommateur », panel de traçabilité, modales d'actions, aide contextuelle,
// réponses de l'assistant, détail carbone, liens lot -> page de vérification publique.
(function () {
  "use strict";

  var PAGE = (location.pathname.split("/").pop() || "index.html").toLowerCase();
  var IS_VARIANT = PAGE.indexOf("--") !== -1;

  var LOTS = {
    "OLV-2026-0001": { name: "Henchir el Ain · Chemlali", cat: "Extra vierge", prod: "Sami Ben Amor", co2: 412,
      steps: [["Parcelle", "Campagne 2026 · Nabeul"], ["Récolte", "01/10/2026 · 3 000 kg"], ["Trituration", "02/10/2026 · Moulin Ennour · 570 L"], ["Analyse", "02/10/2026 · Olea Analyses · 0,38 %"], ["Conditionnement", "03/10/2026 · El Amel · 1 120 blles"], ["Export", "04/10/2026 · Sfax → France"]] },
    "OLV-2026-0002": { name: "Ferme El Wafa · Chetoui", cat: "Vierge", prod: "Mohamed Trabelsi", co2: 688,
      steps: [["Parcelle", "Campagne 2026 · Sfax"], ["Récolte", "15/10/2026 · 2 400 kg"], ["Trituration", "15/10/2026 · El Baraka · 480 L"], ["Analyse", "18/10/2026 · ONAGRI · 0,32 %"], ["Conditionnement", "19/10/2026 · Méditerranée · 1 600 blles"], ["Export", "16/10/2026 · Sfax → Italie"]] },
    "OLV-2026-0003": { name: "Les Oliviers du Nord · Oueslati", cat: "Vierge", prod: "Ali Ben Salah", co2: 356,
      steps: [["Parcelle", "Campagne 2026 · Béja"], ["Récolte", "08/10/2026 · 3 200 kg"], ["Trituration", "08/10/2026 · Moulin Errim · 610 L"], ["Analyse", "09/10/2026 · SGS · 0,89 %"], ["Conditionnement", "12/10/2026 · Prestige · 144 bidons"], ["Export", "20/10/2026 · Radès → France"]] },
    "OLV-2026-0004": { name: "Dar Essalem · Chemlali", cat: "Extra vierge", prod: "Fatma Gharbi", co2: 268,
      steps: [["Parcelle", "Campagne 2026 · Kairouan"], ["Récolte", "12/10/2026 · 1 800 kg"], ["Trituration", "12/10/2026 · Moulin Ennour · 360 L"], ["Analyse", "13/10/2026 · Olea · 0,42 %"], ["Conditionnement", "14/10/2026 · El Amel · 600 blles"], ["Distribution", "16/10/2026 · Tunisie"]] }
  };
  var CO2_SPLIT = [["Verger", 38], ["Trituration", 18], ["Emballage", 20], ["Transport", 24]];
  var CO2_COLOR = ["#5b7d2e", "#c8a24a", "#84a94b", "#1b3a24"];
  var ANSWERS = {
    "average extraction yield": "Rendement moyen : <b>20,0 %</b> sur 6 pressages.<br>• Moulin Ennour : 19–20 % (2 phases)<br>• El Baraka : 19,1–20 % (3 phases)<br>• moulin1hd : 22,2 % — petit lot, à confirmer<br>• Moulin Errim : 19,1 % (traditionnel)",
    "litres were exported": "<b>2 480 L</b> exportés : 1 280 L vers la France (2 dossiers), 1 200 L vers l'Italie (1 dossier). Le lot OLV-2026-0002 (Italie) est le seul déjà expédié.",
    "non-compliant": "1 analyse à surveiller : le lot <b>Ali Ben Salah · Oueslati</b> (SGS, 05/10) affiche K232 = 2,64 — au-dessus de la limite « Vierge » (2,60). Acidité 0,89 % conforme. Une contre-analyse est recommandée.",
    "most kg": "<b>Ali Ben Salah</b> (Béja, Oueslati) est le premier producteur : ~7 100 kg récoltés sur 4 parcelles. Suivi de Mohamed Trabelsi (~6 800 kg) et Sami Ben Amor (~4 200 kg).",
    "breakdown by olive variety": "<b>~17 300 kg</b> récoltés : Chemlali 54 % · Chetoui 26 % · Oueslati 15 % · Arbequina 5 %.",
    "quality category": "4 lots : OLV-2026-0001 <b>Extra vierge</b> (0,38 %) · OLV-2026-0002 <b>Vierge</b> (0,32 %) · OLV-2026-0003 <b>Vierge</b> (0,89 %) · OLV-2026-0004 <b>Extra vierge</b> (0,42 %).",
    "packed per packer": "El Amel Conditionnement : <b>1 160 L</b> (2 lots) · Méditerranée Emballage : <b>1 200 L</b> · Huile Prestige : <b>720 L</b>. Total : 3 080 L.",
    "exports per destination": "France : 2 dossiers · Italie : 1 dossier · 1 lot distribué sur le marché tunisien."
  };
  var HELP = {
    "index.html": "Vue consolidée de la campagne : volumes récoltés et pressés, analyses reçues, lots scellés et exports en cours. Toutes les tuiles sont calculées sur les données réelles de la chaîne.",
    "tracabilite.html": "Tapez un numéro de lot (ex. OLV-2026-0001) puis « Trace » : la chaîne complète parcelle → export s'affiche. « Par lot » remonte l'historique, « par récolte » descend vers les produits, « par société » liste les lots d'un acteur.",
    "producteurs.html": "Registre des oléiculteurs : coordonnées, parcelles rattachées et volumes livrés. « New producer » crée une fiche ; « Edit » ouvre une correction horodatée.",
    "parcelles.html": "Parcelles géoréférencées (déclaration SI Oli) : variété, surface, récoltes et certification associées à chaque producteur.",
    "recoltes.html": "Pesées journalières par parcelle : méthode, maturité et statut (en attente / pressé). Chaque correction est scellée dans la blockchain.",
    "moulins.html": "Fiches des moulins partenaires : procédé, capacité journalière, volume produit et certification.",
    "pressages.html": "Chaque trituration relie une récolte à un volume d'huile et un rendement. Le ticket de pressage (TM-2026-XXXX) suit le lot jusqu'à l'analyse.",
    "laboratoires.html": "Laboratoires accrédités ISO/IEC 17025 qui signent les analyses COI/IOC de vos lots.",
    "analyses.html": "Saisie des résultats COI/IOC (17 paramètres) : l'IA contrôle les seuils, classe l'huile et signale les écarts. Les rapports joints sont lus et comparés automatiquement.",
    "conditionneurs.html": "Emballeurs partenaires : formats, cadence et conformité emballage contact alimentaire.",
    "operations.html": "Mise en bouteille : le lot est scellé (empreinte blockchain) et un QR unique GS1 est généré par contenant. Cliquez un code lot pour voir la page publique.",
    "exportateurs.html": "Exportateurs agréés : références ONH, marchés desservis et volumes annuels.",
    "exports.html": "Dossiers d'export par lot : déclaration, port, destination et statut logistique. Le hash blockchain est enregistré à l'expédition.",
    "certifications.html": "Certificats réellement détenus par les acteurs (bio, ISO 22000, HACCP, 17025) avec dates d'expiration et documents scellés.",
    "conformite.html": "Contrôle automatique de chaque lot sur 21 critères COI/réglementaires. « Manual check » ajoute une vérification terrain.",
    "dossiers.html": "Dossier documentaire par export : certificat d'analyse, EUR.1, phytosanitaire… l'IA détecte les pièces manquantes.",
    "documents.html": "Ged des pièces scellées : chaque document est horodaté, hashé et attaché à une étape de la chaîne.",
    "iot.html": "Sondes terrain : température des cuves, hygrométrie des caves, capteurs parcelle. Les relevés alimentent la chaîne de preuve.",
    "iso22000.html": "Système de management de la sécurité alimentaire : procédures documentées, points critiques HACCP, audits internes et CAPA.",
    "utilisateurs.html": "Comptes de la filière : rôles (producteur, moulin, labo, exportateur, admin) et journal des accès.",
    "journal.html": "Journal des événements sensibles : connexions, signatures de blocs, corrections et exports — chaque ligne est horodatée.",
    "clients.html": "Sociétés clientes de la plateforme : comptes B2B, volumes commandés et lots réservés.",
    "blockchain.html": "Registre des blocs : chaque étape, contrôle IA et correction produit un bloc SHA-256 chaîné, ancré périodiquement sur Bitcoin (OpenTimestamps).",
    "carbone.html": "Bilan CO₂e par lot (méthode ISO 14067 simplifiée) calculé depuis les données réelles : culture, trituration, emballage, transport.",
    "bilan.html": "Bilan matière : kg d'olives entrés vs litres produits par acteur — détection des écarts et pertes.",
    "assistant.html": "Interrogez la filière en langage naturel : rendements, volumes, analyses, exports. Les réponses citent les vraies données du registre.",
    "boutique.html": "Vitrine consommateur : chaque bouteille est vendue avec son QR de traçabilité vérifiable.",
    "verifier.html": "Page publique du consommateur : le scan du QR affiche le voyage du lot, les analyses et la preuve blockchain recalculée."
  };

  /* ---------- styles ---------- */
  var css = document.createElement("style");
  css.textContent =
    ".ox-veil{position:fixed;inset:0;background:rgba(15,23,42,.45);backdrop-filter:blur(3px);z-index:99990;opacity:0;transition:.25s;pointer-events:none}" +
    ".ox-veil.on{opacity:1;pointer-events:auto}" +
    ".ox-modal{position:fixed;inset:0;z-index:99995;display:grid;place-items:center;padding:20px;opacity:0;pointer-events:none;transition:.25s}" +
    ".ox-modal.on{opacity:1;pointer-events:auto}" +
    ".ox-box{width:min(560px,96vw);max-height:88vh;overflow:auto;background:#fff;border-radius:20px;padding:28px;box-shadow:0 30px 80px -20px rgba(15,23,42,.45);transform:translateY(14px);transition:.3s}" +
    ".ox-modal.on .ox-box{transform:none}" +
    ".ox-box h3{font-size:19px;font-weight:700;color:#0f172a;margin-bottom:4px}" +
    ".ox-box p.sub{font-size:13px;color:#64748b;margin-bottom:16px}" +
    ".ox-tbl{width:100%;font-size:13px;border-collapse:collapse;margin:8px 0 4px}" +
    ".ox-tbl td,.ox-tbl th{padding:8px 10px;border-bottom:1px solid #f1f5f9;text-align:left}" +
    ".ox-tbl th{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:#94a3b8}" +
    ".ox-tag{display:inline-flex;align-items:center;gap:5px;padding:4px 10px;border-radius:999px;font-size:12px;font-weight:600}" +
    ".ox-tag.ok{background:#dcfce7;color:#166534}.ox-tag.warn{background:#fef3c7;color:#92400e}.ox-tag.bad{background:#fee2e2;color:#b91c1c}" +
    ".ox-btns{display:flex;gap:10px;justify-content:flex-end;margin-top:22px}" +
    ".ox-btn{padding:10px 18px;border-radius:12px;font-size:13.5px;font-weight:600;border:1px solid #e2e8f0;background:#fff}" +
    ".ox-btn.pri{background:#047857;border-color:#047857;color:#fff}.ox-btn.dan{background:#dc2626;border-color:#dc2626;color:#fff}" +
    ".ox-toast{position:fixed;left:50%;bottom:70px;transform:translateX(-50%);z-index:99999;background:#065f46;color:#fff;font:500 13px/1.4 Inter,system-ui,sans-serif;padding:10px 18px;border-radius:999px;box-shadow:0 10px 30px rgba(6,95,70,.35);opacity:0;transition:.3s;pointer-events:none;max-width:80vw;text-align:center}" +
    ".ox-toast.on{opacity:.97}" +
    ".ox-hash{font:11px ui-monospace,Consolas,monospace;background:#f1f5f9;border-radius:6px;padding:3px 8px;color:#334155;word-break:break-all}" +
    ".ox-help{border-top:1px solid #d1fae5;padding:14px 20px 18px;font-size:13px;color:#065f46;line-height:1.6;display:none}" +
    ".ox-help.on{display:block}" +
    ".ox-banner{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:18px;padding:14px 18px;border-radius:16px;background:linear-gradient(120deg,#0f2d1a,#1d4a2a);color:#d9f2e2}" +
    ".ox-banner b{font-size:14px}.ox-banner span{font-size:12.5px;opacity:.75}" +
    ".ox-banner a{padding:8px 14px;border-radius:99px;background:#c8a24a;color:#0f172a;font-size:12.5px;font-weight:700}" +
    ".ox-banner a.alt{background:rgba(255,255,255,.12);color:#fff}" +
    ".ox-note{display:flex;gap:10px;align-items:center;padding:12px 16px;border-radius:12px;background:#fffbeb;border:1px solid #fde68a;font-size:13px;color:#92400e;margin-bottom:16px}" +
    ".ox-lot{background:#fff;border:1px solid #e2e8f0;border-radius:18px;overflow:hidden;margin-top:8px}" +
    ".ox-lot .hd{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:16px 20px;background:linear-gradient(120deg,#0f2d1a,#1d4a2a);color:#fff}" +
    ".ox-lot .hd b{font-size:15px}.ox-lot .hd span{font-size:12px;opacity:.7}" +
    ".ox-lot .bd{display:grid;gap:0}" +
    ".ox-stp{display:flex;align-items:center;gap:12px;padding:11px 20px;border-top:1px solid #f1f5f9;font-size:13px}" +
    ".ox-stp:first-child{border-top:0}" +
    ".ox-stp .ic{width:32px;height:32px;border-radius:10px;background:#ecfdf5;display:grid;place-items:center;font-size:15px;flex-shrink:0}" +
    ".ox-stp b{font-weight:600}.ox-stp small{color:#64748b;display:block}" +
    ".ox-stp .ok{margin-left:auto;color:#059669;font-size:11.5px;font-weight:700;white-space:nowrap}" +
    ".ox-foot{display:flex;gap:10px;flex-wrap:wrap;padding:14px 20px;border-top:1px solid #f1f5f9;background:#fafcfa}" +
    ".ox-foot a{padding:9px 16px;border-radius:99px;font-size:12.5px;font-weight:700;background:#0f2d1a;color:#fff}" +
    ".ox-foot a.alt{background:#fff;border:1px solid #d1d5db;color:#334155}" +
    ".ox-bar{display:flex;height:10px;border-radius:8px;overflow:hidden;margin:14px 0 8px}" +
    ".ox-leg{display:grid;grid-template-columns:1fr 1fr;gap:4px 14px;font-size:12px;color:#64748b}" +
    ".ox-leg i{display:inline-block;width:9px;height:9px;border-radius:3px;margin-right:6px}" +
    ".ox-msg{display:flex;margin-bottom:12px}.ox-msg.u{justify-content:flex-end}" +
    ".ox-msg div{max-width:78%;padding:10px 14px;border-radius:14px;font-size:13px;line-height:1.55}" +
    ".ox-msg.u div{background:#047857;color:#fff;border-bottom-right-radius:4px}" +
    ".ox-msg.a div{background:#fff;border:1px solid #e2e8f0;border-bottom-left-radius:4px}" +
    ".ox-sel{outline:2px solid #059669;outline-offset:2px}";
  document.head.appendChild(css);

  function veil() {
    var v = document.querySelector(".ox-veil");
    if (!v) { v = document.createElement("div"); v.className = "ox-veil"; document.body.appendChild(v); }
    return v;
  }
  function oxToast(msg) {
    var t = document.querySelector(".ox-toast");
    if (!t) { t = document.createElement("div"); t.className = "ox-toast"; document.body.appendChild(t); }
    t.textContent = msg; t.classList.add("on");
    clearTimeout(t._t); t._t = setTimeout(function () { t.classList.remove("on"); }, 2600);
  }
  function oxModal(html) {
    var m = document.querySelector(".ox-modal");
    if (!m) { m = document.createElement("div"); m.className = "ox-modal"; document.body.appendChild(m); }
    m.innerHTML = '<div class="ox-box">' + html + "</div>";
    veil().classList.add("on"); m.classList.add("on");
    function off(e) { if (!e || e.target === m || e.target.closest("[data-ox-close]")) { m.classList.remove("on"); veil().classList.remove("on"); m.removeEventListener("click", off); } }
    m.addEventListener("click", off);
    veil().onclick = off;
    return m;
  }
  function oxConfirm(title, text, ok, dan) {
    oxModal("<h3>" + title + '</h3><p class="sub">' + text + '</p><div class="ox-btns">' +
      '<button class="ox-btn" data-ox-close>Annuler</button><button class="ox-btn ' + (dan ? "dan" : "pri") + '" id="ox-ok">' + ok + "</button></div>");
    document.getElementById("ox-ok").onclick = function () {
      document.querySelector(".ox-modal").classList.remove("on"); veil().classList.remove("on");
      oxToast("Action enregistrée — un bloc de correction sera scellé dans la chaîne");
    };
  }

  /* ---------- sidebar : groupe Consommateur + réparation des liens ---------- */
  var nav = document.querySelector("aside nav");
  if (nav && !nav.querySelector(".ox-consumer")) {
    var g = document.createElement("div");
    g.className = "ox-consumer";
    g.innerHTML =
      '<p class="text-xs font-semibold text-emerald-600/60 uppercase tracking-widest px-3 mb-1">Consommateur<div class="space-y-0.5">' +
      '<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-all text-green-100/70 hover:text-white hover:bg-white/10' + (PAGE === "boutique.html" ? " bg-emerald-600 text-white shadow-sm" : "") + '" href="boutique.html"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide w-4 h-4 flex-shrink-0"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg><span>Boutique</span></a>' +
      '<a class="flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-all text-green-100/70 hover:text-white hover:bg-white/10' + (PAGE === "verifier.html" ? " bg-emerald-600 text-white shadow-sm" : "") + '" href="verifier.html"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide w-4 h-4 flex-shrink-0"><rect width="5" height="5" x="3" y="3" rx="1"/><rect width="5" height="5" x="16" y="3" rx="1"/><rect width="5" height="5" x="3" y="16" rx="1"/><path d="M21 16h-3a2 2 0 0 0-2 2v3"/><path d="M21 21v.01"/><path d="M12 7v3a2 2 0 0 1-2 2H7"/><path d="M3 12h.01"/><path d="M12 3h.01"/><path d="M12 16v.01"/><path d="M16 12h1"/><path d="M21 12v-1"/></svg><span>Vérifier une bouteille</span></a>' +
      "</div>";
    nav.appendChild(g);
  }
  document.querySelectorAll('a[href*="404-local.html#journal"]').forEach(function (a) { a.setAttribute("href", "journal.html"); });
  document.querySelectorAll('a[href*="404-local.html#clients"]').forEach(function (a) { a.setAttribute("href", "clients.html"); });

  /* ---------- bandeau vitrine sur le dashboard ---------- */
  if (PAGE === "index.html") {
    var main = document.querySelector("main > div, main");
    if (main && !document.querySelector(".ox-banner")) {
      var b = document.createElement("div");
      b.className = "ox-banner";
      b.innerHTML = "<b>Vitrine consommateur</b><span>Chaque bouteille scellée est déjà visible — et vérifiable — côté public.</span>" +
        '<span style="flex:1"></span><a href="boutique.html">Voir la boutique →</a><a class="alt" href="verifier.html">Tester le scan QR</a>';
      main.insertBefore(b, main.firstChild);
    }
  }

  /* ---------- codes lot -> page de vérification publique ---------- */
  document.querySelectorAll("span.font-mono, td, .stp, b").forEach(function (el) {
    if (el.children.length === 0 && /^OLV-2026-\d{4}$/.test((el.textContent || "").trim()) && !el.closest("a")) {
      var id = el.textContent.trim();
      el.innerHTML = '<a href="verifier.html?lot=' + id + '" style="color:#047857;text-decoration:underline dotted" title="Ouvrir la page publique de vérification">' + id + "</a>";
    }
  });

  /* ---------- bandeau « correction » sur les pages formulaire ---------- */
  if (IS_VARIANT && /mode=/.test(location.search)) {
    var card = document.querySelector("main") || document.body;
    var n = document.createElement("div");
    n.className = "ox-note";
    n.innerHTML = "<span>✎</span><div><b>Mode correction.</b> La valeur d'origine est conservée : la nouvelle saisie créera un bloc de correction scellé et horodaté.</div>";
    card.insertBefore(n, card.firstChild.nextSibling);
  }

  /* ---------- aide contextuelle « How does this page work? » ---------- */
  document.querySelectorAll("button").forEach(function (btn) {
    if ((btn.textContent || "").indexOf("How does this page work") === -1) return;
    var host = btn.closest("div.mt-8") || btn.parentElement;
    if (!host) return;
    var p = document.createElement("div");
    p.className = "ox-help";
    p.textContent = HELP[PAGE] || "Cet écran fait partie de la chaîne de traçabilité : chaque saisie est horodatée, scellée dans la blockchain et vérifiable par vos clients.";
    host.appendChild(p);
    btn.addEventListener("click", function (e) { e.stopImmediatePropagation(); e.preventDefault(); p.classList.toggle("on"); }, true);
  });

  /* ---------- traçabilité : bouton Trace fonctionnel ---------- */
  if (PAGE === "tracabilite.html") {
    var input = document.querySelector('main input[type="text"], main input:not([type])');
    var traceBtn = [].slice.call(document.querySelectorAll("button")).find(function (b) { return (b.textContent || "").trim() === "Trace"; });
    var empty = [].slice.call(document.querySelectorAll("main div")).find(function (d) {
      return (d.textContent || "").indexOf("Enter a lot number") > -1;
    });
    if (traceBtn) traceBtn.removeAttribute("disabled");
    function doTrace() {
      var q = (input && input.value || "").toUpperCase();
      var m = q.match(/OLV-?2026-?0*(\d{1,4})/i);
      var id = m ? "OLV-2026-" + ("000" + m[1]).slice(-4) : "OLV-2026-0001";
      var lot = LOTS[id];
      if (!lot) { oxToast("Lot « " + q + " » introuvable — essayez OLV-2026-0001"); return; }
      var ic = ["🌳", "🧺", "🏭", "🧪", "🍾", "🚢"];
      var el = empty || document.querySelector("main .text-center");
      if (!el) return;
      el.outerHTML =
        '<div class="ox-lot"><div class="hd"><div style="font-size:22px">📦</div><div><b>' + id + " — " + lot.name + "</b><span>" + lot.cat + " · " + lot.prod + ' · scellé sur Bitcoin</span></div></div>' +
        '<div class="bd">' + lot.steps.map(function (s, i) {
          return '<div class="ox-stp"><div class="ic">' + ic[i] + "</div><div><b>" + s[0] + "</b><small>" + s[1] + '</small></div><span class="ok">✓ Scellé</span></div>';
        }).join("") + "</div>" +
        '<div class="ox-foot"><a href="verifier.html?lot=' + id + '">Voir la page publique consommateur →</a><a class="alt" href="blockchain.html">Registre blockchain</a></div></div>';
      oxToast("Chaîne complète du lot " + id + " — 6 étapes scellées");
    }
    if (traceBtn) traceBtn.addEventListener("click", function (e) { e.preventDefault(); e.stopImmediatePropagation(); doTrace(); }, true);
    if (input) input.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); doTrace(); } });
  }

  /* ---------- carbone : détail par lot ---------- */
  if (PAGE === "carbone.html") {
    var panel = [].slice.call(document.querySelectorAll("main div")).find(function (d) {
      return d.className.indexOf("md:col-span-3") > -1;
    });
    [].slice.call(document.querySelectorAll("button")).forEach(function (b) {
      var code = b.querySelector(".font-mono");
      if (!code || !/^OLV-/.test(code.textContent)) return;
      var id = code.textContent.trim();
      b.addEventListener("click", function (e) {
        e.preventDefault(); e.stopImmediatePropagation();
        var lot = LOTS[id]; if (!lot || !panel) return;
        var per = (lot.co2 / 560).toFixed(2).replace(".", ",");
        panel.innerHTML =
          '<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px"><div><p class="text-xs text-slate-400">' + id + " · " + lot.name + '</p><p class="text-2xl font-bold text-slate-900">' + lot.co2 + ' kg CO₂e <span class="text-sm font-normal text-slate-400">· ~' + per + ' kg / litre</span></p></div><a href="verifier.html?lot=' + id + '" class="text-xs font-semibold text-emerald-700">Page publique →</a></div>' +
          '<div class="ox-bar">' + CO2_SPLIT.map(function (s, i) { return '<i style="width:' + s[1] + "%;background:" + CO2_COLOR[i] + '"></i>'; }).join("") + "</div>" +
          '<div class="ox-leg">' + CO2_SPLIT.map(function (s, i) { return '<span><i style="background:' + CO2_COLOR[i] + '"></i>' + s[0] + " " + s[1] + " %</span>"; }).join("") + "</div>" +
          '<p class="text-xs text-slate-400 mt-4">Calcul simplifié ISO 14067 sur les données réelles de la chaîne : surface, rendement, emballage, distance port → destination.</p>';
      }, true);
    });
  }

  /* ---------- assistant : réponses démo ---------- */
  if (PAGE === "assistant.html") {
    var chat = document.querySelector(".flex-1.overflow-y-auto.space-y-4");
    function answer(q) {
      if (!chat) return;
      var key = Object.keys(ANSWERS).find(function (k) { return q.toLowerCase().indexOf(k) > -1; });
      var a = ANSWERS[key] || "D'après le registre : 6 producteurs, 9 récoltes (~17,3 t), 6 pressages (~2 700 L), 5 analyses labo et 3 dossiers d'export sont actuellement tracés et scellés.";
      var u = document.createElement("div"); u.className = "ox-msg u"; u.innerHTML = "<div>" + q + "</div>";
      var r = document.createElement("div"); r.className = "ox-msg a"; r.innerHTML = "<div>" + a + "</div>";
      chat.appendChild(u); setTimeout(function () { chat.appendChild(r); chat.scrollTop = chat.scrollHeight; }, 450);
      chat.scrollTop = chat.scrollHeight;
    }
    document.querySelectorAll(".grid.grid-cols-2 > button").forEach(function (b) {
      b.addEventListener("click", function (e) { e.preventDefault(); e.stopImmediatePropagation(); answer(b.textContent.trim()); }, true);
    });
    var form = document.querySelector("form.flex.gap-3"), inp = form && form.querySelector("input"), sb = form && form.querySelector("button");
    if (sb) sb.removeAttribute("disabled");
    if (form) form.addEventListener("submit", function (e) { e.preventDefault(); if (inp && inp.value.trim()) { answer(inp.value.trim()); inp.value = ""; } });
  }

  /* ---------- blockchain : sélection du mode d'ancrage ---------- */
  document.querySelectorAll("button, [role=button]").forEach(function (el) {
    var t = (el.textContent || "");
    if (!/^Internal/.test(t.trim())) return;
    el.addEventListener("click", function (e) {
      e.preventDefault(); e.stopImmediatePropagation();
      document.querySelectorAll(".ox-sel").forEach(function (x) { x.classList.remove("ox-sel"); });
      el.classList.add("ox-sel");
      oxToast(/OpenTimestamps/.test(t) ? "Ancrage interne + Bitcoin activé — preuve publique vérifiable par vos clients" : "Ancrage interne activé — gratuit et instantané");
    }, true);
  });

  /* ---------- gestion des clics d'action (capture, avant nav.js) ---------- */
  document.addEventListener("click", function (e) {
    var btn = e.target.closest("button, [role=button]");
    if (!btn || btn.closest(".ox-modal")) return;
    var label = (btn.textContent || "").replace(/\s+/g, " ").trim();

    /* Navigation/identité */
    if (/^Sign out$/i.test(label)) { e.preventDefault(); e.stopImmediatePropagation(); location.href = "../index.html"; return; }
    if (/^Change my password$/i.test(label)) {
      e.preventDefault(); e.stopImmediatePropagation();
      oxModal('<h3>Changer le mot de passe</h3><p class="sub">OliveTrace Admin · super administrateur</p>' +
        '<table class="ox-tbl"><tr><th>Champ</th><th></th></tr><tr><td>Mot de passe actuel</td><td><input type="password" value="············" style="width:100%;padding:8px 10px;border:1px solid #e2e8f0;border-radius:8px"></td></tr>' +
        '<tr><td>Nouveau mot de passe</td><td><input type="password" placeholder="Min. 10 caractères" style="width:100%;padding:8px 10px;border:1px solid #e2e8f0;border-radius:8px"></td></tr></table>' +
        '<div class="ox-btns"><button class="ox-btn" data-ox-close>Annuler</button><button class="ox-btn pri" id="ox-pw">Enregistrer</button></div>');
      document.getElementById("ox-pw").onclick = function () { document.querySelector(".ox-modal").classList.remove("on"); veil().classList.remove("on"); oxToast("Mot de passe mis à jour — un événement de sécurité est journalisé"); };
      return;
    }
    if (/^(fr|en|ar|عربي)$/i.test(label)) { e.preventDefault(); e.stopImmediatePropagation(); oxToast("La version connectée propose FR / EN / عربي — démo affichée en anglais"); return; }
    if (PAGE.indexOf("iso22000--") === 0 && /^Dashboard$/i.test(label)) { e.preventDefault(); e.stopImmediatePropagation(); location.href = "iso22000.html"; return; }

    /* Actions ligne → formulaires et confirmations */
    if (/^(Edit|Correct)$/i.test(label)) {
      var base = PAGE.replace("--form.html", ".html").replace("--samples.html", ".html");
      var target = base.replace(".html", "--form.html");
      e.preventDefault(); e.stopImmediatePropagation();
      location.href = target + "?mode=correction";
      return;
    }
    if (/^Cancel$/i.test(label) || /^Deactivate$/i.test(label)) {
      e.preventDefault(); e.stopImmediatePropagation();
      oxConfirm(/^Deactivate$/i.test(label) ? "Désactiver ce compte ?" : "Annuler cette entrée ?",
        "Cette action sera enregistrée comme bloc de correction dans la chaîne (l'original reste consultable).",
        /^Deactivate$/i.test(label) ? "Désactiver" : "Confirmer l'annulation", true);
      return;
    }
    if (/^Sign out everywhere$/i.test(label)) {
      e.preventDefault(); e.stopImmediatePropagation();
      oxConfirm("Révoquer toutes les sessions ?", "Toutes les sessions actives de cet utilisateur seront fermées immédiatement.", "Tout révoquer", true);
      return;
    }
    if (/^Import Ecobalyse factors$/i.test(label)) {
      e.preventDefault(); e.stopImmediatePropagation();
      oxModal('<h3>Facteurs d’émission Ecobalyse</h3><p class="sub">Import des facteurs ADEME / Agribalyse pour affiner les bilans carbone.</p>' +
        '<p style="font-size:13px;color:#475569;line-height:1.6">Format attendu : CSV ou JSON Ecobalyse. Les facteurs sont comparés aux ordres de grandeur actuels avant application, puis horodatés comme document de référence.</p>' +
        '<div class="ox-btns"><button class="ox-btn" data-ox-close>Fermer</button><button class="ox-btn pri" id="ox-imp">Choisir un fichier…</button></div>');
      document.getElementById("ox-imp").onclick = function () { document.querySelector(".ox-modal").classList.remove("on"); veil().classList.remove("on"); oxToast("Facteurs importés — recalcul des bilans en cours"); };
      return;
    }
    if (/^Document$/i.test(label) || /^Attach$/i.test(label)) {
      e.preventDefault(); e.stopImmediatePropagation();
      var ctx = (btn.closest("tr") || btn.closest("div")) || btn;
      var code = (ctx.textContent || "").match(/(OLV|TM|DE|TN|ZIT|CERT|BV|LAB)[-A-Z0-9]{1,12}/);
      oxModal('<h3>Document scellé' + (code ? " — " + code[0] : "") + '</h3><p class="sub">Pièce horodatée et vérifiée par l’IA avant enregistrement.</p>' +
        '<div style="border:1px dashed #cbd5e1;border-radius:14px;padding:26px;text-align:center;background:#f8fafc">' +
        '<div style="font-size:34px">📄</div><p style="font-size:13.5px;font-weight:600;margin-top:8px">' + (code ? code[0] : "document") + '_scelle.pdf</p>' +
        '<p style="font-size:12px;color:#64748b;margin-top:4px">SHA-256 <span class="ox-hash">7f3a…c92e</span> · ancré bloc ' + (code ? "#34" : "#12") + "</p>" +
        '<span class="ox-tag ok" style="margin-top:12px">✓ Cohérence IA vérifiée</span></div>' +
        '<div class="ox-btns"><button class="ox-btn" data-ox-close>Fermer</button><button class="ox-btn pri" id="ox-dl">Télécharger</button></div>');
      document.getElementById("ox-dl").onclick = function () { document.querySelector(".ox-modal").classList.remove("on"); veil().classList.remove("on"); oxToast("Document exporté avec sa preuve d’horodatage"); };
      return;
    }
    if (/Avis IA indicatif/i.test(label)) {
      e.preventDefault(); e.stopImmediatePropagation();
      var card = btn.closest(".bg-white") || document.body;
      var tx = (card.textContent || "").replace(/\s+/g, " ");
      function num(k) { var m = tx.match(new RegExp(k + "\\s*\\|?\\s*([0-9]+[.,][0-9]+)")); return m ? m[1] : null; }
      var cat = /Extra virgin/i.test(tx) ? "Extra vierge" : "Vierge";
      var rows = [["Acidité", num("Acidity"), "≤ 0,8 %"], ["Peroxyde", num("Peroxide"), "≤ 20"], ["K232", num("K232"), "≤ 2,50"], ["K270", num("K270"), "≤ 0,22"], ["Oléique", num("Oleic"), "55–83 %"], ["Campestérol", num("Campesterol"), "≤ 4,0 %"]];
      oxModal('<h3>Avis IA indicatif — ' + cat + '</h3><p class="sub">17 paramètres évalués selon COI/T.15/NC n°3 · CE 2568/91</p>' +
        '<table class="ox-tbl"><tr><th>Paramètre</th><th>Valeur</th><th>Limite ' + cat + '</th><th></th></tr>' +
        rows.map(function (r) {
          var v = r[1] ? r[1] + (/Acidité|Oléique|Campestérol/.test(r[0]) ? " %" : "") : "—";
          return "<tr><td>" + r[0] + "</td><td><b>" + v + "</b></td><td>" + r[2] + '</td><td><span class="ox-tag ' + (r[1] ? "ok" : "warn") + '">' + (r[1] ? "✓" : "n/a") + "</span></td></tr>";
        }).join("") + "</table>" +
        '<div class="ox-btns"><span class="ox-tag ok" style="margin-right:auto">Classification ' + cat + ' confirmée</span><button class="ox-btn" data-ox-close>Fermer</button></div>');
      return;
    }
  }, true);
})();
