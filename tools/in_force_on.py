"""Print a Mexican federal law, or one article of it, as it stood on a date.

    python tools/in_force_on.py 2010-01-01 constitucion              # every file of the Constitution that day
    python tools/in_force_on.py 2010-01-01 constitucion 41           # article 41
    python tools/in_force_on.py 2026-01-01 codigos/codigo-penal-federal 7

Picks the version by the `In-force:` trailers (the real dates; commit dates before 1970 are clamped), so it is
right for any day in any time zone. Only the branch you have checked out is read (`main`); texts that apply after
the build day are on the `future` branch. Standard library only.
"""
import subprocess
import sys


def git(*args: str) -> str:
    return subprocess.run(['git', '-c', 'core.quotepath=off', *args], capture_output=True, text=True,
                          encoding='utf-8', check=True).stdout


def commit_on(day: str, path: str) -> str | None:
    """The newest commit in force on or before `day` that touched `path`."""
    fmt = '%H%x1f%(trailers:key=In-force,valueonly,separator=)'
    for line in git('log', '--no-merges', '--first-parent', f'--format={fmt}', 'HEAD', '--', path).splitlines():
        h, d = (line.split('\x1f') + [''])[:2]
        d = d.strip()
        if d and d <= day:
            return h
    return None


def order(name: str):
    stem = name.rsplit('/', 1)[-1][:-3]
    folder = name.rsplit('/', 2)[-2]
    rank = {'encabezado': 0}.get(stem, 1 if folder == 'articulos' else 2)
    head = stem.split('-')[0].split('~')[0]
    return (rank, int(head) if head.isdigit() else 10 ** 6, stem)


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    day, law = sys.argv[1], sys.argv[2].strip('/')
    unit = sys.argv[3] if len(sys.argv) > 3 else None
    path = f'{law}/articulos/{unit}.md' if unit else law
    h = commit_on(day, path)
    if not h:
        sys.exit(f'{path}: no text on or before {day} (not yet in force, or the file did not exist then)')
    names = git('ls-tree', '-r', '--name-only', h, '--', path).split('\n')
    names = [n for n in names if n]
    if not names:
        sys.exit(f'{path}: not in the text in force on {day} (removed by commit {h[:10]})')
    names.sort(key=order)
    out = sys.stdout.buffer
    p = subprocess.Popen(['git', 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    for n in names:
        p.stdin.write(f'{h}:{n}\n'.encode('utf-8'))
        p.stdin.flush()
        hdr = p.stdout.readline().split()
        size = int(hdr[2])
        body = p.stdout.read(size)
        p.stdout.read(1)
        if not unit:
            out.write(f'==> {n} <==\n'.encode('utf-8'))
        out.write(body)
    p.stdin.close()
    p.wait()


if __name__ == '__main__':
    main()
