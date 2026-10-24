"""
A quick check that every sample of the course still works.

    python tests/smoke_test.py

The samples are copied to a temporary folder and run there, so nothing in the
repository is changed. For every web application and RESTful service the test
requests all the addresses that need no parameters and expects an answer without
an error. The web applications of module 07 are tested together with their
RESTful service, which is started on a free port.

The archives of the folder downloads must hold the current files of the samples
(tools/make_zips.py makes them). The solutions of the assignments (the folder
exercises) are checked as well:
the programs run with the answers a user would type, the SQL scripts run on a
course database, and the applications are requested like the samples.

The Supabase samples are tested only if SUPABASE_URL and SUPABASE_SECRET_KEY are
set (in the environment or in the file .env) - be aware that they add rows to
the tables of that project.

Run it after changing the samples, or after upgrading the packages in requirements.txt.
"""

import os
import shutil
import socket
import sqlite3
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


def port_is_free(port: int) -> bool:
    with socket.socket() as s:
        return s.connect_ex(("127.0.0.1", port)) != 0


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
        # next to teaching-samples, as in the repository: some solutions use the databases of module 05
        exercises = Path(temporary) / "exercises"
        shutil.copytree(ROOT / "exercises", exercises, ignore=shutil.ignore_patterns("__pycache__", "*.db"))

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

        # --- the solutions of the assignments: programs, with the answers they ask for
        # (the film catalogue works next to the database VanityFair02, as its README says)
        vanity_fair_02_folder = samples / "05-python-db-sqlite/database/VanityFair02"
        shutil.copy(exercises / "05-03-sqlite-postgresql/film_catalogue.py", vanity_fair_02_folder)
        for script, path, typed in [
            ("02-01-python-intro/exam_results.py", exercises / "02-01-python-intro/exam_results.py",
             "Ana\n93\nMarko\nabc\n47\nIvana\n78\n\n"),
            ("03-02-python-procedural/report.py", exercises / "03-02-python-procedural/report.py", ""),
            ("03-03-python-oop/cinema.py", exercises / "03-03-python-oop/cinema.py", ""),
            ("05-03-sqlite-postgresql/film_catalogue.py", vanity_fair_02_folder / "film_catalogue.py", "l\nq\n"),
        ]:
            ok, details = run(path.parent, [path.name], typed=typed)
            results.append((f"exercises/{script}", "ok" if ok else "FAILED", "" if ok else details))

        # --- SQL scripts: on a new database, or on a course database built above
        vanity_fair_02 = samples / "05-python-db-sqlite/database/VanityFair02/VanityFair02.db"
        for scripts, database in [
            (["05-01-relational-model/create-tables.sql", "05-01-relational-model/insert-data.sql"], ":memory:"),
            (["05-02-sql/screening.sql", "05-02-sql/queries.sql"], vanity_fair_02),
        ]:
            try:
                with sqlite3.connect(database) as connection:
                    for script in scripts:
                        connection.executescript((exercises / script).read_text(encoding="utf-8"))
                ok, details = True, ""
            except sqlite3.Error as error:
                ok, details = False, f"{script}: {error}"
            results.append((f"exercises/{Path(scripts[0]).parent} (SQL)", "ok" if ok else "FAILED", details))

        # --- applications and services
        for main in sorted(exercises.rglob("main.py")):
            if "FastAPI(" in main.read_text(encoding="utf-8"):
                ok, details = run(main.parent, ["-c", CHECK_APPLICATION])
                results.append((f"exercises/{main.parent.relative_to(exercises)}", "ok" if ok else "FAILED", details))

        # the client of the films service calls the address localhost:8001
        client = "exercises/06-02-fastapi-rest/client.py"
        if port_is_free(8001):
            service = start_service(exercises / "06-02-fastapi-rest", 8001)
            try:
                ok, details = run(exercises / "06-02-fastapi-rest", ["client.py"])
            finally:
                service.terminate()
                service.wait()
            results.append((client, "ok" if ok else "FAILED", "" if ok else details))
        else:
            results.append((client, "skipped", "the port 8001 is in use"))

    # --- the downloads: every archive of the folder downloads must hold the current files of its samples
    check = subprocess.run([sys.executable, str(ROOT / "tools" / "make_zips.py"), "--check"], capture_output=True, text=True)
    last_line = check.stdout.strip().splitlines()[-1] if check.stdout.strip() else ""
    results.append(("downloads (the ZIP archives)", "ok" if check.returncode == 0 else "FAILED",
                    "" if check.returncode == 0 else last_line))

    width = max(len(name) for name, _, _ in results)
    for name, outcome, details in results:
        print(f"{name:<{width}}  {outcome:<8} {details}")
    failed = [name for name, outcome, _ in results if outcome == "FAILED"]
    print(f"\n{len(results)} samples, {len(failed)} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
