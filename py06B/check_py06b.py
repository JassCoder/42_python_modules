#!/usr/bin/env python3
"""PY06B Code Nexus v1.0 evaluation readiness checker.

Run from py06B:
    python3 check_py06b.py

This is a development tool, NOT one of the subject's turn-in files.
It uses Python standard-library modules for test verification.
"""
from __future__ import annotations

import ast
import contextlib
import csv
import importlib
import io
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
passed = 0
failed = 0
warnings = 0


def check(label: str, test, *, advisory: bool = False) -> None:
    global passed, failed, warnings
    try:
        test()
    except Exception as exc:
        if advisory:
            warnings += 1
            print(f"[WARN] {label}: {type(exc).__name__}: {exc}")
        else:
            failed += 1
            print(f"[FAIL] {label}: {type(exc).__name__}: {exc}")
    else:
        passed += 1
        print(f"[PASS] {label}")


def require(condition: bool, explanation: str) -> None:
    if not condition:
        raise AssertionError(explanation)


def capture(call, *args):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        call(*args)
    return output.getvalue()


def expect_error(call, exc_type: type[Exception], *args) -> None:
    try:
        call(*args)
    except exc_type:
        return
    except Exception as exc:
        raise AssertionError(
            f"Expected {exc_type.__name__}, got {type(exc).__name__}"
        ) from exc
    raise AssertionError(f"Expected {exc_type.__name__}, no error raised")


def import_attr(module: str, attr: str):
    return getattr(importlib.import_module(module), attr)


def has_files() -> None:
    expected = [
        "data_processor.py", "data_stream.py", "data_pipeline.py",
        "ex3/__init__.py", "ex3/creature.py", "ex3/capability.py",
        "ex3/factory.py", "battle.py", "capacitor.py",
        "ex4/__init__.py", "ex4/strategy.py", "tournament.py",
    ]
    missing = [p for p in expected if not (ROOT / p).is_file()]
    require(not missing, f"Missing files: {', '.join(missing)}")


def check_commands() -> None:
    import shutil
    files = [
        "data_processor.py", "data_stream.py", "data_pipeline.py",
        "battle.py", "capacitor.py", "tournament.py",
        *[str(p.relative_to(ROOT)) for folder in ("ex3", "ex4")
          for p in sorted((ROOT / folder).glob("*.py"))],
    ]
    for command in (
        [sys.executable, "-m", "py_compile", *files],
        ["flake8", *files],
        ["mypy", *files],
    ):
        if not shutil.which(command[0]):
            raise AssertionError(f"Missing command: {command[0]}")
        result = subprocess.run(command, cwd=ROOT, text=True,
                                capture_output=True, timeout=60)
        require(result.returncode == 0,
                f"{' '.join(command[:2])}:\n"
                f"{(result.stdout + result.stderr).strip()}")


def ex0() -> None:
    from data_processor import NumericProcessor, TextProcessor, LogProcessor
    n, t, log = NumericProcessor(), TextProcessor(), LogProcessor()
    require(n.validate([2, 3.5, -1]), "numeric mixed list rejected")
    require(not n.validate("bad"), "numeric accepted string")
    require(t.validate(["hello", "world"]), "text rejected string list")
    require(not t.validate(42), "text accepted integer")
    require(log.validate({"log_level": "INFO", "log_message": "hi"}),
            "log rejected dict")
    require(not log.validate({"level": 1}), "log accepted invalid dict")
    expect_error(n.ingest, ValueError, "bad")
    expect_error(t.ingest, ValueError, 42)
    expect_error(log.ingest, ValueError, {"level": 1})
    n.ingest([2, 3.5, -1])
    require([n.output(), n.output(), n.output()] ==
            [(0, "2"), (1, "3.5"), (2, "-1")], "numeric FIFO/ranks broken")
    expect_error(n.output, IndexError)
    n.ingest(7)
    require(n.output() == (3, "7"), "processing rank reset after output")
    t.ingest(["hello", "world"])
    require([t.output(), t.output()] ==
            [(0, "hello"), (1, "world")], "text FIFO broken")
    log.ingest([{"log_level": "NOTICE", "log_message": "connected"}])
    require(isinstance(log.output()[1], str), "log output is not a string")


def ex0_log_format() -> None:
    from data_processor import LogProcessor
    p = LogProcessor()
    p.ingest({"log_level": "NOTICE", "log_message": "connected"})
    require(p.output()[1] == "NOTICE: connected",
            "PDF example expects 'NOTICE: connected' for log entries")


def ex1() -> None:
    from data_processor import NumericProcessor, TextProcessor, LogProcessor
    from data_stream import DataStream
    stream = DataStream()
    n, t, log = NumericProcessor(), TextProcessor(), LogProcessor()
    for item in (n, t, log):
        stream.register_processor(item)
    output = capture(stream.process_stream, [
        42, [3.14, -1], "hello", ["a", "b"],
        {"log_level": "INFO", "log_message": "ok"}, None,
    ])
    require("None" in output, "missing unhandled-input error")
    require((n.total_processed, t.total_processed, log.total_processed)
            == (3, 3, 1), "wrong routing counts")
    require(n.output() == (0, "42"), "numeric stream ordering failed")
    require(n.remaining == 2, "remaining statistic not updated")
    capture(stream.print_processors_stats)


def ex2() -> None:
    from data_processor import NumericProcessor, TextProcessor
    from data_pipeline import DataStream, CsvPlugin, JsonPlugin
    stream = DataStream()
    n, t = NumericProcessor(), TextProcessor()
    stream.register_processor(n)
    stream.register_processor(t)
    stream.process_stream([1, 2, 3, "hello", "world"])
    csv_output = capture(stream.output_pipeline, 2, CsvPlugin())
    require("1,2" in csv_output and "hello,world" in csv_output,
            "CSV export didn't receive expected values")
    require((n.remaining, t.remaining) == (1, 0),
            "output_pipeline didn't consume correct number per processor")
    json_output = capture(stream.output_pipeline, 3, JsonPlugin())
    require('"item_2": "3"' in json_output,
            "JSON export didn't preserve processing rank")
    require((n.remaining, t.remaining) == (0, 0),
            "pipeline failed on short or empty processor")
    expect_error(stream.output_pipeline, ValueError, -1, CsvPlugin())


def ex2_csv_escaping() -> None:
    from data_pipeline import CsvPlugin
    result = capture(CsvPlugin().process_output, [
        (0, "hello,world"), (1, 'say "hi"'), (2, "line\nbreak"),
    ])
    payload = result.split("CSV Output:", 1)[-1].strip("\n")
    parsed = list(csv.reader(io.StringIO(payload, newline="")))
    require(parsed == [["hello,world", 'say "hi"', "line\nbreak"]],
            f"invalid CSV row: {parsed!r}")


def ex2_json_escaping() -> None:
    from data_pipeline import JsonPlugin
    special = 'say "hello" \\ newline\n tab\t'
    result = capture(JsonPlugin().process_output, [(5, special)])
    payload = result.split("JSON Output:", 1)[-1].strip()
    data = json.loads(payload)
    require(data == {"item_5": special},
            f"JSON round-trip mismatch: {data!r}")


def ex3() -> None:
    from ex3 import FlameFactory, TransformCreatureFactory
    from ex3.creature import Creature
    from ex3.capability import TransformCapability
    flame, transform = FlameFactory(), TransformCreatureFactory()
    f, fe = flame.create_base(), flame.create_evolved()
    t, te = transform.create_base(), transform.create_evolved()
    require([f.name, fe.name, t.name, te.name] ==
            ["Flameling", "Pyrodon", "Shiftling", "Morphagon"],
            "factory family/order mismatch")
    require(all(isinstance(x, Creature) for x in (f, fe, t, te)),
            "factory returned non-Creature")
    require(not isinstance(f, TransformCapability),
            "Flameling should not transform")
    require(not issubclass(TransformCapability, Creature),
            "capability must not inherit from Creature")
    for c in (t, te):
        require(isinstance(c, TransformCapability),
                "transforming entity lacks capability")
        normal = c.attack()
        c.transform()
        require(c.attack() != normal, "attack unchanged after transform")
        c.revert()
        require(c.attack() == normal, "revert didn't restore normal attack")
    import ex3
    require(set(ex3.__all__) == {
        "FlameFactory", "TransformCreatureFactory"},
        "ex3 __all__ must expose only factories")


def ex4() -> None:
    from ex3.creature import Flameling, Shiftling
    from ex4 import NormalStrategy, AggressiveStrategy, InvalidStrategyError
    normal, aggressive = NormalStrategy(), AggressiveStrategy()
    require(normal.is_valid(Flameling()), "normal rejected Flameling")
    require(normal.is_valid(Shiftling()), "normal rejected Shiftling")
    require(not aggressive.is_valid(Flameling()),
            "aggressive accepted non-transforming creature")
    require(aggressive.is_valid(Shiftling()), "aggressive rejected Shiftling")
    output = capture(aggressive.act, Shiftling())
    require("boosted strike" in output and "returns to normal" in output,
            "aggressive transform/attack/revert sequence incorrect")
    expect_error(aggressive.act, InvalidStrategyError, Flameling())


def tournament_pairs() -> None:
    from tournament import tournament
    from ex3 import FlameFactory, TransformCreatureFactory
    from ex4 import NormalStrategy, AggressiveStrategy
    three = [
        (FlameFactory(), NormalStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
        (FlameFactory(), NormalStrategy()),
    ]
    output = capture(tournament, three)
    require(output.count("* Battle *") == 3,
            "3 opponents must produce exactly 3 battles")
    bad = [
        (TransformCreatureFactory(), AggressiveStrategy()),
        (FlameFactory(), AggressiveStrategy()),
        (FlameFactory(), NormalStrategy()),
    ]
    output = capture(tournament, bad)
    require("aborting tournament" in output.lower(),
            "invalid strategy did not abort tournament")
    require(output.count("* Battle *") == 1,
            "tournament continued after invalid strategy")


def demo(name: str, expected: str) -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / name)],
        cwd=ROOT, capture_output=True, text=True, timeout=10
    )
    require(result.returncode == 0,
            f"script exited {result.returncode}: {result.stderr.strip()}")
    require(expected in result.stdout,
            f"standalone script lacks expected demonstration: {expected!r}")


def import_policy() -> None:
    project = [
        "data_processor.py", "data_stream.py", "data_pipeline.py",
        "battle.py", "capacitor.py", "tournament.py",
        *[str(p.relative_to(ROOT)) for folder in ("ex3", "ex4")
          for p in (ROOT / folder).glob("*.py")],
    ]
    disallowed = []
    for filename in project:
        tree = ast.parse((ROOT / filename).read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split(".")[0] not in {"abc", "typing",
                            "ex3", "ex4", "data_processor", "data_stream",
                            "data_pipeline"}:
                        disallowed.append(f"{filename}: import {alias.name}")
            if isinstance(node, ast.ImportFrom) and node.level == 0:
                if (node.module or "").split(".")[0] not in {
                    "abc", "typing", "ex3", "ex4", "data_processor",
                    "data_stream", "data_pipeline"
                }:
                    disallowed.append(
                        f"{filename}: from {node.module} import ...")
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in {"eval", "exec"}:
                    disallowed.append(f"{filename}: forbidden {node.func.id}()")
    require(not disallowed, "; ".join(disallowed))


def main() -> int:
    print("=== PY06B CODE NEXUS EVALUATION CHECK ===")
    print("Required checks:")
    check("Required submission files", has_files)
    check("Compile + flake8 + mypy", check_commands)
    check("Authorized imports and no eval/exec", import_policy)
    check("EX0 validators, ingestion, FIFO and errors", ex0)
    check("EX1 polymorphic routing and stats", ex1)
    check("EX2 export pipeline and consumption", ex2)
    check("EX3 creature hierarchy, factories, transform", ex3)
    check("EX4 strategies and dedicated exception", ex4)
    check("EX4 three-opponent pairing and abort", tournament_pairs)
    print("\nCompliance / presentation checks:")
    check("EX0 log formatting matches subject example",
          ex0_log_format, advisory=True)
    check("EX2 CSV special characters", ex2_csv_escaping, advisory=True)
    check("EX2 JSON special characters", ex2_json_escaping, advisory=True)
    check("EX0 standalone demo", lambda: demo(
        "data_processor.py", "Testing Numeric Processor"), advisory=True)
    check("EX1 standalone demo", lambda: demo(
        "data_stream.py", "DataStream statistics"), advisory=True)
    print(f"\nRESULT: {passed} passed, {failed} failed, {warnings} warnings")
    if failed:
        print("NOT READY: fix FAIL items first.")
        return 1
    if warnings:
        print("CORE CHECKS PASSED; fix WARN items before evaluation.")
        return 0
    print("CHECKER PASSED. Peer review is still recommended.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
