import { createServer } from "node:http";
import { watch, readFile } from "node:fs";
import { spawnSync } from "node:child_process";
import { dirname, extname, join, normalize, sep } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const dist = join(here, "dist");
const port = Number(process.env.PORT) || 4823;
const types = { ".html": "text/html; charset=utf-8", ".css": "text/css", ".js": "text/javascript", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".otf": "font/otf", ".xml": "application/xml", ".txt": "text/plain; charset=utf-8" };
const reload = `<script>new EventSource("/__reload").onmessage = () => location.reload();</script>`;
const clients = new Set();

const build = () => spawnSync(process.execPath, [join(here, "build.mjs")], { stdio: "inherit" }).status === 0;
build();

let timer;
const onChange = (_, file) => {
  if (file && String(file).startsWith("dist")) return;
  clearTimeout(timer);
  timer = setTimeout(() => build() && clients.forEach((res) => res.write("data: reload\n\n")), 100);
};
watch(here, { recursive: true }, onChange);
watch(join(here, ".."), (e, f) => f === "catalog.json" && onChange(e, f));

createServer((req, res) => {
  let path;
  try { path = decodeURIComponent(new URL(req.url, "http://x").pathname); } catch { return res.writeHead(400).end(); }
  if (path === "/__reload") {
    res.writeHead(200, { "content-type": "text/event-stream", "cache-control": "no-cache" });
    clients.add(res);
    req.on("close", () => clients.delete(res));
    return;
  }
  let file = normalize(join(dist, path));
  if (file !== dist && !file.startsWith(dist + sep)) return res.writeHead(403).end();
  if (path.endsWith("/") || !extname(path)) file = join(file, "index.html");
  readFile(file, (err, body) => {
    if (err) return res.writeHead(404).end("not found");
    const type = types[extname(file)] || "application/octet-stream";
    res.writeHead(200, { "content-type": type, "cache-control": "no-store" });
    res.end(type.startsWith("text/html") ? String(body).replace("</body>", `${reload}</body>`) : body);
  });
}).listen(port, () => console.log(`persianskills dev: http://localhost:${port}  (edit site/ or catalog.json; the page reloads)`));
