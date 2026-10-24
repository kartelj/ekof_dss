"""
Makes the downloads of the course: one ZIP archive for every folder of teaching-samples.

    python tools/make_zips.py            makes downloads/<folder>.zip for every folder that has changed
    python tools/make_zips.py --check    only checks that the archives hold the current files

A student downloads the archive of a module from the course page, unzips it, and works in that one
folder: the archive holds the files of the samples, requirements.txt and, for the Supabase samples,
.env.example. The files are at the top of the archive, so unzipping it - on Windows and on macOS -
makes one folder with the name of the archive.

requirements.txt is made from the imports of the samples: it names only the packages that they use,
without versions - pip then installs the newest versions that work with the Python of the student.
An import that is not in PACKAGES stops the program: add the package that it comes from.

Run it after changing a sample, and commit the archives together with the change. An archive is
written again only when its files have changed, so git sees only real changes.
"""

import ast
import io
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAMPLES = ROOT / "teaching-samples"
DOWNLOADS = ROOT / "downloads"

SKIPPED_FOLDERS = {"__pycache__", ".venv", "venv", ".pytest_cache"}
SKIPPED_FILES = {".DS_Store", "Thumbs.db", ".env"}
SKIPPED_SUFFIXES = {".db", ".db-journal", ".sqlite3", ".pyc"}
DATE = (2026, 1, 1, 0, 0, 0)  # the same date for every file: the archive depends only on the files


# the package that every import comes from, and why we need it (None: it comes with another package)
PACKAGES = {
    "fastapi": ("fastapi", "web framework: pages and RESTful services"),
    "uvicorn": ("uvicorn", "web server that runs FastAPI applications"),
    "fastapi.templating": ("jinja2", "HTML templates"),
    "httpx2": ("httpx2", "HTTP client: calling RESTful services from Python"),
    "sqlmodel": ("sqlmodel", "working with a relational database through Python classes"),
    "supabase": ("supabase", "client for the Supabase cloud database"),
    "dotenv": ("python-dotenv", "reading settings from the .env file"),
    "pydantic": None,  # comes with fastapi and sqlmodel
    "sqlalchemy": None,  # comes with sqlmodel
    "postgrest": None,  # comes with supabase
}
FORMS = ("python-multipart", "reading the data of HTML forms")  # FastAPI needs it for Form() and request.form()


def requirements(folder: Path) -> str:
    """The text of requirements.txt: the packages that the samples of the folder import, without versions."""
    own = {p.stem for p in folder.rglob("*.py")} | {p.name for p in folder.rglob("*") if p.is_dir()}
    needed = {}
    for path in folder.rglob("*.py"):
        if "__pycache__" in path.parts:
            continue
        source = path.read_text(encoding="utf-8")
        for node in ast.walk(ast.parse(source)):
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                names = [node.module]
            else:
                continue
            for name in names:
                top = name.split(".")[0]
                if top in sys.stdlib_module_names or top in own:
                    continue
                key = name if name in PACKAGES else top
                if key not in PACKAGES:
                    raise SystemExit(f"{path}: which package does the import {name} come from? Add it to PACKAGES.")
                if PACKAGES[key]:
                    needed[PACKAGES[key][0]] = PACKAGES[key][1]
        if "fastapi" in needed and (".form()" in source or "Form(" in source):
            needed[FORMS[0]] = FORMS[1]
    if not needed:
        return ""
    order = [package for package, _ in [p for p in PACKAGES.values() if p] + [FORMS]]
    lines = [f"{package:<18} # {needed[package]}" for package in sorted(needed, key=order.index)]
    return f"""# The Python packages of these samples. Install them once, in this folder:
#
#   python -m venv .venv
#   .venv\\Scripts\\activate             (macOS:  source .venv/bin/activate)
#   pip install -r requirements.txt
#
# pip installs the newest versions that work with your Python (3.12 or newer).

{chr(10).join(lines)}
"""


def contents(folder: Path) -> dict[str, bytes]:
    """The files that the archive of the folder holds: their names in the archive, and their bytes."""
    files = {}
    for path in sorted(folder.rglob("*")):
        relative = path.relative_to(folder)
        if (
            path.is_file()
            and not set(relative.parts) & SKIPPED_FOLDERS
            and path.name not in SKIPPED_FILES
            and path.suffix not in SKIPPED_SUFFIXES
        ):
            files[relative.as_posix()] = path.read_bytes()
    packages = requirements(folder)
    if packages:  # the programs of module 02 need none
        files["requirements.txt"] = packages.encode("utf-8")
    if "supabase" in folder.name:
        files[".env.example"] = (ROOT / ".env.example").read_bytes()
    return files


def is_up_to_date(archive: Path, files: dict[str, bytes]) -> bool:
    if not archive.exists():
        return False
    with zipfile.ZipFile(archive) as existing:
        return sorted(existing.namelist()) == sorted(files) and all(
            existing.read(name) == data for name, data in files.items()
        )


def write(archive: Path, files: dict[str, bytes]) -> None:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as new:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16  # an ordinary file: read and write for the owner, read for the others
            new.writestr(info, files[name])
    archive.write_bytes(buffer.getvalue())


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    DOWNLOADS.mkdir(exist_ok=True)
    stale = []
    for folder in sorted(p for p in SAMPLES.iterdir() if p.is_dir()):
        archive = DOWNLOADS / f"{folder.name}.zip"
        files = contents(folder)
        if is_up_to_date(archive, files):
            print(f"{archive.name:<40} up to date")
        elif check_only:
            stale.append(archive.name)
            print(f"{archive.name:<40} OUT OF DATE")
        else:
            write(archive, files)
            print(f"{archive.name:<40} written, {len(files)} files, {archive.stat().st_size // 1024} KB")
    if stale:
        print(f"{len(stale)} archives are out of date - run: python tools/make_zips.py")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
