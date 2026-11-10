import { readFileSync, writeFileSync, mkdirSync, cpSync, rmSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import assert from "node:assert/strict";

const here = dirname(fileURLToPath(import.meta.url));
const out = join(here, "dist");
const catalog = JSON.parse(readFileSync(join(here, "..", "catalog.json"), "utf8"));
const { repo, site, checked, skills } = catalog;
const gh = `https://github.com/${repo}`;

const VARIETIES = { iran: "Iran", afghanistan: "Afghanistan", tajikistan: "Tajikistan", all: "Every variety" };
const CATEGORIES = { writing: "Writing", localization: "Localization", translation: "Translation", typography: "Typography", documents: "Documents", dates: "Dates", ui: "UI", evals: "Evals", tools: "Tools", domain: "Domain" };
for (const s of skills) {
  assert.ok(s.name && s.author && s.url && s.description && s.license, `incomplete entry: ${s.name}`);
  assert.ok(s.variety in VARIETIES, `bad variety: ${s.name}`);
  assert.ok(s.category in CATEGORIES, `bad category: ${s.name}`);
  assert.ok(!s.here || s.path, `in-repo skill needs a path: ${s.name}`);
  assert.match(s.url, /^https:\/\//, `url must be https: ${s.name}`);
}

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const num = (n) => n.toLocaleString("en-US");

const icon = {
  github: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="currentColor"><path d="M8 0a8 8 0 0 0-2.53 15.59c.4.07.55-.17.55-.38v-1.33c-2.23.48-2.7-1.07-2.7-1.07-.36-.92-.89-1.17-.89-1.17-.73-.5.05-.49.05-.49.8.06 1.23.83 1.23.83.72 1.22 1.88.87 2.33.66.07-.52.28-.87.5-1.07-1.78-.2-3.65-.89-3.65-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 0 1 4 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.66 3.95.29.25.54.73.54 1.48v2.2c0 .21.15.46.55.38A8 8 0 0 0 8 0Z"/></svg>',
  copy: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="5.5" y="5.5" width="8" height="8" rx="1.5"/><path d="M10.5 3.5v-.5A1.5 1.5 0 0 0 9 1.5H3A1.5 1.5 0 0 0 1.5 3v6A1.5 1.5 0 0 0 3 10.5h.5"/></svg>',
};

const title = "Persian Skills: agent skills for Persian, Dari and Tajik";
const description = "Open-source agent skills that make AI write Persian correctly for readers in Iran, Afghanistan and Tajikistan. For Claude Code, Codex, Cursor and any agent that reads SKILL.md.";
const agents = [["claude-code", "Claude Code"], ["codex", "Codex"], ["cursor", "Cursor"], ["gemini", "Gemini CLI"], ["copilot", "GitHub Copilot"], ["windsurf", "Windsurf"], ["opencode", "OpenCode"], ["cline", "Cline"], ["roo", "Roo Code"], ["goose", "Goose"], ["kiro", "Kiro"], ["amp", "Amp"]];

const varieties = [
  { where: "Iran", name: "فارسی", lang: "fa", sample: "دانشجو با اتوبوس به بیمارستان رفت.", values: ["Perso-Arabic, RTL", "toman, rial", "Farvardin", "fa-IR"] },
  { where: "Afghanistan", name: "دری", lang: "fa-AF", sample: "محصل با بس به شفاخانه رفت.", values: ["Perso-Arabic, RTL", "afghani ؋", "Hamal", "fa-AF"] },
  { where: "Tajikistan", name: "Тоҷикӣ", lang: "tg", sample: "Донишҷӯ бо автобус ба беморхона рафт.", values: ["Cyrillic, LTR", "сомонӣ", "январ", "tg"] },
];
const facts = ["Script", "Money", "First month", "Locale"];

const credits = [
  ["ali2000hos/persian-writing", "https://github.com/ali2000hos/persian-writing", "The persian-writing skill is copied unchanged from this repo. Code under MIT, fonts under the SIL OFL."],
  ["Edyt", "https://edyt.app", "The persian-localization rules come from a native speaker's review of Edyt's Persian translation."],
  ["Every author in the list", "#skills", "Each row links to its author's repo. Each skill keeps the license its author chose."],
];
const sources = [
  ["Unicode CLDR", "https://github.com/unicode-org/cldr", "Months, currency, numbers and weekend data for fa-AF and tg."],
  ["Academy of Sciences of Afghanistan", "https://asa.gov.af", "Afghanistan's official language authority."],
  ["Tajikistan's Committee on Language and Terminology", "https://kumitaizabon.tj", "Publisher of the Tajik orthography rules approved on 4 October 2011."],
  ["Persian and Dari vocabulary", "https://journals.openedition.org/abstractairanica/57034", "Review of Newid and Thurmair's comparative Farsi/Dari vocabulary."],
];

const licenseLabel = (l) => (l === "none" ? "None" : l === "see repo" || l === "unclear" ? "See repo" : l);
const source = (s) => s.url.replace(/^https:\/\/github\.com\//, "");
const edyt = readFileSync(join(here, "edyt-mark.svg"), "utf8").trim().replace("<svg ", '<svg class="edyt" aria-hidden="true" ').replaceAll('fill="#141414"', 'fill="currentColor"');

const row = (s, i) => {
  const href = s.here ? `${gh}/tree/main/${s.path}` : s.url;
  const tags = [s.here ? '<span class="tag here">In this repo</span>' : "", s.draft ? '<span class="tag draft">Draft</span>' : "", s.kind === "mcp" ? '<span class="tag">MCP</span>' : ""].join("");
  const text = `${s.name} ${s.author} ${s.description} ${VARIETIES[s.variety]} ${CATEGORIES[s.category]}`.toLowerCase();
  return `<a class="row" href="${esc(href)}" data-variety="${s.variety}" data-text="${esc(text)}" target="_blank" rel="noopener">
  <span class="n">${i + 1}</span>
  <div><b>${esc(s.name)}</b><span class="src">${esc(source(s))}</span>${tags ? `<span class="tags">${tags}</span>` : ""}<p class="desc">${esc(s.description)}</p></div>
  <span class="col">${VARIETIES[s.variety]}</span>
  <span class="col">${esc(licenseLabel(s.license))}</span>
  <span class="stars">${s.stars === undefined ? "" : num(s.stars)}</span>
</a>`;
};

const linkList = (items) =>
  `<ul>${items.map(([name, href, note]) => `<li><a href="${esc(href)}"${href.startsWith("#") ? "" : ' target="_blank" rel="noopener"'}>${esc(name)}</a><span>${esc(note)}</span></li>`).join("")}</ul>`;

const authors = new Set(skills.map((s) => s.author)).size;
const cmd = (text) => `<pre class="cmd"><code>${text.split("\n").map((l) => `<span class="p">$ </span>${esc(l)}`).join("\n")}</code><button class="copy" type="button" aria-label="Copy" data-copy="${esc(text)}">${icon.copy}</button></pre>`;

const page = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title}</title>
<meta name="description" content="${esc(description)}">
<link rel="canonical" href="${site}/">
<meta property="og:title" content="${title}">
<meta property="og:description" content="${esc(description)}">
<meta property="og:url" content="${site}/">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0b0b0a">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/lexend-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="top"><div class="bar">
  <a class="brand" href="/" aria-label="Persian Skills home">${edyt}<span class="slash" aria-hidden="true">/</span>Persian Skills</a>
  <nav class="links" aria-label="Sections">
    <a class="hide-sm" href="#skills">Skills</a><a class="hide-sm" href="#install">Install</a><a class="hide-sm" href="#sources">Sources</a><a class="hide-sm" href="#contribute">Contribute</a><a class="btn solid" href="${gh}" target="_blank" rel="noopener">${icon.github}GitHub</a>
  </nav>
</div></header>

<main class="wrap">
<section class="hero">
  <div>
    <h1 class="wordmark"><span>Persian</span><span>Skills</span></h1>
    <p class="tagline">Agent skills for every Persian reader</p>
    <span class="underline" aria-hidden="true"></span>
  </div>
  <p class="lead">Skills that make AI agents write Persian the way its readers do: <b>Farsi</b> for Iran, <b>Dari</b> for Afghanistan, <b>Tajik</b> in Cyrillic. One command installs them into any agent that reads SKILL.md.</p>
</section>

<section class="grid2" id="install">
  <div>
    <h2 class="label">Install</h2>
    ${cmd(`npx skills add ${repo}`)}
    <div class="more">
      <div><small>One skill</small>${cmd(`npx skills add ${repo} --skill dari-writing`)}</div>
      <div><small>Claude Code plugin</small>${cmd(`/plugin marketplace add ${repo}\n/plugin install persian-skills@persianskills`)}</div>
    </div>
  </div>
  <div>
    <h2 class="label">Works with</h2>
    <div class="agents">${agents.map(([file, name]) => `<span class="agent" title="${name}"><img src="/agents/${file}.svg" alt="${name}" width="32" height="32"></span>`).join("")}</div>
    <p class="note">For ChatGPT, Gemini and other chat apps, upload a skill's SKILL.md as knowledge.</p>
  </div>
</section>

<section class="section">
  <h2 class="label">One language, three standards</h2>
  <div class="varieties">
    ${varieties
      .map(
        (v) => `<article class="variety">
      <div class="where">${v.where}</div>
      <div class="name" lang="${v.lang}" dir="auto">${v.name}</div>
      <p class="sample" lang="${v.lang}" dir="auto">${v.sample}</p>
      <dl>${facts.map((f, i) => `<dt>${f}</dt><dd>${v.values[i]}</dd>`).join("")}</dl>
    </article>`,
      )
      .join("\n    ")}
  </div>
  <p class="note">The same sentence in each: “The student took the bus to the hospital.” Afghans say shafakhana for hospital, and most Tajiks can't read Persian script, so your agent has to know who it is writing for.</p>
</section>

<section class="section" id="skills">
  <h2 class="label">Skills directory</h2>
  <label class="search"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="7" cy="7" r="5"/><path d="m11 11 3.5 3.5"/></svg><input type="search" placeholder="Search skills..." aria-label="Search skills"><kbd>/</kbd></label>
  <div class="tabs" role="group" aria-label="Filter by variety">
    ${Object.entries({ any: `All (${num(skills.length)})`, ...VARIETIES }).map(([k, label], i) => `<button type="button" data-filter="${k}" aria-pressed="${i === 0}">${label}</button>`).join("")}
  </div>
  <div class="thead"><span>#</span><span>Skill</span><span class="col">Variety</span><span class="col">License</span><span class="stars">Stars</span></div>
  <div class="list">
${skills.map(row).join("\n")}
  </div>
  <p class="empty" hidden>No skills match.</p>
  <p class="note">${num(skills.length)} skills and tools from ${num(authors)} authors, checked on ${checked}. Stars are the author's repo stars. The first four live in this repo; the rest install from their authors' repos.</p>
</section>

<section class="section credits" id="sources">
  <div><h2 class="label">Credits</h2>${linkList(credits)}</div>
  <div><h2 class="label">Dari and Tajik sources</h2>${linkList(sources)}</div>
</section>

<section class="section closing" id="contribute">
  <h2>Built a Persian skill?</h2>
  <p>Add a row to catalog.json and open a pull request. Dari, Hazaragi and Tajik skills are the scarcest.</p>
  <div class="btns">
    <a class="btn solid" href="${gh}/edit/main/catalog.json" target="_blank" rel="noopener">Add a skill</a>
    <a class="btn" href="${gh}/issues" target="_blank" rel="noopener">${icon.github}Report a problem</a>
  </div>
</section>
</main>

<footer><div class="wrap">
  <span>Code under MIT · <a href="${gh}" target="_blank" rel="noopener">${repo}</a></span>
  <a href="https://edyt.app" target="_blank" rel="noopener">Made by the team behind Edyt</a>
</div></footer>

<script>
const rows = [...document.querySelectorAll(".row")];
const empty = document.querySelector(".empty");
const input = document.querySelector(".search input");
let variety = "any";
const apply = () => {
  const q = input.value.trim().toLowerCase();
  let shown = 0;
  rows.forEach((r) => {
    const v = r.dataset.variety;
    const fits = variety === "any" || v === variety || (variety !== "all" && v === "all");
    r.hidden = !(fits && (!q || r.dataset.text.includes(q)));
    if (!r.hidden) shown++;
  });
  empty.hidden = shown > 0;
};
input.addEventListener("input", apply);
document.addEventListener("keydown", (e) => { if (e.key === "/" && document.activeElement !== input) { e.preventDefault(); input.focus(); } });
document.querySelectorAll("[data-filter]").forEach((b) => b.addEventListener("click", () => {
  variety = b.dataset.filter;
  document.querySelectorAll("[data-filter]").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
  apply();
}));
document.querySelectorAll(".copy").forEach((b) => b.addEventListener("click", async () => {
  try { await navigator.clipboard.writeText(b.dataset.copy); b.setAttribute("aria-label", "Copied"); b.style.color = "var(--ok)"; } catch {}
}));
</script>
</body>
</html>
`;

rmSync(out, { recursive: true, force: true });
mkdirSync(out, { recursive: true });
writeFileSync(join(out, "index.html"), page);
for (const f of ["style.css", "favicon.svg"]) cpSync(join(here, f), join(out, f));
for (const d of ["fonts", "agents"]) cpSync(join(here, d), join(out, d), { recursive: true });
writeFileSync(join(out, "robots.txt"), `User-agent: *\nAllow: /\nSitemap: ${site}/sitemap.xml\n`);
writeFileSync(
  join(out, "sitemap.xml"),
  `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<url><loc>${site}/</loc><lastmod>${checked}</lastmod></url>\n</urlset>\n`,
);
console.log(`built ${skills.length} skills into ${out}`);
