# How this repository was made (Mexico)

This file is written by the build on 2026-10-28, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| Cámara de Diputados, LeyesBiblio: Constitución Política de los Estados Unidos Mexicanos (texto vigente, consolidated PDFs), read through the Internet Archive Wayback Machine | <https://www.diputados.gob.mx/LeyesBiblio/pdf/CPEUM.pdf> | 2026-10-28 | 78 | Public legal text; Cámara de Diputados del H. Congreso de la Unión, Secretaría de Servicios Parlamentarios. Archived copies: Internet Archive. |
| Cámara de Diputados: reformas constitucionales por orden cronológico (ref/cpeum_crono.htm) | <https://www.diputados.gob.mx/LeyesBiblio/ref/cpeum_crono.htm> | 2026-10-28 | 1 | Public information, Cámara de Diputados. |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitucion` | Constitución Política de los Estados Unidos Mexicanos | 117 | 2006-04-08 to 2026-10-08 |

The build made 138 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 120 | one law on its in-force day |
| 17 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-10-28.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 290 laws in the record.
- 237 tags.

## Dates

Each commit is dated at noon (America/Mexico_City) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Código Civil Federal art. 3: laws bind and take effect three days after publication in the Diario Oficial de la Federación; art. 4: a law that fixes its own start day binds from that day https://www.diputados.gob.mx/LeyesBiblio/pdf/2_110121.pdf

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-28
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-28 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/mexico-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `f5a4f88bc462ee0fee93926e3a9e88d29cd2906a943f31727333460afa636d2e` (5323735 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `2c539b066cea838fa825f02014ab5cfef2750fd6` |
| parse.py | `1368e636d133d585644f19c7b06352632f10b5d5` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

Not yet run for this build.

Not yet run for this build.

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Constitución: history starts at the oldest consolidated copy the Internet Archive holds (Cámara de Diputados pdf/1.pdf captured 20060813201302, last reform DOF 2006-04-07); 1917-2006 is not rebuilt, and the first version names the 170 earlier decrees.
- Constitución: 8 archived copies cut off at exactly 1 MiB were dropped (20190923002305, 20200918083844, 20210125021153, 20210927164804, 20220516151601, 20230608153526, 20230925125132, 20241203191611); for each last-reform date the newest copy is used (78 copies from 90 readable ones).
- Constitución: in-force dates come from each decree's first transitorio that speaks of entry into force ("al día siguiente de su publicación" = DOF + 1, "el día de su publicación" = DOF, a fixed date, or "a los N días"); otherwise Código Civil Federal art. 3 (three days after publication). Counts: Código Civil Federal art. 3 (tres días después de su publicación): 1; a los 120 días de su publicación: 1; día de su publicación: 2; día siguiente al de su publicación: 116.
- Constitución: where a decree puts single provisions in force on later dates (for example the 2014 political-electoral reform, DOF 10-02-2014), the whole article takes effect on the decree's general date; the staggered dates are in the decree's transitorios unit.
- Constitución: credits come from the publisher's paragraph notes ("Párrafo reformado DOF dd-mm-yyyy", in copies from 2013 on, read for every unit across all later copies): a note date inside the gap between two copies names the decree published that day. Several decrees that day, or no note date: the decree whose own title names the article, only if exactly one fits. Otherwise the change is unexplained and dated on the copy's last-reform day. Counts: {'credited_notes': 413, 'credited_title': 0, 'credited_self': 120, 'unexplained': 140}.
- Constitución: units are the preámbulo, the headings (estructura), articles 1-136, the 1917 transitorios and one unit per reform decree's transitorios as the publisher prints them; the publisher's notes and cover page are left out of the text.
- Constitución: copies before 2013 print the transitorios of only some earlier decrees; transitorios the publisher added later for decrees before the gap arrive as unexplained publisher changes.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote fetch.py, reforms.py and parse.py. No model output is used as legal text, dates or credits: all come from the cached official copies by deterministic code.
