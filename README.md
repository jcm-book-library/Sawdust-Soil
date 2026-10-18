# Sawdust & Soil

My woodwork and garden companion for the Ballarat house. It has:

- **Parametric plans** for each woodwork project. Sliders change the dimensions, and the app redraws a to-scale drawing, the cut list, a cutting plan, warnings, the shopping list and the build steps.
- **A garden bed planner and a monthly calendar** for Ballarat.

The Google Sheet "Sawdust & Soil" holds the data, and this app reads and writes it.

- **Live site:** https://jcm-book-library.github.io/Sawdust-Soil/ (once GitHub Pages is turned on)
- **Sheet:** https://docs.google.com/spreadsheets/d/1S5kGsM0CJkQQGEvisQMZDhrfdCosY025MqKxtej9Rvc/edit

## Files
| File | What it is |
|---|---|
| `app.html` | The app source. Edit this. The same file is published as the claude.ai artifact. |
| `index.html` | Built from `app.html` for GitHub Pages. Rebuild it with `python3 tools/build-pages.py`. |
| `manifest.webmanifest`, `icons/` | Home-screen install and icons. |

## Pages
| Page | What's on it |
|---|---|
| Today | This month's garden and workshop jobs for Ballarat, frost risk, the next task, and the woodwork path. |
| Garden | Driveway bed renovation phases, the keep-or-remove guide, the bed planner (plant counts, mulch, edging, cost) and the plant library. |
| Workshop | Bookshelf boxes, cat perch, catio pod and display cabinet, plus a refresher after 20 years away. |
| List | One shopping list, grouped by where to buy each item. |

## How it connects
- **Inside claude.ai:** it uses the Google Sheets connector.
- **On GitHub Pages:** it uses Google sign-in with an OAuth Client ID. The ID is saved in the browser under `ss_gconfig`. Use the same Client ID as Jackets & Manuscripts. Its Google Cloud project already lists `https://jcm-book-library.github.io` as an authorised origin, so this site works with it too. Sign-in lasts about an hour. After that, press **Connect** again.
- **Offline:** everything is also kept in the browser. If the sheet can't be reached, changes are kept locally and sync the next time it can.

## Sheet tabs
The app owns these tabs and rewrites them whole. You can still edit cells directly, for example tick `done` on your phone. The next time the app syncs, the sheet's version wins.

| Tab | Columns |
|---|---|
| `Tasks` | id, task, phase, done, done_on |
| `List` | id, item, qty, source, project, done, group |
| `Projects` | key, value (JSON of slider settings, or the "built it" record), updated, note |

Don't rename the tabs or reorder the columns.
