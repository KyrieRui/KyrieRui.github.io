"""Study-time tracker: add, view, total and save to JSON using only the standard library."""

import argparse
import json
import sys
from pathlib import Path


def make_record(subject, minutes):
    """Create one record. Zero minutes is allowed; negative numbers, booleans and decimals are not."""
    if not isinstance(subject, str) or not subject.strip():
        raise ValueError("The subject can't be empty")
    if type(minutes) is not int or minutes < 0:
        raise ValueError("Minutes must be a whole number that is not negative")
    return {"subject": subject.strip(), "minutes": minutes}


def validate_records(data):
    """Check the records from the file. Never treat damaged content as empty records and overwrite it."""
    if not isinstance(data, list):
        raise TypeError("The outside of the records file must be a list")
    records = []
    for item in data:
        if not isinstance(item, dict) or set(item) != {"subject", "minutes"}:
            raise ValueError("Each record must have exactly two fields: subject and minutes")
        records.append(make_record(item["subject"], item["minutes"]))
    return records


def total_minutes(records, subject=None):
    """Total all records, or only the records for one subject."""
    return sum(
        item["minutes"]
        for item in records
        if subject is None or item["subject"] == subject
    )


def load_records(path):
    """Start with an empty list if the file doesn't exist; if the format is damaged, let the caller handle the error."""
    try:
        content = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return []
    return validate_records(json.loads(content))


def save_records(path, records):
    """Check the records before writing; the file always holds the complete current records."""
    validated = validate_records(records)
    content = json.dumps(validated, ensure_ascii=False, indent=2) + "\n"
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Record and total minutes of study")
    parser.add_argument("--file", default="study-records.json", help="Path of the JSON records file")
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add", help="Add a study record")
    add.add_argument("subject", help="Subject name")
    add.add_argument("minutes", type=int, help="Minutes (a whole number, not negative)")
    commands.add_parser("list", help="List all records")
    total = commands.add_parser("total", help="Total the study time")
    total.add_argument("--subject", help="Only total this subject")
    args = parser.parse_args(argv)

    try:
        records = load_records(args.file)
        if args.command == "add":
            record = make_record(args.subject, args.minutes)
            records.append(record)
            save_records(args.file, records)
            print(f"Recorded: {record['subject']} {record['minutes']} minutes")
        elif args.command == "list":
            if not records:
                print("No records yet")
            for index, record in enumerate(records, 1):
                print(f"{index}. {record['subject']}: {record['minutes']} minutes")
        else:
            print(f"Total: {total_minutes(records, args.subject)} minutes")
    except (OSError, TypeError, ValueError) as error:
        print(f"Can't process the records: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
