"""Check a search string against a validation set of known-relevant papers.

Usage:  python3 search_check.py

Fetches each paper's title + abstract (Crossref, then Europe PMC; ERIC for
records without a DOI) and tests whether it would be retrieved by a
title/abstract/keyword search built from the blocks below.

Matching mimics common database behaviour: case-insensitive, hyphens split
words ("out-of-class" == "out of class"), `*` = right truncation, quoted
phrases = adjacent words. It is a simulation, not a live database run.
"""
import csv
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent

# --- Search blocks (keep in sync with search-string.md) ----------------------

P = ["neurodivers*", "neurodivergen*", "neurodevelopment*", "neuro-developmental",
     "intellectual disabilit*", "developmental disabilit*", "learning disabilit*",
     "learning difficult*", "learning disorder*", "learning difference*", "specific learning",
     "SpLD", "dyslexi*", "reading difficult*", "literacy difficult*",
     "attention deficit*", "hyperactiv*", "ADHD", "autis*", "ASD", "asperger*",
     "special educational need*", "special need*", "disabilit*", "disabled"]

CONCEPT = ["beyond the classroom", "beyond classroom*", "outside the classroom",
           "outside of the classroom", "out-of-class", "after-class", "after school",
           "out-of-school", "extracurricular", "extra-curricular", "self-access",
           "distance learning", "distance education", "informal*", "non-formal", "nonformal",
           "naturalistic", "non-instructed", "uninstructed", "incidental", "self-instruct*",
           "self-taught", "self-study", "autonom*", "independent learn*", "independent study",
           "self-directed", "self-regulat*", "extramural", "recreation*", "leisure",
           "digital*", "technolog*", "internet", "online", "web-based", "virtual", "comput*",
           "software", "mobile", "app", "apps",
           "game*", "gaming", "gamif*", "YouTube", "video*", "television", "TV", "screen",
           "screens", "media", "multimedia", "subtitl*", "caption*", "cartoon*", "audiovisual*",
           "unexpected bilingual*", "non-interactive", "noninteractive",
           "parent*", "caregiv*", "family", "families", "home", "home-based", "homework"]

CONTEXT_A = ["English", "EFL", "ESL", "EAL", "ELL", "ELLs", "TESOL", "TEFL", "ELT",
             "foreign language*", "second language*", "third language*",
             "additional language*", "L2", "L3", "non-native", "non-English"]

# Draft B: bare "English" replaced by English N3 (...)
NEAR_TERMS = ["learn*", "teach*", "lesson*", "class*", "homework", "proficien*", "acqui*",
              "vocabular*", "literacy", "reading", "skill*", "instruct*", "extramural",
              "exposure", "input"]
CONTEXT_B = [("english", NEAR_TERMS, 3)] + [t for t in CONTEXT_A if t != "English"]

DRAFTS = {
    "Draft A": {"P": P, "Concept": CONCEPT, "Context": CONTEXT_A},
    "Draft B": {"P": P, "Concept": CONCEPT, "Context": CONTEXT_B},
}

# --- Validation set ----------------------------------------------------------

# Papers the review must retrieve (supplied by the author, 2026-09-28)
TARGETS = [
    ("Alexandra et al. 2025", "10.52217/ijlhe.v8i1.1769"),
    ("Blazquez-Arribas et al. 2020", "ERIC:EJ1242672"),
    ("Pfenninger 2015", "10.14746/ssllt.2015.5.1.6"),
    ("Schurz 2026", "10.1075/itl.25021.sch"),
    ("Torsani 2025", "10.54855/callej.252626"),
]

# Author keywords where the publisher page exposed them
KEYWORDS = {
    "10.52217/ijlhe.v8i1.1769": "Foreign Language; Perspectives; Potentially Dyslexic; "
                                "Teaching English; Y-Generation Parents",
    "10.14746/ssllt.2015.5.1.6": "dyslexia; L3 acquisition; multisensory instruction; "
                                 "intervention; literacy skills",
}


def get_json(url, retries=3):
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code < 500 or attempt == retries - 1:
                raise
            time.sleep(2 ** (attempt + 1))


def strip_tags(text):
    return html.unescape(re.sub(r"<[^>]+>", " ", text or ""))


def fetch(record_id):
    """Return title + abstract (+ keywords) for a DOI or an ERIC id."""
    if record_id.startswith("ERIC:"):
        q = urllib.parse.quote(f"id:{record_id[5:]}")
        doc = get_json(f"https://api.ies.ed.gov/eric/?search={q}&fields=title,description&format=json")
        doc = doc["response"]["docs"][0]
        return f"{doc['title']} {doc['description']}"
    text = ""
    try:
        m = get_json("https://api.crossref.org/works/" + urllib.parse.quote(record_id))["message"]
        text = " ".join(m.get("title", []) + m.get("subtitle", [])) + " " + strip_tags(m.get("abstract"))
        has_abstract = bool(m.get("abstract"))
    except Exception:
        has_abstract = False
    if not has_abstract:
        q = urllib.parse.quote(f'DOI:"{record_id}"')
        res = get_json("https://www.ebi.ac.uk/europepmc/webservices/rest/search"
                       f"?query={q}&resultType=core&format=json")["resultList"]["result"]
        if res:
            r = res[0]
            kws = "; ".join(r.get("keywordList", {}).get("keyword", []))
            text = f"{r.get('title', '')} {strip_tags(r.get('abstractText'))} {kws}"
    return f"{text} {KEYWORDS.get(record_id, '')}"


# --- Matching ----------------------------------------------------------------

def words_of(text):
    return re.findall(r"[a-z0-9]+", text.lower())


def word_match(pattern, word):
    return word.startswith(pattern[:-1]) if pattern.endswith("*") else word == pattern


def phrase_in(term, words):
    parts = [p for p in re.split(r"[^a-z0-9*]+", term.lower()) if p]
    n = len(parts)
    return any(all(word_match(parts[j], words[i + j]) for j in range(n))
               for i in range(len(words) - n + 1))


def near(anchor, others, k, words):
    """`anchor Nk (others)`: any of `others` within k words, either side."""
    for i, w in enumerate(words):
        if word_match(anchor, w):
            window = words[max(0, i - k):i] + words[i + 1:i + k + 1]
            if any(phrase_in(o, window) for o in others):
                return True
    return False


def hits(block, words):
    out = []
    for term in block:
        if isinstance(term, tuple):
            if near(*term, words):
                out.append(f"{term[0]} N{term[2]} (...)")
        elif phrase_in(term, words):
            out.append(term)
    return out


def main():
    records = list(TARGETS)
    with open(HERE / "candidate-studies.csv", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rid = row["doi_or_id"]
            if row["tier"] == "A" and rid.startswith("10.") and rid not in dict(TARGETS).values():
                records.append((f"[A-tier] {row['citation']} {row['year']}", rid))

    for label, rid in records:
        try:
            words, err = words_of(fetch(rid)), "no text returned"
        except Exception as e:
            words, err = [], e
        if not words:
            print(f"{label[:58]:60s}FETCH FAILED, re-run ({err})")
            continue
        line = f"{label[:58]:60s}"
        for name, blocks in DRAFTS.items():
            missing = [b for b, terms in blocks.items() if not hits(terms, words)]
            line += f"{name}: {'found' if not missing else 'MISSED (' + ', '.join(missing) + ')':30s} "
        print(line)


if __name__ == "__main__":
    main()
