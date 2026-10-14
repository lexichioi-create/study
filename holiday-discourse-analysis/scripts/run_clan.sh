#!/usr/bin/env bash
# CLAN 분석 일괄 실행 스크립트
# 사용법: CLAN_BIN=/path/to/unix-clan/unix/bin ./scripts/run_clan.sh
# Unix CLAN 소스: https://dali.talkbank.org/clan/unix-clan.zip (makefile에서 Ubuntu용 CFLAGS 주석 해제 후 make)
# CLAN은 stdin이 터미널이 아니면 파일 대신 파이프 입력을 읽으므로, 비대화형 셸에서는 script(1)로 의사 터미널을 붙인다.
set -euo pipefail
cd "$(dirname "$0")/.."
: "${CLAN_BIN:?CLAN_BIN must point to the CLAN bin directory}"
F=data/holiday.cha
OUT=clan-output
mkdir -p "$OUT"

run() { # run <output-name> <command...>
  local name=$1; shift
  script -qec "$*" /dev/null 2>&1 | tr -d '\r' > "$OUT/$name.txt"
}

run 01_check          "$CLAN_BIN/check $F"
run 02_freq_MAR       "$CLAN_BIN/freq +t*MAR +o $F"
run 03_freq_LEX       "$CLAN_BIN/freq +t*LEX +o $F"
run 04_mlu_words      "$CLAN_BIN/mlu -t%mor $F"
run 05_mlt            "$CLAN_BIN/mlt $F"
run 06_maxwd          "$CLAN_BIN/maxwd -t%mor +g2 +c5 $F"
run 07_vocd           "$CLAN_BIN/vocd -t%mor $F"
# FLUCALC는 말더듬(SLD) 코딩과 단일 언어 지정이 전제라 이 전사본(@Languages: eng, spa)에서는 실행되지 않아 제외했다.
# 비유창성은 아래 KWAL(채움말·반복·수정·미완결 발화)로 대신 집계한다.
run 10_kwal_retrace   "$CLAN_BIN/kwal +s\"[//]\" +s\"[/]\" $F"
run 11_kwal_incomplete "$CLAN_BIN/kwal +s\"+...\" +s\"+//.\" $F"
run 12_kwal_fillers   "$CLAN_BIN/kwal +s\"&-*\" $F"
run 13_kwal_codeswitch "$CLAN_BIN/kwal +s\"*@s:spa\" $F"
run 14_kwal_questions "$CLAN_BIN/kwal +s\"?\" $F"
# CHIP은 원래 성인(+b)-아동(+c) 상호작용용이다. 여기서는 LEX를 ADU, MAR를 CHI 자리에 놓았을 뿐 연령·역할 의미는 없다.
run 15_chip_summary   "$CLAN_BIN/chip +bLEX +cMAR -t%mor +d1 $F"
run 16_chip_coded     "$CLAN_BIN/chip +bLEX +cMAR -t%mor -f $F"
run 17_combo_ofcourse "$CLAN_BIN/combo +s\"of^course\" $F"
run 18_combo_idontknow "$CLAN_BIN/combo +s\"I^don't^know\" $F"
# 담화 코딩 파일(coding/holiday_coded.cha, scripts/discourse_coding.py가 생성)의 %cod 코드 집계
C=coding/holiday_coded.cha
run 19_check_coded      "$CLAN_BIN/check $C"
run 20_freq_cod_LEX     "$CLAN_BIN/freq +t*LEX +t%cod -t* +o $C"
run 21_freq_cod_MAR     "$CLAN_BIN/freq +t*MAR +t%cod -t* +o $C"
# 에피소드(@G)별 코드 빈도: +n은 다음 @G까지를 한 에피소드로 본다
run 22_gemfreq_cod      "$CLAN_BIN/gemfreq +n +sE0 +sE1 +sE2 +sE3 +sE4 +sE5 +sE6 +sE7 +sE8 +t%cod -t* $C"
echo "done: $(ls "$OUT" | wc -l) files in $OUT/"
