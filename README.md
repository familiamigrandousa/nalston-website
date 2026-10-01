# NALSTON — Corporate website

Static HTML, CSS and JavaScript for Nalston Strategic Group LLC. No build step, framework, external font requests, analytics, tracking cookies or backend. Images are local responsive WebP files.

## Preview

Run `python -m http.server 8080` from this folder and visit http://localhost:8080. Opening index.html directly also works, except clipboard access may require localhost or HTTPS.

## Publish the existing GitHub Pages site

Repository: https://github.com/familiamigrandousa/nalston-website

The files are ready to commit to the existing repository. Preserve the current Pages deployment configuration. This project is served from the repository root and supports the /nalston-website/ subpath through relative asset and navigation URLs. No DNS changes are included.

```sh
git add .
git commit -m "Redesign Nalston corporate website"
git push
```

Current canonical URL, Open Graph URLs, JSON-LD, robots.txt, sitemap.xml and the 404 base URL use https://familiamigrandousa.github.io/nalston-website/ while the custom domain remains unconnected.

## When connecting nalstongroup.com

After configuring the custom domain in GitHub Pages and verifying HTTPS, update all public URL metadata in one step:

```sh
python tools/set_site_url.py https://nalstongroup.com/
```

Then commit the updated files. GitHub's domain configuration manages CNAME; no CNAME file is added preemptively. Do not alter email-related MX, SPF, DKIM or DMARC records. The script only changes metadata and absolute site URLs, not the email address.

## Pages and maintenance

- index.html: hero, company, capabilities, markets, working approach, suppliers and partners, final CTA and contact.
- company.html, capabilities.html, contact.html: complete supporting pages.
- privacy.html, terms.html: website-specific policies.
- 404.html: branded recovery page. The absolute base URL intentionally points to the published site so nested missing routes can load assets and navigate home.
- styles.css / script.js: shared styles, accessible mobile navigation and optional email composer.
- assets/CREDITS.md: photography sources and licenses.

Shared headers and footers are static HTML. Keep them consistent when editing a page. The site content is in English for business counterparties. Do not introduce unverified customers, certifications, offices, sales figures or operating history. Market focus is not an office-location claim. Photography is illustrative.

## Contact behavior

The site cannot send messages itself. The form validates required fields, prepares a mailto draft, and offers Copy inquiry as a fallback. The user must send the email. No contact data is posted, stored or logged by the site. Without JavaScript, direct email links remain available and the optional form is hidden.

## Verification

See QA.md for the completed browser checks and any deployment-specific limitations. Review company policies as business practices evolve.

## Guia de lanzamiento en espanol

Consulta [PUBLICAR.md](PUBLICAR.md) para los comandos de publicacion y la conexion de nalstongroup.com.
