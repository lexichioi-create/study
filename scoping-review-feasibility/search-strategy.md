# Search strategy v2: fixed to retrieve the 5 benchmark papers

> Date: 2026-09-28 · Validation files: [`search-validation/`](search-validation/) · Builds on the pilot in [`search-log.md`](search-log.md)

**TL;DR:** The original string retrieved **0 of your 5 papers**, and 0 of the 9 pilot core studies. The main cause is the Context block: 4 of the 5 abstracts never say "EFL" or "foreign language". Draft A below retrieves **5/5 and 9/9**. In ERIC it also returns fewer records than the original (2,258 vs 2,661), because it drops very broad truncations such as `diffi*` and `comp*`.

Labels: **[fact]** checked directly · **[inference]** drawn from checked facts · **[guess]** beyond the checked data

---

## 1. Problem: where each paper drops out [fact]

The test used each paper's title, abstract and author keywords (see [section 8](#8-how-to-re-run-the-check)).

| Paper | P | Concept | Context | Result |
|---|---|---|---|---|
| Alexandra et al. (2025) | ✅ dyslexi\* | ❌ none | ✅ "foreign language" | Missed |
| Blázquez-Arribas et al. (2020) | ⚠️ only `diffi*` ("difficulties detected") | ✅ digital | ❌ none | Missed |
| Pfenninger (2015) | ✅ dyslexi\* | ✅ digital, comp\* | ❌ none | Missed |
| Schurz (2026) | ✅ ADHD | ✅ extramural | ❌ none | Missed |
| Torsani (2025) | ✅ dyslexi\*, ADHD | ✅ tech\* | ❌ none | Missed |

- **Adding your "maybe" Context terms** fixes none of the 5 in Scopus/WoS-style title-abstract-keyword searching. [fact]
  - In ERIC it picks up Blázquez-Arribas and Pfenninger, but only through ERIC's index term "English (Second Language)". Other databases do not use that term. [fact]

## 2. Root causes

- **The Context block requires words the authors did not use.** [fact]
  - Schurz: only "extramural English" and "English proficiency".
  - Torsani: only "English homework".
  - Pfenninger: "FL" in the title; "second language (L2)" and "third language (L3)" in the abstract.
  - Blázquez-Arribas: "TESOL" and "English as a second language", although the setting is Spain.
- **Parent-mediated learning had no Concept terms.** Alexandra et al. describe parents using YouTube and flashcards at home, but none of your Concept terms appear. [fact]
- **"Special educational needs" was missing from P.** Blázquez-Arribas and Torsani both use it. Blázquez-Arribas matched P only by accident, through `diffi*`. [fact]
- **Some terms are so broad that they stop filtering.** [fact: ERIC counts and test output]
  - `diffi*`, `ADD` (the verb "add"): P matches 172,628 ERIC records, against 89,474 after the fix.
  - `comp*` matched Schurz through "comparatively". `CALL` matches "a call for research". `EL` matches the Spanish article "el". `IDLE` matches "idle".
- **Some phrases cannot match how authors write.** [fact: word-level matching]
  - `"English as additional*"` misses "English as **an** additional language".
  - `"language beyond classroom"` misses "language learning beyond **the** classroom".
  - `"neuro developmental disorder"` misses "neurodevelopmental".
  - `"naturalistic learning"` misses "naturalistic … input" and "naturalistically" (Hindi & Meir, 2026a).
- **No single database holds all 5.** [fact]
  - Only Blázquez-Arribas and Pfenninger are in ERIC.
  - Crossref records for Schurz and Torsani hold only the main title ("Learning on their terms"; "From Classroom to Caregiving"). Tools built on Crossref data (OpenAlex, Semantic Scholar, Lens) will not find their subtitle words in the title field.
  - IJLHE (Alexandra et al.) is not in DOAJ, and OpenAlex does not flag it as a core journal. It may be findable only through Google Scholar or OpenAlex. [inference: weak–medium; check in Scopus and WoS]

## 3. Fix: Draft A (conventional, recommended)

Search title, abstract and keywords, and combine the three blocks with AND.

### P (population)

```
(neurodiver* OR neurodevelopmental OR "neuro-developmental" OR "intellectual disabilit*" OR "learning disabilit*" OR "learning difficult*" OR "learning disorder*" OR "learning difference*" OR "specific learning" OR SpLD OR dyslexi* OR "attention deficit*" OR ADHD OR hyperactiv* OR autis* OR ASD OR asperger* OR "special educational need*" OR "special need*")
```

### Concept (learning beyond the classroom)

```
("beyond the classroom" OR "outside the classroom" OR "outside class*" OR "out-of-class" OR "after class*" OR "after school" OR "out-of-school" OR extracurricular OR "extra-curricular" OR "self-access" OR "distance learning" OR "distance education" OR informal* OR "non-formal" OR nonformal OR naturalistic* OR "non-instructed" OR uninstructed OR "self-instruct*" OR "self-taught" OR "self-learning" OR autonom* OR "independent learn*" OR "independent stud*" OR "self-directed" OR "self-regulat*" OR "learner-directed" OR extramural OR ISLL OR recreation* OR leisure OR hobb* OR incidental* OR digital* OR technolog* OR internet OR online OR "web-based" OR computer* OR software OR virtual OR multimedia OR "e-learning" OR elearning OR mobile OR app OR apps OR iPad* OR iPod* OR tablet* OR smartphone* OR game* OR gaming OR gamif* OR video* OR YouTube OR television OR TV OR cartoon* OR screen OR screens OR "social media" OR subtitl* OR caption* OR "text-to-speech" OR audiovisual OR parent* OR caregiv* OR family OR families OR home OR homework OR "unexpected bilingual*" OR "non-interactive" OR noninteractive OR "language exposure" OR "media exposure")
```

### Context (English as an additional language)

```
(English OR EFL OR ESL OR ELT OR ELL OR ELLs OR EAL OR TESOL OR TEFL OR "foreign language*" OR "second language*" OR "third language*" OR "additional language*" OR "target language*" OR L2 OR L3 OR "non-native" OR nonnative OR "non-English")
```

- **Key change:** the single word `English` replaces EFL-only terms. It is the only term that retrieves Schurz (2026), Torsani (2025) and Hindi & Meir (2026b). [fact: leave-one-out test]
- **EFL becomes a screening rule, not a search term.** Include a study when English is not the main language of the society where learners live. Search terms cannot express that rule reliably. [inference: medium]

### Database syntax

| Database | Wrap each block in | Proximity (Draft B) | Notes |
|---|---|---|---|
| Scopus | `TITLE-ABS-KEY( … )` | `W/3` | Wildcards inside quotes are allowed |
| Web of Science | `TS=( … )` | `NEAR/3` | Wildcards inside quotes are allowed |
| EBSCO (ERIC, APA PsycInfo, Education Source) | `TI ( … ) OR AB ( … ) OR SU ( … )` | `N3` | |
| ProQuest (LLBA, Dissertations) | `NOFT( … )` | `NEAR/3` | |
| PubMed | add `[tiab]` to each term | `"English learning"[tiab:~3]` | Expand phrase wildcards if PubMed rejects them |

- If a platform rejects a wildcard inside quotes, write out each form. For example, `"learning disabilit*"` becomes `"learning disability" OR "learning disabilities"`.
- **Scopus, full string:**

```
TITLE-ABS-KEY(neurodiver* OR neurodevelopmental OR "neuro-developmental" OR "intellectual disabilit*" OR "learning disabilit*" OR "learning difficult*" OR "learning disorder*" OR "learning difference*" OR "specific learning" OR SpLD OR dyslexi* OR "attention deficit*" OR ADHD OR hyperactiv* OR autis* OR ASD OR asperger* OR "special educational need*" OR "special need*")
AND TITLE-ABS-KEY("beyond the classroom" OR "outside the classroom" OR "outside class*" OR "out-of-class" OR "after class*" OR "after school" OR "out-of-school" OR extracurricular OR "extra-curricular" OR "self-access" OR "distance learning" OR "distance education" OR informal* OR "non-formal" OR nonformal OR naturalistic* OR "non-instructed" OR uninstructed OR "self-instruct*" OR "self-taught" OR "self-learning" OR autonom* OR "independent learn*" OR "independent stud*" OR "self-directed" OR "self-regulat*" OR "learner-directed" OR extramural OR ISLL OR recreation* OR leisure OR hobb* OR incidental* OR digital* OR technolog* OR internet OR online OR "web-based" OR computer* OR software OR virtual OR multimedia OR "e-learning" OR elearning OR mobile OR app OR apps OR iPad* OR iPod* OR tablet* OR smartphone* OR game* OR gaming OR gamif* OR video* OR YouTube OR television OR TV OR cartoon* OR screen OR screens OR "social media" OR subtitl* OR caption* OR "text-to-speech" OR audiovisual OR parent* OR caregiv* OR family OR families OR home OR homework OR "unexpected bilingual*" OR "non-interactive" OR noninteractive OR "language exposure" OR "media exposure")
AND TITLE-ABS-KEY(English OR EFL OR ESL OR ELT OR ELL OR ELLs OR EAL OR TESOL OR TEFL OR "foreign language*" OR "second language*" OR "third language*" OR "additional language*" OR "target language*" OR L2 OR L3 OR "non-native" OR nonnative OR "non-English")
```

- **Web of Science:** use the same string, replacing each `TITLE-ABS-KEY` with `TS=`.

## 4. Draft B (higher risk, fewer records)

- **What changes:** in the Context block, replace `English` with this proximity group. Leave everything else as in Draft A.

```
(English NEAR/3 (learn* OR teach* OR acqui* OR homework OR proficien* OR extramural OR lesson* OR class* OR course* OR skill* OR vocabular* OR exposure OR input OR instruction))
```

- **Gain:** about 31% fewer ERIC records than Draft A (section 5). It also cuts noise such as "English-language publications". [fact: ERIC estimate]
- **Risk:** it misses any abstract that mentions English only in another pattern, such as "English-mediated" with no nearby learning word. [inference: medium]
- **Test result:** 5/5 and 9/9, the same as Draft A. [fact]

## 5. Volume check in ERIC (2026-09-28) [fact]

| String | P × Concept × Context | Peer-reviewed | Blázquez-Arribas | Pfenninger 2015 |
|---|---:|---:|:---:|:---:|
| Original | 2,661 | 1,848 | ❌ | ❌ |
| Original + "maybe" terms | 6,999 | 4,586 | ✅\* | ✅\* |
| **Draft A** | **2,258** | **1,034** | ✅ | ✅ |
| Draft A without `English` | 1,126 | 530 | ✅ | ✅ |
| Draft B (proximity, approximate) | 1,562 | 698 | ✅ | ✅ |

- \*Found only through ERIC's own index term. Other databases would miss these two.
- The other 3 benchmark papers are not in ERIC, so ERIC can confirm only these 2.
- Method: ERIC API, default fields; phrase wildcards written out by hand; Draft B approximated with `"English <word>"~4` pairs.
- The parent and home terms (`parent*`, `caregiv*`, `family`, `families`, `home`, `homework`) add about 890 ERIC records (1,366 → 2,258). They are needed for Alexandra et al. (2025), who is caught only by `parent*` and `YouTube`. [fact]

## 6. What changed from your list

| Your term | Change | Reason |
|---|---|---|
| `diffi*` | Removed; replaced by `"learning difficult*"`, `"specific learning"`, SpLD | Matches any "difficult…" word |
| `ADD` | Removed (`"attention deficit*"` already covers it) | Matches the verb "add" |
| `"learning di*"` | Written out as disabilit\* / difficult\* / disorder\* / difference\* | Also matches "learning diary", "learning digital…" |
| `"neuro developmental disorder"` | `neurodevelopmental`, `"neuro-developmental"` | Authors write it as one word |
| `asperger` | `asperger*` | Catches "Asperger's" |
| (none) | + `"special educational need*"`, `"special need*"`, `hyperactiv*` | Needed for Blázquez-Arribas; used in European literature |
| `comp*`, `tech*` | `computer*`, `technolog*`, `software` | `comp*` matched "comparatively"; `tech*` matches "technique" |
| `CALL`, `IDLE` | Removed; covered by `computer*`, `informal*`, `digital*` | Match "call" and "idle" |
| `"language beyond classroom"` | `"beyond the classroom"`, `"outside the classroom"` | Phrase never occurs in that form |
| `app`, `game` | `app OR apps`, `game* OR gaming OR gamif*` | Plurals were missed |
| `independent`, `autonomous` | `"independent learn*"`, `"independent stud*"`, `autonom*` | "independent variable" is noise; autonom\* adds "autonomy" |
| `"naturalistic learning"` | `naturalistic*` | Catches "naturalistically" |
| (none) | + parent\*, caregiv\*, family, home, homework, YouTube | Needed for Alexandra et al.; supports Torsani |
| (none) | + screen, video\*, TV, `"unexpected bilingual*"`, `"non-interactive"` | Needed for the pilot's autism core studies |
| `"English foreign*"`, EFL only | + `English`, `"second language*"`, `"third language*"`, L2, L3, TESOL | Needed for 4 of the 5 papers |
| `EL` | Removed | Matches Spanish "el" |
| `"English as additional*"` | `"additional language*"`, EAL | Missed "as **an** additional" |

- **Optional P terms**, if your definition covers them: `dyspraxi*`, `"developmental coordination disorder"`, `dyscalculi*`, `"developmental language disorder"`.

## 7. Prevention

- **Keep a known-item test set.** Check every string change against the 14 records in `search-validation/`. Checking whether known relevant papers are retrieved is a standard step in developing a search (Bramer et al., 2018).
- **Report the exact string used in each database, with the search date.** PRISMA-S asks for this (Rethlefsen et al., 2021).
- **Get the search peer reviewed.** Ask a librarian to review it with the PRESS checklist before the final run (McGowan et al., 2016 ⚠️pre-2018; still the standard tool).
- **Add supplementary sources** for journals outside Scopus/WoS/ERIC.
  - Google Scholar (no truncation, 256-character limit), e.g. `(dyslexia OR ADHD OR autism OR "special educational needs") English (parents OR home OR extramural OR technology)`.
  - Backward and forward citation searching from all included studies. JBI guidance includes reference-list searching as a final step (Peters et al., 2020).
- **Check for shared samples.** Pfenninger (2015) and Pfenninger (2016) both report 40 participants with 10 trained dyslexic learners, so they probably report one sample. [inference: medium]

## 8. How to re-run the check

```
cd scoping-review-feasibility/search-validation
python3 validate_search.py                    # all strings
python3 validate_search.py draft_A_sensitive  # one string
```

- `benchmark-records.json` holds the 5 benchmark papers and 9 pilot core studies (titles, abstracts, author keywords).
  - Pfenninger (2016) has no public abstract in Crossref, so its record uses the ERIC abstract.
  - Author keywords could not be retrieved for Blázquez-Arribas, Schurz or Torsani. All three are retrieved on title and abstract alone, so this does not change the result.
- `search-strategies.json` holds the original, original + "maybe", Draft A and Draft B as term blocks.
- The script checks words the way most databases do: case-insensitive, hyphens split words, `*` truncates the end of a word. Each platform tokenizes a little differently, so run one live test in each database. [inference: medium]

---

## References

- Alexandra, N. F., Artini, L. P., & Ana, I. K. T. A. (2025). Teaching English to second-grade dyslexia-prone students: Perspectives of Y-generation parents on foreign language learning in elementary school. *IJLHE: International Journal of Language, Humanities, and Education, 8*(1), 83–92. https://doi.org/10.52217/ijlhe.v8i1.1769
- Blázquez-Arribas, L., Barros-del Río, M. A., Alcalde Peñalver, E., & Sigona, C. M. (2020). Teaching English to adults with disabilities: A digital solution through En-Abilities. *Teaching English with Technology, 20*(1), 80–103. (ERIC EJ1242672)
- Bramer, W. M., de Jonge, G. B., Rethlefsen, M. L., Mast, F., & Kleijnen, J. (2018). A systematic approach to searching: An efficient and complete method to develop literature searches. *Journal of the Medical Library Association, 106*(4), 531–541. https://doi.org/10.5195/jmla.2018.283
- Hindi, I., & Meir, N. (2026a). Different paths to multilingualism in autism spectrum disorder (ASD): Naturalistic and non-interactive. *Journal of Child Language, 53*(2), 343–364. https://doi.org/10.1017/S0305000924000540
- Hindi, I., & Meir, N. (2026b). Non-interactive and naturalistic language exposure in autism: An investigation of narrative production in bilingual children. *Journal of Communication Disorders, 122*, Article 106650. https://doi.org/10.1016/j.jcomdis.2026.106650
- McGowan, J., Sampson, M., Salzwedel, D. M., Cogo, E., Foerster, V., & Lefebvre, C. (2016). PRESS peer review of electronic search strategies: 2015 guideline statement. *Journal of Clinical Epidemiology, 75*, 40–46. https://doi.org/10.1016/j.jclinepi.2016.01.021 ⚠️pre-2018
- Peters, M. D. J., Marnie, C., Tricco, A. C., Pollock, D., Munn, Z., Alexander, L., McInerney, P., Godfrey, C. M., & Khalil, H. (2020). Updated methodological guidance for the conduct of scoping reviews. *JBI Evidence Synthesis, 18*(10), 2119–2126. https://doi.org/10.11124/JBIES-20-00167
- Pfenninger, S. E. (2015). MSL in the digital ages: Effects and effectiveness of computer-mediated intervention for FL learners with dyslexia. *Studies in Second Language Learning and Teaching, 5*(1), 109–133. https://doi.org/10.14746/ssllt.2015.5.1.6 ⚠️pre-2018
- Pfenninger, S. E. (2016). Taking L3 learning by the horns: Benefits of computer-mediated intervention for dyslexic school children. *Innovation in Language Learning and Teaching, 10*(3), 220–237. https://doi.org/10.1080/17501229.2014.959962 ⚠️pre-2018
- Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., Ayala, A. P., Moher, D., Page, M. J., Koffel, J. B., & PRISMA-S Group. (2021). PRISMA-S: An extension to the PRISMA statement for reporting literature searches in systematic reviews. *Systematic Reviews, 10*, Article 39. https://doi.org/10.1186/s13643-020-01542-z
- Schurz, A. (2026). Learning on their terms: Retrospective accounts of extramural English experiences among students with ADHD. *ITL – International Journal of Applied Linguistics, 177*(1), 88–115. https://doi.org/10.1075/itl.25021.sch
- Torsani, S. (2025). From classroom to caregiving: Technology as a tool for special educational needs inclusion, a case study. *Computer-Assisted Language Learning Electronic Journal, 26*(2), 149–172. https://doi.org/10.54855/callej.252626
