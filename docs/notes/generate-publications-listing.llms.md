# Autogenerate a Quarto publications listing from Excel (xlsx → YAML → custom listing)

tool

quarto

Author

Gang He

Published

April 10, 2026

## What problem does this solve?

Editing a long **publications list** as raw YAML is error-prone and awkward for researchers. Instead, import publications from a BibTeX file or maintain publication rows in **Excel** (`publications.xlsx`), run **`xlsx_to_yml.py`** to produce **`publications.yml`**, and let Quarto’s [**custom listing**](https://quarto.org/docs/websites/website-listings.html#custom-listings) plus your own **`pub-listing.ejs`** and **`pub-listing.css`** render the page with categories, filters, links, and badges as your template defines.

In this repository the script lives at `files/scripts/xlsx_to_yml.py`, and `_quarto.yml` runs it under `pre-render` before each build when needed (see below).

## Prerequisites

1.  **Python 3** and:

    ``` bash
    pip install openpyxl
    ```

    Optional: install `pyyaml`; the script will try to validate the written YAML with PyYAML if available.

2.  Place **`publications.xlsx`** in the project root (next to `_quarto.yml`). By default the script reads that file and writes **`publications.yml`**; you can pass different paths on the command line.

3.  Copy **`pub-listing.ejs`** and **`pub-listing.css`** from the template repo (or author your own), and keep them where your listing `.qmd` (e.g. `publications.qmd`) expects—often alongside that page.

## Step 1: Prepare the spreadsheet

The **first row must be headers**, and header text must match the table below exactly (case and spaces matter). Columns not in the mapping become lowercase hyphenated keys; sticking to the table avoids stray fields. For first time users, especially if you have a long list of publications, you can use bib file to create the spreadsheet using online tools, such as this [one](https://paperpile.com/t/ris-to-excel-converter/).

| Excel column | YAML key | Notes |
|----|----|----|
| Section | `section` | Drives Quarto `include: section: "..."` blocks, e.g. `Selected Work` vs `Peer-reviewed Journal Paper` |
| Authors | `authors` | Markdown allowed (bold, `*` for corresponding author, etc.) |
| Year | `year` | Prefer a number; the script coerces to int when possible |
| Date | `date` | Optional; useful for sort or display |
| Title | `title` | Paper title |
| Paper Link | `path` | Primary URL (site post or external) |
| Journal | `journal` | Journal name |
| Volume | `volume` | Volume |
| Issue | `issue` | Issue |
| Pages | `pages` | Pages |
| DOI | `doi` | DOI |
| PDF | `pdf` | PDF URL |
| Preprint | `preprint` | Preprint URL |
| SharedIt | `sharedit` | Share / readcube-style link |
| Supplemental Information | `supplemental` | Supplementary materials |
| GitHub | `github` | Repository |
| Code | `code` | Code archive (e.g. Zenodo) |
| Data | `data` | Data URL |
| Highly Cited | `highlycited` | Flag; rendering depends on EJS/CSS |
| Hot Paper | `hotpaper` | Flag |
| Awards | `awards` | Awards text |
| Media Coverage | `mediacoverage` | Press links (e.g. `|` inside the cell; parsed by template) |
| Invited Presentation | `invitedpresentation` | Invited talk, etc. |
| Categories | `categories` | **List**: separate with comma, semicolon, or pipe, e.g. `2025, selected, peer-reviewed` |

Empty rows are skipped; rows that yield no fields after parsing are omitted from the YAML.

## Step 2: Run the converter

From the project root (default `publications.xlsx` → `publications.yml`):

``` bash
python files/scripts/xlsx_to_yml.py
```

Or pass explicit paths:

``` bash
python files/scripts/xlsx_to_yml.py path/to/in.xlsx path/to/out.yml
```

**Incremental runs:** if the output file already exists, the script compares modification times of `publications.xlsx` and `publications.yml` and **only regenerates** when Excel is newer, avoiding redundant writes. To force a rebuild:

``` bash
python files/scripts/xlsx_to_yml.py --force
```

## Step 3: Hook into Quarto (`pre-render`)

Under **`project`** in **`_quarto.yml`**, add `pre-render` so every `quarto render` / `quarto preview` runs the converter first (still subject to the “only if Excel changed” logic):

``` yaml
project:
  type: website
  pre-render:
    - python files/scripts/xlsx_to_yml.py
```

If your script sits at the repo root instead of `files/scripts/`, use `python xlsx_to_yml.py`.

## Step 4: Wire the publications page (YAML + custom template)

In **`publications.qmd`** (filename up to you), set `listing` with `contents: publications.yml`, `type: custom`, `template: pub-listing.ejs`, and use `include` to split listings by `section`. A minimal pattern matching this site:

``` yaml
title: "Publications"
listing:
  - id: selected-work
    contents: publications.yml
    type: custom
    page-size: 100
    categories: numbered
    template: pub-listing.ejs
    include:
      section: "Selected Work"
  - id: peer-reviewed
    contents: publications.yml
    type: custom
    page-size: 100
    categories: numbered
    template: pub-listing.ejs
    include:
      section: "Peer-reviewed Journal Paper"
css: pub-listing.css
```

In the body, use fenced divs whose **id** matches each listing **id**:

``` markdown
## Selected Work

::: {#selected-work}
:::

## Other Peer-reviewed Journal Papers

::: {#peer-reviewed}
:::
```

This site also uses a Lua filter when raw HTML from EJS interacts badly with Quarto’s listing wrapper; if you see stray `:::` in output, add `filters: [files/scripts/remove-stray-divfence.lua]` in `publications.qmd`.

## Examples and where to get the templates

- Live demo (academic template): [pub-listing example](https://drganghe.github.io/quarto-academic-website-template/pub-listing.html)
- Template docs and files: **[quarto-academic-website-template README](https://github.com/drganghe/quarto-academic-website-template/blob/main/README.md)**
- This site: [publications.html](https://drganghe.github.io/publications.html) and [`publications.qmd`](https://github.com/drganghe/drganghe.github.io/blob/main/publications.qmd) in the [repo](https://github.com/drganghe/drganghe.github.io)

After copying `pub-listing.ejs` and `pub-listing.css`, adjust CSS for your brand.

## Troubleshooting

**New papers missing after build**  
Confirm Excel is saved and that `publications.yml` is not newer than `publications.xlsx` unless you intend to skip conversion; run once with `--force`, then `quarto render`.

**YAML errors or empty listing**  
Verify headers match the table exactly. For tricky titles or authors, the script quotes YAML scalars; if it still fails, simplify the cell temporarily to isolate the issue.

**Local test without editing `_quarto.yml`**  
Run `python files/scripts/xlsx_to_yml.py`, then `quarto render publications.qmd` (or a full site render).

## Cheat sheet

| Step | Action |
|----|----|
| 1 | Maintain `publications.xlsx` with the correct column headers |
| 2 | Run `python files/scripts/xlsx_to_yml.py` (or rely on `pre-render`) |
| 3 | Point `publications.qmd` at `publications.yml` + `pub-listing.ejs` + `pub-listing.css` |
| 4 | `quarto render` and publish |

Day-to-day you only edit the spreadsheet; the site listing stays in sync with that data.

## Learn more

- [Quarto Academic Website Template](https://github.com/drganghe/quarto-academic-website-template)
- [Quarto Academic Website Examples and Tips](https://drganghe.github.io/quarto-academic-site-examples.html)
