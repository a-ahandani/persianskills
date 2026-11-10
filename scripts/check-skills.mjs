import { readFileSync, readdirSync, existsSync, statSync } from "node:fs";
import { dirname, join, basename, relative } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const skillsDir = join(root, "skills");
const ALLOWED = new Set(["name", "description", "license", "compatibility", "allowed-tools", "metadata"]);
const persian = /[؀-ۿ]/g;
const letters = /[A-Za-z؀-ۿ]/g;
const share = (s) => (s.match(persian) || []).length / Math.max(1, (s.match(letters) || []).length);

const parse = (text) => {
  const m = text.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!m) return null;
  const [, fm, body] = m;
  const keys = [...fm.matchAll(/^([A-Za-z][\w-]*):/gm)].map((k) => k[1]);
  const field = (k) => {
    const r = fm.match(new RegExp(`^${k}:[ \\t]*(.*)\\n?((?:^[ \\t]+.*\\n?)*)`, "m"));
    if (!r) return "";
    const first = r[1].replace(/^[>|]-?\s*$/, "");
    return `${first} ${r[2]}`.replace(/\s+/g, " ").trim().replace(/^["']|["']$/g, "");
  };
  const meta = fm.match(/^metadata:\s*\n((?:^[ \t]+.*\n?)*)/m)?.[1] || "";
  const metaKeys = [...meta.matchAll(/^[ \t]+([\w-]+):/gm)].map((k) => k[1]);
  return { keys, name: field("name"), description: field("description"), metaKeys, body };
};

const prose = (body) => {
  let fenced = false;
  const out = [];
  for (const line of body.split("\n")) {
    if (/^\s*```/.test(line)) { fenced = !fenced; continue; }
    if (fenced || /^\s*\|/.test(line)) continue;
    out.push(line.replace(/«[^»]*»/g, "").replace(/`[^`]*`/g, "").replace(/\([^)]*\)/g, ""));
  }
  return out;
};

const TOP = new Set(["SKILL.md", "LICENSE", "NOTICE", "references", "scripts", "assets", "evals", "tests"]);
const TOOL_FILES = new Set(["package.json", "tsconfig.json", "remotion.config.ts", "__init__.py"]);
const kebab = /^[a-z0-9]+(-[a-z0-9]+)*$/;
const IGNORED = new Set([".DS_Store", "__pycache__", "node_modules", ".venv", "venv", "out", "work"]);
const fileName = (path) => {
  const parts = path.split(/[\\/]/);
  const f = parts.at(-1);
  if (parts.length === 1 && TOP.has(f)) return true;
  if (parts.includes("fonts") || TOOL_FILES.has(f)) return true;
  if (f.endsWith(".py")) return /^[a-z0-9]+(_[a-z0-9]+)*\.py$/.test(f);
  return /^[a-z0-9]+(-[a-z0-9]+)*\.[a-z0-9]+$/.test(f);
};
const layout = (dir) => {
  const problems = [];
  for (const top of readdirSync(dir)) if (!TOP.has(top) && !IGNORED.has(top)) problems.push(`not in the skill layout: ${top}`);
  for (const path of readdirSync(dir, { recursive: true })) {
    if (path.split(/[\\/]/).some((p) => IGNORED.has(p))) continue;
    const full = join(dir, path);
    const isDir = statSync(full).isDirectory();
    if (isDir ? !path.split(/[\\/]/).every((d) => kebab.test(d) || d === "fonts") : !fileName(path)) problems.push(`name breaks the rule: ${path}`);
    if (!isDir && path !== "SKILL.md" && basename(path) === "SKILL.md") problems.push(`nested skill: ${path}`);
  }
  return problems;
};

const files = readdirSync(skillsDir, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => join(skillsDir, d.name, "SKILL.md"));
const strays = readdirSync(skillsDir, { recursive: true }).filter((f) => basename(f) === "SKILL.md" && f.split(/[\\/]/).length !== 2);
const names = new Map();
let failures = 0;

for (const file of files.sort()) {
  const dir = dirname(file);
  const rel = relative(root, dir);
  const problems = [];
  if (!existsSync(file)) { console.log(`✗ ${rel}: no SKILL.md`); failures++; continue; }
  const s = parse(readFileSync(file, "utf8"));
  if (!s) { console.log(`✗ ${rel}: no frontmatter`); failures++; continue; }

  const extra = s.keys.filter((k) => !ALLOWED.has(k));
  if (extra.length) problems.push(`frontmatter fields not allowed: ${extra.join(", ")}`);
  if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(s.name) || s.name.length > 64) problems.push(`bad name "${s.name}"`);
  if (!/^(persian|dari|tajik)-/.test(s.name) || /-(skill|skills|toolkit)$/.test(s.name)) problems.push(`name "${s.name}" must start with persian-, dari- or tajik- and name a topic`);
  if (s.name !== basename(dir)) problems.push(`name "${s.name}" differs from folder "${basename(dir)}"`);
  if (names.has(s.name)) problems.push(`name also used by ${names.get(s.name)}`);
  names.set(s.name, rel);

  if (!s.description) problems.push("missing description");
  if (s.description.length > 1024) problems.push(`description is ${s.description.length} characters (max 1024)`);
  if (share(s.description.replace(/«[^»]*»/g, "")) > 0.3) problems.push("description is not in English");
  if (/^(i|we|you)\b/i.test(s.description)) problems.push("description is not in the third person");
  for (const k of ["author", "source"]) if (!s.metaKeys.includes(k)) problems.push(`metadata.${k} missing`);

  const lines = s.body.split("\n").length;
  if (lines > 500) problems.push(`body is ${lines} lines (max 500)`);
  const text = prose(s.body);
  const headings = text.filter((l) => /^#{1,6}\s/.test(l));
  const titles = headings.filter((l) => /^#\s/.test(l));
  if (titles.length !== 1) problems.push(`${titles.length} level-1 titles (want 1)`);
  const badHeadings = headings.filter((l) => share(l) > 0.5);
  if (badHeadings.length) problems.push(`headings not in English: ${badHeadings.slice(0, 3).map((h) => h.trim()).join(" | ")}`);
  if (share(text.join(" ")) > 0.35) problems.push(`instructions look Persian (${Math.round(share(text.join(" ")) * 100)}% Persian letters outside examples)`);
  if (headings.some((l) => /\p{Extended_Pictographic}/u.test(l))) problems.push("emoji in headings");

  problems.push(...layout(dir));
  const refs = [...s.body.matchAll(/(?:\]\(|`)((?:references|scripts|assets|evals|tests)\/[^)`\s#]+)/g)].map((m) => m[1]);
  for (const ref of new Set(refs)) if (!existsSync(join(dir, ref))) problems.push(`missing file ${ref}`);

  if (problems.length) {
    failures++;
    console.log(`✗ ${rel}\n${problems.map((p) => `    - ${p}`).join("\n")}`);
  }
}

for (const stray of strays) { console.log(`✗ skills/${stray}: a skill must sit directly in skills/<name>/`); failures++; }
console.log(`\n${files.length} skills checked, ${failures} with problems.`);
process.exit(failures ? 1 : 0);
