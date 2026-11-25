/* OliveTrace — Vitrine consommateur : utilitaires partagés (panier, bouteilles, SHA-256). */
(function () {
  "use strict";
  var LOTS = window.OLIVE_LOTS || [];
  var VT = (window.VT = {});

  VT.lots = LOTS;
  VT.lot = function (id) {
    return LOTS.filter(function (l) { return l.id === id; })[0] || LOTS[0];
  };
  VT.param = function (k) { return new URLSearchParams(location.search).get(k); };
  VT.esc = function (s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  };
  VT.money = function (n) { return n.toLocaleString("fr-FR") + " <small>TND</small>"; };

  /* ---------- SHA-256 (pur JS, fonctionne aussi en file://) ---------- */
  var K = [], H0 = [];
  (function () {
    var n = 2, c = 0;
    function frac(x) { return ((x - Math.floor(x)) * 4294967296) | 0; }
    while (c < 64) {
      var p = true;
      for (var d = 2; d * d <= n; d++) if (n % d === 0) { p = false; break; }
      if (p) { if (c < 8) H0[c] = frac(Math.pow(n, 1 / 2)); K[c] = frac(Math.pow(n, 1 / 3)); c++; }
      n++;
    }
  })();
  VT.sha256 = function (str) {
    var bytes = new TextEncoder().encode(str), l = bytes.length;
    var words = [], i;
    for (i = 0; i < l; i++) words[i >> 2] |= bytes[i] << (24 - (i % 4) * 8);
    words[l >> 2] |= 0x80 << (24 - (l % 4) * 8);
    var nw = (((l + 8) >> 6) + 1) * 16;
    for (i = words.length; i < nw; i++) words[i] = words[i] | 0;
    words[nw - 1] = l * 8;
    var h = H0.slice(), w = new Array(64);
    function rr(x, n) { return (x >>> n) | (x << (32 - n)); }
    for (var j = 0; j < nw; j += 16) {
      var a = h[0], b = h[1], c = h[2], d = h[3], e = h[4], f = h[5], g = h[6], hh = h[7];
      for (i = 0; i < 64; i++) {
        if (i < 16) w[i] = words[j + i] | 0;
        else {
          var s0 = rr(w[i - 15], 7) ^ rr(w[i - 15], 18) ^ (w[i - 15] >>> 3);
          var s1 = rr(w[i - 2], 17) ^ rr(w[i - 2], 19) ^ (w[i - 2] >>> 10);
          w[i] = (w[i - 16] + s0 + w[i - 7] + s1) | 0;
        }
        var t1 = (hh + (rr(e, 6) ^ rr(e, 11) ^ rr(e, 25)) + ((e & f) ^ (~e & g)) + K[i] + w[i]) | 0;
        var t2 = ((rr(a, 2) ^ rr(a, 13) ^ rr(a, 22)) + ((a & b) ^ (a & c) ^ (b & c))) | 0;
        hh = g; g = f; f = e; e = (d + t1) | 0; d = c; c = b; b = a; a = (t1 + t2) | 0;
      }
      h[0] = (h[0] + a) | 0; h[1] = (h[1] + b) | 0; h[2] = (h[2] + c) | 0; h[3] = (h[3] + d) | 0;
      h[4] = (h[4] + e) | 0; h[5] = (h[5] + f) | 0; h[6] = (h[6] + g) | 0; h[7] = (h[7] + hh) | 0;
    }
    return h.map(function (x) { return ("00000000" + (x >>> 0).toString(16)).slice(-8); }).join("");
  };
  /* JSON canonique (clés triées, sans espaces) — identique à scripts/gen_vitrine.py */
  VT.canon = function canon(v) {
    if (Array.isArray(v)) return "[" + v.map(canon).join(",") + "]";
    if (v && typeof v === "object")
      return "{" + Object.keys(v).sort().map(function (k) { return JSON.stringify(k) + ":" + canon(v[k]); }).join(",") + "}";
    return JSON.stringify(v);
  };
  VT.stepHash = function (prev, st) {
    return VT.sha256(prev + VT.canon({ k: st.k, date: st.date, place: st.place, data: st.data }));
  };

  /* ---------- Bouteille SVG ---------- */
  var uid = 0;
  VT.bottle = function (lot, cls) {
    var id = "b" + (uid++), c = lot.color, can = lot.volume === "5 L";
    var label =
      '<text x="60" y="__Y1__" text-anchor="middle" font-family="Georgia,serif" font-size="7" letter-spacing="1.6" fill="#8a6d2a">OLIVETRACE</text>' +
      '<text x="60" y="__Y2__" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="__FS__" fill="#0f1f14"' +
        (lot.name.length > 12 ? ' textLength="58" lengthAdjust="spacingAndGlyphs"' : "") + ">" + VT.esc(lot.name) + "</text>" +
      '<text x="60" y="__Y3__" text-anchor="middle" font-family="Arial,sans-serif" font-size="5" letter-spacing="1.2" fill="#5b6b52">' + VT.esc(lot.category.toUpperCase()) + "</text>" +
      '<path d="M52 __Y4__ q8 -7 16 0" stroke="#c8a24a" stroke-width="1.1" fill="none"/>' +
      '<text x="60" y="__Y5__" text-anchor="middle" font-family="Arial,sans-serif" font-size="5" letter-spacing=".6" fill="#5b6b52">' + VT.esc(lot.variety.toUpperCase()) + " · " + VT.esc(lot.volume) + "</text>" +
      '<text x="60" y="__Y6__" text-anchor="middle" font-family="Arial,sans-serif" font-size="4.2" fill="#8a8f84">' + VT.esc(lot.id) + "</text>";
    var fs = lot.name.length > 12 ? 9 : 10.5;
    if (can) {
      return '<svg class="bottle ' + (cls || "") + '" viewBox="0 0 120 220" xmlns="http://www.w3.org/2000/svg"><defs>' +
        '<linearGradient id="' + id + 'm" x1="0" x2="1"><stop offset="0" stop-color="#5d5a4e"/><stop offset=".25" stop-color="#d9d4c3"/><stop offset=".5" stop-color="#8f8a78"/><stop offset=".8" stop-color="#c9c3af"/><stop offset="1" stop-color="#4f4c42"/></linearGradient>' +
        '<linearGradient id="' + id + 'c" x1="0" x2="1"><stop offset="0" stop-color="' + c + '"/><stop offset=".5" stop-color="' + c + '" stop-opacity=".75"/><stop offset="1" stop-color="' + c + '"/></linearGradient></defs>' +
        '<rect x="70" y="14" width="18" height="16" rx="3" fill="#c8a24a"/><rect x="18" y="26" width="84" height="12" rx="4" fill="url(#' + id + 'm)"/>' +
        '<rect x="14" y="36" width="92" height="176" rx="10" fill="url(#' + id + 'c)"/>' +
        '<rect x="14" y="36" width="92" height="176" rx="10" fill="url(#' + id + 'm)" opacity=".25"/>' +
        '<rect x="22" y="72" width="76" height="104" rx="6" fill="#f8f3e6"/><rect x="25" y="75" width="70" height="98" rx="4" fill="none" stroke="#c8a24a" stroke-width=".6"/>' +
        label.replace("__Y1__", 96).replace("__Y2__", 116).replace("__FS__", fs).replace("__Y3__", 130).replace("__Y4__", 142).replace("__Y5__", 155).replace("__Y6__", 165) +
        "</svg>";
    }
    return '<svg class="bottle ' + (cls || "") + '" viewBox="0 0 120 300" xmlns="http://www.w3.org/2000/svg"><defs>' +
      '<linearGradient id="' + id + 'g" x1="0" x2="1"><stop offset="0" stop-color="#0d1a10"/><stop offset=".18" stop-color="' + c + '"/><stop offset=".42" stop-color="#0f2214"/><stop offset=".78" stop-color="' + c + '" stop-opacity=".85"/><stop offset="1" stop-color="#08120a"/></linearGradient>' +
      '<linearGradient id="' + id + 'h" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>' +
      '<linearGradient id="' + id + 'k" x1="0" x2="1"><stop offset="0" stop-color="#7a5c1c"/><stop offset=".45" stop-color="#ecd28f"/><stop offset="1" stop-color="#8a6a24"/></linearGradient></defs>' +
      '<rect x="46" y="6" width="28" height="34" rx="4" fill="url(#' + id + 'k)"/><rect x="44" y="36" width="32" height="6" rx="2" fill="#9c7b2e"/>' +
      '<path d="M48 42 h24 v34 c0 14 30 22 30 52 v152 a14 14 0 0 1 -14 14 h-56 a14 14 0 0 1 -14 -14 v-152 c0 -30 30 -38 30 -52z" fill="url(#' + id + 'g)"/>' +
      '<rect x="27" y="110" width="7" height="160" rx="3.5" fill="url(#' + id + 'h)" opacity=".45"/>' +
      '<rect x="24" y="150" width="72" height="100" rx="5" fill="#f8f3e6"/><rect x="27" y="153" width="66" height="94" rx="3" fill="none" stroke="#c8a24a" stroke-width=".6"/>' +
      label.replace("__Y1__", 172).replace("__Y2__", 191).replace("__FS__", fs).replace("__Y3__", 204).replace("__Y4__", 215).replace("__Y5__", 229).replace("__Y6__", 239) +
      "</svg>";
  };
  VT.tint = function (lot) {
    var t = { "#4d7c0f": ["#eef2df", "#d9e3bf"], "#166534": ["#e6efe3", "#c9dcc6"], "#a16207": ["#f3ecd9", "#e4d4ae"], "#365314": ["#ecefe0", "#d3dbbd"] };
    var p = t[lot.color] || ["#eef0e2", "#dfe5cc"];
    return "--c1:" + p[0] + ";--c2:" + p[1];
  };
  VT.badges = function (lot) {
    return '<div class="badges">' + (lot.bio ? '<span class="bdg bio">Bio</span>' : "") +
      '<span class="bdg ' + (lot.category === "Extra vierge" ? "ev" : "v") + '">' + lot.category + "</span></div>";
  };

  /* ---------- Panier (localStorage) ---------- */
  var KEY = "olivetrace-cart";
  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function save(c) { try { localStorage.setItem(KEY, JSON.stringify(c)); } catch (e) {} }
  VT.cart = load();
  VT.count = function () { var n = 0; for (var k in VT.cart) n += VT.cart[k]; return n; };
  VT.add = function (id, q) {
    VT.cart[id] = (VT.cart[id] || 0) + (q || 1);
    if (VT.cart[id] <= 0) delete VT.cart[id];
    save(VT.cart); VT.refresh();
    var b = document.querySelector(".vt-cart");
    if (b && q > 0) { b.classList.remove("bump"); void b.offsetWidth; b.classList.add("bump"); }
  };
  VT.toast = function (msg, icon) {
    var t = document.querySelector(".toast");
    if (!t) { t = document.createElement("div"); t.className = "toast"; document.body.appendChild(t); }
    t.innerHTML = "<i>" + (icon || "✓") + "</i>" + msg;
    t.classList.add("on");
    clearTimeout(t._t); t._t = setTimeout(function () { t.classList.remove("on"); }, 2600);
  };

  /* ---------- Header, footer, tiroir panier ---------- */
  VT.header = function (active, dark) {
    var nav = [["boutique.html", "Boutique", "shop"], ["boutique.html#producteurs", "Producteurs", "prod"],
               ["boutique.html#comment", "Comment ça marche", "how"], ["verifier.html", "Vérifier une bouteille", "verify"]];
    return '<header class="vt-head' + (dark ? " dark" : "") + '"><div class="wrap">' +
      '<a class="vt-logo" href="boutique.html"><i><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\"><ellipse cx=\"11\" cy=\"14\" rx=\"6.2\" ry=\"7.6\" transform=\"rotate(-28 11 14)\" fill=\"currentColor\"/><path d=\"M14 7c1.5-3 4-4.5 7-4.5-1 3-3.5 5-7 4.5z\" fill=\"#84a94b\"/></svg></i><span>OliveTrace<small>Huiles de Tunisie · traçables</small></span></a>' +
      '<nav class="vt-nav">' + nav.map(function (n) { return '<a href="' + n[0] + '"' + (n[2] === active ? ' class="on"' : "") + ">" + n[1] + "</a>"; }).join("") + "</nav>" +
      '<div class="vt-actions"><a class="vt-pro" href="index.html">Espace professionnel →</a>' +
      '<button class="vt-cart" onclick="VT.open()" aria-label="Panier"><svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg><b>0</b></button></div>' +
      "</div></header>";
  };
  VT.footer = function () {
    return '<footer class="vt-foot"><div class="wrap"><div class="cols">' +
      '<div><a class="vt-logo" href="boutique.html" style="color:#fff;margin-bottom:16px"><i><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\"><ellipse cx=\"11\" cy=\"14\" rx=\"6.2\" ry=\"7.6\" transform=\"rotate(-28 11 14)\" fill=\"currentColor\"/><path d=\"M14 7c1.5-3 4-4.5 7-4.5-1 3-3.5 5-7 4.5z\" fill=\"#84a94b\"/></svg></i><span>OliveTrace<small>Huiles de Tunisie · traçables</small></span></a>' +
      '<p style="max-width:340px">La première vitrine nationale où chaque bouteille d’huile d’olive tunisienne prouve son origine — de la parcelle à votre table.</p></div>' +
      '<div><h5>Boutique</h5><a href="boutique.html#huiles">Toutes les huiles</a><a href="boutique.html#producteurs">Nos producteurs</a><a href="boutique.html#comment">Comment ça marche</a></div>' +
      '<div><h5>Confiance</h5><a href="verifier.html">Vérifier une bouteille</a><a href="blockchain.html">Registre blockchain</a><a href="certifications.html">Certifications</a></div>' +
      '<div><h5>Professionnels</h5><a href="index.html">Espace filière</a><a href="tracabilite.html">Traçabilité B2B</a><a href="../index.html">Hub TNtrace</a></div>' +
      '</div><div class="legal"><span>© 2026 OliveTrace · TNtrace — Démonstration</span><span>Paiement sécurisé · Livraison Tunisie & UE</span></div></div></footer>';
  };

  function shell() {
    var d = document.createElement("div");
    d.innerHTML =
      '<div class="veil" onclick="VT.close()"></div>' +
      '<aside class="drawer" aria-label="Panier"><div class="dr-head"><h3>Votre panier</h3><button class="x" onclick="VT.close()">✕</button></div>' +
      '<div class="dr-body" id="vt-items"></div><div class="dr-foot" id="vt-sum"></div></aside>' +
      '<div class="modal" id="vt-modal" onclick="if(event.target===this)VT.closeModal()"><div class="modal-box" id="vt-mbox"></div></div>';
    while (d.firstChild) document.body.appendChild(d.firstChild);
  }
  VT.open = function () {
    document.querySelector(".veil").classList.add("on");
    document.querySelector(".drawer").classList.add("on");
  };
  VT.close = function () {
    document.querySelector(".veil").classList.remove("on");
    document.querySelector(".drawer").classList.remove("on");
  };
  VT.totals = function () {
    var sub = 0;
    for (var k in VT.cart) sub += VT.lot(k).price * VT.cart[k];
    var ship = sub === 0 || sub >= 150 ? 0 : 8;
    return { sub: sub, ship: ship, tot: sub + ship };
  };
  VT.refresh = function () {
    var n = VT.count(), badge = document.querySelector(".vt-cart b");
    if (badge) { badge.textContent = n; badge.classList.toggle("on", n > 0); }
    var box = document.getElementById("vt-items"), sum = document.getElementById("vt-sum");
    if (!box) return;
    var ids = Object.keys(VT.cart);
    if (!ids.length) {
      box.innerHTML = '<div class="empty"><div style="width:64px;height:64px;margin:0 auto;border-radius:50%;display:grid;place-items:center;background:var(--cream);color:var(--olive)"><svg width=\"18\" height=\"18\" viewBox=\"0 0 24 24\" fill=\"none\"><ellipse cx=\"11\" cy=\"14\" rx=\"6.2\" ry=\"7.6\" transform=\"rotate(-28 11 14)\" fill=\"currentColor\"/><path d=\"M14 7c1.5-3 4-4.5 7-4.5-1 3-3.5 5-7 4.5z\" fill=\"#84a94b\"/></svg></div><b>Votre panier est vide</b>Chaque huile est tracée de la parcelle à la bouteille.<br><br><a class="btn btn-ink btn-sm" href="boutique.html#huiles" onclick="VT.close()">Découvrir les huiles</a></div>';
      sum.innerHTML = ""; return;
    }
    box.innerHTML = ids.map(function (id) {
      var l = VT.lot(id), q = VT.cart[id];
      return '<div class="ci"><div class="th" style="' + VT.tint(l) + '">' + VT.bottle(l) + "</div>" +
        "<div><h4>" + VT.esc(l.name) + "</h4><small>" + l.category + " · " + l.volume + " · " + l.id + "</small><br>" +
        '<div class="qty"><button onclick="VT.add(\'' + id + '\',-1)">−</button><span>' + q + '</span><button onclick="VT.add(\'' + id + "',1)\">+</button></div></div>" +
        '<div class="pr">' + (l.price * q) + ' TND<a href="verifier.html?lot=' + id + '">Voir le voyage →</a></div></div>';
    }).join("");
    var t = VT.totals();
    sum.innerHTML = '<div class="row"><span>Sous-total</span><span>' + t.sub + ' TND</span></div>' +
      '<div class="row"><span>Livraison</span><span>' + (t.ship ? t.ship + " TND" : "Offerte") + "</span></div>" +
      (t.ship ? '<div class="row" style="font-size:12px"><span>Livraison offerte dès 150 TND</span><span></span></div>' : "") +
      '<div class="row tot"><span>Total</span><span>' + t.tot + ' TND</span></div>' +
      '<button class="btn btn-gold" style="width:100%" onclick="VT.checkout()">Commander · ' + t.tot + " TND</button>" +
      '<p style="font-size:11.5px;color:var(--muted);text-align:center;margin-top:12px">🔒 Chaque bouteille livrée porte un QR unique vérifiable</p>';
  };

  VT.openModal = function (html) {
    document.getElementById("vt-mbox").innerHTML = html;
    document.getElementById("vt-modal").classList.add("on");
  };
  VT.closeModal = function () { document.getElementById("vt-modal").classList.remove("on"); };
  VT.checkout = function () {
    VT.close();
    var t = VT.totals();
    VT.openModal(
      '<div style="display:flex;justify-content:space-between;align-items:flex-start"><div><span class="eyebrow">Paiement sécurisé</span><h3>Finaliser la commande</h3></div><button class="x" onclick="VT.closeModal()">✕</button></div>' +
      '<div class="f2"><label class="field"><span>Prénom & nom</span><input value="Amira Ben Youssef"></label><label class="field"><span>Téléphone</span><input value="+216 22 345 678"></label></div>' +
      '<label class="field"><span>Adresse de livraison</span><input value="12 rue de Carthage, La Marsa 2070"></label>' +
      '<div class="field"><span>Moyen de paiement</span><div class="pay">' +
      '<input type="radio" name="pay" id="p1" checked><label for="p1"><i>💳</i>Carte bancaire</label>' +
      '<input type="radio" name="pay" id="p2"><label for="p2"><i>📱</i>D17 / e-Dinar</label>' +
      '<input type="radio" name="pay" id="p3"><label for="p3"><i>🏠</i>À la livraison</label></div></div>' +
      '<div class="row tot" style="margin-top:22px"><span>Total à payer</span><span>' + t.tot + " TND</span></div>" +
      '<button class="btn btn-gold" style="width:100%" onclick="VT.pay()">Payer ' + t.tot + " TND</button>"
    );
  };
  VT.pay = function () {
    var box = document.getElementById("vt-mbox");
    box.innerHTML = '<div class="success" style="padding:40px 0"><div class="spin"></div><p style="margin-top:18px;color:var(--muted)">Paiement en cours de validation…</p></div>';
    setTimeout(function () {
      var ids = Object.keys(VT.cart), no = "CMD-2026-" + (4100 + Math.floor(Math.random() * 800));
      box.innerHTML = '<div class="success"><div class="ok">✓</div><span class="eyebrow">Commande confirmée</span><h3>Merci, Amira !</h3>' +
        '<p style="color:var(--muted)">Commande <b style="color:var(--ink)">' + no + "</b> · livraison estimée sous 48 h</p>" +
        "<ul>" + ids.map(function (id) {
          var l = VT.lot(id);
          return "<li><span>" + VT.cart[id] + " × " + VT.esc(l.name) + ' <small style="color:var(--muted)">' + l.id + '</small></span><a href="verifier.html?lot=' + id + '">Voyage & preuve →</a></li>';
        }).join("") + "</ul>" +
        '<p style="font-size:12.5px;color:var(--muted);margin-bottom:20px">Chaque bouteille est rattachée à son lot scellé sur la blockchain. Scannez son QR à réception pour vérifier son authenticité.</p>' +
        '<button class="btn btn-ink" style="width:100%" onclick="VT.closeModal()">Continuer mes achats</button></div>';
      VT.cart = {}; save(VT.cart); VT.refresh();
    }, 1400);
  };

  VT.reveal = function () {
    var els = document.querySelectorAll(".rv");
    if (!("IntersectionObserver" in window)) { els.forEach(function (e) { e.classList.add("in"); }); return; }
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); } });
    }, { threshold: 0.12 });
    els.forEach(function (e) { io.observe(e); });
  };

  VT.boot = function (active, dark) {
    var h = document.getElementById("vt-header");
    if (h) h.outerHTML = VT.header(active, dark);
    var f = document.getElementById("vt-footer");
    if (f) f.outerHTML = VT.footer();
    shell(); VT.refresh(); VT.reveal();
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") { VT.close(); VT.closeModal(); } });
  };

  var st = document.createElement("style");
  st.textContent = ".spin{width:46px;height:46px;margin:0 auto;border-radius:50%;border:3px solid var(--line);border-top-color:var(--olive);animation:spin .8s linear infinite}@keyframes spin{to{transform:rotate(360deg)}}";
  document.head.appendChild(st);
})();
