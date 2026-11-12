// click-row.js — injecté par single-file (--browser-script).
// Clique la première ligne cliquable du tableau (détail machine/ligne)
// pour capturer la vue détaillée expandée dans le DOM.
(function () {
  var tries = 0;
  var timer = setInterval(function () {
    tries++;
    if (tries > 60) { clearInterval(timer); return; }
    try {
      var row = document.querySelector(
        "main tr.cursor-pointer, [role=main] tr.cursor-pointer, tr.cursor-pointer, [class*=cursor-pointer]"
      );
      if (!row) return;
      clearInterval(timer);
      row.scrollIntoView({ block: "center" });
      row.click();
    } catch (e) { /* réessaie */ }
  }, 500);
})();
