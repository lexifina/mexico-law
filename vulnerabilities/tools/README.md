# Tools

The scripts behind this Mexico-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/mexico-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only mexico-law, its commit and its
language (`es`). `build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py`, `patch_mx.py`,
`merged_articles.py` and `config.json` sit two folders above the scripts.

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, maps paths to the folders since the move (`map_moved.py`), adds this repository's history rows, and runs the detectors (`bash run.sh <shards>`) |
| `add_root.py` | Builds the history rows from this repository's own commits (global-law replays it only up to an earlier commit), so the history detectors read every change |
| `map_moved.py` | Rewrites the paths in the history table to each act's folder since the move of 11 November 2026 (`data/paths.json`), so that an act's history is not split in two at the move; `run.sh` runs it after the history is indexed |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category (here the one flag, with the old and the new date in one sentence) |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in Spanish and English, light and dark |
| `config.json` | The repository, the Spanish category names, the folders and files that are not law, and the chart's labels |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts (`python -X utf8 patch_detectors.py <scripts dir>`; a fix already in place is skipped) |
| `patch_detectors_vi.py`, `patch_es.py`, `patch_ca.py`, `patch_en.py`, `patch_de.py`, `patch_en_et.py`, `patch_co.py`, `patch_sv.py`, `patch_pt.py`, `patch_ru.py`, `patch_r18.py`, `patch_xk.py`, `patch_mo.py`, `patch_lu.py`, `patch_li.py` | The same for the Vietnamese, Spanish, Catalan, English (two rounds), German, Colombian, Salvadoran, Brazilian, Russian, Kosovar, Macanese, Luxembourg and Liechtenstein blind spots and a round on currencies, found by other runs; this run's copy carries them all. Of them, `patch_es.py`'s and `patch_co.py`'s date forms ("hasta el día 31 de diciembre de 2020", "1o. de enero", "a más tardar el 31 de diciembre de 2020") also serve Mexican Spanish |
| `patch_mx.py` | The fix below, made for this repository |
| `apply_patches.py` | Applies every patch above once, in order (`patch_mx.py` last), recording each in `.kit_patches.json` beside the scripts so that none runs twice (`python -X utf8 apply_patches.py <scripts dir>`) |
| `redo.py` | Runs the patches, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews] [--full]`; `--full` runs every step again through `run.sh`; `EMBED_FONTS` names the script that embeds the chart's fonts). It applies the patches through the `apply_patches.py` beside it, `patch_mx.py` among them; only `--full` runs the publisher-note scan again |
| `merged_articles.py` | Hand-check helper: the article files at the commit read that hold other articles' headings, and those that hold a decree's transitional provisions (`python -X utf8 merged_articles.py <bare repo> <sha>`; the counts in the README) |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
It was run as `bash run_triage.sh '^(data/|tools/|README|REPRODUCE|LICENSE|jurisdiction\.json)|/README\.md$'`. The 40
strongest lapsed time limits were all in law texts, so the two reviews of that category drew the same flags; `build_vulns.py`
keeps the later review of each flag.

Changes made for this repository:

- `add_root.py` counts as law, besides decrees and agreements (`Kind: law`) and the oldest available text of an act
  (`publisher`), which the kit already counted, the Supreme Court rulings that struck out or conditioned text
  (`Kind: court`, 40 commits): 2,483 of the 2,504 commits. The other 21 are documentation (one with `Kind: documentation`,
  20 without an `In-force:` trailer). Without `court`, a provision the Court invalidated would look, to the history
  detectors, as if it had never changed. The first run was made without it; `add_root.py` and every later step of `run.sh`
  were then run again (repeal gaps went from 55 to 56; the other counts did not change).
- `patch_mx.py`, publisher notes: the Cámara de Diputados marks a slip in the published text with "(sic DOF 03-02-1983)",
  the DOF issue that carried it, sometimes with the right word first ("(funcionario, sic DOF 20-01-1975)"). The scan read
  only "(sic)" and "[sic]": publisher notes went from 6 to 55. `detectors/notes_scan.py` was then run again, before the
  build; the model does not review this category.
- `config.json` counts as not law `data/`, `tools/` and the top-level files (`README`, `REPRODUCE.md`, `LICENSE`,
  `jurisdiction.json`), and each act's `README.md` (its list of provisions) wherever it is. Each act folder, including
  the 56 closed acts that keep their old top-level folder, is law. It gives the chart shorter Spanish labels for the two
  reference categories, which otherwise ran into their bars.
- `pins.json` already named the language (`es`); Spanish month names were already in the time-limit search.
