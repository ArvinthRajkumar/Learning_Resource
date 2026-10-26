# learning_resource

A collection of self-contained learning guides written in plain HTML, CSS and JavaScript. There's no build step, no npm, no frameworks and no network requests. Every page works when you double-click it from disk (`file://`) and when it's served from GitHub Pages.

## Resources

| Resource | Path |
| --- | --- |
| AI/ML Engineer Assessment Prep | `resources/ai-ml-engineer-prep/index.html` |
| DSA Master Guide (Python) | `resources/dsa-master-guide/index.html` |
| Diffusion Models from Scratch | `resources/diffusion-from-scratch/index.html` |
| System Design Guide | `resources/system-design-guide/index.html` |
| Python and SQL Guide | `resources/python-sql-guide/index.html` |

## Open locally

- Double-click `index.html`, or open it from your browser's File menu. That's all.
- To serve it instead (useful for checking `resources.json` loading the way GitHub Pages does it):
  `python3 -m http.server 8000`, then open http://localhost:8000.
- To run the Python solutions and tests for the AI/ML guide:
  `python3 resources/ai-ml-engineer-prep/solutions/run_all.py`
- To check every example in the DSA guide (about 1,000 calls):
  `python3 resources/dsa-master-guide/solutions/test_dsa.py`
- To re-run every Python and SQL example in the System Design and Python and SQL guides (each compares its output with the recorded text):
  `python3 resources/system-design-guide/solutions/test_snippets.py` and `python3 resources/python-sql-guide/solutions/test_snippets.py`

## Repository layout

```
index.html                 landing page; card grid built from resources.json
resources.json             list of resources (id, title, description, tags, path, updated)
assets/base.css            design system: tokens, light/dark, components, print
assets/base.js             theme, TOC drawer + scroll-spy, search, progress, copy, quiz engine, shortcuts
templates/                 starter page that shows every component
resources/<id>/            one folder per resource
tools/                     optional maintenance scripts (Python 3, standard library only):
                           check_site.py, embed_code.py, build_interview.py, sync_resources.py
```

## Add a new resource in 3 steps

1. **Create the folder and page.** Copy `templates/resource-template.html` to `resources/<new-id>/index.html`. Set `data-resource="<new-id>"` on `<html>`. Progress and quiz data are stored under `lr:<new-id>:<key>`, so resources never collide. For more than one page, add a `parts.js` manifest (copy `resources/ai-ml-engineer-prep/parts.js`) to get the parts menu and hub progress bars.
2. **Register it.** Add an entry to `resources.json`:
   ```json
   { "id": "<new-id>", "title": "...", "description": "...", "tags": ["..."], "path": "resources/<new-id>/index.html", "updated": "YYYY-MM-DD" }
   ```
3. **Sync the offline copy.** Run `python3 tools/sync_resources.py`. This copies `resources.json` into `index.html`, because browsers block `fetch()` on `file://`, so the landing page carries an inline copy. Then run `python3 tools/check_site.py` to validate links, ids and section counts.

## Page features (driven by markup, see the template)

- `section[data-track][id]` gets a "Mark as done" checkbox. The data feeds the progress bar.
- `pre > code.lang-py` gets syntax highlighting and a Copy button. Tables and code scroll horizontally inside their own wrapper.
- `.quiz` with `data-type` set to `single`, `multi`, `fill` or `numeric`, plus `data-answer`, becomes an interactive question. Wrap questions in `.quiz-set[data-set]` with a `.quiz-controls` element to get shuffle, reset, retry-missed and scoring.
- `<details class="recall">` creates a click-to-reveal self-check.
- Inline SVG diagrams use the `d-*` classes from `base.css`, so they follow the light or dark theme.
- Keyboard: `/` search, `t` light or dark theme (default follows the system), `j`/`k` next or previous section, `?` help, `Esc` close.
- Print: the page expands every `details` element and quiz explanation, and hides navigation.

## Deploy on GitHub Pages

1. Push the repository to GitHub.
2. Go to Settings, then Pages. Under Build and deployment, pick "Deploy from a branch", then select your branch and the `/ (root)` folder. Save.
3. After a minute the site is at `https://<user>.github.io/<repo>/`. All links are relative, so no configuration is needed. A `.nojekyll` file is included so GitHub serves the files exactly as they are.

## Conventions

- Plain HTML, CSS and JS only. Don't add CDNs, external fonts or trackers.
- Relative paths only.
- Mobile first: tap targets of at least 44px, body text of at least 16px, no hover-only features.
- localStorage keys: `lr:<resource-id>:<key>`. The theme is shared under `lr:site:theme`.
- Code shown on a page should be embedded from a tested file: `<code class="lang-py" data-embed="solutions/x.py"></code>`, then run `python3 tools/embed_code.py`.
- Interview questions live in `resources/<id>/data/interview-questions.json`. Pages show them through `<div class="iq-list" data-iq="Topic"></div><!-- /iq -->` (one topic) or `<div class="iq-bank"></div><!-- /iqbank -->` (all). Run `python3 tools/build_interview.py` after editing.
- Before committing, run `python3 tools/check_site.py` (links, anchors, ids, quiz keys, section counts, no em or en dashes).
