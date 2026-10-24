"""
Makes the downloads of the course: one ZIP archive for every folder of teaching-samples.

    python tools/make_zips.py            makes downloads/<folder>.zip for every folder that has changed
    python tools/make_zips.py --check    only checks that the archives hold the current files

A student downloads the archive of a module from the course page, unzips it, and works in that one
folder: the archive holds the files of the samples, requirements.txt (the packages of the course)
and, for the Supabase samples, .env.example. The files are at the top of the archive, so unzipping
it - on Windows and on macOS - makes one folder with the name of the archive.

Run it after changing a sample, and commit the archives together with the change. An archive is
written again only when its files have changed, so git sees only real changes.
"""

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
NO_PACKAGES = {"02-python-intro"}  # programs for the terminal, without packages
DATE = (2026, 1, 1, 0, 0, 0)  # the same date for every file: the archive depends only on the files


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
    if folder.name not in NO_PACKAGES:
        files["requirements.txt"] = (ROOT / "requirements.txt").read_bytes()
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
