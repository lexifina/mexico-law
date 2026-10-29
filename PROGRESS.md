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
- [x] fetch all records (`--no-word`): 313 laws (1 constitution, 9 codes, 303 leyes), 3,755 DOF records,
      3,629 with a Word file.
- [ ] fetch Word + extractos (4 threads): STOPPED by the user's stop at 2026-10-29 ~00:27, after 9 of 313 laws
      (Constitution, the 9 codes). Small laws take 1-2 s a file; the big codes ~8 s. About 3,000 files are left,
      roughly an hour. A file being written when the fetch was killed could be truncated: if a build fails to
      gunzip one, delete that file and rerun fetch.py.
- [x] wip pushed: bfdfdae, 606 commits, 9 complete laws (Constitution + 8 codes). check_repo: 0 failures
      (605 commits, 504 version days), check_words: 701/701 texts, check_corpus pass, test_corpus OK
      (on the 343-commit build), test_noon clean.
- [ ] full build, all checks, then main ONCE (force-push over the placeholder), then append-only.
      Main has NOT been pushed: it still holds only the placeholder ee03ec1.

## Fixes made during the work (all in the scripts)
- parse.py: article numbers like `1,000`, `410 A`, `32-B Bis`, `30 SEXTUS`/`SÉPTIMUS`; PARSE_VERSION 5.
- fetch.py: codes of conduct/ethics are dropped wherever CONDUCTA/ETICA appears in the title.
- build.py: only laws whose fetch is complete are built (`complete()`); check_repo/check_words use the same filter.
- Commits from different laws are not merged: SCJN extractos are per law, and one DOF edition can carry several
  decrees, so one commit per law per publication (a deviation from "one commit per act across laws").

## Still to do before main
- Finish the fetch; run survey.py to catch article-numbering patterns in the leyes (duplicates show as `~2`).
- `--today 2026-10-29` (last retrieval day) for the final build; build twice and compare heads (determinism).
- Hand-check tools/in_force_on.py on 2-3 provisions at several dates (e.g. Constitution art. 3 around
  2019-05-15/16, art. 1 around 2011-06-10/11).
- Write memory `mexico_law_history.md`, add it to MEMORY.md, and SendMessage gitlaw-global when main is pushed.

## Next commands
```
cd C:/Users/alany/Documents/lexifina/scripts/mexico-law
python -E -s fetch.py --threads 4                       # resumable; everything cached
sh push_wip.sh                                          # checks GitHub for foreign commits, builds wip, pushes
python -E -s build.py C:/Users/alany/Documents/mexico-law --today 2026-10-29 --branch wip
python -E -s check_repo.py C:/Users/alany/Documents/mexico-law --branch wip
python -E -s check_words.py
cd C:/Users/alany/Documents/mexico-law && git push -f origin wip    # check GitHub for foreign commits first
```

## Last pushed
- wip: bfdfdae (606 commits) + a PROGRESS.md commit on top
- main: not pushed (placeholder ee03ec1)
