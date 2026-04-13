import { readdirSync, readFileSync, writeFileSync, statSync } from 'node:fs';
import { join, relative, dirname } from 'node:path';

const DIST = join(process.cwd(), 'dist');

function walk(dir, cb) {
  for (const n of readdirSync(dir)) {
    const p = join(dir, n);
    const s = statSync(p);
    if (s.isDirectory()) walk(p, cb);
    else cb(p);
  }
}

function prefix(filePath) {
  const rel = relative(dirname(filePath), DIST);
  return rel === '' ? '.' : rel;
}

walk(DIST, (file) => {
  if (!file.endsWith('.html')) return;
  const pfx = prefix(file);
  let html = readFileSync(file, 'utf8');

  // Rewrite absolute root-anchored paths in href/src to relative. Skip URLs,
  // data:, #, mailto:, protocol-relative, etc.
  html = html.replace(/(href|src)="\/([^"/]|\/)/g, (match, attr, ch) => {
    if (ch === '/') return match; // protocol-relative //example.com
    return `${attr}="${pfx}/${ch}`;
  });
  html = html.replace(/(href|src)="\/"/g, `$1="${pfx}/index.html"`);

  // Append index.html to every internal href ending in '/'. Browsers refuse
  // to auto-load index.html on file:// directory URLs.
  html = html.replace(/href="([^"#?]*?)\/"/g, (match, path) => {
    if (/^(https?:|mailto:|tel:|data:|ftp:|#)/.test(path)) return match;
    if (path === '' || path === '.') return match; // leave plain "./"/"/"
    return `href="${path}/index.html"`;
  });

  writeFileSync(file, html);
});

console.log('[fix-paths] rewrote absolute / paths to relative for file:// use');
