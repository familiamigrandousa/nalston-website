"""Dependency-free checks for static pages, local links, image assets and SEO."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.refs, self.meta = path, set(), [], {}
        self.h1 = 0
        self.canonical = None
        self.jsonld = ""
        self.in_jsonld = False
        self.feed(path.read_text(encoding="utf-8-sig"))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            assert a["id"] not in self.ids, f"{self.path.name}: duplicate ID {a['id']}"
            self.ids.add(a["id"])
        self.h1 += tag == "h1"
        if tag == "meta":
            self.meta[a.get("name", a.get("property"))] = a.get("content")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical = a["href"]
        if tag in ("a", "link") and "href" in a:
            self.refs.append(a["href"])
        if "src" in a:
            self.refs.append(a["src"])
        if "srcset" in a:
            self.refs.extend(part.strip().split()[0] for part in a["srcset"].split(","))
        if tag == "img":
            assert a.get("alt") and a.get("width") and a.get("height"), f"{self.path.name}: image metadata"
        if tag == "script" and a.get("type") == "application/ld+json":
            self.in_jsonld = True

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_jsonld = False

    def handle_data(self, data):
        if self.in_jsonld:
            self.jsonld += data


pages = {p.name: Page(p) for p in ROOT.glob("*.html")}
base = pages["index.html"].canonical
count = 0
for name, page in pages.items():
    assert page.h1 == 1, f"{name}: expected exactly one H1"
    assert page.meta.get("description") and page.meta.get("viewport"), f"{name}: missing metadata"
    assert page.meta.get("og:url") == page.canonical, f"{name}: inconsistent canonical"
    assert page.meta.get("twitter:card") == "summary_large_image", f"{name}: missing social card"
    for ref in page.refs + [page.meta["og:image"]]:
        local = ref.removeprefix(base) if ref.startswith(base) else ref
        parsed = urlparse(local)
        if parsed.scheme or parsed.netloc:
            continue
        path = ROOT / unquote(parsed.path) if parsed.path else page.path
        assert path.is_file(), f"{name}: missing {ref}"
        if parsed.fragment and path.suffix == ".html":
            assert unquote(parsed.fragment) in pages[path.name].ids, f"{name}: missing anchor {ref}"
        count += 1
    if page.jsonld:
        data = json.loads(page.jsonld)
        assert data["legalName"] == "Nalston Strategic Group LLC"
        assert data["url"] == base

urls = [node.text for node in ET.parse(ROOT / "sitemap.xml").iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
assert len(urls) == 6 and all(url.startswith(base) for url in urls)
assert base + "sitemap.xml" in (ROOT / "robots.txt").read_text()
assert (ROOT / ".nojekyll").exists()
assert all("http" not in ref or ref.startswith(base) for p in pages.values() for ref in p.refs if ref.endswith((".css", ".js", ".webp")))
print(f"PASS: {len(pages)} HTML pages, {count} local references, anchors, metadata, JSON-LD and sitemap.")
