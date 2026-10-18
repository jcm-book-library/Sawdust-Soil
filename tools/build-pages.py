"""Build index.html for GitHub Pages from app.html.

app.html is the single source. It is also what gets published as the claude.ai
artifact (which adds its own document skeleton), so it has no <head>. This adds
the doctype, metadata, icons and manifest that a normal website needs.

Run from the repo root:  python3 tools/build-pages.py
"""
from pathlib import Path

HEAD = """<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#121714">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="S&amp;S">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="manifest" href="manifest.webmanifest">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
<!-- Built from app.html by tools/build-pages.py. Edit app.html, not this file. -->
</head>
<body>
"""

root = Path(__file__).resolve().parent.parent
app = (root / "app.html").read_text(encoding="utf-8")
html = HEAD + app + "\n</body>\n</html>\n"
(root / "index.html").write_text(html, encoding="utf-8")
print("index.html built,", len(html), "bytes")
