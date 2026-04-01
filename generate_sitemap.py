# GolfVilla.com — Sitemap Generator
# Scans all HTML files in the site and SEO-Files/ to build sitemap.xml
# USAGE: python generate_sitemap.py
# Run AFTER all other generators have been run.
# Run from: C:\Users\rbend\Desktop\GOLFVILLA-WEBSITE\Funnel Websites\golfvilla-com\

import os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEO_DIR = os.path.join(BASE_DIR, "SEO-Files")
DOMAIN = "https://www.golfvilla.com"
OUTPUT = os.path.join(BASE_DIR, "sitemap.xml")
TODAY = datetime.date.today().isoformat()

urls = []

# ── Core pages ──────────────────────────────────────────────────────────────
CORE_PAGES = [
    ("", "1.0", "weekly"),
    ("what-is-a-golf-villa/", "0.9", "monthly"),
    ("caribbean-golf-villa/", "0.9", "monthly"),
    ("dominican-republic-golf-villa/", "0.9", "monthly"),
    ("cap-cana-golf-villa/", "1.0", "weekly"),
    ("luxury-golf-villa/", "0.8", "monthly"),
    ("golf-villa-rental/", "0.8", "monthly"),
    ("golf-villa-packages/", "0.8", "monthly"),
    ("book/", "0.9", "weekly"),
]

for path, priority, freq in CORE_PAGES:
    urls.append({
        "loc": f"{DOMAIN}/{path}",
        "lastmod": TODAY,
        "changefreq": freq,
        "priority": priority
    })

# ── SEO-Files pages ──────────────────────────────────────────────────────────
if os.path.isdir(SEO_DIR):
    for fname in sorted(os.listdir(SEO_DIR)):
        if fname.endswith(".html"):
            slug = fname[:-5]  # remove .html
            urls.append({
                "loc": f"{DOMAIN}/SEO-Files/{slug}",
                "lastmod": TODAY,
                "changefreq": "monthly",
                "priority": "0.6"
            })

# ── Build XML ────────────────────────────────────────────────────────────────
lines = ['<?xml version="1.0" encoding="UTF-8"?>']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for u in urls:
    lines.append("  <url>")
    lines.append(f"    <loc>{u['loc']}</loc>")
    lines.append(f"    <lastmod>{u['lastmod']}</lastmod>")
    lines.append(f"    <changefreq>{u['changefreq']}</changefreq>")
    lines.append(f"    <priority>{u['priority']}</priority>")
    lines.append("  </url>")

lines.append("</urlset>")

sitemap_content = "\n".join(lines)

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"✅ sitemap.xml generated — {len(urls)} URLs")
print(f"   Saved to: {OUTPUT}")
print(f"\n   Submit at: https://search.google.com/search-console")
print(f"   Sitemap URL: {DOMAIN}/sitemap.xml")
