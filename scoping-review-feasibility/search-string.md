# Final search string (validated 2026-09-28)

**TL;DR:** One final string retrieves all 5 required papers and all 11 core studies. It was tested live in ERIC (about 1,699 records) and PubMed (305 records). Beyond your 5, it also returns relevant papers: 8 known core studies, 3 new likely-eligible studies, and 1 related review. Three of the 5 papers are not in ERIC or PubMed, so the database list matters as much as the string (section 5).

- **Checker**: [`search_check.py`](search_check.py). Run `python3 search_check.py` after every edit.
- **Labels**: **[fact]** = checked in records or live searches · **[inference]** = derived from checked facts · **[unverified]** = not checked

---

## 1. The final string (EBSCO syntax, fields TI, AB, SU)

```
#1 Participants
neurodivers* OR neurodivergen* OR neurodevelopment* OR "neuro-developmental"
OR "intellectual disabilit*" OR "developmental disabilit*" OR "learning disabilit*"
OR "learning difficult*" OR "learning disorder*" OR "learning difference*"
OR "specific learning" OR SpLD OR dyslexi* OR "reading difficult*" OR "literacy difficult*"
OR "attention deficit*" OR hyperactiv* OR ADHD OR autis* OR ASD OR asperger*
OR "special educational need*" OR "special need*"

#2 Concept: learning beyond the classroom
"beyond the classroom" OR "beyond classroom*" OR "outside the classroom" OR "outside of the classroom"
OR "out-of-class" OR "out of class" OR "after-class" OR "after class" OR "after school"
OR "out-of-school" OR "out of school" OR extracurricular OR "extra-curricular" OR "extra curricular"
OR "self-access" OR "distance learning" OR "distance education"
OR informal* OR "non-formal" OR nonformal OR "naturalistic exposure" OR "naturalistic acqui*"
OR "naturalistic learn*" OR "non-instructed" OR uninstructed
OR "incidental learn*" OR "incidental acqui*" OR "incidental exposure"
OR "self-instruct*" OR "self-taught" OR "self-teach*" OR "self-learn*" OR "self-study"
OR autonomy OR autonomous OR "independent learn*" OR "independent study"
OR "self-directed" OR "self-regulat*" OR extramural OR recreation* OR leisure
OR digital* OR technolog* OR internet OR online OR "web-based" OR virtual OR computer* OR software
OR mobile OR app OR apps OR game* OR gaming OR gamif*
OR YouTube OR video OR videos OR "video game*" OR videogame* OR television
OR "screen time" OR "screen media" OR "screen exposure" OR "screen-based" OR screens
OR "social media" OR "media exposure" OR "media use" OR multimedia
OR subtitl* OR caption* OR cartoon* OR audiovisual*
OR "unexpected bilingual*" OR "non-interactive" OR noninteractive
OR parent* OR caregiv* OR "at home" OR "home-based" OR "home learning" OR "home literacy"
OR "home environment*" OR homework

#3 Context: English as a non-dominant language
(English N3 (learn* OR teach* OR lesson* OR class* OR homework OR proficien* OR acqui*
  OR vocabular* OR literacy OR reading OR skill* OR instruct* OR extramural OR exposure OR input))
OR EFL OR ESL OR EAL OR ELL OR ELLs OR TESOL OR TEFL OR ELT
OR "foreign language*" OR "second language*" OR "third language*" OR "additional language*"
OR L2 OR L3 OR "non-native" OR "non-English" OR "unexpected bilingual*"

#4  #1 AND #2 AND #3
```

- **No date or language filters**. Two core studies date from 2014 and 2015.
- Translations for other databases are in section 6.

## 2. Evidence that it works [fact]

| Test | Result |
|---|---|
| 5 required papers (simulated on real title + abstract + keywords) | **5/5** |
| 11 A-tier studies in `candidate-studies.csv` | **11/11** |
| 9 B-tier studies | 8/9. The miss (a conference abstract) has no beyond-the-classroom wording at all |
| **ERIC, live** (API run, proximity applied locally) | **≈1,699** records. Retrieves Blázquez-Arribas (EJ1242672), Pfenninger 2015 (EJ1134871) and Pfenninger 2016 (EJ1117317) |
| **PubMed, live** (section 6 string) | **305** records. Retrieves Zhukova 2023, Dumont 2024, Dumont 2025, Hindi & Meir 2026a and 2026b, and Gagnon 2026 |

**Why the Context block uses proximity (`English N3 …`) instead of the bare word `English`** (tested on an earlier draft of the other two blocks):

- **ERIC**: with bare `English`, 1,204 of 2,356 hits matched Context only through that word. A random sample was almost all off-topic (e.g., "Business Education Index 1995").
- **PubMed**: bare `English` gave 1,301 hits and proximity gave 268. No known study was lost.

## 3. Other papers it returns that fit the PCC

Verdicts are one person's title/abstract judgment; screen them properly with 2 reviewers. [inference]

**A. Known core studies, retrieved live** (not among your 5):

| Study | Found in | Why it fits |
|---|---|---|
| Zhukova et al. (2023) | ERIC, PubMed | Russian child with autism, English learned via media/internet |
| Dumont et al. (2024, 2025) | PubMed (2025 also in ERIC) | Autistic children who acquired English from screens (Belgium in 2024) |
| Hindi & Meir (2026a, 2026b) | PubMed | Hebrew-speaking autistic children, non-interactive English exposure |
| Gagnon et al. (2026) | PubMed | Unexpected bilingualism via non-interactive media |
| Papadima-Sophocleous & Charalambous (2014) | ERIC | SpLD university students, 8 weeks of independent mobile practice |
| Pfenninger (2016) | ERIC | Dyslexia, software designed for private use, English as L3 |

**B. New, likely eligible** (not in your candidate list yet):

| Study | Found in | P | Concept | Context |
|---|---|---|---|---|
| Abdulrahman & Hamasaeed (2026) | ERIC EJ1513906 | SEN students | Parent involvement, home environment | English, Kurdistan (Iraq) |
| Subekti & Lestariningsih (2023) | ERIC EJ1410084 | Autism (undergraduate) | 14 online one-to-one guidance sessions | English L2, Indonesia |
| Coskun & Mitrani (2020) | ERIC EJ1252628 | Undiagnosed dyslexia | Game-based vocabulary learning with spaced repetition | English vocabulary |

**C. New related review** (use for citation chasing and to show how your review differs):

- **Jiang et al. (2022)**: a systematic review of technology tools used "in and out of class" by ESL/EFL learners with learning difficulties (16 articles and 1 chapter). ERIC EJ1380245.

**D. New, borderline** (full text needed):

| Study | Found in | Open question |
|---|---|---|
| Golshan et al. (2019) | PubMed | Iran, autism, EFL tutorials plus paired classes. Is this outside the classroom? |
| Hashim et al. (2022) | PubMed | Autism, English vocabulary learning. The setting and whether the context is EFL are unclear |
| Du et al. (2024) | PubMed | AI tools for L2 speaking practice. Participants have autistic *traits*, not a diagnosis |

## 4. Why reviewers are unlikely to fault it

The rows follow the PRESS 2015 checklist for search peer review (McGowan et al., 2016).

| PRESS element | What this string does |
|---|---|
| Translation of the research question | Each block is one PCC element. Every Concept term maps to a sub-type stated in the protocol (see below) |
| Boolean and proximity operators | OR within blocks, AND between blocks, no NOT. Proximity is used only in Context, and the reason was tested (section 2) |
| Subject headings | ERIC descriptors and MeSH are added (section 6). MeSH `Multilingualism` was tested and left out (next table) |
| Text words | Truncation checked for collisions. For example, `comput*` became `computer*` because it also matches "computational" |
| Spelling, syntax, line numbers | Machine-checked by `search_check.py` |
| Limits and filters | None |

**Validation**: recall is reported against a known-item set of 5 required + 11 core studies (Bramer et al., 2018). **Reporting**: log date, database, exact string and hit count per PRISMA-S (Rethlefsen et al., 2021).

**Answers to likely reviewer questions:**

| Likely question | Answer |
|---|---|
| "Why doesn't Context require 'EFL'?" | Authors rarely label the setting. The Spanish study says "English as a second language" and the Swiss study says "L3". EFL status is therefore decided at screening, and the eligibility criteria define it as "English is not the dominant societal language". [fact: records] |
| "Why are technology and parents in Concept?" | The protocol defines beyond-the-classroom learning to include self-directed, technology-mediated, home or parent-mediated, and non-interactive (screen) learning. Two required papers are parent-mediated (Alexandra et al., 2025; Torsani, 2025). |
| "Why keep 'special educational needs'?" | Studies from EFL countries label neurodivergent learners this way (Blázquez-Arribas et al., 2020; Torsani, 2025). Bare `disabilit*` was removed; physical- or sensory-only samples are excluded at screening. |
| "Why no MeSH `Multilingualism`?" | Tested: it adds 140 PubMed records, almost all heritage-language bilingual families. That is outside an EFL Context. [fact: live test] |

## 5. Database plan: a string can't find papers the database doesn't index

| Required paper | ERIC | OpenAlex (Crossref-based) | Other |
|---|:-:|:-:|---|
| Blázquez-Arribas et al. (2020) | ✅ | – | |
| Pfenninger (2015) | ✅ | ✅ | DOAJ |
| Schurz (2026) | ❌ | ✅ | Scopus, LLBA [unverified] |
| Torsani (2025) | ❌ | ✅ | Scopus [unverified] |
| Alexandra et al. (2025) | ❌ | ✅ | **Not in DOAJ**. Likely only in Crossref-based indexes and Google Scholar [inference] |

The ✅/❌ entries were checked on 2026-09-28 against the ERIC API, the DOAJ API and OpenAlex lookups. [fact]

**Recommended sources:**

- **Core databases**: ERIC, APA PsycINFO, LLBA, Scopus, Web of Science (SSCI), PubMed. Combining several databases is needed for adequate recall (Bramer et al., 2017).
- **Crossref-based index (required for Alexandra et al., 2025)**: OpenAlex or Lens.org. Check that source's Boolean and proximity syntax before running. [unverified syntax]
- **Google Scholar**: screen the first 200–300 results, as Haddaway et al. (2015) recommend.
- **Citation chasing**: backward and forward from all included studies and from Jiang et al. (2022).

## 6. Translations for each database

| Database | Field | Proximity | Notes |
|---|---|---|---|
| EBSCO (ERIC, APA PsycINFO) | `TI (…) OR AB (…) OR SU (…)` | `English N3 (…)` | |
| ProQuest (LLBA) | `NOFT(…)` | `English NEAR/3 (…)` | |
| Scopus | `TITLE-ABS-KEY(…)` | `English W/3 (…)` | |
| Web of Science | `TS=(…)` | `English NEAR/3 (…)` | |
| PubMed | `[tiab]` on each term | `"english learning"[tiab:~3]` etc. | PubMed ignores proximity for terms with `*` (PubMed Help), so each word form is listed. `ASD`, `L2`, `L3` are dropped because they collide with atrial septal defect and lumbar vertebrae |

**ERIC descriptors to add with OR** (each confirmed to exist in ERIC) [fact]:

- **#1 Participants**: DE "Dyslexia", "Attention Deficit Hyperactivity Disorder", "Autism Spectrum Disorders", "Autism", "Asperger Syndrome", "Learning Disabilities", "Intellectual Disability", "Developmental Disabilities", "Special Needs Students"
- **#2 Concept**: DE "Informal Education", "Independent Study", "Home Study", "Parent Participation", "Educational Games", "Video Games", "Leisure Time", "Television Viewing", "Homework"

Neither ERIC nor MeSH has a "Neurodiversity" heading, so the free-text terms cover it. [fact]

<details>
<summary>PubMed full string (run live 2026-09-28 → 305 records)</summary>

```
(neurodivers*[tiab] OR neurodivergen*[tiab] OR neurodevelopment*[tiab] OR "neuro-developmental"[tiab] OR "intellectual disabilit*"[tiab] OR "developmental disabilit*"[tiab] OR "learning disabilit*"[tiab] OR "learning difficult*"[tiab] OR "learning disorder*"[tiab] OR "learning difference*"[tiab] OR "specific learning"[tiab] OR SpLD[tiab] OR dyslexi*[tiab] OR "reading difficult*"[tiab] OR "literacy difficult*"[tiab] OR "attention deficit*"[tiab] OR hyperactiv*[tiab] OR ADHD[tiab] OR autis*[tiab] OR asperger*[tiab] OR "special educational need*"[tiab] OR "special need*"[tiab] OR "Neurodevelopmental Disorders"[Mesh] OR "Dyslexia"[Mesh] OR "Learning Disabilities"[Mesh] OR "Intellectual Disability"[Mesh])
AND
("beyond the classroom"[tiab] OR "beyond classroom*"[tiab] OR "outside the classroom"[tiab] OR "out-of-class"[tiab] OR "after-class"[tiab] OR "after school"[tiab] OR "out-of-school"[tiab] OR extracurricular[tiab] OR "extra-curricular"[tiab] OR "self-access"[tiab] OR "distance learning"[tiab] OR "distance education"[tiab] OR informal*[tiab] OR "non-formal"[tiab] OR nonformal[tiab] OR "naturalistic exposure"[tiab] OR "naturalistic acqui*"[tiab] OR "naturalistic learn*"[tiab] OR "non-instructed"[tiab] OR uninstructed[tiab] OR "incidental learn*"[tiab] OR "incidental acqui*"[tiab] OR "incidental exposure"[tiab] OR "self-instruct*"[tiab] OR "self-taught"[tiab] OR "self-teach*"[tiab] OR "self-learn*"[tiab] OR "self-study"[tiab] OR autonomy[tiab] OR autonomous[tiab] OR "independent learn*"[tiab] OR "independent study"[tiab] OR "self-directed"[tiab] OR "self-regulat*"[tiab] OR extramural[tiab] OR recreation*[tiab] OR leisure[tiab] OR digital*[tiab] OR technolog*[tiab] OR internet[tiab] OR online[tiab] OR "web-based"[tiab] OR virtual[tiab] OR computer*[tiab] OR software[tiab] OR mobile[tiab] OR app[tiab] OR apps[tiab] OR game*[tiab] OR gaming[tiab] OR gamif*[tiab] OR YouTube[tiab] OR video[tiab] OR videos[tiab] OR "video game*"[tiab] OR videogame*[tiab] OR television[tiab] OR "screen time"[tiab] OR "screen media"[tiab] OR "screen exposure"[tiab] OR "screen-based"[tiab] OR screens[tiab] OR "social media"[tiab] OR "media exposure"[tiab] OR "media use"[tiab] OR multimedia[tiab] OR subtitl*[tiab] OR caption*[tiab] OR cartoon*[tiab] OR audiovisual*[tiab] OR "unexpected bilingual*"[tiab] OR "non-interactive"[tiab] OR noninteractive[tiab] OR parent*[tiab] OR caregiv*[tiab] OR "at home"[tiab] OR "home-based"[tiab] OR "home learning"[tiab] OR "home literacy"[tiab] OR "home environment*"[tiab] OR homework[tiab] OR "Screen Time"[Mesh] OR "Television"[Mesh] OR "Video Games"[Mesh] OR "Mobile Applications"[Mesh] OR "Computer-Assisted Instruction"[Mesh] OR "Internet"[Mesh] OR "Parents"[Mesh])
AND
("english learning"[tiab:~3] OR "english learn"[tiab:~3] OR "english learned"[tiab:~3] OR "english learner"[tiab:~3] OR "english learners"[tiab:~3] OR "english teaching"[tiab:~3] OR "english taught"[tiab:~3] OR "english lessons"[tiab:~3] OR "english classes"[tiab:~3] OR "english homework"[tiab:~3] OR "english proficiency"[tiab:~3] OR "english acquisition"[tiab:~3] OR "english acquired"[tiab:~3] OR "english acquire"[tiab:~3] OR "english vocabulary"[tiab:~3] OR "english literacy"[tiab:~3] OR "english reading"[tiab:~3] OR "english skills"[tiab:~3] OR "english instruction"[tiab:~3] OR "english extramural"[tiab:~3] OR "english exposure"[tiab:~3] OR "english input"[tiab:~3] OR EFL[tiab] OR ESL[tiab] OR EAL[tiab] OR ELL[tiab] OR ELLs[tiab] OR TESOL[tiab] OR TEFL[tiab] OR ELT[tiab] OR "foreign language*"[tiab] OR "second language*"[tiab] OR "third language*"[tiab] OR "additional language*"[tiab] OR "non-native"[tiab] OR "non-English"[tiab] OR "unexpected bilingual*"[tiab])
```

</details>

## 7. How it was built

| Step | Finding |
|---|---|
| Original string | 0/5 required, 0/11 core. The Context block needed an EFL label that 4 of the 5 papers never use; parent-led home learning had no Concept terms [fact] |
| Earlier draft (bare `English`) | 5/5 and 11/11, but half the ERIC hits entered only via `English` [fact] |
| Tightened (this version) | `English` → `English N3 (…)`. Bare `disabilit*`, `home`, `family`, `media`, `screen`, `TV` narrowed or removed. `comput*` → `computer*`, `video*` → `video`/`videos`/`video game*` |
| Recall gap found | Mufidah (2024) says only "self-learning", so `"self-learn*"` and `"self-teach*"` were added [fact] |

## 8. Limits

- **Three of the 5 papers were verified by simulation, not live**. Alexandra, Schurz and Torsani are not in ERIC or PubMed, and OpenAlex search was rate-limited that day. [fact]
- **The ERIC count is an estimate**. The ERIC API has no proximity operator, so `N3` was applied locally to its 2,297 raw hits. [fact]
- **Not measured**: hit counts in Scopus, Web of Science, APA PsycINFO and LLBA (subscription access needed).

---

## References

- Abdulrahman, B. S., & Hamasaeed, Z. B. (2026). Exploring the challenges of teaching English to students with special educational needs: Parental perspectives in Kurdistan Region of Iraq. *Discover Education, 5*(1), Article 322. https://doi.org/10.1007/s44217-026-01244-z
- Alexandra, N. F., Artini, L. P., & Ana, I. K. T. A. (2025). Teaching English to second-grade dyslexia-prone students: Perspectives of Y-generation parents on foreign language learning in elementary school. *IJLHE: International Journal of Language, Humanities, and Education, 8*(1), 83–92. https://doi.org/10.52217/ijlhe.v8i1.1769
- Blázquez-Arribas, L., Barros-del Río, M. A., Alcalde Peñalver, E., & Sigona, C. M. (2020). Teaching English to adults with disabilities: A digital solution through En-Abilities. *Teaching English with Technology, 20*(1), 80–103. ERIC EJ1242672
- Bramer, W. M., de Jonge, G. B., Rethlefsen, M. L., Mast, F., & Kleijnen, J. (2018). A systematic approach to searching: An efficient and complete method to develop literature searches. *Journal of the Medical Library Association, 106*(4), 531–541. https://doi.org/10.5195/jmla.2018.283
- Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco, O. H. (2017). Optimal database combinations for literature searches in systematic reviews: A prospective exploratory study. *Systematic Reviews, 6*, Article 245. https://doi.org/10.1186/s13643-017-0644-y ⚠️ pre-2018 (methods standard)
- Coskun, Z. N., & Mitrani, C. (2020). An instructional design for vocabulary acquisition with a hidden disability of dyslexia. *Cypriot Journal of Educational Sciences, 15*(2), 305–318. https://doi.org/10.18844/cjes.v15i2.4671
- Du, Y., Wang, C., Zou, B., & Xia, Y. (2024). Personalizing AI tools for second language speaking: The role of gender and autistic traits. *Frontiers in Psychiatry, 15*, Article 1464575. https://doi.org/10.3389/fpsyt.2024.1464575
- Dumont, C., Belenger, M., Destrebecqz, A., & Kissine, M. (2025). Exploring unexpected bilingualism in autism: Enhanced sensitivity to non-adjacent dependencies. *Developmental Science, 28*(4), Article e70026. https://doi.org/10.1111/desc.70026
- Dumont, C., Belenger, M., Eigsti, I.-M., & Kissine, M. (2024). Enhanced pitch discrimination in autistic children with unexpected bilingualism. *Autism Research, 17*(9), 1844–1852. https://doi.org/10.1002/aur.3221
- Gagnon, D., Ostrolenk, A., & Mottron, L. (2026). Early manifestations of unexpected bilingualism in minimally verbal autism. *Journal of Child Psychology and Psychiatry, 67*(5), 652–662. https://doi.org/10.1111/jcpp.70032
- Golshan, F., Moinzadeh, M., Narafshan, M. H., & Afarinesh, M. R. (2019). The efficacy of teaching English as a foreign language to Iranian students with autism spectrum disorder on their social skills and willingness to communicate. *Iranian Journal of Child Neurology, 13*(3), 61–73. PMC6586454
- Haddaway, N. R., Collins, A. M., Coughlin, D., & Kirk, S. (2015). The role of Google Scholar in evidence reviews and its applicability to grey literature searching. *PLOS ONE, 10*(9), Article e0138237. https://doi.org/10.1371/journal.pone.0138237 ⚠️ pre-2018 (methods standard)
- Hashim, H. U., Yunus, M. M., & Norman, H. (2022). Autism children and English vocabulary learning: A qualitative inquiry of the challenges they face in their English vocabulary learning journey. *Children, 9*(5), Article 628. https://doi.org/10.3390/children9050628
- Hindi, I., & Meir, N. (2026a). Different paths to multilingualism in autism spectrum disorder (ASD): Naturalistic and non-interactive. *Journal of Child Language, 53*(2), 343–364. https://doi.org/10.1017/S0305000924000540
- Hindi, I., & Meir, N. (2026b). Non-interactive and naturalistic language exposure in autism: An investigation of narrative production in bilingual children. *Journal of Communication Disorders, 122*, Article 106650. https://doi.org/10.1016/j.jcomdis.2026.106650
- Jiang, Y., Wang, Q., & Weng, Z. (2022). The influence of technology in educating English language learners at-risk or with disabilities: A systematic review. *Center for Educational Policy Studies Journal, 12*(4), 53–74. https://doi.org/10.26529/cepsj.1426
- McGowan, J., Sampson, M., Salzwedel, D. M., Cogo, E., Foerster, V., & Lefebvre, C. (2016). PRESS peer review of electronic search strategies: 2015 guideline statement. *Journal of Clinical Epidemiology, 75*, 40–46. https://doi.org/10.1016/j.jclinepi.2016.01.021 ⚠️ pre-2018 (methods standard)
- Mufidah, N. (2024). Exploring influential factors and strategies for addressing speech delay of a child with autism spectrum disorder (ASD) in English (L2) language acquisition. *Journal on English as a Foreign Language, 14*(1), 73–96. https://doi.org/10.23971/jefl.v14i1.6580
- Papadima-Sophocleous, S., & Charalambous, M. (2014). Impact of iPod Touch-supported repeated reading on the English oral reading fluency of L2 students with specific learning difficulties. *The EUROCALL Review, 22*(1), 47–58. https://doi.org/10.4995/eurocall.2014.3639 ⚠️ pre-2018
- Pfenninger, S. E. (2015). MSL in the digital ages: Effects and effectiveness of computer-mediated intervention for FL learners with dyslexia. *Studies in Second Language Learning and Teaching, 5*(1), 109–133. https://doi.org/10.14746/ssllt.2015.5.1.6 ⚠️ pre-2018 (required paper)
- Pfenninger, S. E. (2016). Taking L3 learning by the horns: Benefits of computer-mediated intervention for dyslexic school children. *Innovation in Language Learning and Teaching, 10*(3), 220–237. https://doi.org/10.1080/17501229.2014.959962 ⚠️ pre-2018
- Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., Ayala, A. P., Moher, D., Page, M. J., Koffel, J. B., & PRISMA-S Group. (2021). PRISMA-S: An extension to the PRISMA Statement for Reporting Literature Searches in Systematic Reviews. *Systematic Reviews, 10*, Article 39. https://doi.org/10.1186/s13643-020-01542-z
- Schurz, A. (2026). Learning on their terms: Retrospective accounts of extramural English experiences among students with ADHD. *ITL – International Journal of Applied Linguistics, 177*(1), 88–115. https://doi.org/10.1075/itl.25021.sch
- Subekti, A. S., & Lestariningsih, F. E. (2023). Individualized guidance to empower an L2 learner with autism spectrum disorder in academic essay writing. *TEFLIN Journal, 34*(2), 320–336. https://doi.org/10.15639/teflinjournal.v34i2/320-336
- Torsani, S. (2025). From classroom to caregiving: Technology as a tool for special educational needs inclusion, a case study. *Computer-Assisted Language Learning Electronic Journal, 26*(2), 149–172. https://doi.org/10.54855/callej.252626
- Zhukova, M. A., Talantseva, O. I., An, I., & Grigorenko, E. L. (2023). Brief report: Unexpected bilingualism: A case of a Russian child with ASD. *Journal of Autism and Developmental Disorders, 53*(5), 2153–2160. https://doi.org/10.1007/s10803-021-05161-y
