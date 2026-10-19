# Sawdust & Soil: notes for Claude

**Read the house rules first:** [HOUSE-RULES.md](https://github.com/jcm-book-library/control-room/blob/main/HOUSE-RULES.md) in `control-room` (plain text: https://raw.githubusercontent.com/jcm-book-library/control-room/main/HOUSE-RULES.md). They cover Google Sheet safety, branches and pull requests into `main`, using cheaper models to save usage credits, and the build template. The notes below are this repo's own; where they are more specific, they win. The project charter is `project.json`.

## This repo
- `app.html` is the app source; the same file is published as the claude.ai artifact.
- `python3 tools/build-pages.py` rebuilds `index.html` from `app.html` for GitHub Pages.
- Data lives in the Google Sheet "Sawdust & Soil" (tabs `Tasks`, `List`, `Projects`).
- Sheet rule from the README: "Don't rename the tabs or reorder the columns." The app owns these tabs and rewrites them whole; the sheet's version wins on the next sync.
- Everything is also kept in the browser, so changes are kept locally if the sheet can't be reached.
