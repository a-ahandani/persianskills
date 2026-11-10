import { readFileSync, writeFileSync, mkdirSync, cpSync, rmSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import assert from "node:assert/strict";

const here = dirname(fileURLToPath(import.meta.url));
const out = join(here, "dist");
const catalog = JSON.parse(readFileSync(join(here, "..", "catalog.json"), "utf8"));
const { repo, site, checked, skills } = catalog;
const gh = `https://github.com/${repo}`;

const VARIETIES = ["iran", "afghanistan", "tajikistan", "all"];
const CATEGORIES = ["writing", "localization", "translation", "typography", "documents", "dates", "ui", "evals", "tools", "domain"];
for (const s of skills) {
  assert.ok(s.name && s.author && s.url && s.en && s.fa && s.license, `incomplete entry: ${s.name}`);
  assert.ok(VARIETIES.includes(s.variety), `bad variety: ${s.name}`);
  assert.ok(CATEGORIES.includes(s.category), `bad category: ${s.name}`);
  assert.ok(!s.here || s.path, `in-repo skill needs a path: ${s.name}`);
  assert.match(s.url, /^https:\/\//, `url must be https: ${s.name}`);
}

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);

const icon = {
  github: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="currentColor"><path d="M8 0a8 8 0 0 0-2.53 15.59c.4.07.55-.17.55-.38v-1.33c-2.23.48-2.7-1.07-2.7-1.07-.36-.92-.89-1.17-.89-1.17-.73-.5.05-.49.05-.49.8.06 1.23.83 1.23.83.72 1.22 1.88.87 2.33.66.07-.52.28-.87.5-1.07-1.78-.2-3.65-.89-3.65-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82a7.6 7.6 0 0 1 4 0c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.28.82 2.15 0 3.07-1.87 3.75-3.66 3.95.29.25.54.73.54 1.48v2.2c0 .21.15.46.55.38A8 8 0 0 0 8 0Z"/></svg>',
  copy: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="5.5" y="5.5" width="8" height="8" rx="1.5"/><path d="M10.5 3.5v-.5A1.5 1.5 0 0 0 9 1.5H3A1.5 1.5 0 0 0 1.5 3v6A1.5 1.5 0 0 0 3 10.5h.5"/></svg>',
  globe: '<svg viewBox="0 0 16 16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="8" cy="8" r="6.5"/><path d="M1.5 8h13M8 1.5c1.8 1.8 2.6 4 2.6 6.5S9.8 12.7 8 14.5M8 1.5C6.2 3.3 5.4 5.5 5.4 8s.8 4.7 2.6 6.5"/></svg>',
};

const T = {
  fa: {
    dir: "rtl",
    path: "/",
    other: { lang: "en", path: "/en/", label: "English" },
    title: "مهارت‌های فارسی برای ایجنت‌های هوش مصنوعی | Persian Skills",
    description: "مهارت‌های متن‌باز برای اینکه ایجنت هوش مصنوعی فارسی را درست بنویسد: فارسی ایران، دری افغانستان و تاجیکی، برای Claude Code و Codex و Cursor.",
    nav: ["مهارت‌ها", "نصب", "منابع", "مشارکت"],
    pill: "متن‌باز و رایگان",
    h1: "مهارت‌های فارسی برای ایجنت‌های هوش مصنوعی",
    lead: "با این مهارت‌ها ایجنت شما فارسی را درست و طبیعی می‌نویسد، چه برای خواننده‌ای در ایران، چه در افغانستان و چه در تاجیکستان.",
    install: "نصب مهارت‌ها",
    viewGithub: "مشاهده در GitHub",
    varietiesTitle: "یک زبان، سه گونه",
    varietiesText: "در افغانستان به بیمارستان شفاخانه می‌گویند و بیشتر تاجیک‌ها خط فارسی را نمی‌خوانند. ایجنت باید بداند برای چه کسی می‌نویسد.",
    facts: ["خط", "پول", "ماه اول سال", "کد زبان"],
    varieties: [
      { where: "ایران", name: "فارسی", sample: "دانشجو با اتوبوس به بیمارستان رفت.", values: ["فارسی، راست به چپ", "تومان، ریال", "فروردین", "fa-IR"] },
      { where: "افغانستان", name: "دری", sample: "محصل با بس به شفاخانه رفت.", values: ["فارسی، راست به چپ", "افغانی ؋", "حمل", "fa-AF"] },
      { where: "تاجیکستان", name: "Тоҷикӣ", cyr: true, sample: "Донишҷӯ бо автобус ба беморхона рафт.", values: ["سیریلیک، چپ به راست", "сомонӣ", "январ", "tg"] },
    ],
    sampleNote: "یک جمله، به سه گونه‌ی فارسی.",
    installTitle: "نصب",
    installText: "ابزار skills ایجنت‌های نصب‌شده روی سیستم شما را پیدا می‌کند و مهارت‌ها را در جای درست می‌گذارد.",
    steps: [
      ["همه‌ی مهارت‌ها", "چهار مهارت این مخزن، یک‌جا.", `npx skills add ${repo}`],
      ["فقط یک مهارت", "نام مهارت را بعد از <code>--skill</code> بنویسید.", `npx skills add ${repo} --skill dari-writing`],
      ["افزونه‌ی Claude Code", "داخل Claude Code این دو فرمان را بزنید.", `/plugin marketplace add ${repo}\n/plugin install persian-skills@persianskills`],
    ],
    chatNote: "برای ChatGPT و Gemini و دیگر چت‌ها، فایل SKILL.md هر مهارت را به‌عنوان دانش بارگذاری کنید.",
    skillsTitle: "مهارت‌ها",
    skillsText: (n, a) => `${n} مهارت و ابزار از ${a} سازنده، بررسی‌شده در ${new Date(checked).toLocaleDateString("fa-IR", { dateStyle: "long", timeZone: "UTC" })}. چهار مهارت اول در همین مخزن است و بقیه را از مخزن سازنده‌اش نصب کنید.`,
    filters: { any: "همه", iran: "ایران", afghanistan: "افغانستان", tajikistan: "تاجیکستان", all: "همه‌ی گونه‌ها" },
    categories: { writing: "نگارش", localization: "بومی‌سازی", translation: "ترجمه", typography: "تایپوگرافی", documents: "سند و فایل", dates: "تاریخ", ui: "رابط کاربری", evals: "ارزیابی", tools: "ابزار", domain: "تخصصی" },
    here: "در همین مخزن",
    draft: "پیش‌نویس، بدون بازبینی بومی",
    noLicense: "بدون مجوز",
    by: "از",
    empty: "در این دسته مهارتی نیست.",
    creditsTitle: "سپاس و منابع",
    creditsSkillsTitle: "سازندگان",
    credits: [
      ["ali2000hos/persian-writing", "https://github.com/ali2000hos/persian-writing", "مهارت persian-writing بی‌تغییر از این مخزن آمده است. کد با مجوز MIT و فونت‌ها با مجوز SIL OFL."],
      ["Edyt", "https://edyt.app/fa", "قواعد persian-localization از بازبینی ترجمه‌ی فارسی Edyt به دست یک فارسی‌زبان آمده است."],
      ["همه‌ی سازندگان فهرست", "#skills", "هر ردیف فهرست به مخزن سازنده‌اش می‌رود. مجوز هر مهارت همان است که سازنده‌اش گذاشته."],
    ],
    sourcesTitle: "منابع دری و تاجیکی",
    sources: [
      ["Unicode CLDR", "https://github.com/unicode-org/cldr", "داده‌ی ماه‌ها، پول، اعداد و تعطیلی هفته برای fa-AF و tg."],
      ["آکادمی علوم افغانستان", "https://asa.gov.af", "مرجع رسمی زبان در افغانستان."],
      ["کمیته‌ی زبان و اصطلاحات تاجیکستان", "https://kumitaizabon.tj", "مرجع دستور خط تاجیکی، مصوب ۱۲ مهر ۱۳۹۰ (۴ اکتبر ۲۰۱۱)."],
      ["واژه‌های فارسی و دری", "https://journals.openedition.org/abstractairanica/57034", "معرفی واژه‌نامه‌ی تطبیقی فارسی و دری نوید و تورمایر."],
    ],
    closingTitle: "مهارت فارسی ساخته‌اید؟",
    closingText: "یک ردیف به catalog.json اضافه کنید و درخواست ادغام بفرستید. مهارت‌های دری، هزارگی و تاجیکی از همه کمترند.",
    addSkill: "افزودن مهارت",
    reportIssue: "گزارش مشکل",
    footer: ["کد با مجوز MIT", "ساخته‌ی تیم Edyt"],
    copy: "کپی",
    copied: "کپی شد",
    num: (n) => n.toLocaleString("fa-IR"),
  },
  en: {
    dir: "ltr",
    path: "/en/",
    other: { lang: "fa", path: "/", label: "فارسی" },
    title: "Persian Skills: agent skills for Persian, Dari and Tajik",
    description: "Open-source agent skills that make AI write Persian correctly for readers in Iran, Afghanistan and Tajikistan. For Claude Code, Codex, Cursor and any agent that reads SKILL.md.",
    nav: ["Skills", "Install", "Sources", "Contribute"],
    pill: "Open source, free",
    h1: "Persian skills for AI agents",
    lead: "Skills that make your agent write correct, natural Persian, whether the reader is in Iran, Afghanistan or Tajikistan.",
    install: "Install the skills",
    viewGithub: "View on GitHub",
    varietiesTitle: "One language, three standards",
    varietiesText: "Afghans say shafakhana for hospital, and most Tajiks can't read Persian script. Your agent has to know who it is writing for.",
    facts: ["Script", "Money", "First month", "Locale"],
    varieties: [
      { where: "Iran", name: "فارسی", sample: "دانشجو با اتوبوس به بیمارستان رفت.", values: ["Perso-Arabic, RTL", "toman, rial", "Farvardin", "fa-IR"] },
      { where: "Afghanistan", name: "دری", sample: "محصل با بس به شفاخانه رفت.", values: ["Perso-Arabic, RTL", "afghani ؋", "Hamal", "fa-AF"] },
      { where: "Tajikistan", name: "Тоҷикӣ", cyr: true, sample: "Донишҷӯ бо автобус ба беморхона рафт.", values: ["Cyrillic, LTR", "сомонӣ", "январ", "tg"] },
    ],
    sampleNote: "The same sentence in each: “The student took the bus to the hospital.”",
    installTitle: "Install",
    installText: "The skills CLI finds the agents on your machine and puts each skill where that agent looks for it.",
    steps: [
      ["Every skill", "All four skills in this repo.", `npx skills add ${repo}`],
      ["One skill", "Name it after <code>--skill</code>.", `npx skills add ${repo} --skill dari-writing`],
      ["Claude Code plugin", "Run both inside Claude Code.", `/plugin marketplace add ${repo}\n/plugin install persian-skills@persianskills`],
    ],
    chatNote: "For ChatGPT, Gemini and other chat apps, upload a skill's SKILL.md as knowledge.",
    skillsTitle: "Skills",
    skillsText: (n, a) => `${n} skills and tools from ${a} authors, checked on ${checked}. The first four live in this repo; install the rest from their authors' repos.`,
    filters: { any: "All", iran: "Iran", afghanistan: "Afghanistan", tajikistan: "Tajikistan", all: "Every variety" },
    categories: { writing: "Writing", localization: "Localization", translation: "Translation", typography: "Typography", documents: "Documents", dates: "Dates", ui: "UI", evals: "Evals", tools: "Tools", domain: "Domain" },
    here: "In this repo",
    draft: "Draft, no native review yet",
    noLicense: "No license",
    by: "by",
    empty: "Nothing in this group yet.",
    creditsTitle: "Credits and sources",
    creditsSkillsTitle: "Authors",
    credits: [
      ["ali2000hos/persian-writing", "https://github.com/ali2000hos/persian-writing", "The persian-writing skill is copied unchanged from this repo. Code under MIT, fonts under the SIL OFL."],
      ["Edyt", "https://edyt.app", "The persian-localization rules come from a native speaker's review of Edyt's Persian translation."],
      ["Every author in the list", "#skills", "Each row links to its author's repo. Each skill keeps the license its author chose."],
    ],
    sourcesTitle: "Dari and Tajik sources",
    sources: [
      ["Unicode CLDR", "https://github.com/unicode-org/cldr", "Months, currency, numbers and weekend data for fa-AF and tg."],
      ["Academy of Sciences of Afghanistan", "https://asa.gov.af", "Afghanistan's official language authority."],
      ["Tajikistan's Committee on Language and Terminology", "https://kumitaizabon.tj", "Publisher of the Tajik orthography rules approved on 4 October 2011."],
      ["Persian and Dari vocabulary", "https://journals.openedition.org/abstractairanica/57034", "Review of Newid and Thurmair's comparative Farsi/Dari vocabulary."],
    ],
    closingTitle: "Built a Persian skill?",
    closingText: "Add a row to catalog.json and open a pull request. Dari, Hazaragi and Tajik skills are the scarcest.",
    addSkill: "Add a skill",
    reportIssue: "Report a problem",
    footer: ["Code under MIT", "Made by the team behind Edyt"],
    copy: "Copy",
    copied: "Copied",
    num: (n) => n.toLocaleString("en-US"),
  },
};

const licenseLabel = (t, l) => (l === "none" ? t.noLicense : l === "see repo" || l === "unclear" ? (t === T.fa ? "مجوز: در مخزن" : "License: see repo") : l);

const row = (t, s, lang) => {
  const href = s.here ? `${gh}/tree/main/${s.path}` : s.url;
  const tags = [
    s.here ? `<span class="tag here">${t.here}</span>` : "",
    s.draft ? `<span class="tag draft">${t.draft}</span>` : "",
    `<span class="tag">${t.filters[s.variety]}</span>`,
    `<span class="tag">${t.categories[s.category]}</span>`,
    s.kind === "mcp" ? `<span class="tag" dir="ltr">MCP</span>` : "",
    `<span class="tag"><bdi>${esc(licenseLabel(t, s.license))}</bdi></span>`,
    s.stars ? `<span class="tag">★ ${t.num(s.stars)}</span>` : "",
  ].join("");
  return `<a class="row" href="${esc(href)}" data-variety="${s.variety}" target="_blank" rel="noopener">
  <div class="title"><b dir="ltr">${esc(s.name)}</b><small>${t.by} <bdi>${esc(s.author)}</bdi></small></div>
  <p class="desc">${esc(s[lang])}</p>
  <div class="meta">${tags}</div>
</a>`;
};

const linkList = (items) =>
  `<ul>${items.map(([name, href, note]) => `<li><a href="${esc(href)}"${href.startsWith("#") ? "" : ' target="_blank" rel="noopener"'}><bdi>${esc(name)}</bdi></a><span>${esc(note)}</span></li>`).join("")}</ul>`;

const page = (lang) => {
  const t = T[lang];
  const authors = new Set(skills.map((s) => s.author)).size;
  const [navSkills, navInstall, navSources, navContribute] = t.nav;
  const favicon = `data:image/svg+xml,${encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="9" fill="#141414"/><text x="16" y="23" text-anchor="middle" font-family="Tahoma,sans-serif" font-size="20" font-weight="700" fill="#eda220">پ</text></svg>')}`;
  return `<!doctype html>
<html lang="${lang}" dir="${t.dir}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(t.title)}</title>
<meta name="description" content="${esc(t.description)}">
<link rel="canonical" href="${site}${t.path}">
<link rel="alternate" hreflang="fa" href="${site}/">
<link rel="alternate" hreflang="en" href="${site}/en/">
<link rel="alternate" hreflang="x-default" href="${site}/">
<meta property="og:title" content="${esc(t.title)}">
<meta property="og:description" content="${esc(t.description)}">
<meta property="og:url" content="${site}${t.path}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="${favicon}">
<link rel="preload" href="${lang === "fa" ? "/fonts/sahel-black.woff2" : "/fonts/lexend-latin-wght-normal.woff2"}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="${t.path}" dir="ltr"><span class="brand-mark" aria-hidden="true">پ</span>persianskills</a>
  <nav class="links" aria-label="${navSkills}">
    <a href="#skills">${navSkills}</a><a href="#install">${navInstall}</a><a href="#sources">${navSources}</a><a href="#contribute">${navContribute}</a>
  </nav>
  <div class="top-actions">
    <a class="btn" href="${t.other.path}" hreflang="${t.other.lang}" lang="${t.other.lang}">${icon.globe}${t.other.label}</a>
    <a class="btn solid" href="${gh}" target="_blank" rel="noopener" aria-label="GitHub">${icon.github}<span dir="ltr">GitHub</span></a>
  </div>
</div></header>

<main>
<section class="hero"><div class="wrap">
  <span class="pill">${t.pill}</span>
  <h1>${t.h1}</h1>
  <p class="lead">${t.lead}</p>
  <div class="cta">
    <a class="btn solid lg" href="#install">${t.install}</a>
    <a class="btn lg" href="${gh}" target="_blank" rel="noopener">${icon.github}${t.viewGithub}</a>
  </div>
  <span class="underline" aria-hidden="true"></span>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><div><h2>${t.varietiesTitle}</h2><p>${t.varietiesText}</p></div></div>
  <div class="varieties">
    ${t.varieties
      .map(
        (v) => `<article class="variety">
      <div class="where">${v.where}</div>
      <div class="name${v.cyr ? " cyr" : ""}" ${v.cyr ? 'lang="tg" dir="ltr"' : 'lang="fa" dir="rtl"'}>${v.name}</div>
      <p class="sample${v.cyr ? " cyr" : ""}" ${v.cyr ? 'lang="tg" dir="ltr"' : 'lang="fa" dir="rtl"'}>${v.sample}</p>
      <dl>${t.facts.map((f, i) => `<dt>${f}</dt><dd><bdi>${v.values[i]}</bdi></dd>`).join("")}</dl>
    </article>`,
      )
      .join("\n    ")}
  </div>
  ${t.sampleNote ? `<p class="note">${t.sampleNote}</p>` : ""}
</div></section>

<section class="section" id="install"><div class="wrap"><div class="panel">
  <h2>${t.installTitle}</h2>
  <p class="lead">${t.installText}</p>
  <div class="steps">
    ${t.steps
      .map(
        ([title, text, cmd]) => `<div class="step"><div><h3>${title}</h3><p>${text}</p></div><pre class="cmd"><code>${esc(cmd)}</code><button class="copy" type="button" aria-label="${t.copy}" data-copied="${t.copied}">${icon.copy}</button></pre></div>`,
      )
      .join("\n    ")}
  </div>
  <div class="agents">${["Claude Code", "Codex", "Cursor", "Gemini CLI", "GitHub Copilot", "Windsurf", "OpenCode", "Cline", "Roo Code", "Goose", "Kiro", "Amp"].map((a) => `<span>${a}</span>`).join("")}</div>
  <p class="note">${t.chatNote}</p>
</div></div></section>

<section class="section" id="skills"><div class="wrap">
  <div class="section-head">
    <div><h2>${t.skillsTitle}</h2><p>${t.skillsText(t.num(skills.length), t.num(authors))}</p></div>
    <div class="filters" role="group" aria-label="${t.skillsTitle}">
      ${["any", ...VARIETIES].map((k, i) => `<button type="button" data-filter="${k}" aria-pressed="${i === 0}">${t.filters[k]}</button>`).join("")}
    </div>
  </div>
  <div class="list">
${skills.map((s) => row(t, s, lang)).join("\n")}
  </div>
  <p class="empty" hidden>${t.empty}</p>
</div></section>

<section class="section" id="sources"><div class="wrap">
  <div class="section-head"><div><h2>${t.creditsTitle}</h2></div></div>
  <div class="credits">
    <div class="card"><h3>${t.creditsSkillsTitle}</h3>${linkList(t.credits)}</div>
    <div class="card"><h3>${t.sourcesTitle}</h3>${linkList(t.sources)}</div>
  </div>
</div></section>

<section class="closing" id="contribute"><div class="wrap">
  <h2>${t.closingTitle}</h2>
  <p>${t.closingText}</p>
  <div class="cta">
    <a class="btn solid lg" href="${gh}/edit/main/catalog.json" target="_blank" rel="noopener">${t.addSkill}</a>
    <a class="btn lg" href="${gh}/issues" target="_blank" rel="noopener">${t.reportIssue}</a>
  </div>
</div></section>
</main>

<footer><div class="wrap">
  <span>${t.footer[0]}</span>
  <span><a href="${gh}" target="_blank" rel="noopener" dir="ltr">${repo}</a> · <a href="${lang === "fa" ? "https://edyt.app/fa" : "https://edyt.app"}" target="_blank" rel="noopener">${t.footer[1]}</a></span>
</div></footer>

<script>
const rows = [...document.querySelectorAll(".row")];
const empty = document.querySelector(".empty");
document.querySelectorAll("[data-filter]").forEach((b) => b.addEventListener("click", () => {
  const f = b.dataset.filter;
  document.querySelectorAll("[data-filter]").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
  let shown = 0;
  rows.forEach((r) => { const v = r.dataset.variety; r.hidden = !(f === "any" || v === f || (f !== "all" && v === "all")); if (!r.hidden) shown++; });
  empty.hidden = shown > 0;
}));
document.querySelectorAll(".copy").forEach((b) => b.addEventListener("click", async () => {
  try { await navigator.clipboard.writeText(b.previousElementSibling.textContent); b.setAttribute("aria-label", b.dataset.copied); b.style.color = "var(--ok)"; } catch {}
}));
</script>
</body>
</html>
`;
};

rmSync(out, { recursive: true, force: true });
mkdirSync(join(out, "en"), { recursive: true });
writeFileSync(join(out, "index.html"), page("fa"));
writeFileSync(join(out, "en", "index.html"), page("en"));
cpSync(join(here, "style.css"), join(out, "style.css"));
cpSync(join(here, "fonts"), join(out, "fonts"), { recursive: true });
writeFileSync(join(out, "robots.txt"), `User-agent: *\nAllow: /\nSitemap: ${site}/sitemap.xml\n`);
writeFileSync(
  join(out, "sitemap.xml"),
  `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<url><loc>${site}/</loc><lastmod>${checked}</lastmod></url>\n<url><loc>${site}/en/</loc><lastmod>${checked}</lastmod></url>\n</urlset>\n`,
);
console.log(`built ${skills.length} skills into ${out}`);
