# Mexican federal law in git

9 federal laws in force (1 constitution, 8 codes, 0 laws), every consolidated text the
Supreme Court's compilation (SCJN "Legislación") gives for them, one commit per decree taking effect, from
1889-10-10 to 2026-10-08. Each commit is a law (or a fe de erratas) taking effect; `git blame` names it.

Layout: `constitucion/`, `codigos/<name>/`, `leyes/<name>/`. Inside each: `encabezado.md` (title and
promulgation), `articulos/<n>.md` (one file per article, one paragraph per line; `2-bis`, `5-a` for Bis/letter
articles), `transitorios/original.md` and `transitorios/dof-<date>.md` (the transitorios of each amending decree,
as SCJN prints them).

## Questions, as git commands

| Question | Command |
|---|---|
| What did article 41 of the Constitution say on 1 Jan 2010? | `python tools/in_force_on.py 2010-01-01 constitucion 41` |
| The whole Federal Penal Code on a date | `python tools/in_force_on.py 2020-06-30 codigos/codigo-penal-federal` |
| Every change to an article, newest first | `git log --follow -p -- constitucion/articulos/41.md` |
| Word by word | `git log -p --word-diff -- constitucion/articulos/41.md` |
| Which decree wrote each paragraph | `git blame constitucion/articulos/41.md` |
| Everything one decree changed | `git show <commit>` |
| Everything in force by a date (raw git) | `git log --before="2010-01-01T23:59:59-06:00" -1` |
| Changes adopted but not yet in force | `git log main..future` |

PowerShell: `$r = git rev-list -1 --before="2010-01-01T23:59:59-06:00" HEAD; git show "$($r):constitucion/articulos/41.md"`.
Prefer `tools/in_force_on.py`: it reads the `In-force:` trailer, so it is right for dates before 1970 too (git
cannot store those; they are clamped to 1970-01-01).

## Dates

| Date | Where |
|---|---|
| Entry into force (the commit date, 12:00 Mexico City) | author/committer date and `In-force:` |
| Publication in the Diario Oficial de la Federación | `Published:` |
| Date of the decree (expedición) | `Issued:` |
| The date the decree states, when the commit is held back | `In-force-stated:` |

The entry into force is read from the decree's own first transitorio as SCJN's extracto quotes it ("entrará en
vigor al día siguiente de su publicación", "a los noventa días", "el 1o. de enero de 1987"). How each was read is in
`In-force-basis:`:

| Basis | Commits |
|---|---|
| day after publication | 336 |
| default | 75 |
| date named in the decree | 66 |
| N days/months after publication | 60 |
| day of publication | 28 |
| default (rule not read) | 17 |
| erratum | 17 |
| date named in the decree (from the transitorios in the text) | 4 |
| day of publication (from the transitorios in the text) | 1 |
| day after publication (from the transitorios in the text) | 1 |

`default` means no rule was found and Código Civil Federal art. 3 was applied (three days after publication); the
trailer says so. When the first transitorio has exceptions ("salvo lo dispuesto en ...") the commit carries
`In-force-exceptions: yes`: the commit date is the decree's general date, and the parts with other dates are
explained in that decree's `transitorios/dof-<date>.md`.

SCJN gives one whole text per publication, so a decree that takes effect later than a decree published after it
is printed in the later text too. Each commit changes only the files its publication changed, and commits are
ordered by entry into force, so the two are kept apart wherever they touch different files. Where they touch the
same file, SCJN's text of that file carries both, and the later commit is held back to the date the earlier change
took effect, and says so (`In-force-stated:`; 21 commits on main). Texts in force after 2026-10-28 are on the
branch `future`, never merged.

## How it is checked

- Every version's files, read back from git, equal the text built from SCJN's Word file for that publication
  (`check_repo.py`).
- An independent check compares the letters and digits of every version with the raw Word XML, read by a separate
  20-line reader (`check_words.py`), not by the build's parser.
- Rebuilding from the same cache gives the same commit hashes.

## What "author" means

The author of a commit is the decree whose DOF publication SCJN made that consolidated text for:
`Decreto DOF 02.06.2026 (144/2026 edicion vespertina)`, with an address that cannot exist (`...@dof.invalid`).
The first commit of a law is authored by the law itself when SCJN starts with the original publication; when it
starts later, the commit is labelled `Kind: baseline`. A fe de erratas is its own commit (`Kind: erratum`). Where
SCJN gives the same text after two publications of one day, the change is credited to neither
(`Kind: unattributed`, authored by the compilation, with a `Candidate:` line for each); there are
1 such commits.

## What it does not show

- Only federal laws in force today, as SCJN lists them; abrogated laws and regulations are not here.
- Publications SCJN has no Word text for are listed in `ledger.csv` (`text` = `no file`); their changes appear in the
  next text SCJN gives, credited to that publication.
- The editor's notes ("(REFORMADO, D.O.F. ...)", "N. DE E.") are SCJN's and stay in the text; they are not law.
- Blame credits whole paragraphs; use `--word-diff` to see the words.
- Words unchanged does not mean law unchanged: decrees that delay or condition a provision (in their transitorios)
  do not change its words.

## How it is built

From SCJN Legislación with the scripts in `scripts/mexico-law/` of the Lexifina repository; see `REPRODUCE.md`.
606 commits on `wip`, 0 on `future`; 632 DOF publications, 608 consolidated texts.

## Licence

See `LICENSE` and `SOURCES.md`. Mexican legislative texts carry no copyright (Ley Federal del Derecho de Autor,
art. 14, fr. VIII). Source: Suprema Corte de Justicia de la Nación, Legislación, <https://legislacion.scjn.gob.mx>
[Consulta: octubre de 2026].
