"""
A quick check that every sample of the course still works.

    python tests/smoke_test.py

The samples are copied to a temporary folder and run there, so nothing in the
repository is changed. For every web application and RESTful service the test
requests all the addresses that need no parameters and expects an answer without
an error. The web applications of module 07 are tested together with their
RESTful service, which is started on a free port.

The Supabase samples are tested only if SUPABASE_URL and SUPABASE_SECRET_KEY are
set (in the environment or in the file .env) - be aware that they add rows to
the tables of that project.

Run it after changing the samples, or after upgrading the packages in requirements.txt.
"""

import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# executed inside the folder of an application: requests the home address and every other
# GET address without parameters (the addresses are taken from the description of the application)
CHECK_APPLICATION = """
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
paths = ["/"]
for path, operations in app.openapi()["paths"].items():
    if "get" in operations and "{" not in path and path != "/":
        paths.append(path)

failures = []
for path in paths:
    status = client.get(path).status_code
    # 422 only means that the address needs parameters; everything from 400 up is otherwise a failure
    if status >= 400 and status != 422:
        failures.append(f"{path} -> {status}")
if failures:
    raise SystemExit("; ".join(failures))
print(f"{len(paths)} addresses")
"""


def load_dotenv_file() -> None:
    """Reads the file .env of the repository (if there is one) into the environment."""
    env_file = ROOT / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.strip().startswith("#"):
                name, value = line.split("=", 1)
                os.environ.setdefault(name.strip(), value.strip())


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def run(folder: Path, arguments: list[str], env: dict | None = None, typed: str = "") -> tuple[bool, str]:
    """
    Runs Python in the given folder; returns whether it succeeded, and the last line it printed.
    `typed` is what the user would type (one answer per line), for programs that call input().
    """
    result = subprocess.run(
        [sys.executable, *arguments], cwd=folder, env=env, input=typed, capture_output=True, text=True, timeout=300
    )
    output = (result.stdout + result.stderr).strip().splitlines()
    return result.returncode == 0, output[-1] if output else ""


def start_service(folder: Path, port: int) -> subprocess.Popen:
    """Starts the application of the given folder with Uvicorn, and waits until it answers."""
    process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "main:app", "--port", str(port)],
        cwd=folder, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    for _ in range(50):
        time.sleep(0.2)
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/openapi.json", timeout=2)
            return process
        except OSError:
            if process.poll() is not None:
                break
    process.kill()
    raise RuntimeError(f"the service in {folder} did not start")


def main() -> int:
    load_dotenv_file()
    has_supabase = bool(os.environ.get("SUPABASE_URL") and os.environ.get("SUPABASE_SECRET_KEY"))
    results = []  # (name of the sample, "ok" / "FAILED" / "skipped", details)

    with tempfile.TemporaryDirectory() as temporary:
        samples = Path(temporary) / "teaching-samples"
        shutil.copytree(ROOT / "teaching-samples", samples, ignore=shutil.ignore_patterns("__pycache__", "*.db"))

        def record(folder: Path, ok: bool, details: str) -> None:
            results.append((str(folder.relative_to(samples)), "ok" if ok else "FAILED", details))

        # --- the programs of the introduction to Python, with the answers they ask for
        intro = samples / "02-python-intro"
        for script, typed in [
            ("01_hello.py", ""),
            ("02_variables.py", ""),
            ("03_input.py", "Ana\n3\n1250\n"),
            ("04_if.py", "77\n"),
            ("05_loops.py", ""),
            ("06_lists.py", ""),
            ("07_dictionaries.py", "pen\n"),
            ("08_functions.py", ""),
            ("09_modules.py", ""),
            ("10_errors.py", "abc\n"),
            ("11_shopping_list.py", "a\nnotebook\n1250\na\npen\n12,5\n120\ns\nx\nq\n"),
        ]:
            ok, details = run(intro, [script], typed=typed)
            results.append((f"02-python-intro/{script}", "ok" if ok else "FAILED", "" if ok else details))

        # --- programs that are not web applications
        for script in [
            "05-python-db-sqlite/database/create_databases.py",
            "05-python-db-sqlite/01-sqlite-with-sql/main.py",
            "05-python-db-sqlite/02-sqlite-with-model/main.py",
        ]:
            path = samples / script
            ok, details = run(path.parent, [path.name])
            results.append((script, "ok" if ok else "FAILED", "" if ok else details))

        for script in [
            "05-python-db-supabase/01-supabase-with-request/main.py",
            "05-python-db-supabase/02-supabase-with-model/main.py",
        ]:
            if has_supabase:
                path = samples / script
                ok, details = run(path.parent, [path.name])
                results.append((script, "ok" if ok else "FAILED", "" if ok else details))
            else:
                results.append((script, "skipped", "Supabase is not configured"))

        # --- web applications and RESTful services: every folder with a main.py that creates a FastAPI application
        applications = sorted(
            p.parent for p in samples.rglob("main.py") if "FastAPI(" in p.read_text(encoding="utf-8")
        )
        for folder in applications:
            if "supabase" in str(folder.relative_to(samples)) and folder.name != "01-rest-service-new" and not has_supabase:
                results.append((str(folder.relative_to(samples)), "skipped", "Supabase is not configured"))
                continue

            if folder.name == "web-app":
                # a web application of the complete system needs its RESTful service
                port = free_port()
                service = start_service(folder.parent / "rest-service", port)
                try:
                    env = dict(os.environ, REST_SERVICE_URL=f"http://127.0.0.1:{port}/api")
                    ok, details = run(folder, ["-c", CHECK_APPLICATION], env)
                finally:
                    service.terminate()
                    service.wait()
            else:
                ok, details = run(folder, ["-c", CHECK_APPLICATION])
            record(folder, ok, details)

    width = max(len(name) for name, _, _ in results)
    for name, outcome, details in results:
        print(f"{name:<{width}}  {outcome:<8} {details}")
    failed = [name for name, outcome, _ in results if outcome == "FAILED"]
    print(f"\n{len(results)} samples, {len(failed)} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
