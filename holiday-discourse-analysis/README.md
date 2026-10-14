# 담화 분석: 두 EFL 학습자의 명절 대화 (CHAT/CLAN)

> 자료: [`data/holiday.cha`](data/holiday.cha) · CLAN 원출력: [`clan-output/`](clan-output/) · 발화별 코딩: [`coding/holiday_coding.csv`](coding/holiday_coding.csv) · 자동 요약표: [`coding/summary.md`](coding/summary.md)
> 분석일: 2026-10-14 · 도구: Unix CLAN (21-Sep-2026 빌드) + Python 코딩 스크립트

**TL;DR:** 두 화자의 참여량은 거의 대칭적이지만(발화권 46 대 45, 단어 656 대 626), 담화 역할은 에피소드마다 "설명자/청자"로 교대된다. 의미 협상 21건은 역할을 따라 갈린다. 설명자 LEX는 이해 점검(6/7)을, 청자 MAR는 확인 점검(5/7)을 주로 쓴다. LEX의 긴 어휘 탐색 세 차례는 모두 근사어로 끝나고 MAR가 그대로 수용한다. 전사본은 CLAN CHECK를 통과했지만, 중복 의심 발화·끼어들기 기호·비언어 맥락 누락 등 보완할 점이 6가지 남아 있다(8절).

표기: **[사실]** 전사본·CLAN 출력에서 직접 확인 · **[추론: 강/중/약]** 사실에서 도출한 해석과 그 강도 · **[추측]** 자료 밖의 해석

줄 번호 `L`은 텍스트 편집기 기준 파일 줄 번호다. 이 빌드의 CLAN 출력은 `@UTF8` 줄을 빼고 세므로 같은 발화가 1 작게 표시된다(예: L8 → CLAN line 7).

---

## 1. 핵심 결과

- **참여 대칭**: 발화권 LEX 46, MAR 45이고 단어 수 차이는 30개다. 발화권당 단어(MLT)도 14.3 대 13.9로 비슷하다. [사실: `05_mlt.txt`]
- **역할 교대 구조**: 9개 에피소드 중 7개에서 한 화자가 단어의 60% 이상을 차지하고, 주 화자는 E7까지 번갈아 바뀐다. 과제 질문(L8, L54–57)이 거시 구조를 만든다. [사실: 에피소드 표] [추론: 강]
- **의미 협상의 역할 분화**: 이해 점검(CMC) 7건 중 6건이 LEX, 확인 점검(CC) 7건 중 5건이 MAR다. 자기 문화를 설명하는 쪽은 상대의 이해를 점검하고, 듣는 쪽은 자기 이해를 확인한다. [사실: 빈도] [추론: 중]
- **담화표지도 같은 방향**: LEX는 청자 지향 표현(담화표지 `you know` 3회, `do/did you know …?` 4회, 부가의문 `right ?` 3회)을 쓴다. MAR는 화자 지향 표지(`I mean` 4회, `I think` 4회)를 쓴다. [사실: FREQ/grep] [추론: 중]
- **어휘 탐색 → 근사어 → 수용**: LEX의 탐색 발화 14건 중 12건은 세 차례 긴 탐색(ritual, baptized, divine)이고, 2건은 마니또 정의 시도(L31, L33)다. 긴 탐색 세 번 모두 MAR가 근사어를 받아들이고 대화가 진행된다. 정확성보다 진행성을 택하는 양상이다(Rydell, 2019). [사실] [추론: 중]
- **문법 오류는 협상 대상이 아님**: `we left the food there`(습관 현재에 과거형), `is going to came`, `Asians different` 등은 어떤 수정 요청도 유발하지 않았다. 협상 21건은 모두 어휘·지시 대상·내용 확인을 향한다. [사실] 이는 "let it pass" 원리(Firth, 1996)와 맞는다. [추론: 중]
- **어휘 정렬은 MAR 쪽이 강함**: 앞선 상대 발화와 단어가 겹치는 반응 비율은 MAR 35.0%, LEX 26.3%다. 모방(IMITAT)도 MAR 7건, LEX 4건이다. [사실: CHIP] [추론: 중]
- **비교 담화의 수렴**: "비슷하다"(MAR, L113)에서 "다르다"(LEX, L120–121)로 이어진 협상은 MAR의 단계적 양보(L124 → L126 → L128)로 수렴한다. 이후 둘은 "관습은 다르지만 믿음은 같다"(L189–192)는 공통 기반에 도달한다. [사실] [추론: 중]
- **전사 보완 6건**: L82/L84 중복 의심, L48 발음 대조 소실, 끼어들기 기호, 한국어 차용어 표기, 사진·검색 등 비언어 맥락, `%mor` 부재다. [사실] 세부는 8절에 있다.

## 2. 자료와 방법

### 2.1 자료 [사실]

| 항목 | 값 |
|---|---|
| 화자 | MAR, LEX (헤더 역할: Participant) |
| 상황 | "two EFL learners talk about how they celebrate holidays" (`@Situation`) |
| 언어 | `@Languages: eng, spa` |
| 발화 수 | 214 (LEX 114, MAR 100) |
| 화자 배경(발화 근거) | MAR: 페루(L144–147 "in my country… in Peru") · LEX: 한국(L25 "here in Korea, we call that Manito") |

- 두 화자는 대화 전부터 아는 사이로 보인다(L29–30). [추론: 중] 관계의 성격은 알 수 없다.

### 2.2 CLAN 분석 절차

CLAN은 TalkBank의 CHAT 전사 분석 도구이며, 이 분석은 Unix 소스를 직접 컴파일해 실행했다(MacWhinney, 2000; MacWhinney & Fromm, 2022). 전체 명령은 [`scripts/run_clan.sh`](scripts/run_clan.sh)에 있다.

| 명령 | 목적 | 출력 |
|---|---|---|
| `check` | CHAT 형식 검증 | `01_check.txt` → **ALL FILES CHECKED OUT OK** |
| `freq +t*SPK +o` | 화자별 어휘 빈도, TTR | `02`, `03` |
| `mlu -t%mor` | 주 발화줄 기준 단어 MLU | `04` |
| `mlt` | 발화권 길이 | `05` |
| `maxwd` | 최장 발화 | `06` |
| `vocd -t%mor` | 어휘 다양도 D | `07` |
| `kwal`, `combo` | 수정·미완결·채움말·코드전환·질문·관용 표현 추출 | `10`–`18` |
| `chip +bLEX +cMAR -t%mor` | 화자 간 반복·정렬 | `15`, `16` |

- **`-t%mor`의 의미**: 이 전사본에는 형태소 층위(`%mor`)가 없다. 그래서 MLU는 형태소가 아니라 **단어** 기준이다. [사실]
- **CHIP 주의**: CHIP은 원래 성인(ADU)–아동(CHI) 상호작용용이다(Sokolov & MacWhinney, 1990). 여기서는 LEX를 ADU, MAR를 CHI 자리에 놓았을 뿐 연령 의미는 없다.
- **제외한 명령**: FLUCALC는 말더듬 코딩과 단일 언어 지정을 전제한다. 이 파일에서는 실행되지 않아 KWAL 집계로 대신했다.

### 2.3 수동 담화 코딩

[`scripts/discourse_coding.py`](scripts/discourse_coding.py)가 발화마다 수동 코드와 CHAT 기호 기반 자동 코드를 붙인다. 스크립트의 단어 수는 CLAN MLU와 정확히 일치한다(656/626). [사실]

| 범주 | 코드 | 정의 | 근거 틀 |
|---|---|---|---|
| 의미 협상 | CR | 명료화 요청 (`what is that ?`, `Manito ?`) | Long (1983); Varonis & Gass (1985) |
| | CC | 확인 점검: 상대 발화를 재구성해 확인 (`so you eat it .`) | 같음 |
| | CMC | 이해 점검: 상대가 내 말을 아는지 확인 (`do you know bow ?`) | 같음 |
| 수정 | SSR / RETRACE / REPEAT | 자기 수정(어휘 교체) / `[//]` / `[/]` | Schegloff et al. (1977) |
| | OC | 타인 시작 이의·정정 (L145) | 같음 |
| 의사소통 전략 | WS, APX, CIRC, APW, CSW, RES, ABN, MLC | 어휘 탐색, 근사어, 우회 설명, 범용어, 코드 전환, 외부 자원(검색·사진), 메시지 포기, 메타언어 논평 | Dörnyei & Scott (1997) |
| 상호작용 | MIN, ASM, AGR, DIS, COL, CMP | 최소 반응, 평가, 동의·정렬, 불일치, 공동 완성, 문화 비교 | Pickering & Garrod (2004) 외 |
| 담화 구조 | TSK, TOP, QI, CLS | 과제·발화권 관리, 화제 개시·전환, 정보 질문, 종결 | Sacks et al. (1974) |

- **발화권(turn)**: 화자가 바뀌는 지점마다 새 발화권으로 셌다. CLAN MLT의 집계(46/45)와 일치한다. [사실]
- **신뢰도**: 코더는 1인이다. 2차 코더 검증은 하지 않았다(10절).

## 3. 양적 결과 (CLAN)

| 지표 | LEX | MAR | 출처 |
|---|---:|---:|---|
| 발화 수 | 114 | 100 | MLU |
| 단어(토큰) | 656 | 626 | FREQ |
| 유형(type) / TTR | 189 / 0.288 | 179 / 0.286 | FREQ |
| VOCD D | 53.47 | 57.20 | VOCD |
| MLU (단어, SD) | 5.75 (4.42) | 6.26 (5.75) | MLU `-t%mor` |
| 발화권 | 46 | 45 | MLT |
| 발화권당 단어 / 발화 | 14.26 / 2.48 | 13.91 / 2.22 | MLT |
| 질문(`?` 종결) | 22 | 11 | KWAL |
| 최소 반응 발화 (`yeah .` 등) | 16 | 24 | 코딩 스크립트 |
| 최장 발화 | 28단어 (L83) | 26단어 (L15) | MAXWD |
| `[//]` 수정 / `[/]` 반복 | 1 / 0 | 3 / 1 | KWAL |
| `+...` 흐려짐 / `+//.` 자기 중단 | 1 / 1 | 4 / 0 | KWAL |
| 채움말 `&-` | 1 | 1 | KWAL |
| `@s:spa` 코드 전환 발화 | 0 | 1 (L149) | KWAL |

- **양은 대칭, 형태는 비대칭**: 총량은 비슷하다. LEX는 짧은 발화와 질문이 많고, MAR는 더 길게 말하며 최소 반응을 더 많이 낸다. [사실] [추론: 중]
- **어휘 다양도**: D 차이(약 3.7)는 작다. VOCD는 무작위 표본 추출이라 실행마다 ±1 정도 변한다(다른 실행: 54.07 / 57.27, 53.23 / 56.70, 53.32 / 57.07). [사실] 이 정도 차이에 해석적 의미를 두기는 어렵다. [추론: 중]
- **VOCD 토큰 수 차이**: VOCD 토큰(658/634)은 FREQ(656/626)보다 많다. VOCD 출력에는 `[//]`·`[/]`로 고쳐진 원래 표현(`you have`, `this person` 등)이 들어 있고, 그 단어 수가 차이(LEX 2, MAR 8)와 정확히 맞는다. [사실]
- **고빈도 표지**: `like` LEX 34 / MAR 14, `yeah` LEX 31 / MAR 40, `of course` LEX 6 / MAR 2, `I don't know` LEX 6 / MAR 3. [사실]

## 4. 담화 구조: 에피소드 지도

| 에피소드 | 줄 | 내용 | 주 화자 (단어 점유) |
|---|---|---|---|
| E0 과제 시작·주제 협상 | L8–11 | LEX 질문 → MAR 명료화 요청 → "traditional holiday"로 범위 축소 | LEX 74% |
| E1 MAR의 크리스마스(페루) | L12–53 | 가족 모임, 게임, Secret Santa=마니또, 칠면조, 파네토네, 자정 불꽃, 선물 | MAR 66% |
| E2 역할 전환 | L54–62 | LEX "ask me" → MAR 질문 3연속 → LEX가 질문을 추석으로 돌려 MAR에게 반환 | LEX 64% |
| E3 MAR의 추석 | L63–68 | "nothing" → "what ?" → 친구들과 보낸 하루 | MAR 98% |
| E4 LEX의 추석 성묘·차례 | L69–112 | 묘지, 조상, 음식, 절, 친척 모임, "ritual" 탐색 | LEX 84% |
| E5 비교: 코코·멕시코 | L113–128 | 유사성 제안 → 차이 강조 → 수렴 | MAR 73% |
| E6 음식: 두고 오기 vs 먹기 | L129–172 | 음식 처리 질문, 페루 Día de los Muertos, 막걸리, 음복 | LEX 58% |
| E7 사진·조상의 음식 | L173–203 | 사진 보여주기, "spirit of the food" 공동 구성 | MAR 53% |
| E8 페루 묘지·종결 | L204–221 | 바퀴벌레 농담 거절, 장난감, "very interesting", "yay" | MAR 64% |

- **E2의 발화권 관리**: LEX는 `ask me`(L54)로 역할 교대를 요청한다. 그런데 MAR가 질문하자 다시 `what did you do this Chuseok ?`(L62)로 질문자 자리를 되찾는다. [사실] 그 결과 MAR의 추석(E3)이 먼저 나오고, LEX의 추석(E4)은 `because in our case`(L69)라는 대조 틀로 시작한다. [추론: 강]
- **대칭 종결 공식**: MAR는 두 번의 서사를 같은 방식으로 닫는다. `that's all that we did`(L53), `that's all`(L68)이다. [사실]
- **E0과 E2의 거울 구조**: 질문을 받은 쪽이 둘 다 범위를 되묻는다. MAR `what kind of holiday ?`(L9), LEX `what holidays ?`(L58)이다. [사실]

## 5. 의미 협상

### 5.1 분포 [사실]

| 유형 | LEX | MAR | 계 | 집중 에피소드 |
|---|---:|---:|---:|---|
| 명료화 요청 CR | 4 | 3 | 7 | E0–E3 |
| 확인 점검 CC | 2 | 5 | 7 | MAR: E4·E6 |
| 이해 점검 CMC | 6 | 1 | 7 | LEX: E4 (5건) |

- **역할에 따른 분화**: LEX의 CMC 6건은 모두 자기 관습을 설명하는 E4·E6에 있다. MAR의 CC 5건도 같은 에피소드에서 청자로서 나온다. [사실] 협상 유형은 개인 성향보다 그 순간의 담화 역할을 따르는 것으로 보인다. [추론: 중]
- **이론적 위치**: 상호작용 연구에서 의미 협상은 L2 발달을 돕는 기제 중 하나다. 다만 그 효과는 과제, 대화 상대 등 여러 조건에 좌우된다(Loewen & Sato, 2018).

### 5.2 사례 1: 명료화 + 재구성 (L17–21)

```
L17 *MAR: and <you have> [//] basically we try to do it Christmas funny .   ← 유발(trigger)
L18 *LEX: funny ?                                                        ← 신호(indicator): 반복형 명료화 요청
L19 *LEX: in a fun way, you mean ?                                       ← 신호: 재구성형 확인 점검
L20 *MAR: yeah, yeah, yeah .                                             ← 응답(response)
L21 *MAR: because we try to play some games and also do the Secret_Santa .
```

- **구조**: Varonis & Gass (1985)의 유발–신호–응답 모형에 맞는다. 응답에 대한 반응(reaction) 단계 없이 MAR가 바로 서사로 돌아간다. [사실]
- **형태 교정 기능**: L19의 `in a fun way`는 `funny`를 `fun`으로 바꾼 재구성이다. 확인 점검 안에 암묵적 교정이 들어 있다. [추론: 중]
- **흡수(uptake) 없음**: MAR는 이후 `fun`을 쓰지 않는다(FREQ: MAR `fun` 0회). [사실]

### 5.3 사례 2: 18줄에 걸친 "Manito" 협상 (L22–40)

```
L22 *MAR: do you know Secret_Santa ?          ← 이해 점검
L23 *LEX: what is that ?                      ← 명료화 요청
L24 *LEX: oh, like, yeah, Manito .            ← 자기 해결 + 한국어 대응어
L26 *MAR: Manito ?                            ← 명료화 요청 (반복형)
L28 *LEX: I guess that's a French word .      ← 메타언어 논평
L29 *LEX: I thought, oh, your ex is French .   ← 짧은 부연 (L29–30)
L30 *MAR: he never told me about Manito .
L31 *LEX: Manito is, I guess it's something like +//.
L32 *LEX: oh, bye Paula .                     ← 설명 중단
L33 *LEX: I guess it's something like +...
L34 *LEX: wait, I don't know .                ← 메시지 포기
L35 *MAR: Manito ?                            ← 명료화 재요청
L37 *LEX: ... you have like to give a present to someone .   ← 우회 설명
L38 *MAR: yeah, but you are secret .          ← 공동 구성 (핵심 의미 보충)
L39 *LEX: yeah, yeah, <you don't> [//] the other person doesn't know ...
L40 *MAR: yeah .
```

- **확장된 협상**: 명료화 요청이 두 번 나오고, 그 사이에 이탈·외부 중단·포기가 끼어든다. [사실]
- **해결은 공동 작업**: LEX가 정의의 절반(선물), MAR가 나머지 절반(비밀)을 채운다. L39에서 LEX가 MAR의 보충을 자기 말로 다시 받는다. [사실] 협상이 단순 오해 해소를 넘어 개념을 함께 만드는 과정이 된다. [추론: 중]
- **방향의 역전**: MAR가 영어 표현(Secret Santa)을 꺼냈지만 설명 부담은 한국어 대응어를 꺼낸 LEX에게 넘어간다. [사실]

### 5.4 사례 3: 해소되지 않은 극성(polarity) 모호성 (L154–156)

```
L154 *LEX: and then if there's like makgeolli, you haven't heard of makgeolli, right ?
L155 *MAR: yeah .
L156 *LEX: we have the makgeolli .
```

- **모호성**: 부정 의문에 대한 `yeah`는 "들어봤다"와 "안 들어봤다(네, 맞아요)" 둘 다로 읽힌다. [사실] 영어와 한국어·스페인어는 부정 의문 응답 방식이 다를 수 있다. [추론: 약]
- **처리 방식**: LEX는 확인 없이 진행한다. 이는 대화 진행에 지장이 없는 불명확성을 그냥 넘기는 "let it pass" 처리로 볼 수 있다(Firth, 1996). [추론: 중] MAR가 실제로 막걸리를 알았는지는 자료로 판단할 수 없다.

## 6. 수정과 의사소통 전략

### 6.1 수정 [사실]

- **자기 수정 8건**: `[//]` 4건(MAR 3, LEX 1)과 어휘 교체 4건이다. 어휘 교체는 L51 `artificial fireworks` → `fireworks`, L71 `tombs` → `cemetery`, L75 `spirits` → `ancestors`, L149 `who left` → `who died`다.
- **타인 시작 수정 1건**: MAR가 `in Mexico and also in my country`(L144)라고 하자 LEX가 `but you're not from Mexico .`(L145)로 이의를 제기한다. MAR는 `no, no . but in Peru`(L146–147)로 스스로 고친다.
- **자기 수정 선호**: 수정은 거의 모두 화자 자신이 시작하고 완료한다. 대화 분석의 "자기 수정 선호" 경향과 일치한다(Schegloff et al., 1977). [추론: 중]
- **L1 전이 가능성**: `artificial fireworks`는 스페인어 `fuegos artificiales`의 직역일 수 있다. [추론: 중] `the reverence`(L95)는 스페인어 `reverencia`(절, 인사)의 동족어일 수 있다. [추론: 중]

### 6.2 LEX의 세 차례 어휘 탐색

| 줄 | 탐색 표지 | 해결 | MAR의 처리 | 목표어 후보 [추론: 중] |
|---|---|---|---|---|
| L99–109 | `what do you call that ?` `I forgot .` `it's not ceremony .` `there is this English term` | `it's like ritual .` (근사어) | `yeah . yeah . something like that .` | ancestral rite, memorial service |
| L137–140 | `I don't know how to call it baptized .` | `baptized` (종교 유추) | `you go with the food, like kind of to share and eat…` (후보 이해 제시) | blessed, consecrated |
| L158–161 | `wait, I'll search the term .` | 검색 → `divine` | `yeah . yeah .` | sacred, blessed |

- **공통 경로**: 탐색 표지 → 근사어 → 청자 수용 → 진행이다. [사실] 이는 L2 화자가 어휘의 정확성보다 대화의 진행성을 택한다는 관찰과 맞는다(Rydell, 2019). [추론: 중]
- **비속어 감탄**: `what the fuck ?`(L104, L140)은 두 번 모두 탐색이 길어지는 지점에 나온다. [사실] 탐색 난항을 표시하는 기능일 수 있다. [추론: 약] 화자의 정서 상태는 자료로 판단하지 않는다.
- **외부 자원**: L159의 검색과 L174–175의 사진 보여주기는 언어 밖 자원을 동원한 전략이다(Dörnyei & Scott, 1997). [사실] 다만 전사본에는 무엇을 검색하고 보여줬는지가 없다(8절).

### 6.3 전략 목록 (Dörnyei & Scott, 1997 분류) [사실]

| 전략 | 사례 (줄) | 화자 |
|---|---|---|
| 근사어 | ritual (L109), baptized (L139), divine (L161), tempura (L83), the reverence (L95), tombs/graves (L69–70) | 주로 LEX |
| 우회 설명 | 마니또 정의 (L37), 영혼의 음식 (L194, L200) | LEX |
| 범용어 | `this thing` (L73), `those kind of …` (L83, L99, L137, L169; 5회) | LEX |
| 코드 전환 | `el@s:spa Día_de_los_Muertos@s:spa` + 영어 풀이 (L149) | MAR |
| 메타언어 논평 | French word (L28), 발음 대조 (L48), Japanese word (L83), `I don't know how to say it in English` (L148) | 둘 다 |
| 메시지 포기 | `wait, I don't know .` (L34) | LEX |
| 외부 자원 | 검색 (L159), 사진 (L174–175) | LEX |

- **명시적 코드 전환의 신호화**: MAR는 스페인어를 쓰기 전에 `I don't know how to say it in English`(L148)로 예고하고, 쓴 뒤에는 영어로 풀이한다. [사실] 코드 전환을 영어 담화 안에서 투명하게 만드는 방식이다. [추론: 중]
- **단어 제안 수용**: MAR의 `the reverence`(L95) 제안을 LEX가 `yeah, yeah . we do that .`(L96–97)으로 받는다. Pietikäinen (2018)의 커플 ELF 대화에서는 상대에게 단어를 제안하는 일을 피했다. 이 대화에서는 제안이 나오고 수용된다. [사실] 관계 친밀도나 과제 성격의 차이일 수 있다. [추측]

## 7. 상호작용적 정렬과 상호문화 비교

### 7.1 청자 지원

- **최소 반응**: MAR의 최소 반응 24건 중 17건이 LEX가 설명하는 E4·E6·E7에 있다. [사실] 그중 L162–163, L177–179처럼 `yeah`가 연달아 나오는 구간은 LEX의 설명을 계속 이어가게 하는 신호로 기능한다. [추론: 중]
- **CHIP 정렬 지표**: MAR의 반응 중 35.0%가 앞선 LEX 발화(CHIP 기본 탐색 범위)와 단어를 공유한다(LEX는 26.3%). 모방(IMITAT: 확장·축소 포함)도 MAR 7건, LEX 4건이다. [사실] 대화 상대의 표현을 재사용하는 어휘 정렬은 L2 대화에서도 관찰된다(Michel & Cappellini, 2019; Pickering & Garrod, 2004). [추론: 중]

### 7.2 유사성과 차이의 협상 (L113–128)

```
L113 *MAR: I think it's very similar to Mexican .
L114 *MAR: did you see the movie Coco ?
L120 *LEX: but it's not that pretty .
L121 *LEX: you know, it's like Asians different .
L123 *MAR: but I mean, the fact that you go to the tomb and give food, I think it's very related to it .
L124 *MAR: but of course, it's very different, like in some ways .
L126 *MAR: in this case, it's quite different, I guess .
L128 *MAR: I think it's different .
```

- **공통 기반 자원**: MAR는 대중문화(영화 Coco)를 비교의 공통 기반으로 끌어온다. [사실]
- **단계적 수렴**: MAR는 `very related`(L123)를 유지하다가 `very different, like in some ways`(L124), `quite different, I guess`(L126), `different`(L128)로 옮겨 간다. [사실] 유보 표현이 점점 줄어드는 순서다. [추론: 중]

### 7.3 관습의 차이, 믿음의 공유 (L187–203)

```
L187 *MAR: but we leave it .
L188 *LEX: we drink it .
L189 *MAR: no, we didn't drink because we thought that <this person> [//] the soul of this person is going to came to drink it .
L190 *LEX: yeah, us too .
L192 *LEX: me too .
L194 *LEX: they will eat it and drink it, but that's what the spirit of the food .
L200 *LEX: like the human food and then the ancestors .
L202 *MAR: because you cannot see it .
L203 *LEX: yeah, of course .
```

- **대조 병렬**: L187–188은 같은 구조의 짧은 대조 쌍이다. [사실]
- **층위 분리**: 두 화자는 "음식을 두고 온다/먹는다"는 관습과 "영혼이 와서 먹는다"는 믿음을 구분한다. 그리고 믿음 층위에서 정렬한다(L190, L192). [사실] [추론: 강]
- **공동 설명**: "인간의 음식"과 "영혼의 음식"을 구분한 LEX의 설명(L194, L200)에 MAR가 근거(`because you cannot see it`, L202)를 덧붙이고, LEX가 승인한다(L203). [사실]

### 7.4 공동 완성과 거절

- **수용된 공동 완성**: L38, L141, L202, L217. [사실]
- **거절된 공동 완성**: MAR의 흐려진 발화(L207 `like in Peru +...`) 뒤에 LEX가 `of course, cockroaches will eat it .`(L208)로 끝을 채운다. MAR는 `no .`(L211)로 거절하고 원래 하려던 내용(장난감, L212–214)을 이어 간다. [사실] 상대가 완성한 내용이 의도와 다를 때 발화권을 되찾는 장면이다. [추론: 중]
- **`of course` 8회**: LEX 6회, MAR 2회이며 모두 E5 이후에 나온다. [사실] 질문에 대한 `of course`는 당연함을 함축할 수 있다. [추론: 약] 그러나 전사본에서 MAR의 부정적 반응은 관찰되지 않는다. [사실]

## 8. 전사 품질 점검: CHECK 통과 후 남은 사항

CHECK는 형식 오류만 잡는다. 아래는 형식은 맞지만 분석 타당도에 영향을 주는 항목이다.

| # | 문제 (줄) | 원인 [추론] | 수정안 | 예방 |
|---|---|---|---|---|
| 1 | L82와 L84가 `but yeah, I know .`로 동일 | 전사 중 복붙 중복 또는 실제 반복 | 음성 확인 후 하나 삭제하거나 `[/]`/`%com:`으로 표시 | 전사 후 연속 동일 발화 자동 검출 |
| 2 | L48 `in Spanish we said panettone, not panettone like Italian`에서 대조가 사라짐 | 철자를 이탈리아어로 통일 | `panetón@s:spa` 등 실제 발음형으로 전사하거나 `%pho:`/`%com:` 추가 | 발음 대조 발화는 철자 통일 금지 |
| 3 | L41, L207의 `+...` 뒤에 상대 발화가 바로 이어짐 | 상대가 끊었는지 스스로 흐렸는지 구분이 없음 | 상대가 끊었으면 `+/.`, 이어 말하기는 `+,` 사용 | 겹침은 `[>]`/`[<]` 표기 |
| 4 | `Chuseok`, `makgeolli`, `soju`, `Manito`에 언어 표지 없음 | `@Languages`에 kor 없음 | 표기 정책을 정한 뒤 일관 적용. 표지하려면 `@Languages`에 kor을 추가하고 `@s:kor` 사용 | 차용어 처리 규칙을 전사 지침에 명시 |
| 5 | 사진(L174–182)·검색(L159)의 맥락 없음. `this one`의 지시 대상 복원 불가 | 비언어 층위 미전사 | `%act:`/`%com:` 층위 추가 | 영상 기반 전사, `@Media`와 시간 정보 연결 |
| 6 | `%mor` 없음 → 형태소 MLU·품사 분석 불가 | MOR 미실행 | `mor` 실행(후속 `post`)으로 `%mor` 생성 | CHECK 직후 MOR 실행을 표준 절차로 |

- **선택적 검토**: L50 `and then we have at twelve, we have the artificial fireworks`의 `we have` 반복은 `[/]` 코딩 후보다. 음성으로 확인할 필요가 있다.

## 9. 교육적 시사점

- **목표 어휘**: 탐색된 개념의 영어 표현을 미리 다룰 수 있다. ancestral rite / memorial service(차례), bow(절), blessed / consecrated(음복 맥락), Day of the Dead. [추론: 중]
- **부정 의문 응답**: `you haven't heard of X, right ?`에 대한 응답 방식은 짧은 연습으로 다룰 만하다(5.4절). [추론: 약]
- **전략 명시 교수**: 이 대화의 근사어·우회 설명·외부 자원 사용은 모두 성공적으로 기능했다. 이를 실제 사례로 보여 주며 전략을 명시적으로 가르칠 수 있다(Dörnyei & Scott, 1997). [추론: 중]

## 10. 한계

- **단일 코더**: 수동 코드는 분석자 1인의 해석이다. 약 20%를 2차 코더가 독립 코딩해 Cohen's κ를 보고하는 것이 표준이다.
- **음성·영상 없음**: 휴지, 겹침, 억양, 시선, 제스처를 분석할 수 없다. 특히 사진·검색 장면은 해석이 제한된다.
- **사례 1건**: 대화 1편, 화자 2명이므로 일반화할 수 없다. 이 결과는 기술적(descriptive) 관찰이다.
- **VOCD 변동성**: D값은 실행마다 약간 달라진다(3절).

## 11. 재현 방법

```bash
# 1) CLAN 빌드 (Unix 소스)
curl -L -o unix-clan.zip https://dali.talkbank.org/clan/unix-clan.zip && unzip unix-clan.zip
cd unix-clan/src
#   makefile: "for Ubuntu" CFLAGS 줄 주석 해제, LIB = -lncurses 로 변경, ../unix/obj/*.o 와 ../unix/bin/* 의 macOS 바이너리 삭제
make check freq mlu mlt kwal chip maxwd combo vocd

# 2) 분석 실행 (이 폴더에서)
CLAN_BIN=/path/to/unix-clan/unix/bin ./scripts/run_clan.sh
python3 scripts/discourse_coding.py
```

- CLAN은 표준입력이 터미널이 아니면 파일 대신 파이프 입력을 읽는다. 그래서 스크립트는 `script(1)`로 의사 터미널을 붙여 실행한다.

## 참고문헌

**2018년 이후 문헌**

- Loewen, S., & Sato, M. (2018). Interaction and instructed second language acquisition. *Language Teaching, 51*(3), 285–329. https://doi.org/10.1017/S0261444818000125
- MacWhinney, B., & Fromm, D. (2022). Language sample analysis with TalkBank: An update and review. *Frontiers in Communication, 7*, Article 865498. https://doi.org/10.3389/fcomm.2022.865498
- Michel, M., & Cappellini, M. (2019). Alignment during synchronous video versus written chat L2 interactions: A methodological exploration. *Annual Review of Applied Linguistics, 39*, 189–216. https://doi.org/10.1017/S0267190519000072
- Pietikäinen, K. S. (2018). Misunderstandings and ensuring understanding in private ELF talk. *Applied Linguistics, 39*(2), 188–212. https://doi.org/10.1093/applin/amw005 (온라인 선공개 2016)
- Rydell, M. (2019). Negotiating co-participation: Embodied word searching sequences in paired L2 speaking tests. *Journal of Pragmatics, 149*, 60–77. https://doi.org/10.1016/j.pragma.2019.05.027

**2018년 이전 문헌**: 각 분석 틀의 원전이라 인용했다.

- Dörnyei, Z., & Scott, M. L. (1997). Communication strategies in a second language: Definitions and taxonomies. *Language Learning, 47*(1), 173–210. https://doi.org/10.1111/0023-8333.51997005 — 의사소통 전략 분류의 표준 틀
- Firth, A. (1996). The discursive accomplishment of normality: On 'lingua franca' English and conversation analysis. *Journal of Pragmatics, 26*(2), 237–259. https://doi.org/10.1016/0378-2166(96)00014-8 — "let it pass" 개념의 원전
- Long, M. H. (1983). Native speaker/non-native speaker conversation and the negotiation of comprehensible input. *Applied Linguistics, 4*(2), 126–141. https://doi.org/10.1093/applin/4.2.126 — CR/CC/CMC 범주의 원전
- MacWhinney, B. (2000). *The CHILDES project: Tools for analyzing talk* (3rd ed.). Lawrence Erlbaum Associates. — CHAT/CLAN 매뉴얼이 인용하도록 지정한 판
- Pickering, M. J., & Garrod, S. (2004). Toward a mechanistic psychology of dialogue. *Behavioral and Brain Sciences, 27*(2), 169–190. https://doi.org/10.1017/S0140525X04000056 — 대화 정렬 이론의 원전
- Sacks, H., Schegloff, E. A., & Jefferson, G. (1974). A simplest systematics for the organization of turn-taking for conversation. *Language, 50*(4), 696–735. https://doi.org/10.2307/412243 — 발화권 개념의 원전
- Schegloff, E. A., Jefferson, G., & Sacks, H. (1977). The preference for self-correction in the organization of repair in conversation. *Language, 53*(2), 361–382. https://doi.org/10.2307/413107 — 수정 조직의 원전
- Sokolov, J. L., & MacWhinney, B. (1990). The CHIP framework: Automatic coding and analysis of parent-child conversational interaction. *Behavior Research Methods, Instruments, & Computers, 22*(2), 151–161. https://doi.org/10.3758/BF03203138 — CHIP 명령의 원전
- Varonis, E. M., & Gass, S. (1985). Non-native/non-native conversations: A model for negotiation of meaning. *Applied Linguistics, 6*(1), 71–90. https://doi.org/10.1093/applin/6.1.71 — 비원어민 간 의미 협상 모형의 원전

서지 정보는 2026-10-14에 Crossref API로 대조했다. Pietikäinen (2018)의 권·호·쪽수는 Crossref에 온라인판만 있어 EMCA Wiki 서지 정보로 보완했다. 한국 학술지(KCI) 문헌은 쓰지 않았다.
