# Reproduce

Everything here can be rebuilt from SCJN Legislación with the scripts in `scripts/mexico-law/` of the Lexifina
repository (private). Nothing in the legal text was written by an AI, and no model runs at build time.

## Sources
- SCJN Legislación, https://legislacion.scjn.gob.mx, retrieved up to 2026-10-28: 1895 requests
  (2026-10-28T22:56:28 to 2026-10-29T00:22:48). See `SOURCES.md` for robots.txt, terms and the sources not used.
- Fetch rate: one process, at most 3 requests at a time, a 0.6 s pause before each request, every answer (errors
  too) cached; the fetcher stops at once on any bot challenge.
- Data: `DATA-SHA256SUMS` lists the sha256 of every cached file (gzip, mtime 0); sha256 of that list:
  `96a7dbb2cf5f1486af69012f6fcfac416880b69874e6ff4b07aaa182b0956b3f`.

## Commands, in order
```
cd scripts/mexico-law
python -E -s catalogue.py                 # federal, in force: Constitución, Código, Ley -> cache/catalogue.json
python -E -s fetch.py --threads 3         # records, Word texts and extractos of every chosen law
python -E -s build.py <checkout> --today 2026-10-28 --branch wip
python -E -s check_repo.py <checkout>     # git text == parsed SCJN text for every version
python -E -s check_words.py <checkout>    # letters and digits of every version == raw Word XML
python ../global-law/check_corpus.py <checkout>
```
`build.py` refuses a non-empty target that is not an earlier build, keeps `origin`, and writes the history with one
streamed `git fast-import`. The documentation commit is dated by `--today` (the retrieval day), never the run day.

## Decisions made by hand
- Chosen laws: SCJN's federal ordenamientos "VIGENTE" of type CONSTITUCION, CODIGO (codes of conduct and of ethics
  dropped) and LEY.
- Text: one Word paragraph per line, whitespace collapsed, soft hyphens removed; the version banner ("TEXTO
  ORIGINAL." / "ÚLTIMA REFORMA PUBLICADA ...") is left out because it changes in every version.
- An article starts at a paragraph beginning "Artículo N" / "Art. N" / "ARTICULO N" (with o., Bis, Ter, letters);
  the headings and editor's notes just before it belong to it. The body ends at the first "TRANSITORIOS" heading;
  each later "D.O.F. <date>." block is one decree's transitorios.
- Entry into force: the first transitorio that speaks of it, read by `inforce.py`; default Código Civil Federal
  art. 3 (three days after publication) when none is found. Fe de erratas and aclaraciones: day of publication.
- Time zone America/Mexico_City hard-coded: UTC-6; summer time (UTC-5) from the first Sunday of April to the last
  Sunday of October 1996-2022 (2001: 6 May to 30 September); abolished from 30 October 2022.

## Tools
Python 3.12.10, requests 2.34.2, git version 2.46.0.windows.1. Script sha256:
- scjn.py `2db44e15f4b69b0285a94223cfb211e92542653be26b1f8f16817db2f988b9c0`
- catalogue.py `e9d5107e2daa832273b63f1e70bcd56a8e8df8acd8049752203cc277cf2ce7d5`
- fetch.py `bdf0b4eb3e92c92a88c9d97b4bed32e352b293ba9e1c6c0f8f593d6687138858`
- docx_text.py `53a8dfce5d23737971bc207c629a83e5dcf46247d8acaaa36d18cd6977063303`
- parse.py `327b8b9106d59fcceb5491757a63003770d85b48b6ff37d45c455c52f4d9012b`
- inforce.py `0cd17d410c6ba14c7cbab9df683f6c1802490cb29ce23e79a0ef4aa9eeeb2f61`
- build.py `fc750cf4c9a7adf9b3bc502605485cae6ed13cf6bdd2c5a2f35c5c34a0a4a5e5`
- docs.py `e0c4ca5609c047fab4319479dd0b8ff1c74ff115f191dc3c17168f8bea814a10`
- check_repo.py `a537ae119080a8a1dcf474cc3cd229e475e484953391af33493c416806028979`
- check_words.py `caee67a63ffc47d950d585b82a76b9b28ae814c8cd8b135e02d3eba721410530`

## AI
Built by Claude Code with Claude Opus 5.5 (`claude-opus-5-5`): it chose the source after the gates, wrote the
scripts, and ran them. No AI wrote or edited legal text; commit subjects and bodies are built by code from SCJN's
records and extractos. No model runs at build time.

## Result
606 commits on `wip`, 0 on `future`. Rebuild check: see PROGRESS in the builder folder.
