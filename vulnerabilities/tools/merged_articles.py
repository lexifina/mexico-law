"""Hand-check helper: article files at the pin that hold the headings of other articles (articles without a file of
their own), and article files that hold a decree's transitional provisions.

    python -X utf8 merged_articles.py <bare repo> <sha>

An article heading is a line that starts "Artículo", "ARTÍCULO", "ARTICULO" or "Art." and a number; a file's own
heading is its first line. Prints, per act, the files and the number of other headings each holds, and the totals."""
import collections, re, subprocess, sys

repo, sha = sys.argv[1], sys.argv[2]
git = lambda *a: subprocess.run(["git", "-c", "core.quotepath=false", *a], cwd=repo, capture_output=True).stdout.decode("utf-8")
per_file = collections.defaultdict(list)
for line in git("grep", "-n", "-E", r"^(Artículo|ARTÍCULO|ARTICULO|Art\.)\s+[0-9]", sha, "--", "*/art-*.md").splitlines():
    _, path, ln, text = line.split(":", 3)
    if int(ln) > 1:
        per_file[path].append(text)
per_act = collections.defaultdict(list)
for path, heads in per_file.items():
    per_act[path.rsplit("/", 1)[0]].append((path.rsplit("/", 1)[1], len(heads), heads[0][:60]))
for act, rows in sorted(per_act.items(), key=lambda kv: -sum(r[1] for r in kv[1])):
    print(f"{sum(r[1] for r in rows):5d}  {act}  ({len(rows)} files)")
    for r in sorted(rows, key=lambda r: -r[1])[:3]:
        print(f"         {r[0]}: {r[1]}  e.g. {r[2]}")
print("headings in another article's file:", sum(len(h) for h in per_file.values()), "in", len(per_file), "files of", len(per_act), "acts")
print("\ntransitional provisions inside an article's file:")
for line in git("grep", "-n", "-i", "-E", r"^(disposiciones |artículos |articulos )?transitori(o|a)s?\b.{0,40}$", sha, "--", "*/art-*.md").splitlines():
    print("  ", line.split(":", 1)[1][:120])
