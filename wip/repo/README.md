# Mexico: law history in git

The law of Mexico as a git history: one file per provision, one commit per decree on the day it took effect, and the decree that made each change as the commit's author. `git blame` names the decree behind every paragraph; `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `mx/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitucion/` | Constitución Política de los Estados Unidos Mexicanos (1917) | 117 | From the text in force on 8 April 2006 (the oldest copy available, after the reform published in the DOF on 7 April 2006) to the reform of 7 October 2026: reforms 167 to 285, every one with its own commit |
| `lfpdppp/` | Ley Federal de Protección de Datos Personales en Posesión de los Particulares | 3 | The law of 2010 as enacted (in force 6 July 2010, never amended), the new law of the same name that replaced it (DOF 20 March 2025, in force 21 March 2025), and its reform of 14 November 2025 |

The per-act `README.md` in each folder lists every provision, how often it changed and when.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 82 of the Constitution say on 1 January 2020? | `python tools/en_vigor_el.py 2020-01-01 constitucion 82` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2020-01-01T23:59:59Z" main -- constitucion/art-082.md):constitucion/art-082.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2020-01-01T23:59:59Z" main -- constitucion/art-082.md; git show "$($r):constitucion/art-082.md"` |
| Which decree wrote each paragraph of art. 41? | `git blame constitucion/art-041.md` |
| Every change to art. 41, word by word | `git log -p --word-diff constitucion/art-041.md` |
| Every decree in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one decree changed | `git show law/decreto-cpeum-285` (tags `law/<key>` mark each decree's commit) |
| The whole Constitution on a date | `python tools/en_vigor_el.py 2010-01-01 constitucion` |
| The text on a version's day | `git show constitucion/2014-02-11` (tags `<act>/<in-force day>`) |
| A decree's own transitorios (in-force rules, deadlines) | `constitucion/transitorios-<DOF date>-<reform number>.md` |
| Decrees published but not yet in force | `git log main..futuro` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, America/Mexico_City, on the day the change took effect** (the in-force date). The DOF publication date is the `Published:` trailer, and the in-force day is in `In-force:`, which the tools read.
- **The in-force day is read from each decree's own first transitorio**: for reforms 167 to 285, "entrará en vigor al día siguiente de su publicación" is the day after publication (116 decrees), "el día de su publicación" the same day (2), and "a los 120 días de su publicación" 120 days later (1, reform 193). A fixed date in the transitorio would be used as given.
- **Default rule.** Código Civil Federal art. 3: laws "obligan y surten sus efectos tres días después de su publicación en el periódico oficial"; art. 4: a law that fixes the day it starts binds from that day. The default is used only where no transitorio can be read (the erratum of 25 June 2009).
- **Staggered dates are not split.** Some decrees put single provisions in force later (for example the political-electoral reform of 10 February 2014, whose provisions on arts. 65, 69, 74, 76, 83 and 89 start on 1 December 2018). Here the whole article changes on the decree's general in-force day; the later dates are in the decree's transitorios file, which is part of the record.
- **The Cámara prints a reform the day it is published**; here it appears only on its in-force day, so no wording appears before its decree applies.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a change that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- Health checks: no merge commits on `main`, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse with `git interpret-trailers --parse`.
- **Against the official text today:** the last version equals the Cámara de Diputados' consolidated text as archived on 10 October 2026 (last reform DOF 07-10-2026), provision by provision. Read a second, independent way (plain text, notes removed), that copy contains every one of the record's 4,100 paragraphs verbatim, and they cover 99.9% of its body text; the rest is the cover page and the Cámara's notes. The same check passes for all 78 copies used (223,778 paragraphs, none missing).
- Every version carries the sha256 of the archived PDF it was read from and the capture's address.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the decree that made the change, with an e-mail address that cannot exist (`decreto-cpeum-285@diputados.invalid`), so `git blame` and `git log --author` name decrees. Decrees are numbered as in the Cámara's chronological list of constitutional reforms. The committer is always Lexifina.

- **Credits come only from the source.** From 2013 the Cámara marks each paragraph with the reforms that touched it ("Párrafo reformado DOF 10-06-2011, 29-01-2016"). A changed provision is credited to a decree when such a note, in that copy or any later one, gives the DOF date of a decree published between the two copies compared. When several decrees were published that day, it is credited only if exactly one decree's title fits the article. Each decree's transitorios file is credited to that decree.
- **Unexplained changes** are committed by the publisher, the Cámara de Diputados, and labelled "unexplained" (17 commits): mostly the Cámara's own proofreading (accents, commas, "sic" notes, in 2008 and 2013), transitorios of 1993-2004 decrees that it added to its compilation in 2020, and three changes that two decrees of the same day could each have made (art. 73 on 12 October 2011, art. 43 on 17 May 2021, art. 41 on 2 June 2026).
- **Errata** ("Fe de erratas") printed in the DOF are commits of their own; the erratum of 25 June 2009 corrects art. 16.
- Blame credits whole lines (one paragraph per line). In a provision written by several decrees, use `git log -p --word-diff` to see exactly which words each changed.

## What it does not show

- **The Constitution before April 2006.** The Cámara de Diputados keeps only the current text and each decree as published; the oldest consolidated copy the Internet Archive holds runs to the reform of 7 April 2006. The first commit is "oldest version available" and names the 170 earlier decrees (1917-2006); that history is not rebuilt.
- **The text between two archived copies.** 98 distinct copies exist (2006-2026); 8 were cut off by the archive at 1 MiB and are not used, and for each reform date the newest copy is used (78). Where one copy is followed by several decrees, each decree's changes are separated only as far as the notes allow; a provision changed by two decrees between copies shows only its final wording, credited to both.
- **The Cámara's notes** are not in the text; they are used only to credit decrees.
- **Applicability data.** Where a transitorio says a provision applies only from a later election or to later cases, that is in the transitorios file, not in the dates.
- **The LFPDPPP as two laws.** The 2025 law abrogated the 2010 law and took its name; `lfpdppp/` shows both as one history, and the commit of 21 March 2025 replaces every article. Files with the same number (`art-016.md`) hold different laws' articles before and after that day.
- **Other acts.** Only the Constitution and the LFPDPPP so far; the Código Penal Federal and Código Civil Federal have archived copies but are not built yet.

## How it is built

`tools/fetch.py` lists every archived copy of the consolidated PDF in the Internet Archive and downloads each once (cached by the sha256 of the URL, every request logged), `tools/reforms.py` reads the Cámara's chronological list of reforms, `tools/parse.py` (Constitution) and `tools/parse_lfpdppp.py` (LFPDPPP) turn the cache into the corpus, and the shared builder `tools/build.py` writes the history with `git fast-import`. The same corpus always gives the same hashes. `REPRODUCE.md` records every command, tool version, data hash and decision, and the result of a hash-for-hash rebuild.

No AI model wrote or changed legal text. Claude Opus 5.5 wrote the scripts and chose the sources; see `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Names the amending act | Bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [Leyes Federales Vigentes, Cámara de Diputados](https://www.diputados.gob.mx/LeyesBiblio/) | Official legislation | current text only, plus each decree as published | yes, a note per paragraph from 2013, and a chronological list of reforms | no | Used, through the Internet Archive: the site does not answer from our machine. `pdf/1.pdf`, `pdf/1_<date>.pdf` and `pdf/CPEUM.pdf` (98 archived copies, 2006-2026) and `ref/cpeum_crono.htm` |
| [Internet Archive Wayback Machine](https://web.archive.org/) | Archive | yes, by capture | n/a | CDX API | Every copy used is pinned by its capture timestamp |
| [Diario Oficial de la Federación](https://www.dof.gob.mx/) | Official gazette | n/a | n/a | no | Not read; the Cámara gives the DOF date of every decree |
| [SCJN Legislación](https://legislacion.scjn.gob.mx/) | Official legislation | possibly | possibly | no | Not explored |
| [lex-mx](https://github.com/ingteranalvarez/lex-mx) | Volunteer git repo | current text, daily since 2026 | partly | n/a | Prior art; no text copied |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

The legal texts are official texts of the United Mexican States, as consolidated by the Cámara de Diputados del H. Congreso de la Unión (Secretaría de Servicios Parlamentarios) and archived by the Internet Archive. The Ley Federal del Derecho de Autor, art. 14, fracción VIII, excludes legislative texts from copyright protection. The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`.

This repository is not legal advice and not an official publication.

## En español

Historia del derecho mexicano en git: un archivo por disposición y un commit por decreto, fechado el día de su entrada en vigor y firmado por el decreto que hizo el cambio (`git blame` nombra el decreto de cada párrafo). Contiene la Constitución Política de los Estados Unidos Mexicanos desde el texto vigente el 8 de abril de 2006 (la copia más antigua disponible) hasta la reforma publicada en el DOF el 7 de octubre de 2026: las reformas 167 a 285. Contiene también la Ley Federal de Protección de Datos Personales en Posesión de los Particulares: la ley de 2010 tal como se publicó, la nueva ley del mismo nombre (DOF 20-03-2025) que la abrogó, y su reforma del 14 de noviembre de 2025.

- Texto vigente en una fecha: `python tools/en_vigor_el.py 2020-01-01 constitucion 82`
- Fechas: las del primer artículo transitorio de cada decreto; regla supletoria, art. 3 del Código Civil Federal (tres días después de su publicación).
- Autoría: cada cambio se atribuye a un decreto solo si una nota de la Cámara ("Párrafo reformado DOF …") da su fecha; lo que ninguna nota explica queda como "unexplained", a nombre de la Cámara de Diputados.
- Fuente: Cámara de Diputados del H. Congreso de la Unión, Leyes Federales Vigentes, copias del Internet Archive. Ningún modelo de IA escribió texto legal.
