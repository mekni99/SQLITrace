// capture.mjs — Capture automatique des écrans TNtrace via SingleFile CLI.
//
// Principe :
//   1. Lance Edge/Chrome avec --remote-debugging-port=9222 et un profil dédié
//      (une seule connexion manuelle, les cookies persistent).
//   2. Se connecte via CDP, lit les liens <a href> de la sidebar.
//   3. Pour chaque route, appelle single-file-node.js -> export self-contained
//      directement dans pages/<produit>/<slug>.html
//
// Usage :
//   node scripts/capture.mjs <produit>            ex: node scripts/capture.mjs aquatrace
//   node scripts/capture.mjs <produit> --variants tente aussi les formulaires
//
// Produits connus : aquatrace, machine, olivetrace, datetrace, conservetrace,
// berrytrace, milktrace, medtrace, waterjuicetrace, energy, tnsupply,
// tnfleet, tnfret — ou une URL complète en 1er argument.

import { chromium } from "playwright";
import { spawn, execFile } from "node:child_process";
import { existsSync, mkdirSync, statSync } from "node:fs";
import path from "node:path";
import readline from "node:readline";
import { fileURLToPath } from "node:url";
import { promisify } from "node:util";

const execFileP = promisify(execFile);
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const SINGLE_FILE = path.join(ROOT, "scripts", "sf.mjs");
const CDP_HTTP = "http://127.0.0.1:9222";
const WANT_BROWSER = (process.env.BROWSER || "chrome").toLowerCase();
const PROFILE_DIR = path.join(ROOT, `capture-profile-${WANT_BROWSER}`);

const BROWSERS = [
  WANT_BROWSER === "edge"
    ? "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    : "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  WANT_BROWSER === "edge"
    ? "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe"
    : "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
  process.env.BROWSER_PATH,
].filter(Boolean);

const arg = process.argv[2];
if (!arg) {
  console.error("Usage: node scripts/capture.mjs <produit|url> [--variants]");
  process.exit(1);
}
const WITH_VARIANTS = process.argv.includes("--variants");

const SUBDOMAIN_MAP = {
  datetrace: "date", olivetrace: "olivetrace", aquatrace: "aquatrace",
  machine: "machine", conservetrace: "conservetrace", berrytrace: "berrytrace",
  milktrace: "milktrace", medtrace: "medtrace",
  waterjuicetrace: "waterjuicetrace", energy: "energy", tnsupply: "tnsupply",
  tnfleet: "tnfleet", tnfret: "tnfret",
};
const baseUrl = arg.startsWith("http")
  ? arg
  : `https://${SUBDOMAIN_MAP[arg] || arg}.tntrace.tn/`;
const product = arg.startsWith("http")
  ? new URL(baseUrl).hostname.split(".")[0]
  : arg;
const outDir = path.join(ROOT, "pages", product);
mkdirSync(outDir, { recursive: true });

// ---------------------------------------------------------------------------
// 1) Navigateur avec debug CDP
// ---------------------------------------------------------------------------
async function cdpAlive() {
  try {
    const r = await fetch(CDP_HTTP + "/json/version");
    return r.ok;
  } catch { return false; }
}

async function ensureBrowser() {
  if (await cdpAlive()) {
    console.log("Navigateur CDP déjà actif sur :9222 — réutilisé.");
    return;
  }
  const exe = BROWSERS.find(existsSync);
  if (!exe) {
    console.error("Edge/Chrome introuvable. Définis EDGE_PATH.");
    process.exit(1);
  }
  console.log(`Lancement de ${path.basename(exe)} (profil: ${PROFILE_DIR})`);
  spawn(exe, [
    "--remote-debugging-port=9222",
    `--user-data-dir=${PROFILE_DIR}`,
    "--no-first-run",
    "--no-default-browser-check",
    baseUrl,
  ], { detached: true, stdio: "ignore" }).unref();
  for (let i = 0; i < 40; i++) {
    await new Promise(r => setTimeout(r, 500));
    if (await cdpAlive()) return;
  }
  console.error("Le navigateur n'a pas démarré en debug.");
  process.exit(1);
}

function waitEnter(msg) {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  return new Promise(res => rl.question(msg + " [Entrée pour continuer] ", () => { rl.close(); res(); }));
}

// ---------------------------------------------------------------------------
// 2) Connexion Playwright via CDP + lecture du menu
// ---------------------------------------------------------------------------
async function getPage(browser) {
  const ctx = browser.contexts()[0] || await browser.newContext();
  return ctx.pages()[0] || await ctx.newPage();
}

async function collectRoutes(page) {
  return await page.evaluate(() => {
    const origin = location.origin;
    // Tous les liens same-origin (sidebar + éventuels liens de détail dans le contenu)
    const links = [...document.querySelectorAll("a[href]")];
    const seen = new Set();
    const routes = [];
    for (const a of links) {
      const href = a.getAttribute("href") || "";
      if (href.startsWith("#") || href.startsWith("javascript:")) continue;
      try {
        const u = new URL(href, origin);
        if (u.origin !== origin) continue;
        const key = u.pathname.replace(/\/+$/, "") || "/";
        if (!seen.has(key)) { seen.add(key); routes.push(u.href); }
      } catch {}
    }
    return routes;
  });
}

// ---------------------------------------------------------------------------
// 3) Sauvegarde SingleFile
// ---------------------------------------------------------------------------
async function savePage(url, filename) {
  const out = path.join(outDir, filename);
  const args = [
    SINGLE_FILE, url, out,
    "--browser-server", CDP_HTTP,
    "--browser-wait-until", "networkIdle",
    "--browser-wait-until-delay", "800",
    "--filename-conflict-action", "overwrite",
  ];
  try {
    await execFileP("node", args, { timeout: 120000, maxBuffer: 10 * 1024 * 1024 });
    return existsSync(out) && statSync(out).size > 20000;
  } catch (e) {
    console.log(`   ! échec ${url} : ${String(e.message).slice(0, 120)}`);
    return false;
  }
}

function slugOf(url) {
  const p = new URL(url).pathname.replace(/\/+$/, "");
  const seg = p.split("/").filter(Boolean);
  if (seg[0] === "app") seg.shift();
  if (!seg.length || seg[seg.length - 1] === "dashboard") return "index.html";
  return seg.join("-") + ".html";
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------
await ensureBrowser();
const browser = await chromium.connectOverCDP(CDP_HTTP);
let page = await getPage(browser);

console.log(`Ouverture de ${baseUrl}`);
// Réutilise l'onglet déjà ouvert par le navigateur s'il pointe déjà dessus,
// sinon navigue (waitUntil souple : les SPA mettent du temps à répondre).
const pages = browser.contexts()[0]?.pages() || [];
page = pages.find(p => p.url().includes("tntrace.tn")) || pages[0] || page;
if (!page.url().includes(new URL(baseUrl).hostname)) {
  await page.goto(baseUrl, { waitUntil: "commit", timeout: 90000 }).catch(() => {});
}
await page.waitForTimeout(4000);

// Flux login automatique : bouton « Connexion » -> « Se connecter » (champs
// pré-remplis par l'app) -> attente de l'arrivée sur /app/*
async function ensureLoggedIn() {
  for (let attempt = 0; attempt < 3; attempt++) {
    const url = page.url();
    if (url.includes("/app/")) return true;
    // Certains produits (machine) n'ont pas de préfixe /app :
    // connecté = bouton « Déconnexion » présent et pas de formulaire login.
    const logoutBtn = page.locator('button:has-text("Déconnexion"), button:has-text("Logout"), button:has-text("Se déconnecter")').first();
    const loginForm = page.locator('input[type=password], input[type=email]').first();
    if ((await logoutBtn.count()) && !(await loginForm.count())) return true;
    // page d'accueil avec bouton Connexion ?
    const conn = page.locator('button:has-text("Connexion"), a:has-text("Connexion"), button:has-text("Login"), a:has-text("Login")').first();
    if (await conn.count()) {
      await conn.click().catch(() => {});
      await page.waitForTimeout(2000);
    }
    // formulaire de login ?
    const submit = page.locator('button:has-text("Se connecter"), button:has-text("Sign in"), button[type=submit]').first();
    if (await submit.count()) {
      await submit.click().catch(() => {});
      await page.waitForTimeout(4000);
      continue;
    }
    break;
  }
  return page.url().includes("/app/");
}

if (!(await ensureLoggedIn())) {
  console.log("\n>>> CONNECTE-TOI dans le navigateur qui vient de s'ouvrir.");
  console.log(">>> Une fois connecté (dashboard visible), la capture reprend seule.");
  // Poll l'URL jusqu'à arriver sur /app/* (max 10 min) — pas besoin d'Entrée.
  for (let i = 0; i < 300; i++) {
    await new Promise(r => setTimeout(r, 2000));
    if (page.url().includes("/app/") || (await ensureLoggedIn())) break;
    if (i === 150) console.log(">>> Toujours en attente de connexion…");
  }
  await ensureLoggedIn();
}

// Déplie les éventuels menus « Plus / More » pour révéler tous les liens
for (const label of ["Plus", "More", "Autres"]) {
  const more = page.locator(`button:has-text("${label}"), a:has-text("${label}")`).first();
  if (await more.count()) {
    await more.click().catch(() => {});
    await page.waitForTimeout(800);
  }
}
const routes = await collectRoutes(page);
console.log(`\n${routes.length} routes détectées — capture en cours...`);

let ok = 0, fail = 0;
for (const u of routes) {
  const name = slugOf(u);
  process.stdout.write(`  capture ${name} ... `);
  const good = await savePage(u, name);
  console.log(good ? "OK" : "ÉCHEC");
  good ? ok++ : fail++;
}

console.log(`\nTerminé : ${ok} capturées, ${fail} échecs -> ${outDir}`);
if (WITH_VARIANTS) {
  console.log("(--variants : non encore automatisé pour ce produit — fais-le à la main)");
}
await browser.close();
process.exit(0);
