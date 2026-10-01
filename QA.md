# NALSTON — verification record

Reviewed October 1, 2026, against the local static site.

## Browser review

- Opened in the Codex browser and visually inspected the home, company, capabilities and contact layouts.
- Checked the six content pages at 320, 390, 768, 1024 and 1440 CSS pixels: no horizontal document overflow; one H1 on every page.
- Inspected desktop and mobile homepage screenshots, then completed a second refinement pass.
- Fixed process-label overlap on mobile, improved form spacing, raised mobile field text to 16px, and improved footer link spacing.
- Confirmed the corrected mobile process layout visually.
- Checked the mobile navigation open state, Escape dismissal and section navigation with the sticky header.
- Confirmed local responsive photographs load, including the deferred capabilities image.
- Contact: required fields reject an empty draft; all select options are available; a complete test inquiry copies successfully. No email was sent.
- No console warnings or errors were returned during the reviewed browsing session.
- Verified a local fixture with the JavaScript file omitted: navigation and direct email remain available, and the optional composer stays hidden.
- Reviewed the generated 1200 × 630 Open Graph image.

Screenshots are retained locally in the ignored .qa directory, including desktop-final.jpg, mobile-final.jpg and mobile-approach.jpg. They are not part of the public deployment.

## Static and behavior checks

- `python tools/check_site.py`: seven HTML documents, 187 local references, anchors, image metadata, canonical/Open Graph consistency, JSON-LD, robots and sitemap passed.
- `node --check script.js`: passed.
- An isolated JavaScript test verified the mailto recipient, subject/body encoding, draft content, copy behavior and accurate status messages without invoking an email client.
- Tested `tools/set_site_url.py` against isolated copies: all deployment URLs changed to the custom domain and the email address remained intact. Production files retain the GitHub Pages URL.
- `git diff --check`: passed.

## Deployment boundaries

The browser tests used the local server; this redesign has not been pushed or deployed. Actual email delivery depends on the visitor sending their draft through an email application. The branded 404 uses the published base URL so nested missing paths work after deployment; its links and assets were checked statically.

On the current project URL, robots.txt is inside /nalston-website/. Robots directives are normally read at the host root; the included file becomes the root robots.txt after connecting the custom domain. The sitemap remains directly accessible on either deployment.

No customers, operating metrics, certifications, facilities, founding date or jurisdiction have been introduced. Photography is illustrative and its sources are documented in assets/CREDITS.md.
