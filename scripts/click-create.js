// click-create.js — injecté par single-file (--browser-script) dans chaque
// page avant capture. Poll jusqu'au montage React, clique le bouton « +
// Nouveau… » principal (hors sidebar), la modale reste ouverte à la capture.
(function () {
  var CREATE_RE =
    /nouveau|nouvelle|nouvel\b|ajouter|new\b|add\b|créer|creer|create|enregistrer|déclarer|declarer|signaler|planifier|importer|lancer|ouvrir/i;
  var EXCLUDE_RE =
    /actualiser|refresh|déconnexion|logout|log out|se déconnecter|export|télécharg|filtrer|rechercher|search|voir\b|view\b|détail|detail|éditer|edit|supprimer|delete|fermer|close|annuler|cancel|précédent|suivant|envoyer|send|imprimer|print|partager|share|marquer|lire|read|tout\b|all\b|aide|help/i;

  var tries = 0;
  var timer = setInterval(function () {
    tries++;
    if (tries > 80) { clearInterval(timer); return; } // ~40 s max
    try {
      var btns = Array.prototype.slice
        .call(document.querySelectorAll("main button, main a, [role=main] button, [role=main] a"))
        .filter(function (b) {
          if (b.closest("aside, nav")) return false;
          var label = (b.textContent || "").trim();
          if (!label || label.length > 60) return false;
          return CREATE_RE.test(label) && !EXCLUDE_RE.test(label);
        });
      // Repli : tous les boutons de la page hors sidebar
      if (!btns.length) {
        btns = Array.prototype.slice
          .call(document.querySelectorAll("button"))
          .filter(function (b) {
            if (b.closest("aside, nav")) return false;
            var label = (b.textContent || "").trim();
            return label && label.length <= 60 && CREATE_RE.test(label) && !EXCLUDE_RE.test(label);
          });
      }
      if (!btns.length) return; // réessaie au prochain tick
      clearInterval(timer);
      btns.sort(function (a, b) {
        var ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
        // priorise le haut de page, puis la droite
        var dy = ra.top - rb.top;
        return Math.abs(dy) > 60 ? dy : (rb.x + rb.width) - (ra.x + ra.width);
      });
      var t = btns[0];
      t.scrollIntoView({ block: "center" });
      t.click();
    } catch (e) { /* réessaie */ }
  }, 500);
})();
