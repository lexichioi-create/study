# Revised search string (validated 2026-09-28)

**TL;DR:** The original string retrieves **0 of the 5** required papers. It also retrieves **0 of the 11** core (A-tier) studies in `candidate-studies.csv`. The main cause is the Context block: it requires an EFL label that most authors never write. The revised string (Draft A) retrieves **5/5 + 11/11**.

- Checker script: [`search_check.py`](search_check.py). Run `python3 search_check.py` after every edit.
- Labels: **[fact]** = checked in the records · **[inference]** = derived from checked facts · **[guess]** = outside the data

---

## 1. Final string: Draft A (recommended, recall-first)

Search each block in **title + abstract + keywords**, then combine: `P AND Concept AND Context`.

```
#1 Participants
neurodivers* OR neurodivergen* OR neurodevelopment* OR "neuro-developmental"
OR "intellectual disabilit*" OR "developmental disabilit*" OR "learning disabilit*"
OR "learning difficult*" OR "learning disorder*" OR "learning difference*"
OR "specific learning" OR SpLD OR dyslexi* OR "reading difficult*" OR "literacy difficult*"
OR "attention deficit*" OR hyperactiv* OR ADHD
OR autis* OR ASD OR asperger*
OR "special educational need*" OR "special need*" OR disabilit* OR disabled

#2 Concept (learning beyond the classroom)
"beyond the classroom" OR "beyond classroom*" OR "outside the classroom" OR "outside of the classroom"
OR "out-of-class" OR "out of class" OR "after-class" OR "after class" OR "after school"
OR "out-of-school" OR "out of school" OR extracurricular OR "extra-curricular" OR "extra curricular"
OR "self-access" OR "distance learning" OR "distance education"
OR informal* OR "non-formal" OR nonformal OR naturalistic OR "non-instructed" OR uninstructed OR incidental
OR "self-instruct*" OR "self-taught" OR "self-study" OR autonom* OR "independent learn*" OR "independent study"
OR "self-directed" OR "self-regulat*" OR extramural OR recreation* OR leisure
OR digital* OR technolog* OR internet OR online OR "web-based" OR virtual OR comput* OR software
OR mobile OR app OR apps OR game* OR gaming OR gamif*
OR YouTube OR video* OR television OR TV OR screen OR screens OR media OR multimedia
OR subtitl* OR caption* OR cartoon* OR audiovisual*
OR "unexpected bilingual*" OR "non-interactive" OR noninteractive
OR parent* OR caregiv* OR family OR families OR home OR "home-based" OR homework

#3 Context
English OR EFL OR ESL OR EAL OR ELL OR ELLs OR TESOL OR TEFL OR ELT
OR "foreign language*" OR "second language*" OR "third language*" OR "additional language*"
OR L2 OR L3 OR "non-native" OR "non-English"

#4  #1 AND #2 AND #3
```

## 2. Draft B (higher-risk, precision-first)

- **Change**: in #3, replace bare `English` with a proximity term. Everything else stays the same.
- **Risk**: it drops Gagnon et al. (2026), a borderline record that mentions English only as "(here English)". [fact: checker]

```
(English N3 (learn* OR teach* OR lesson* OR class* OR homework OR proficien* OR acqui*
  OR vocabular* OR literacy OR reading OR skill* OR instruct* OR extramural OR exposure OR input))
OR EFL OR ESL OR EAL OR ELL OR ELLs OR TESOL OR TEFL OR ELT
OR "foreign language*" OR "second language*" OR "third language*" OR "additional language*"
OR L2 OR L3 OR "non-native" OR "non-English"
```

## 3. Test results [fact]

| Validation set | Original (core Context) | Original (+ "maybe" terms) | Draft A | Draft B |
|---|:-:|:-:|:-:|:-:|
| 5 required papers | 0/5 | 0/5 | **5/5** | **5/5** |
| A-tier, `candidate-studies.csv` | 0/11 | 0/11 | **11/11** | **11/11** |
| B-tier, `candidate-studies.csv` | 4/9 | 4/9 | 8/9 | 7/9 |

- **Method**: title + abstract (+ author keywords where published) from Crossref, ERIC, or Europe PMC, matched by `search_check.py`.
- **B-tier miss**: de Carvalho et al. (2022) has no beyond-the-classroom term in its abstract. It is a conference abstract, so it can be found only through citation chasing. [fact]
- **Limit**: this is a simulation, not a live database run. Hit counts (screening load) are not yet measured. [fact]

## 4. Problem → Root cause: why each paper was missed [fact]

| Paper | P | Concept | Context | What the record actually says |
|---|:-:|:-:|:-:|---|
| Alexandra et al. (2025) | ✅ | ❌ | ✅ | Parents teach at home "used YouTube and flashcards". No tech or beyond-the-classroom term. |
| Blázquez-Arribas et al. (2020) | ⚠️ | ✅ | ❌ | "TESOL", "English as a second language", "adults with disabilities", "Special Educational Needs". P matched only because `diffi*` hit "the difficulties detected". |
| Pfenninger (2015) | ✅ | ✅ | ❌ | "FL learners", "second language (L2)", "English as a third language (L3)" |
| Schurz (2026) | ✅ | ✅ | ❌ | Only "extramural English", "English proficiency" |
| Torsani (2025) | ✅ | ✅ | ❌ | Only "English homework" |

- **Root cause 1 (Context)**: the block asks for an EFL *label*. Authors describe the setting without it, or with a different label. The Spanish study says "second language", and the Swiss study says "L3". [fact]
- **Root cause 2 (Concept)**: parent-led home learning has no digital or out-of-class wording. [fact: Alexandra et al., 2025]
- **Root cause 3 (P)**: disability and special educational needs (SEN) wording was missing. Retrieval depended on the noisy `diffi*`. [fact: Blázquez-Arribas et al., 2020]

## 5. Fix: what changed and why

**Added**: removing any one row below makes at least one validation paper disappear. [fact: ablation test with the checker]

| Block | Added terms | Only path to (Draft A) |
|---|---|---|
| Context | `English` | Schurz (2026), Torsani (2025), Hindi & Meir (2026b) |
| Context | `"second language*"`, `"third language*"`, `L2`, `L3`, `TESOL` | Pfenninger (2016). In Draft B, also Pfenninger (2015) |
| Concept | `parent*`, `caregiv*`, `YouTube`, `home`, `homework` | Alexandra et al. (2025) |
| Concept | `audiovisual*`, `media` | Morales et al. (2026), which reports "minimal audiovisual exposure" |
| P | `disabilit*`, `"special educational need*"` | Blázquez-Arribas et al. (2020) |

**Syntax fixes** (the original form never matched the real wording):

| Original | Problem | Fixed |
|---|---|---|
| `"neuro developmental disorder"` | does not match the one-word "neurodevelopmental" | `neurodevelopment*` |
| `"language beyond classroom"` | does not match "language learning beyond **the** classroom" | `"beyond the classroom"` |
| `"English second language*"` | does not match "English **as a** second language" | `"second language*"` |
| `asperger`, `self-regulate` | no truncation, so "Asperger's" and "self-regulated" are missed | `asperger*`, `"self-regulat*"` |
| `"extra curricular"` | misses "extracurricular" | three spellings |

**Removed** (noise, already covered by other terms):

| Removed | Why |
|---|---|
| `diffi*` | matches any "difficult/difficulty". Replaced by `"learning difficult*"`, `"reading difficult*"` |
| `comp*` | matches compare, component, comprehension. Schurz matched it only via "comparatively". Replaced by `comput*` |
| `tech*` | matches "technique". Replaced by `technolog*` |
| `"learning di*"` | matches "learning diaries", "learning dimensions". Replaced by explicit forms |
| `ADD`, `EL`, `CALL`, `independent` | common words ("add", Spanish "el", "call for research", "independent variable") |
| `LBC`, `IDLE`, `ISLL`, `SEN` | abstracts spell these out, and the spelled-out form is already in the string |

## 6. Database syntax

| Database | Field | Draft B proximity |
|---|---|---|
| EBSCO (ERIC, PsycINFO) | `TI (…) OR AB (…) OR SU (…)` | `English N3 (…)` |
| ProQuest (LLBA, Dissertations) | `NOFT(…)` | `English NEAR/3 (…)` |
| Scopus | `TITLE-ABS-KEY(…)` | `English W/3 (…)` |
| Web of Science | `TS=(…)` | `English NEAR/3 (…)` |
| PubMed | add `[tiab]` to each term | proximity ignores terms with `*` (PubMed Help), so use Draft A |

- **PubMed noise [inference]**: `ASD` also means atrial septal defect, and `L2`/`L3` also mean lumbar vertebrae. Drop them in PubMed; `autis*` and `"second language*"` cover the relevant records.
- **Hyphens [inference]**: databases handle hyphens differently. The string therefore lists both `"out-of-class"` and `"out of class"`.

## 7. Prevention

- **Validate before every run**: keep the 5 required papers plus the 11 A-tier studies as a validation set, and re-run `search_check.py` after each edit. Testing a search against known relevant records is a standard step in search development (Bramer et al., 2018).
- **Apply EFL at screening, not in the search**: labels do not track the setting. A study in Spain says "second language", and a study in Switzerland says "L3". Code the setting in the charting table instead. [inference: moderate]
- **Never search the title only**: Crossref stores Schurz (2026) as the title "Learning on their terms" plus a separate subtitle. Some indexes may show only the main title. [fact: Crossref record]
- **Log every database run**: record the date, the exact string, the fields searched, and the hit count, following PRISMA-S (Rethlefsen et al., 2021).
- **Check for overlapping samples**: Pfenninger (2015) and Pfenninger (2016) both report 40 Swiss learners (20 with dyslexia, 10 trained). This is likely one sample. [inference: moderate]
- **Update the candidate list**: Pfenninger (2015), Blázquez-Arribas et al. (2020), and Torsani (2025) are not in `candidate-studies.csv` yet. [fact]

---

## References

- Alexandra, N. F., Artini, L. P., & Ana, I. K. T. A. (2025). Teaching English to second-grade dyslexia-prone students: Perspectives of Y-generation parents on foreign language learning in elementary school. *IJLHE: International Journal of Language, Humanities, and Education, 8*(1), 83–92. https://doi.org/10.52217/ijlhe.v8i1.1769
- Blázquez-Arribas, L., Barros-del Río, M. A., Alcalde Peñalver, E., & Sigona, C. M. (2020). Teaching English to adults with disabilities: A digital solution through En-Abilities. *Teaching English with Technology, 20*(1), 80–103. ERIC EJ1242672
- Bramer, W. M., de Jonge, G. B., Rethlefsen, M. L., Mast, F., & Kleijnen, J. (2018). A systematic approach to searching: An efficient and complete method to develop literature searches. *Journal of the Medical Library Association, 106*(4), 531–541. https://doi.org/10.5195/jmla.2018.283
- Gagnon, D., Ostrolenk, A., & Mottron, L. (2026). Early manifestations of unexpected bilingualism in minimally verbal autism. *Journal of Child Psychology and Psychiatry, 67*(5), 652–662. https://doi.org/10.1111/jcpp.70032
- Hindi, I., & Meir, N. (2026b). Non-interactive and naturalistic language exposure in autism: An investigation of narrative production in bilingual children. *Journal of Communication Disorders, 122*, Article 106650. https://doi.org/10.1016/j.jcomdis.2026.106650
- Morales, M., Reyes Payeras, C., González Santibáñez, C., Muñoz, E., & García, A. M. (2026). Paradoxical language dominance in a bilingual child with autism spectrum disorder. *International Journal of Bilingualism, 30*(2), 603–620. https://doi.org/10.1177/13670069251336330
- Pfenninger, S. E. (2015). MSL in the digital ages: Effects and effectiveness of computer-mediated intervention for FL learners with dyslexia. *Studies in Second Language Learning and Teaching, 5*(1), 109–133. https://doi.org/10.14746/ssllt.2015.5.1.6 ⚠️ pre-2018 (required paper)
- Pfenninger, S. E. (2016). Taking L3 learning by the horns: Benefits of computer-mediated intervention for dyslexic school children. *Innovation in Language Learning and Teaching, 10*(3), 220–237. https://doi.org/10.1080/17501229.2014.959962 ⚠️ pre-2018
- Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., Ayala, A. P., Moher, D., Page, M. J., Koffel, J. B., & PRISMA-S Group. (2021). PRISMA-S: An extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. *Systematic Reviews, 10*, Article 39. https://doi.org/10.1186/s13643-020-01542-z
- Schurz, A. (2026). Learning on their terms: Retrospective accounts of extramural English experiences among students with ADHD. *ITL – International Journal of Applied Linguistics, 177*(1), 88–115. https://doi.org/10.1075/itl.25021.sch
- Torsani, S. (2025). From classroom to caregiving: Technology as a tool for special educational needs inclusion, a case study. *Computer-Assisted Language Learning Electronic Journal, 26*(2), 149–172. https://doi.org/10.54855/callej.252626
