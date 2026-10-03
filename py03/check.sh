#!/usr/bin/env bash
# ============================================================
# py03 - Data Quest: Mastering Python Collections
# Automated checker: structure, linters, output diff
# ============================================================
#
# Usage:
#   chmod +x check.sh
#   ./check.sh              # run all checks
#   ./check.sh ex1          # run only exercise 1 checks
#   ./check.sh lint         # run only linters
#   ./check.sh structure    # run only structure check
#
# ============================================================

set -u

# ---------- Colors (auto-disabled when not a TTY) ----------
if [ -t 1 ]; then
    RED=$'\033[31m'
    GRN=$'\033[32m'
    YLW=$'\033[33m'
    BLU=$'\033[34m'
    BLD=$'\033[1m'
    RST=$'\033[0m'
else
    RED=''; GRN=''; YLW=''; BLU=''; BLD=''; RST=''
fi

PASS="${GRN}PASS${RST}"
FAIL="${RED}FAIL${RST}"
WARN="${YLW}WARN${RST}"

# ---------- Counters ----------
TOTAL=0
PASSED=0
FAILED=0

# ---------- Locate repo root ----------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$SCRIPT_DIR"

# ---------- Helpers ----------
header() {
    echo
    echo "${BLU}${BLD}========================================${RST}"
    echo "${BLU}${BLD}  $1${RST}"
    echo "${BLU}${BLD}========================================${RST}"
}

sub() {
    echo
    echo "${BLD}--- $1 ---${RST}"
}

check() {
    # $1 = label, $2 = status (0=pass)
    TOTAL=$((TOTAL + 1))
    if [ "$2" -eq 0 ]; then
        PASSED=$((PASSED + 1))
        echo "  [$PASS] $1"
    else
        FAILED=$((FAILED + 1))
        echo "  [$FAIL] $1"
    fi
}

# Diff two strings; prints unified diff if they differ
diff_out() {
    # $1 = expected (string), $2 = actual (string)
    diff <(printf '%s\n' "$1") <(printf '%s\n' "$2")
}

# ---------- Preflight ----------
preflight() {
    header "Preflight"

    # python3 present?
    if command -v python3 >/dev/null 2>&1; then
        check "python3 available ($(python3 --version 2>&1))" 0
    else
        check "python3 available" 1
        echo "${RED}Cannot continue without python3.${RST}"
        exit 1
    fi

    # flake8 present?
    if command -v flake8 >/dev/null 2>&1; then
        check "flake8 available" 0
    else
        check "flake8 available (install: pip install flake8)" 1
    fi

    # mypy present?
    if command -v mypy >/dev/null 2>&1; then
        check "mypy available" 0
    else
        check "mypy available (install: pip install mypy)" 1
    fi

    # Root dir has ex0..ex6?
    local missing=0
    for d in ex0 ex1 ex2 ex3 ex4 ex5 ex6; do
        [ -d "$ROOT/$d" ] || missing=1
    done
    check "All exercise directories present (ex0..ex6)" $missing
}

# ---------- Structure ----------
check_structure() {
    header "Structure"

    local files=(
        "ex0/ft_command_quest.py"
        "ex1/ft_score_analytics.py"
        "ex2/ft_coordinate_system.py"
        "ex3/ft_achievement_tracker.py"
        "ex4/ft_inventory_system.py"
        "ex5/ft_data_stream.py"
        "ex6/ft_data_alchemist.py"
    )

    for f in "${files[@]}"; do
        if [ -f "$ROOT/$f" ]; then
            check "File exists: $f" 0
        else
            check "File exists: $f" 1
        fi
    done
}

# ---------- Linters ----------
check_lint() {
    header "Linters (flake8 + mypy --strict)"

    if command -v flake8 >/dev/null 2>&1; then
        sub "flake8 ."
        if flake8 "$ROOT"; then
            check "flake8 clean" 0
        else
            check "flake8 reported issues" 1
        fi
    fi

    if command -v mypy >/dev/null 2>&1; then
        sub "mypy . --strict"
        if mypy "$ROOT" --strict; then
            check "mypy --strict clean" 0
        else
            check "mypy --strict reported issues" 1
        fi
    fi

    check_no_ansi
}

# ---------- No ANSI escapes in output files ----------
check_no_ansi() {
    sub "No ANSI escape codes in source files"
    local ansi_found=0
    for f in \
        "ex0/ft_command_quest.py" \
        "ex1/ft_score_analytics.py" \
        "ex2/ft_coordinate_system.py" \
        "ex3/ft_achievement_tracker.py" \
        "ex4/ft_inventory_system.py" \
        "ex6/ft_data_alchemist.py"; do
        if grep -qP '\x1b\[' "$ROOT/$f" 2>/dev/null; then
            echo "  ${RED}ANSI codes found in:${RST} $f"
            ansi_found=1
        fi
    done
    check "No ANSI codes in deterministic outputs" $ansi_found
}

# ============================================================
# Ex0 - ft_command_quest.py
# ============================================================
check_ex0() {
    header "ex0 - ft_command_quest.py"
    local py="$ROOT/ex0/ft_command_quest.py"
    [ -f "$py" ] || { check "ex0 file exists" 1; return; }

    sub "Run with no args"
    local got
    got="$(cd "$ROOT/ex0" && python3 ft_command_quest.py)"
    local exp="=== Command Quest ===
Program name: ft_command_quest.py
No arguments provided!
Total arguments: 1"
    if [ "$got" = "$exp" ]; then
        check "ex0 no-args output" 0
    else
        check "ex0 no-args output" 1
        diff_out "$exp" "$got"
    fi

    sub "Run with 'hello world 42'"
    got="$(cd "$ROOT/ex0" && python3 ft_command_quest.py hello world 42)"
    exp="=== Command Quest ===
Program name: ft_command_quest.py
Arguments received: 3
Argument 1: hello
Argument 2: world
Argument 3: 42
Total arguments: 4"
    if [ "$got" = "$exp" ]; then
        check "ex0 three-args output" 0
    else
        check "ex0 three-args output" 1
        diff_out "$exp" "$got"
    fi

    sub "Run with one quoted arg 'Data Quest'"
    got="$(cd "$ROOT/ex0" && python3 ft_command_quest.py "Data Quest")"
    exp="=== Command Quest ===
Program name: ft_command_quest.py
Arguments received: 1
Argument 1: Data Quest
Total arguments: 2"
    if [ "$got" = "$exp" ]; then
        check "ex0 quoted-arg output" 0
    else
        check "ex0 quoted-arg output" 1
        diff_out "$exp" "$got"
    fi
}

# ============================================================
# Ex1 - ft_score_analytics.py
# ============================================================
check_ex1() {
    header "ex1 - ft_score_analytics.py"
    local py="$ROOT/ex1/ft_score_analytics.py"
    [ -f "$py" ] || { check "ex1 file exists" 1; return; }

    sub "Valid scores"
    local got
    got="$(cd "$ROOT/ex1" && python3 ft_score_analytics.py 1500 2300 1800 2100 1950)"
    local exp="=== Player Score Analytics ===
Scores processed: [1500, 2300, 1800, 2100, 1950]
Total players: 5
Total score: 9650
Average score: 1930.0
High score: 2300
Low score: 1500
Score range: 800"
    if [ "$got" = "$exp" ]; then
        check "ex1 valid scores" 0
    else
        check "ex1 valid scores" 1
        diff_out "$exp" "$got"
    fi

    sub "No args"
    got="$(cd "$ROOT/ex1" && python3 ft_score_analytics.py)"
    exp="=== Player Score Analytics ===
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ..."
    if [ "$got" = "$exp" ]; then
        check "ex1 no args" 0
    else
        check "ex1 no args" 1
        diff_out "$exp" "$got"
    fi

    sub "All invalid args"
    got="$(cd "$ROOT/ex1" && python3 ft_score_analytics.py ab ac)"
    exp="=== Player Score Analytics ===
Invalid parameter: 'ab'
Invalid parameter: 'ac'
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ..."
    if [ "$got" = "$exp" ]; then
        check "ex1 all invalid" 0
    else
        check "ex1 all invalid" 1
        diff_out "$exp" "$got"
    fi

    sub "Mixed valid + invalid"
    got="$(cd "$ROOT/ex1" && python3 ft_score_analytics.py 100 ab 200)"
    exp="=== Player Score Analytics ===
Invalid parameter: 'ab'
Scores processed: [100, 200]
Total players: 2
Total score: 300
Average score: 150.0
High score: 200
Low score: 100
Score range: 100"
    if [ "$got" = "$exp" ]; then
        check "ex1 mixed valid/invalid" 0
    else
        check "ex1 mixed valid/invalid" 1
        diff_out "$exp" "$got"
    fi
}

# ============================================================
# Ex2 - ft_coordinate_system.py (interactive via piped stdin)
# ============================================================
# NOTE: when stdin is piped, the terminal does NOT echo the input
# back to stdout. So the expected string below reflects what the
# program itself prints (prompt + result on the same line).
# ============================================================
check_ex2() {
    header "ex2 - ft_coordinate_system.py"
    local py="$ROOT/ex2/ft_coordinate_system.py"
    [ -f "$py" ] || { check "ex2 file exists" 1; return; }

    sub "Full subject sample (with error recovery, piped)"
    local got
    got="$(cd "$ROOT/ex2" && printf 'hello world\n1.0 , 2.5, 3.0\n4,abc,5\n4,5,6\n' \
        | python3 ft_coordinate_system.py)"
    local exp="=== Game Coordinate System ===
Get a first set of coordinates
Enter new coordinates as floats in format 'x,y,z': Invalid syntax
Enter new coordinates as floats in format 'x,y,z': Got a first tuple: (1.0, 2.5, 3.0)
It includes: X=1.0, Y=2.5, Z=3.0
Distance to center: 4.0311
Get a second set of coordinates
Enter new coordinates as floats in format 'x,y,z': Error on parameter 'abc': could not convert string to float: 'abc'
Enter new coordinates as floats in format 'x,y,z': Distance between the 2 sets of coordinates: 4.9244"
    if [ "$got" = "$exp" ]; then
        check "ex2 subject sample (piped)" 0
    else
        check "ex2 subject sample (piped)" 1
        diff_out "$exp" "$got"
    fi
}

# ============================================================
# Ex3 - ft_achievement_tracker.py (randomized; check shape)
# ============================================================
check_ex3() {
    header "ex3 - ft_achievement_tracker.py"
    local py="$ROOT/ex3/ft_achievement_tracker.py"
    [ -f "$py" ] || { check "ex3 file exists" 1; return; }

    sub "Output shape (randomized, so verify by pattern)"
    local got
    got="$(cd "$ROOT/ex3" && python3 ft_achievement_tracker.py)"

    local required=(
        "=== Achievement Tracker System ==="
        "Player Alice:"
        "Player Bob:"
        "Player Charlie:"
        "Player Dylan:"
        "All distinct achievements:"
        "Common achievements:"
        "Only Alice has:"
        "Only Bob has:"
        "Only Charlie has:"
        "Only Dylan has:"
        "Alice is missing:"
        "Bob is missing:"
        "Charlie is missing:"
        "Dylan is missing:"
    )
    local all_ok=0
    for pattern in "${required[@]}"; do
        if ! grep -qF "$pattern" <<< "$got"; then
            echo "  ${RED}Missing line pattern:${RST} $pattern"
            all_ok=1
        fi
    done
    check "ex3 required labels present" $all_ok

    # Ensure no 'Common to all players' (old wrong label)
    if grep -qF "Common to all players" <<< "$got"; then
        check "ex3 'Common to all players' replaced with 'Common achievements:'" 1
    else
        check "ex3 no legacy 'Common to all players' label" 0
    fi
}

# ============================================================
# Ex4 - ft_inventory_system.py
# ============================================================
check_ex4() {
    header "ex4 - ft_inventory_system.py"
    local py="$ROOT/ex4/ft_inventory_system.py"
    [ -f "$py" ] || { check "ex4 file exists" 1; return; }

    sub "Subject sample"
    local got
    got="$(cd "$ROOT/ex4" && python3 ft_inventory_system.py \
        sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value)"
    local exp="=== Inventory System Analysis ===
Redundant item 'sword' - discarding
Error - invalid parameter 'hello'
Quantity error for 'key': invalid literal for int() with base 10: 'value'
Got inventory: {'sword': 1, 'potion': 5, 'shield': 2, 'armor': 3, 'helmet': 1}
Item list: ['sword', 'potion', 'shield', 'armor', 'helmet']
Total quantity of the 5 items: 12
Item sword represents 8.3%
Item potion represents 41.7%
Item shield represents 16.7%
Item armor represents 25.0%
Item helmet represents 8.3%
Item most abundant: potion with quantity 5
Item least abundant: sword with quantity 1
Updated inventory: {'sword': 1, 'potion': 5, 'shield': 2, 'armor': 3, 'helmet': 1, 'magic_item': 1}"
    if [ "$got" = "$exp" ]; then
        check "ex4 subject sample" 0
    else
        check "ex4 subject sample" 1
        diff_out "$exp" "$got"
    fi

    sub "Empty inventory"
    got="$(cd "$ROOT/ex4" && python3 ft_inventory_system.py)"
    exp="=== Inventory System Analysis ===
Got inventory: {}
At the beginning of the game, your inventory is usually empty ;)"
    if [ "$got" = "$exp" ]; then
        check "ex4 empty inventory" 0
    else
        check "ex4 empty inventory" 1
        diff_out "$exp" "$got"
    fi
}

# ============================================================
# Ex5 - ft_data_stream.py (randomized; check shape)
# ============================================================
check_ex5() {
    header "ex5 - ft_data_stream.py"
    local py="$ROOT/ex5/ft_data_stream.py"
    [ -f "$py" ] || { check "ex5 file exists" 1; return; }

    sub "Output shape (randomized)"
    local got
    got="$(cd "$ROOT/ex5" && python3 ft_data_stream.py)"

    # 1000 events
    local event_count
    event_count="$(grep -c '^Event [0-9]\+: Player ' <<< "$got")"
    if [ "$event_count" -eq 1000 ]; then
        check "ex5 has 1000 events" 0
    else
        check "ex5 has 1000 events (found $event_count)" 1
    fi

    # Event 0 and Event 999 present
    grep -q '^Event 0: Player ' <<< "$got" \
        && check "ex5 includes Event 0" 0 \
        || check "ex5 includes Event 0" 1
    grep -q '^Event 999: Player ' <<< "$got" \
        && check "ex5 includes Event 999" 0 \
        || check "ex5 includes Event 999" 1

    # Built list of 10 events
    grep -q '^Built list of 10 events: \[' <<< "$got" \
        && check "ex5 'Built list of 10 events'" 0 \
        || check "ex5 'Built list of 10 events'" 1

    # 10 Got event / Remains pairs
    local got_count remains_count
    got_count="$(grep -c '^Got event from list: ' <<< "$got")"
    remains_count="$(grep -c '^Remains in list: ' <<< "$got")"
    [ "$got_count" -eq 10 ] \
        && check "ex5 exactly 10 'Got event' lines" 0 \
        || check "ex5 exactly 10 'Got event' lines (found $got_count)" 1
    [ "$remains_count" -eq 10 ] \
        && check "ex5 exactly 10 'Remains in list' lines" 0 \
        || check "ex5 exactly 10 'Remains in list' lines (found $remains_count)" 1

    # Final list empty
    tail -n 1 <<< "$got" | grep -q '^Remains in list: \[\]$' \
        && check "ex5 final 'Remains in list: []'" 0 \
        || check "ex5 final 'Remains in list: []'" 1
}

# ============================================================
# Ex6 - ft_data_alchemist.py (randomized; check shape)
# ============================================================
check_ex6() {
    header "ex6 - ft_data_alchemist.py"
    local py="$ROOT/ex6/ft_data_alchemist.py"
    [ -f "$py" ] || { check "ex6 file exists" 1; return; }

    sub "Output shape (randomized)"
    local got
    got="$(cd "$ROOT/ex6" && python3 ft_data_alchemist.py)"

    local required=(
        "=== Game Data Alchemist ==="
        "Initial list of players:"
        "New list with all names capitalized:"
        "New list of capitalized names only:"
        "Score dict:"
        "Score average is "
        "High scores:"
    )
    local all_ok=0
    for pattern in "${required[@]}"; do
        if ! grep -qF "$pattern" <<< "$got"; then
            echo "  ${RED}Missing line pattern:${RST} $pattern"
            all_ok=1
        fi
    done
    check "ex6 required labels present" $all_ok

    # Check expected frozen parts: capitalized-only filter
    if grep -qF "New list of capitalized names only: ['Alice', 'Charlie', 'Emma', 'Gregory', 'Liam']" <<< "$got"; then
        check "ex6 capitalized-only filter correct" 0
    else
        check "ex6 capitalized-only filter correct" 1
    fi

    # Average is a float (round to 2 decimals, but Python may trim trailing zeros)
    if grep -Eq '^Score average is [0-9]+\.[0-9]+$' <<< "$got"; then
        check "ex6 average is a rounded float" 0
    else
        check "ex6 average is a rounded float" 1
    fi
}

# ---------- Run selected sections ----------
run_all() {
    preflight
    check_structure
    check_lint
    check_ex0
    check_ex1
    check_ex2
    check_ex3
    check_ex4
    check_ex5
    check_ex6

    header "Summary"
    echo "  Total : $TOTAL"
    echo "  ${GRN}Passed: $PASSED${RST}"
    echo "  ${RED}Failed: $FAILED${RST}"

    if [ "$FAILED" -eq 0 ]; then
        echo
        echo "${GRN}${BLD}All checks passed! Ready to submit. 🚀${RST}"
        exit 0
    else
        echo
        echo "${RED}${BLD}Some checks failed — see above.${RST}"
        exit 1
    fi
}

case "${1:-all}" in
    all)        run_all ;;
    lint)       preflight; check_lint ;;
    structure)  check_structure ;;
    ex0)        check_ex0 ;;
    ex1)        check_ex1 ;;
    ex2)        check_ex2 ;;
    ex3)        check_ex3 ;;
    ex4)        check_ex4 ;;
    ex5)        check_ex5 ;;
    ex6)        check_ex6 ;;
    *)
        echo "Usage: $0 {all|lint|structure|ex0|ex1|ex2|ex3|ex4|ex5|ex6}"
        exit 2
        ;;
esac