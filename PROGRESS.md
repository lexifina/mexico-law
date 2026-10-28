# Mexico federal law (lexifina/mexico-law): progress

Corpus `mx/federal/acts`. Source: SCJN "Legislación" (legislacion.scjn.gob.mx), Suprema Corte de Justicia de la Nación.
Builder: `C:/Users/alany/Documents/lexifina/scripts/mexico-law/`; checkout `C:/Users/alany/Documents/mexico-law`.

## Gates (2026-10-28)
- [x] diputados.gob.mx: unreachable from this machine (TCP 80/443 time out); dropped.
- [x] dof.gob.mx: robots.txt disallows `/nota_detalle.php?` (decree pages) for every agent; not used.
- [x] SCJN Legislación: no robots.txt (404); terms allow copying for informative/academic use with the URL and the date of consultation, no commercial use, no ban on automated access; LFDA art. 14 fr. VIII: no copyright in legislative texts. Incapsula script present, no challenge seen (the fetcher stops on any challenge).
- [x] Repo held only the placeholder "Mexico: sources, before any law"; no other branches.

## Data
- `catalogue.py`: federal, in force, type Constitución (1) / Código (9 real codes, codes of conduct dropped) / Ley (303).
- `fetch.py`: for each law, every reform record (pub date, category, DOF number) + the record's Word file = the whole
  consolidated text after that publication + the extracto (decree summary with its transitorios).
- Constitution: 302 records, 301 Word texts, 1917-02-05 .. 2026-10-07.

## Checklist
- [x] gates, catalogue
- [x] fetch: Constitution (+ 9 laws whose title names it)
- [x] builder: parse.py (docx -> files), inforce.py (first transitorio), build.py (fast-import), docs.py
- [x] wip push: Constitution + 9 laws, 343 commits (check_repo 0 failures, check_words 343/343, check_corpus pass,
      test_corpus OK, test_noon clean)
- [ ] fetch all records (`--no-word`), then Word + extractos, 4 threads. SCJN takes ~8 s to make each Word file,
      so ~25-30 files a minute: the full set takes many hours. wip is rebuilt from the laws whose fetch is complete.
- [ ] checks on the full build, main push

## Next commands
```
cd C:/Users/alany/Documents/lexifina/scripts/mexico-law
python -E -s fetch.py --threads 4                       # resumable; everything cached
python -E -s build.py C:/Users/alany/Documents/mexico-law --today 2026-10-28 --branch wip
python -E -s check_repo.py C:/Users/alany/Documents/mexico-law --branch wip
python -E -s check_words.py
cd C:/Users/alany/Documents/mexico-law && git push -f origin wip    # check GitHub for foreign commits first
```

## Last pushed
- wip: 45d0153 (Constitution + 9 laws)
