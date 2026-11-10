import { readFileSync, readdirSync, writeFileSync, mkdirSync, cpSync, rmSync } from "node:fs";
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
  terminal: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="m3 4.5 3.5 3.5L3 11.5M8.5 12h4.5"/></svg>',
  copy: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="5.5" y="5.5" width="8" height="8" rx="1.5"/><path d="M10.5 3.5v-.5A1.5 1.5 0 0 0 9 1.5H3A1.5 1.5 0 0 0 1.5 3v6A1.5 1.5 0 0 0 3 10.5h.5"/></svg>',
};

const title = "Persian Skills: agent skills for Persian, Dari and Tajik";
const description = "Open-source agent skills that make AI write Persian correctly for readers in Iran, Afghanistan and Tajikistan. For Claude Code, Codex, Cursor and any agent that reads SKILL.md.";
const agents = [["claude-code", "Claude Code"], ["codex", "Codex"], ["cursor", "Cursor"], ["gemini", "Gemini CLI"], ["copilot", "GitHub Copilot"], ["windsurf", "Windsurf"], ["opencode", "OpenCode"], ["cline", "Cline"], ["roo", "Roo Code"], ["goose", "Goose"], ["kiro", "Kiro"], ["amp", "Amp"]];

const varieties = [
  { where: "Iran", code: "fa-IR", dir: "rtl", lang: "fa", title: "Farsi in Iran", sample: "<mark>دانشجو</mark> با <mark>اتوبوس</mark> به <mark>بیمارستان</mark> رفت.", desc: "Perso-Arabic, right to left. Prices in tomans, and the year starts in Farvardin." },
  { where: "Afghanistan", code: "fa-AF", dir: "rtl", lang: "fa-AF", title: "Dari in Afghanistan", sample: "<mark>محصل</mark> با <mark>بس</mark> به <mark>شفاخانه</mark> رفت.", desc: "Same script, different words. Prices in afghani (؋), and the year starts in Hamal." },
  { where: "Tajikistan", code: "tg", dir: "ltr", lang: "tg", title: "Tajik in Tajikistan", sample: "<mark>Донишҷӯ</mark> бо <mark>автобус</mark> ба <mark>беморхона</mark> рафт.", desc: "Cyrillic, left to right. Prices in somoni, and dates follow the Gregorian calendar." },
];

const credits = [
  ["Every author in the list", `${gh}/blob/main/CREDITS.md`, "Each copied skill keeps its author's license file. CREDITS.md lists the source repo, commit and every change we made, such as the switch to the Sahel font."],
  ["Edyt", "https://edyt.app", "The persian-localization rules come from a native speaker's review of Edyt's Persian translation."],
  ["Sahel font", "https://github.com/rastikerdar/sahel-font", "Every skill that bundles or recommends a Persian font uses Sahel by Saber Rastikerdar (SIL OFL)."],
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
  const tags = [s.author === "persianskills" ? '<span class="tag here">Original</span>' : "", s.here ? "" : '<span class="tag">Link only</span>', s.draft ? '<span class="tag draft">Draft</span>' : "", s.kind === "mcp" ? '<span class="tag">MCP</span>' : ""].join("");
  const text = `${s.name} ${s.author} ${s.description} ${VARIETIES[s.variety]} ${CATEGORIES[s.category]}`.toLowerCase();
  return `<a class="row" href="${esc(href)}" data-variety="${s.variety}" data-text="${esc(text)}" target="_blank" rel="noopener">
  <span class="n">${i + 1}</span>
  <div><b>${esc(s.name)}</b><span class="src">${esc(source(s))}</span>${tags ? `<span class="tags">${tags}</span>` : ""}<p class="desc">${esc(s.description)}</p></div>
  <span class="col"><span class="tag">${VARIETIES[s.variety]}</span></span>
  <span class="col">${esc(licenseLabel(s.license))}</span>
</a>`;
};

const linkList = (items) =>
  `<ul>${items.map(([name, href, note]) => `<li><a href="${esc(href)}"${href.startsWith("#") ? "" : ' target="_blank" rel="noopener"'}>${esc(name)}</a><span>${esc(note)}</span></li>`).join("")}</ul>`;

const cmd = (comment, text) => `<div class="cmd"><pre><code><span class="c"># ${esc(comment)}</span>\n${esc(text)}</code></pre><button class="copy" type="button" aria-label="Copy" data-copy="${esc(text)}">${icon.copy}</button></div>`;

const skillFiles = readdirSync(join(here, "..", "skills"), { recursive: true }).filter((f) => f.endsWith("SKILL.md")).length;
const skillAuthors = new Set(skills.filter((s) => s.here && s.author !== "persianskills").map((s) => s.author)).size;
const ownSkills = skills.filter((s) => s.here && s.author === "persianskills").length;
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
<meta name="theme-color" content="#eda220">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/lexend-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="top"><div class="bar">
  <a class="brand" href="/" aria-label="Persian Skills home">${edyt}<span class="brand-name"><span class="slash" aria-hidden="true">/</span>Persian Skills</span></a>
  <nav class="links" aria-label="Sections">
    <a href="#skills">Skills</a><a href="#install">Install</a><a href="#agents">Agents</a><a href="#sources">Credits</a><a href="#contribute">Contribute</a>
  </nav>
  <div class="top-actions">
    <a class="btn hide-sm" href="${gh}" target="_blank" rel="noopener">${icon.github}GitHub</a>
    <a class="btn fill" href="#install">${icon.terminal}Install</a>
  </div>
</div></header>

<main>
<section class="hero">
  <div class="wrap">
    <h1>Persian Skills</h1>
    <p class="sub">Agent skills that write Persian the way its readers do.</p>
    <div class="install"><code><span class="p">$ </span>npx skills add ${repo}</code><button class="copy" type="button" aria-label="Copy" data-copy="npx skills add ${repo}">${icon.copy}</button></div>
  </div>
  <div class="wrap" id="varieties">
    <p class="hero-label">One sentence, three standards</p>
    <div class="cards">
    ${varieties
      .map(
        (v, i) => `<article class="card">
      <div class="art"><div class="mini"><div class="mini-top"><span>${v.where}</span><code>${v.code}</code></div><p lang="${v.lang}" dir="${v.dir}">${v.sample}</p></div></div>
      <div class="num">0${i + 1}</div>
      <h3>${v.title}</h3>
      <p>${v.desc}</p>
    </article>`,
      )
      .join("\n    ")}
  </div>
  </div>
</section>

<section class="section wrap" id="skills">
  <h2>Every Persian skill, in one repo.</h2>
  <p class="lede">${num(skillFiles - ownSkills)} skills from ${num(skillAuthors)} authors, copied with their licenses and credit, plus ${num(ownSkills)} of our own, all about the Persian language and written to one standard. Entries marked Link only stay in their authors' repos: they can't be copied, overlap a skill here, or aren't about the language.</p>
  <div class="db">
    <div class="db-head">
      <div class="db-title"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M9 10v10"/></svg>Skills directory</div>
      <div class="tools">
        <div class="tabs" role="group" aria-label="Filter by variety">
          ${Object.entries({ any: `All (${num(skills.length)})`, ...VARIETIES }).map(([k, label], i) => `<button type="button" data-filter="${k}" aria-pressed="${i === 0}">${label}</button>`).join("")}
        </div>
        <label class="search"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="7" cy="7" r="5"/><path d="m11 11 3.5 3.5"/></svg><input type="search" placeholder="Search skills" aria-label="Search skills"><kbd>/</kbd></label>
      </div>
    </div>
    <div class="thead"><span class="n">#</span><span>Skill</span><span class="col">Variety</span><span class="col">License</span></div>
    <div class="list">
${skills.map(row).join("\n")}
    </div>
    <p class="empty" hidden>No skills match.</p>
  </div>
  <p class="note">Checked on ${checked}.</p>
</section>

<section class="section wrap" id="install">
  <div class="frame">
    <h2>Install it your way.</h2>
    <p class="lede">The skills CLI finds the agents on your machine and puts each skill where that agent looks for it.</p>
    <div class="code">
      <div class="file"><span>terminal</span><a href="${gh}" target="_blank" rel="noopener">${icon.github}See the repo</a></div>
      <div class="cmds">
        ${cmd("every skill, pick from the list", `npx skills add ${repo}`)}
        ${cmd("one skill", `npx skills add ${repo} --skill dari-writing`)}
        ${cmd("Claude Code plugin, run inside Claude Code", `/plugin marketplace add ${repo}\n/plugin install persian-skills@persianskills`)}
      </div>
      <div class="status"><b>›</b> npx skills add ${repo}<span>For ChatGPT, Gemini and other chat apps, upload a skill's SKILL.md as knowledge.</span></div>
    </div>
  </div>
</section>

<section class="section wrap" id="agents">
  <h2>Works with the agents you use.</h2>
  <p class="lede">Any agent that reads SKILL.md files can load these skills.</p>
  <div class="logos">${agents.map(([file, name]) => `<div class="logo"><img src="/agents/${file}.svg" alt="" width="30" height="30"><span>${name}</span></div>`).join("")}</div>
</section>

<section class="section wrap" id="sources">
  <div class="frame">
    <h2>Credit where it's due.</h2>
    <div class="credits">
      <div><h3>Credits</h3>${linkList(credits)}</div>
      <div><h3>Dari and Tajik sources</h3>${linkList(sources)}</div>
    </div>
  </div>
</section>

<section class="closing wrap" id="contribute">
  <span class="underline" aria-hidden="true"></span>
  <h2>Built a Persian skill?</h2>
  <p class="lede">Add a row to catalog.json and open a pull request. Dari, Hazaragi and Tajik skills are the scarcest.</p>
  <div class="btns">
    <a class="btn fill blue" href="${gh}/edit/main/catalog.json" target="_blank" rel="noopener">Add a skill</a>
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
const header = document.querySelector("header.top");
new IntersectionObserver(([e]) => header.classList.toggle("solid", !e.isIntersecting), { rootMargin: "-68px 0px 0px 0px" }).observe(document.querySelector(".hero .wrap"));
new IntersectionObserver(([e]) => header.classList.toggle("named", !e.isIntersecting), { rootMargin: "-68px 0px 0px 0px" }).observe(document.querySelector(".hero h1"));
document.addEventListener("keydown", (e) => {
  if (e.key === "/" && !/input|textarea/i.test(document.activeElement.tagName)) { e.preventDefault(); input.focus(); }
});
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
