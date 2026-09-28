"""Check which known-item records a block-based Boolean search string would retrieve.

Simulates a title/abstract/keyword search the way Scopus, Web of Science and
EBSCO treat it: case-insensitive, hyphens and punctuation split words,
`*` truncates the end of a word, quoted phrases must be adjacent words.
Blocks are ANDed; terms inside a block are ORed. `X NEAR/n (a|b)` means X
within n words of a or b, in either order.

Inputs (same folder):
  search-strategies.json  - one entry per search string, as blocks of terms
  benchmark-records.json  - titles, abstracts and author keywords of known items

Usage: python3 validate_search.py [strategy-name ...]
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def term_pattern(term):
    """A term is one word or a quoted phrase; each word may end in *."""
    return [w for w in re.findall(r"[a-z0-9*]+", term.lower().replace("-", " "))]


def word_match(pat, tok):
    return tok.startswith(pat[:-1]) if pat.endswith("*") else tok == pat


def find(term, toks):
    """Return True if the term (word or phrase) occurs in the token list."""
    near = re.match(r"(.+?)\s+NEAR/(\d+)\s+\((.+)\)$", term)
    if near:
        left, n, right = near.group(1), int(near.group(2)), near.group(3).split("|")
        lpos = positions(left.strip(), toks)
        rpos = [p for r in right for p in positions(r.strip(), toks)]
        return any(abs(a - b) <= n for a in lpos for b in rpos)
    return bool(positions(term, toks))


def positions(term, toks):
    pat = term_pattern(term)
    k = len(pat)
    return [i for i in range(len(toks) - k + 1)
            if all(word_match(pat[j], toks[i + j]) for j in range(k))]


def record_text(rec, short_title=False):
    title = rec.get("title_short") if short_title and rec.get("title_short") else rec["title"]
    return " | ".join([title, rec["abstract"], " ; ".join(rec.get("keywords", []))])


def evaluate(strategy, rec, short_title=False):
    toks = tokens(record_text(rec, short_title))
    hits = {}
    for block, terms in strategy.items():
        hits[block] = [t for t in terms if find(t, toks)]
    return hits


def main():
    records = json.loads((HERE / "benchmark-records.json").read_text())
    strategies = json.loads((HERE / "search-strategies.json").read_text())
    names = sys.argv[1:] or list(strategies)
    for name in names:
        strategy = strategies[name]
        print(f"\n=== {name}")
        for group, recs in records.items():
            found = 0
            for rec in recs:
                for short in ([False, True] if rec.get("title_short") else [False]):
                    hits = evaluate(strategy, rec, short)
                    ok = all(hits.values())
                    label = rec["id"] + (" (short title)" if short else "")
                    if not short:
                        found += ok
                    missing = [b for b, h in hits.items() if not h]
                    detail = "; ".join(f"{b}: {', '.join(h[:4]) or '-'}" for b, h in hits.items())
                    print(f"  {'FOUND ' if ok else 'MISSED'} {label:32} "
                          f"{'missing ' + '+'.join(missing) if missing else ''}\n         {detail}")
            print(f"  -> {group}: {found}/{len(recs)} retrieved")


if __name__ == "__main__":
    main()
