#!/usr/bin/env python3
"""Local, private Claude usage logger. Stdlib only, no dependencies."""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_LOG_DIR = Path.home() / ".claude-usage-log"
CODE_PROJECTS_DIR = Path.home() / ".claude" / "projects"


def scan_code(date: str) -> dict:
    if not CODE_PROJECTS_DIR.is_dir():
        return {"found": False, "date": date, "projects": []}

    projects = {}
    for project_dir in CODE_PROJECTS_DIR.iterdir():
        if not project_dir.is_dir():
            continue
        for transcript_path in project_dir.glob("*.jsonl"):
            session_id = transcript_path.stem
            session_touched = False
            slugs = set()
            user_messages = 0
            assistant_messages = 0

            try:
                with transcript_path.open("r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            entry = json.loads(line)
                        except json.JSONDecodeError:
                            continue

                        timestamp = entry.get("timestamp", "")
                        if not timestamp.startswith(date):
                            continue

                        session_touched = True
                        entry_type = entry.get("type")
                        if entry_type == "user":
                            user_messages += 1
                        elif entry_type == "assistant":
                            assistant_messages += 1

                        slug = entry.get("slug")
                        if slug:
                            slugs.add(slug)
            except OSError:
                continue

            if not session_touched:
                continue

            project_name = project_dir.name
            agg = projects.setdefault(
                project_name,
                {
                    "project": project_name,
                    "sessions": 0,
                    "session_ids": [],
                    "user_messages": 0,
                    "assistant_messages": 0,
                    "slugs": set(),
                },
            )
            agg["sessions"] += 1
            agg["session_ids"].append(session_id)
            agg["user_messages"] += user_messages
            agg["assistant_messages"] += assistant_messages
            agg["slugs"] |= slugs

    result_projects = []
    for agg in projects.values():
        agg["slugs"] = sorted(agg["slugs"])
        result_projects.append(agg)
    result_projects.sort(key=lambda p: p["project"])

    return {
        "found": bool(result_projects),
        "date": date,
        "projects": result_projects,
    }


def append_entry(date: str, entry_json: str, log_dir: Path) -> dict:
    entry = json.loads(entry_json)
    entry.setdefault("date", date)
    entry.setdefault("logged_at", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))

    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{date}.jsonl"

    existing_lines = []
    if log_path.exists():
        with log_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    existing = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if (
                    existing.get("surface") == entry.get("surface")
                    and existing.get("project") == entry.get("project")
                ):
                    continue
                existing_lines.append(existing)

    existing_lines.append(entry)

    with log_path.open("w", encoding="utf-8") as f:
        for line_entry in existing_lines:
            f.write(json.dumps(line_entry) + "\n")

    return {"ok": True, "log_path": str(log_path), "entries": len(existing_lines)}


def show(date: str, log_dir: Path) -> None:
    log_path = log_dir / f"{date}.jsonl"
    if not log_path.exists():
        print("[]")
        return
    with log_path.open("r", encoding="utf-8") as f:
        print(f.read().strip())


def main():
    parser = argparse.ArgumentParser(description="Local Claude usage logger")
    sub = parser.add_subparsers(dest="command", required=True)

    scan_parser = sub.add_parser("scan-code", help="Scan Claude Code transcripts for a date")
    scan_parser.add_argument("--date", required=True, help="YYYY-MM-DD")

    append_parser = sub.add_parser("append", help="Append or replace a log entry for a date")
    append_parser.add_argument("--date", required=True, help="YYYY-MM-DD")
    append_parser.add_argument("--json", required=True, help="JSON object for the entry")
    append_parser.add_argument("--log-dir", default=str(DEFAULT_LOG_DIR))

    show_parser = sub.add_parser("show", help="Print the raw log for a date")
    show_parser.add_argument("--date", required=True, help="YYYY-MM-DD")
    show_parser.add_argument("--log-dir", default=str(DEFAULT_LOG_DIR))

    args = parser.parse_args()

    if args.command == "scan-code":
        print(json.dumps(scan_code(args.date), indent=2))
    elif args.command == "append":
        result = append_entry(args.date, args.json, Path(args.log_dir))
        print(json.dumps(result, indent=2))
    elif args.command == "show":
        show(args.date, Path(args.log_dir))


if __name__ == "__main__":
    sys.exit(main())
