# 파일럿 검색 로그 (2026-09-27)

실행 가능성 판단을 위한 **파일럿 검색**이다. 본 리뷰의 최종 검색이 아니다.

## 1. 데이터베이스와 접근 상태

| 데이터베이스 | 상태 | 비고 |
|---|---|---|
| ERIC (IES API) | 사용 | 제목·초록·주제어 불리언 검색 |
| PubMed (E-utilities) | 사용 | `[tiab]` 필드 |
| Europe PMC (REST) | 사용 | 일부는 전문(full text) 검색 |
| Semantic Scholar (bulk search) | 사용 | 제목·초록 불리언 검색 |
| Crossref | 사용 | 서지 확인·표적 검색용 |
| RISS (KCI 등재지 포함) | 사용 | 국내 학술지 검색 |
| OpenAlex | 실패 | 공유 IP의 일일 무료 한도 소진 (API 키 필요) |
| Scopus, Web of Science, PsycINFO, LLBA, ProQuest Dissertations | 미접근 | 기관 구독 필요 |
| Google Scholar | 미접근 | 자동 조회 차단 |

## 2. 개념 블록 (PCC)

- **P (신경발달 조건)**: dyslexi\*, "learning disabilit\*", "learning difficult\*", "specific learning", SpLD, autis\*, Asperger\*, "autism spectrum", ADHD, "attention deficit", hyperactiv\*, neurodivers\*, neurodivergen\*, neurodevelopmental, "special educational needs", "special needs"
- **L (영어/외국어)**: "English as a foreign language", EFL, "foreign language\*", "second language\*", L2, "English learn\*", "English language learn\*", ESL, "additional language", "English acquisition"
- **C (교실 밖 학습, LBC)**: "beyond the classroom", "out-of-class", "out of class", "outside the classroom", "out-of-school", extramural, informal, "self-directed", "self-access", "self-regulated", autonom\*, incidental, "in the wild", "digital wilds", leisure, "video game\*", "digital game\*", gaming, YouTube, television, "screen media", "screen exposure", "social media", subtitl\*, caption\*, "home literacy", "at home", "home environment", parent\*, "mobile app\*", "online learning", "language exposure", "media exposure"

## 3. 적중 건수

### 3.1 3개 블록 교차 (P × L × C)

| 데이터베이스 | P × L | P × L × C |
|---|---:|---:|
| ERIC | 1,446 | 332 (동료심사 148) |
| PubMed | 721 | 109 |
| Semantic Scholar | 3,002 | 403 |

### 3.2 조건별 표적 검색

| 검색 | 데이터베이스 | 적중 |
|---|---|---:|
| 자폐 × 스크린/비상호작용 × 영어/외국어 (+ "unexpected bilingualism") | PubMed | 225 |
| 같은 주제 | Europe PMC | 14 |
| 같은 주제 | Semantic Scholar | 60 |
| 난독증 × 외국어/EFL × LBC 용어 | PubMed | 20 |
| 난독증 × LBC 용어 (전문 검색) | Europe PMC | 35 |
| 난독증·SpLD × 영어 × LBC 용어 | Semantic Scholar | 198 |
| ADHD × 외국어/EFL | PubMed | 70 |
| ADHD × LBC 용어 (전문 검색) | Europe PMC | 206 |
| ADHD × 영어 × LBC 용어 | Semantic Scholar | 163 |
| 자폐 × 영어 × LBC 용어 | Semantic Scholar | 330 |
| 신경다양성(포괄어) × 영어 × LBC 용어 | Semantic Scholar | 112 |
| 신경다양성 × LBC 용어 (전문 검색) | Europe PMC | 14 |
| 조건 × 자기주도/독학/학습자 자율성 × 언어 | Semantic Scholar | 102 |
| 조건 × 게임/팬덤/SNS × 외국어 | Semantic Scholar | 4 |

### 3.3 국내 (RISS, 국내 학술지)

| 검색어 | 적중 | 핵심 후보 |
|---|---:|---:|
| 난독증 영어 | 6 | 0 |
| ADHD 영어 학습 / 주의력결핍 영어 | 2 / 2 | 0 |
| 자폐 영어 | 11 | 0 (경계 1) |
| 학습장애 영어 학습 | 100+ | 0 |
| 신경다양성 영어 | 5 | 0 |

## 4. 선별 방법

- 중복을 포함해 약 2,500건의 제목을 1인이 검토했다. 관련 가능성이 있는 건은 초록까지 확인했다.
- 핵심 후보는 Crossref로 서지 정보(DOI, 권·호·쪽)를 검증했다.
- 분류 기준은 `README.md`의 등급 정의(A/B/C/R/X/K)를 따른다.

## 5. 주요 쿼리 원문

### Semantic Scholar (P × L × C)

```
(dyslexi* | "learning disability" | "learning disabilities" | "learning difficulties" | "specific learning difficulties" | "specific learning disorder" | SpLD | autis* | Asperger* | ADHD | "attention deficit" | neurodivers* | neurodivergen* | "special educational needs")
+ ("English as a foreign language" | EFL | "foreign language" | "foreign languages" | "second language" | L2 | "English learners" | "English language learning" | "English learning" | "unexpected bilingualism")
+ ("beyond the classroom" | "out-of-class" | "out of class" | "outside the classroom" | "out-of-school" | "out of school" | extramural | informal | "self-directed" | "self-regulated" | autonomous | autonomy | incidental | "in the wild" | leisure | "video games" | "digital games" | "video game" | gaming | YouTube | television | screen | screens | "social media" | subtitles | "mobile app" | apps | "at home" | "unexpected bilingualism" | "non-interactive")
```

### PubMed (자폐 × 스크린 표적 검색)

```
("unexpected bilingual*"[tiab]) OR ((autis*[tiab]) AND (screen*[tiab] OR television[tiab] OR YouTube[tiab] OR cartoon*[tiab] OR "non-interactive"[tiab] OR noninteractive[tiab] OR "passive exposure"[tiab] OR "media exposure"[tiab]) AND ("foreign language*"[tiab] OR English[tiab] OR bilingual*[tiab] OR "second language"[tiab]))
```

### 본 리뷰에 추가할 용어 (파일럿에서 도출)

- 자폐 연구 쪽 용어: "unexpected bilingualism", "non-interactive", "noninteractive", "screen-based", "audiovisual exposure", "self-taught", "spontaneously acquired"
- 제2언어습득 쪽 용어: "extramural English", "informal digital learning of English" (IDLE), "language learning beyond the classroom"
- 주의: `screen*`는 "screening"을 대량으로 잡는다. `screen OR screens OR "screen media" OR "screen time"`처럼 절단 없이 쓴다.
