// capture-variants.mjs — Capture les formulaires/modales d'un produit TNtrace.
//
// Pour chaque page déjà capturée dans pages/<produit>/ :
//   - relit l'URL d'origine (commentaire `url:` SingleFile),
//   - relance single-file-cli sur cette URL avec --browser-script
//     click-create.js : le script poll dans la page live, clique le bouton
//     « + Nouveau… » automatiquement, et SingleFile capture le DOM AVEC la
//     modale/formulaire ouvert -> <page>--form.html
//
// Usage : node scripts/capture-variants.mjs aquatrace
// Prérequis : Chrome CDP actif sur :9222 avec session connectée
// (capture-profile-chrome — le même que capture.mjs).

import { execFile } from "node:child_process";
import { readdirSync, readFileSync, existsSync, statSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { promisify } from "node:util";

const execFileP = promisify(execFile);
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const SINGLE_FILE = path.join(ROOT, "scripts", "sf.mjs");
const CLICK_JS = path.join(ROOT, "scripts", "click-create.js");
const CDP_HTTP = "http://127.0.0.1:9222";

const product = process.argv[2];
if (!product) {
  console.error("Usage: node scripts/capture-variants.mjs <produit>");
  process.exit(1);
}
const pagesDir = path.join(ROOT, "pages", product);
if (!existsSync(pagesDir)) {
  console.error(`Dossier introuvable : ${pagesDir}`);
  process.exit(1);
}

function urlOf(file) {
  const head = readFileSync(file, "utf8").slice(0, 3000);
  const m = head.match(/url:\s*(https?:\/\/\S+)/);
  return m ? m[1] : null;
}

// Marqueurs de formulaire/modale — comparés entre base et variante.
const FORM_MARK_RE = /enregistrer|créer|creer|valider|soumettre|annuler|<form|role="dialog"|fixed inset-0/i;
function formScore(html) {
  const m = html.match(new RegExp(FORM_MARK_RE.source, "gi"));
  return m ? m.length : 0;
}

async function capture(url, out, baseHtml) {
  const args = [
    SINGLE_FILE, url, out,
    "--browser-server", CDP_HTTP,
    "--browser-wait-until", "networkIdle",
    // laisse le temps à click-create.js de trouver et cliquer le bouton,
    // puis au formulaire de se rendre avant la capture
    "--browser-wait-until-delay", "5000",
    "--browser-wait-end-delay", "1200",
    "--browser-script", CLICK_JS,
    "--filename-conflict-action", "overwrite",
  ];
  try {
    await execFileP("node", args, { timeout: 180000, maxBuffer: 10 * 1024 * 1024 });
  } catch (e) {
    return { ok: false, err: String(e.message).slice(0, 100) };
  }
  if (!existsSync(out) || statSync(out).size < 5000) return { ok: false, err: "fichier absent/trop petit" };
  const html = readFileSync(out, "utf8");
  const size = statSync(out).size;
  // La variante est valide si le score formulaire a augmenté par rapport
  // à la page de base (modale/champs ajoutés dans le DOM capturé).
  const delta = formScore(html) - formScore(baseHtml);
  return { ok: true, size, delta };
}

const files = readdirSync(pagesDir)
  .filter(f => f.endsWith(".html") && !f.includes("--"))
  .sort();
console.log(`${files.length} pages à traiter pour « ${product} »\n`);

let done = 0, skipped = 0, failed = 0;
for (const f of files) {
  const src = path.join(pagesDir, f);
  const url = urlOf(src);
  if (!url) { console.log(`  ${f} : pas d'URL -> ignoré`); skipped++; continue; }

  const slug = f.replace(/\.html$/, "");
  const out = path.join(pagesDir, `${slug}--form.html`);
  if (existsSync(out)) { console.log(`  ${f} : variante déjà présente -> ignoré`); skipped++; continue; }

  const baseHtml = readFileSync(src, "utf8");
  process.stdout.write(`  ${f} ... `);
  const r = await capture(url, out, baseHtml);
  if (!r.ok) {
    console.log(`ÉCHEC (${r.err})`);
    failed++;
    continue;
  }
  // La variante doit avoir PLUS de marqueurs de formulaire que la base —
  // sinon le clic n'a rien ouvert (page sans formulaire).
  if (r.delta > 0) {
    console.log(`OK (+${r.delta} marqueurs, ${(r.size / 1024).toFixed(0)} Ko)`);
    done++;
  } else {
    console.log(`aucun formulaire détecté (delta ${r.delta}, ${(r.size / 1024).toFixed(0)} Ko)`);
    const { unlinkSync } = await import("node:fs");
    try { unlinkSync(out); } catch {}
    skipped++;
  }
}

console.log(`\nTerminé : ${done} variantes capturées, ${skipped} sans formulaire, ${failed} échecs`);
process.exit(0);
