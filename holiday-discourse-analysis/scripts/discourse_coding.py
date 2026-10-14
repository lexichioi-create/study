"""holiday.cha 발화별 담화 코딩과 요약 집계.

사용법: python3 scripts/discourse_coding.py
출력:  coding/holiday_coding.csv, coding/summary.md

- 줄 번호(L)는 텍스트 편집기 기준 파일 줄 번호다. CLAN 출력의 line 값은 @UTF8 줄을 빼고 세므로 1 작다.
- 수동 코드(CODES)는 분석자 1인의 해석이다. 코드 정의는 README.md 3절을 따른다.
- CHAT 기호에서 자동으로 뽑는 코드: RETRACE([//]), REPEAT([/]), TRAIL(+...), SELFINT(+//.),
  FILLER(&-), CSW(@s), Q(? 종결), MIN(최소 반응 발화).
"""
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHA = ROOT / "data" / "holiday.cha"
OUT_DIR = ROOT / "coding"

EPISODES = [
    (8, 11, "E0 과제 시작·주제 협상"),
    (12, 53, "E1 MAR의 크리스마스(페루)"),
    (54, 62, "E2 역할 전환"),
    (63, 68, "E3 MAR의 추석"),
    (69, 112, "E4 LEX의 추석 성묘·차례"),
    (113, 128, "E5 비교: 코코·멕시코"),
    (129, 172, "E6 음식: 두고 오기 vs 먹기"),
    (173, 203, "E7 사진·조상의 음식"),
    (204, 221, "E8 페루 묘지·종결"),
]

# 수동 코드: 파일 줄 번호 -> 코드 목록
CODES = {
    8: ["TSK", "QI"],
    9: ["CR"],
    12: ["TOP"],
    18: ["CR"],
    19: ["CC"],
    22: ["CMC"],
    23: ["CR"],
    25: ["CMP"],
    26: ["CR"],
    28: ["MLC"],
    31: ["WS"],
    33: ["WS"],
    34: ["ABN"],
    35: ["CR"],
    37: ["CIRC"],
    38: ["COL"],
    39: ["COL"],
    42: ["ASM"],
    46: ["CC"],
    48: ["MLC"],
    51: ["SSR"],
    53: ["CLS"],
    54: ["TSK"],
    55: ["QI"],
    56: ["QI"],
    57: ["QI"],
    58: ["CR"],
    59: ["TSK"],
    60: ["TSK"],
    61: ["TOP"],
    62: ["TOP", "QI"],
    64: ["CR"],
    68: ["CLS"],
    69: ["TOP", "CMP"],
    70: ["CMC", "APX"],
    71: ["SSR"],
    73: ["APW"],
    74: ["CMC"],
    75: ["SSR"],
    76: ["CMC"],
    77: ["CMC"],
    79: ["ASM"],
    80: ["QI"],
    83: ["APX", "MLC"],
    86: ["CC"],
    93: ["CMC"],
    95: ["COL", "APX"],
    96: ["AGR"],
    99: ["APW"],
    100: ["WS"],
    101: ["WS"],
    102: ["WS"],
    103: ["WS", "APX"],
    104: ["WS"],
    105: ["WS"],
    106: ["WS"],
    107: ["WS"],
    109: ["APX"],
    112: ["AGR"],
    113: ["TOP", "CMP"],
    114: ["QI"],
    120: ["DIS"],
    121: ["CMP"],
    122: ["AGR"],
    123: ["CMP"],
    124: ["CMP"],
    125: ["AGR"],
    126: ["CMP"],
    128: ["CMP"],
    129: ["TOP"],
    132: ["CC"],
    135: ["QI"],
    138: ["WS"],
    139: ["WS", "APX"],
    140: ["WS"],
    141: ["CC", "COL"],
    143: ["CMP"],
    144: ["CMP"],
    145: ["OC"],
    148: ["WS", "MLC"],
    149: ["SSR"],
    151: ["CMP"],
    153: ["CMP"],
    154: ["CMC"],
    158: ["WS"],
    159: ["RES"],
    161: ["APX"],
    171: ["CC"],
    172: ["CC"],
    174: ["RES"],
    175: ["RES"],
    183: ["CMP"],
    186: ["AGR"],
    187: ["CMP"],
    188: ["CMP"],
    189: ["CMP"],
    190: ["AGR"],
    192: ["AGR"],
    193: ["CMP"],
    194: ["CIRC"],
    197: ["ASM"],
    198: ["CMP"],
    200: ["CIRC"],
    202: ["COL"],
    203: ["AGR"],
    205: ["CMP"],
    207: ["TOP"],
    208: ["COL"],
    211: ["DIS"],
    215: ["AGR"],
    217: ["COL"],
    219: ["ASM"],
    220: ["CLS"],
    221: ["CLS"],
}

MIN_TOKENS = {"yeah", "okay", "ah", "oh", "wow", "right", "no", "yay"}

GROUPS = {
    "의미 협상": ["CR", "CC", "CMC"],
    "수정·정정": ["SSR", "RETRACE", "REPEAT", "OC"],
    "의사소통 전략": ["WS", "APX", "CIRC", "APW", "CSW", "RES", "ABN", "MLC"],
    "상호작용 관리": ["MIN", "ASM", "AGR", "DIS", "COL", "CMP"],
    "담화 구조": ["TSK", "TOP", "QI", "CLS", "TRAIL", "SELFINT", "FILLER"],
}


def parse(path):
    rows = []
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        m = re.match(r"\*([A-Z]{3}):\t(.*)$", raw)
        if m:
            rows.append({"line": n, "speaker": m.group(1), "utt": m.group(2)})
    return rows


def auto_codes(utt):
    codes = []
    if "[//]" in utt:
        codes.append("RETRACE")
    if "[/]" in utt:
        codes.append("REPEAT")
    if "+..." in utt:
        codes.append("TRAIL")
    if "+//." in utt:
        codes.append("SELFINT")
    if "&-" in utt:
        codes.append("FILLER")
    if "@s" in utt:
        codes.append("CSW")
    if utt.rstrip().endswith("?"):
        codes.append("Q")
    words = re.findall(r"[A-Za-z']+", utt)
    if words and all(w.lower() in MIN_TOKENS for w in words):
        codes.append("MIN")
    return codes


def word_count(utt):
    # CLAN 규칙과 맞춘다: 채움말(&-), 반복·수정된 <...> [/] [//] 구간, 기호는 제외
    s = re.sub(r"<[^>]*>\s*\[//?\]", " ", utt)
    s = re.sub(r"\S+\s*\[//?\]", " ", s)
    s = re.sub(r"&-\S+", " ", s)
    s = re.sub(r"\+\S*", " ", s)
    return len(re.findall(r"[^\W\d][\w'@:]*", s))


def episode_of(line):
    for start, end, name in EPISODES:
        if start <= line <= end:
            return name
    return ""


CATEGORY = {
    **dict.fromkeys(["CR", "CC", "CMC"], "NOM"),
    **dict.fromkeys(["SSR", "OC"], "REP"),
    **dict.fromkeys(["WS", "APX", "CIRC", "APW", "CSW", "RES", "ABN", "MLC"], "CST"),
    **dict.fromkeys(["MIN", "ASM", "AGR", "DIS", "COL", "CMP"], "INT"),
    **dict.fromkeys(["TSK", "TOP", "QI", "CLS"], "ORG"),
}
CODED_HEADER = [
    "@Comment:\tDiscourse codes on %cod as $CATEGORY:CODE. Utterance order is identical to data/holiday.cha; L numbers in README and holiday_coding.csv refer to that file.",
    "@Comment:\tNOM = negotiation of meaning (CR CC CMC); REP = repair (SSR OC); CST = communication strategy (WS APX CIRC APW CSW RES ABN MLC); INT = interaction (MIN ASM AGR DIS COL CMP); ORG = discourse organization (TSK TOP QI CLS)",
    "@Comment:\tEpisodes are lazy gems (@G). E0 task opening; E1 MAR Christmas; E2 role switch; E3 MAR Chuseok; E4 LEX Chuseok rites; E5 Coco and Mexico; E6 food left vs eaten; E7 photo and spirits' food; E8 Peru cemetery and closing",
]


def write_coded_cha(rows, path):
    """원본 CHAT 파일에 @G 에피소드 경계와 %cod 코드 층위를 넣어 CLAN용 코딩 파일을 만든다."""
    by_line = {r["line"]: r for r in rows}
    starts = {start: name.split()[0] for start, _, name in EPISODES}
    first_utt = min(by_line)
    out = []
    for n, raw in enumerate(CHA.read_text(encoding="utf-8").splitlines(), start=1):
        if n == first_utt:
            out += CODED_HEADER
        if n in starts:
            out.append(f"@G:\t{starts[n]}")
        out.append(raw)
        r = by_line.get(n)
        if r:
            codes = r["manual"] + [c for c in r["auto"] if c in ("MIN", "CSW")]
            if codes:
                out.append("%cod:\t" + " ".join(f"${CATEGORY[c]}:{c}" for c in codes))
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def main():
    rows = parse(CHA)
    OUT_DIR.mkdir(exist_ok=True)
    for r in rows:
        r["episode"] = episode_of(r["line"])
        r["auto"] = auto_codes(r["utt"])
        r["manual"] = CODES.get(r["line"], [])
        r["words"] = word_count(r["utt"])

    unknown = set(CODES) - {r["line"] for r in rows}
    assert not unknown, f"코드가 발화 줄이 아닌 곳을 가리킴: {sorted(unknown)}"

    with open(OUT_DIR / "holiday_coding.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["line", "speaker", "episode", "manual_codes", "auto_codes", "words", "utterance"])
        for r in rows:
            w.writerow([r["line"], r["speaker"], r["episode"], ";".join(r["manual"]),
                        ";".join(r["auto"]), r["words"], r["utt"]])
    write_coded_cha(rows, OUT_DIR / "holiday_coded.cha")

    speakers = ["LEX", "MAR"]
    counts = {s: Counter() for s in speakers}
    for r in rows:
        counts[r["speaker"]].update(r["manual"] + r["auto"])

    # 발화권(turn): 화자가 바뀔 때마다 새 turn
    turns = []
    for r in rows:
        if turns and turns[-1]["speaker"] == r["speaker"]:
            turns[-1]["rows"].append(r)
        else:
            turns.append({"speaker": r["speaker"], "rows": [r]})

    ep = defaultdict(lambda: Counter())
    for r in rows:
        ep[r["episode"]][r["speaker"] + "_utt"] += 1
        ep[r["episode"]][r["speaker"] + "_words"] += r["words"]

    md = ["# 담화 코딩 요약 (자동 생성)", "",
          f"- 발화 수: LEX {sum(r['speaker']=='LEX' for r in rows)}, MAR {sum(r['speaker']=='MAR' for r in rows)}",
          f"- 발화권(turn) 수: {len(turns)} (LEX {sum(t['speaker']=='LEX' for t in turns)}, MAR {sum(t['speaker']=='MAR' for t in turns)})",
          "", "## 코드별 빈도 (발화 단위)", "", "| 범주 | 코드 | LEX | MAR | 계 |", "|---|---|---:|---:|---:|"]
    for g, codes in GROUPS.items():
        for c in codes:
            a, b = counts["LEX"][c], counts["MAR"][c]
            md.append(f"| {g} | {c} | {a} | {b} | {a + b} |")
    md += ["", "## 에피소드별 발화·단어 수", "",
           "| 에피소드 | 줄 | LEX 발화 | MAR 발화 | LEX 단어 | MAR 단어 | 단어 점유(주 화자) |",
           "|---|---|---:|---:|---:|---:|---|"]
    for start, end, name in EPISODES:
        c = ep[name]
        lw, mw = c["LEX_words"], c["MAR_words"]
        tot = lw + mw
        lead = "LEX" if lw >= mw else "MAR"
        share = max(lw, mw) / tot if tot else 0
        md.append(f"| {name} | L{start}–{end} | {c['LEX_utt']} | {c['MAR_utt']} | {lw} | {mw} | {lead} {share:.0%} |")
    md += ["", "## 의미 협상 발화 목록", "", "| 줄 | 화자 | 코드 | 발화 |", "|---|---|---|---|"]
    for r in rows:
        nom = [c for c in r["manual"] if c in ("CR", "CC", "CMC")]
        if nom:
            md.append(f"| L{r['line']} | {r['speaker']} | {'+'.join(nom)} | {r['utt']} |")
    (OUT_DIR / "summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
