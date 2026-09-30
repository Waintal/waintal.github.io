#!/usr/bin/env python3
"""Check arXiv and Crossref for publications missing from, or outdated in, data/publications.yaml.

Usage:  python3 scripts/update_publications.py
It only PRINTS suggestions (new entries as ready-to-paste YAML, and preprints that seem to be
published now); it never modifies the data file. Standard library only.
"""
import json, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "publications.yaml"
ARXIV = "https://export.arxiv.org/api/query?search_query=au:Waintal&start=0&max_results=400&sortBy=submittedDate&sortOrder=descending"
# arXiv postings deliberately NOT in the publication list (not in the CV). Add ids here to silence them.
IGNORE = {
    "1010.2627",         # KNIT code description: shown as an extra link ("also") on the KNIT paper entry
}
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}


def get(url, as_json=False):
    req = urllib.request.Request(url, headers={"User-Agent": "waintal-homepage/1.0"})
    raw = urllib.request.urlopen(req, timeout=60).read()
    return json.loads(raw) if as_json else raw


def arxiv_entries():
    root = ET.fromstring(get(ARXIV))
    for e in root.findall("a:entry", NS):
        txt = lambda p: (e.find(p, NS).text if e.find(p, NS) is not None else None)
        authors = [a.find("a:name", NS).text for a in e.findall("a:author", NS)]
        if not any("Waintal" in a for a in authors):
            continue
        yield dict(arxiv=re.sub(r"v\d+$", "", txt("a:id").split("/abs/")[-1]),
                   title=" ".join(txt("a:title").split()), authors=authors,
                   abstract=" ".join(txt("a:summary").split()), year=int(txt("a:published")[:4]),
                   journal_ref=txt("x:journal_ref"), doi=txt("x:doi"))


def join_authors(a):
    return a[0] if len(a) == 1 else ", ".join(a[:-1]) + ("," if len(a) > 2 else "") + " and " + a[-1]


def q(s):
    return json.dumps(s, ensure_ascii=False)  # JSON strings are valid YAML strings


def main():
    text = DATA.read_text()
    known = set(re.findall(r"^\s+arxiv: '?([^'\n]+)'?$", text, re.M))
    nmax = max(int(n) for n in re.findall(r"^- n: (\d+)$", text, re.M))
    entries = list(arxiv_entries())

    new = [e for e in entries if e["arxiv"] not in known and e["arxiv"] not in IGNORE]
    print(f"# {len(entries)} arXiv entries by X. Waintal, {len(new)} not in {DATA.name}\n")
    for i, e in enumerate(reversed(new)):  # oldest first gets the lowest number
        print(f"- n: {nmax + 1 + i}\n  year: {e['year']}\n  title: {q(e['title'])}\n"
              f"  authors: {q(join_authors(e['authors']))}\n  journal: {q(e['journal_ref'] or 'Preprint')}\n"
              + (f"  doi: {e['doi']}\n" if e["doi"] else "")
              + f"  arxiv: '{e['arxiv']}'\n  abstract: {q(e['abstract'])}\n")

    # Preprints that may have been published since: look them up on Crossref by title.
    blocks = re.split(r"^(?=- n: )", text, flags=re.M)
    print("# Preprints that may now be published (check, then update journal/doi/year):")
    checked = 0
    for b in blocks:
        if not re.search(r"^\s+journal: .*(Preprint|Submitted|To appear)", b, re.M):
            continue
        title = re.search(r"^\s+title: (.*)$", b, re.M).group(1).strip("'\"")
        n = re.search(r"^- n: (\d+)", b).group(1)
        checked += 1
        url = "https://api.crossref.org/works?rows=3&query.bibliographic=" + urllib.parse.quote(title + " Waintal")
        try:
            items = get(url, as_json=True)["message"]["items"]
        except Exception as err:
            print(f"  n={n}: Crossref lookup failed ({err})"); continue
        for it in items:
            t = (it.get("title") or [""])[0]
            if it.get("type") == "posted-content" or not t:
                continue
            if re.sub(r"\W", "", t.lower())[:40] == re.sub(r"\W", "", title.lower())[:40]:
                j = (it.get("short-container-title") or it.get("container-title") or [""])[0]
                y = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
                print(f"  n={n}: {title}\n     -> {j} {it.get('volume', '')}, {it.get('page') or it.get('article-number', '')} ({y})  doi: {it.get('DOI')}")
                break
        time.sleep(0.5)
    print(f"  ({checked} preprints checked)")


if __name__ == "__main__":
    sys.exit(main())
