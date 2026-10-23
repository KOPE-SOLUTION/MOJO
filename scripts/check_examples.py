"""Run the documented CPU examples and intentional failures on Mojo 1.2.0."""
from datetime import datetime, timezone
import json
import platform
import sys
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MOJO = shutil.which("mojo")
if not MOJO:
    raise SystemExit("Mojo not found. Activate the course .venv in Ubuntu WSL first.")

def run(args):
    return subprocess.run(args, capture_output=True, text=True, timeout=90, cwd=ROOT)

version_result = run([MOJO, "--version"])
if version_result.returncode:
    raise SystemExit(version_result.stderr)
version = version_result.stdout.strip()
if not version.startswith("Mojo 1.2.0 "):
    raise SystemExit("Expected Mojo 1.2.0, got: " + version)

started_at = datetime.now(timezone.utc).isoformat()
cases = json.loads((ROOT / "scripts/example-cases.json").read_text(encoding="utf-8"))
results = []
with tempfile.TemporaryDirectory(prefix="mojo-course-check-") as tmp:
    for index, case in enumerate(cases):
        source = ROOT / case["path"] if "path" in case else None
        if source is None or source.suffix != ".mojo":
            code = case.get("source")
            if code is None:
                code = source.read_text(encoding="utf-8")
            source = Path(tmp) / ("case_" + str(index) + ".mojo")
            source.write_text(code, encoding="utf-8")
        try:
            result = run([MOJO, str(source)])
            stdout = result.stdout.replace("\r\n", "\n")
            stderr = result.stderr
            if case["exit"] == "failure":
                ok = (result.returncode != 0 and "error:" in stderr.lower()
                      and case["diagnostic"] in stderr)
            else:
                ok = result.returncode == 0 and stdout == case["expected"]
            row = {"name": case["name"], "passed": ok, "returncode": result.returncode,
                   "stdout": stdout, "stderr": stderr}
        except subprocess.TimeoutExpired:
            row = {"name": case["name"], "passed": False, "error": "timeout after 90s"}
        results.append(row)
        print(("PASS " if row["passed"] else "FAIL ") + case["name"], flush=True)

report = {"version": version,
          "started_at_utc": started_at,
          "finished_at_utc": datetime.now(timezone.utc).isoformat(),
          "python": sys.version.split()[0],
          "platform": platform.platform(),
          "cases": results,
          "passed": sum(row["passed"] for row in results), "total": len(results)}
(ROOT / "notes/validation-results.json").write_text(
    json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(str(report["passed"]) + "/" + str(report["total"]) + " expected behaviors confirmed")
raise SystemExit(0 if report["passed"] == report["total"] else 1)
