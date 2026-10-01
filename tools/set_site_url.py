"""Update absolute site metadata after changing the deployment URL. No dependencies."""
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

root = Path(__file__).resolve().parents[1]
if len(sys.argv) != 2:
    raise SystemExit("Usage: python tools/set_site_url.py https://nalstongroup.com/")
new = sys.argv[1].rstrip("/") + "/"
parsed = urlparse(new)
if (parsed.scheme != "https" or not parsed.netloc or parsed.query or parsed.fragment
        or parsed.username or parsed.password
        or any(c.isspace() or c in ("<", ">", '"', "'", "\\") for c in new)):
    raise SystemExit("Provide an absolute HTTPS website URL without query parameters or fragments.")
index = (root / "index.html").read_text(encoding="utf-8-sig")
match = re.search(r'<link rel="canonical" href="([^\"]+)">', index)
if not match:
    raise SystemExit("Could not find the existing homepage canonical URL.")
old = match.group(1)
for path in [*root.glob("*.html"), root / "robots.txt", root / "sitemap.xml"]:
    text = path.read_text(encoding="utf-8-sig")
    if old in text:
        path.write_text(text.replace(old, new), encoding="utf-8")
        print("Updated", path.name)
print("Site URL:", new)
