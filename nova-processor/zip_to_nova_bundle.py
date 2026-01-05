#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import io
import sys
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


TEXT_EXTS_DEFAULT = {
    ".md", ".txt",
    ".yaml", ".yml",
    ".json",
    ".toml",
    ".ini", ".cfg",
    ".py", ".js", ".ts", ".sh", ".bash", ".zsh",
    ".html", ".css",
    ".xml",
    ".csv",
}


@dataclass(frozen=True)
class ZipEntry:
    path: str
    is_text: bool
    size: int


def sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()


def is_probably_text(path: str, ext_whitelist: set[str]) -> bool:
    ext = Path(path).suffix.lower()
    return ext in ext_whitelist


def read_zip_text(zf: zipfile.ZipFile, name: str) -> tuple[str, str]:
    """
    Returns (decoded_text, sha256_hex). Tries UTF-8 first; falls back to latin-1
    with a clear marker if decoding had to be lossy.
    """
    raw = zf.read(name)
    digest = sha256_bytes(raw)

    try:
        text = raw.decode("utf-8")
        return text, digest
    except UnicodeDecodeError:
        # latin-1 is reversible for bytes->str but can look weird; still better than crashing.
        text = raw.decode("latin-1")
        # Mark that decoding was not utf-8; callers can include note.
        return text, digest


def iter_zip_entries(zf: zipfile.ZipFile, ext_whitelist: set[str]) -> tuple[list[ZipEntry], list[ZipEntry]]:
    text_entries: list[ZipEntry] = []
    non_text_entries: list[ZipEntry] = []

    for info in zf.infolist():
        if info.is_dir():
            continue
        name = info.filename

        # Skip macOS metadata noise
        if name.startswith("__MACOSX/") or name.endswith(".DS_Store"):
            continue

        entry = ZipEntry(
            path=name,
            is_text=is_probably_text(name, ext_whitelist),
            size=info.file_size,
        )
        (text_entries if entry.is_text else non_text_entries).append(entry)

    text_entries.sort(key=lambda e: e.path.lower())
    non_text_entries.sort(key=lambda e: e.path.lower())
    return text_entries, non_text_entries


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Compile a .zip filesystem into a single NOVA_BUNDLE markdown file."
    )
    ap.add_argument("zip_path", help="Input .zip file")
    ap.add_argument("--out", default="nova-process.md", help="Output bundle markdown path")
    ap.add_argument("--bundle-id", default=None, help="Optional bundle id")
    ap.add_argument(
        "--text-exts",
        default=",".join(sorted(TEXT_EXTS_DEFAULT)),
        help="Comma-separated list of extensions treated as text",
    )
    ap.add_argument("--include-sha256", action="store_true", help="Include per-file sha256")
    ap.add_argument("--max-bytes", type=int, default=750_000, help="Max bytes per text file (safety)")
    args = ap.parse_args()

    zip_path = Path(args.zip_path)
    out_path = Path(args.out)

    ext_whitelist = {e.strip().lower() for e in args.text_exts.split(",") if e.strip()}
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    bundle_id = args.bundle_id or f"{zip_path.stem}-{now}"

    if not zip_path.exists():
        print(f"ERROR: zip not found: {zip_path}", file=sys.stderr)
        return 2

    parts: list[str] = []
    parts.append("# NOVA_BUNDLE v0.1")
    parts.append(f"bundle_id: {bundle_id}")
    parts.append(f"source_zip: {zip_path.name}")
    parts.append(f"generated_utc: {now}")
    parts.append("")
    parts.append("## MANIFEST")
    parts.append("This bundle preserves file paths from the zip and flattens text files into a single document.")
    parts.append("Binary / non-text files are listed but not embedded (by default).")
    parts.append("")

    with zipfile.ZipFile(zip_path, "r") as zf:
        text_entries, non_text_entries = iter_zip_entries(zf, ext_whitelist)

        parts.append("### Included text files")
        for e in text_entries:
            parts.append(f"- `{e.path}` ({e.size} bytes)")
        if not text_entries:
            parts.append("- (none)")
        parts.append("")

        parts.append("### Excluded non-text files")
        for e in non_text_entries:
            parts.append(f"- `{e.path}` ({e.size} bytes)")
        if not non_text_entries:
            parts.append("- (none)")
        parts.append("")

        # Emit each text file as a chapter
        for e in text_entries:
            if e.size > args.max_bytes:
                parts.append(f"## FILE: {e.path}")
                parts.append("BEGIN_FILE")
                parts.append(f"[SKIPPED: file is {e.size} bytes, exceeds --max-bytes={args.max_bytes}]")
                parts.append("END_FILE")
                parts.append("")
                continue

            text, digest = read_zip_text(zf, e.path)
            parts.append(f"## FILE: {e.path}")
            if args.include_sha256:
                parts.append(f"sha256: {digest}")
            parts.append("BEGIN_FILE")
            parts.append(text.rstrip("\n"))
            parts.append("END_FILE")
            parts.append("")

    out_path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote bundle: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
