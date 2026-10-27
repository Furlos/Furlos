#!/usr/bin/env python3
"""Normalize a small CSV of bookings while flagging uncertain rows.

Demonstration only: no customer data or commercial results are included.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable


OUTPUT_FIELDS = [
    "booking_id",
    "customer_name",
    "email",
    "booking_date",
    "nights",
    "amount",
]
REQUIRED_FIELDS = OUTPUT_FIELDS
DATE_PATTERN = re.compile(r"^(\d{1,2})[./-](\d{1,2})[./-](\d{4})$")
EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
CURRENCY_MARKS = ("€", "$", "£", "EUR", "USD", "GBP")


def normalize_name(value: str) -> str:
    """Collapse whitespace and normalize capitalization without stripping accents."""
    parts = value.split()
    normalized = [part[:1].upper() + part[1:].lower() for part in parts]
    particles = {"de", "del", "la", "las", "los", "y"}
    for index in range(1, len(normalized)):
        if normalized[index].lower() in particles:
            normalized[index] = normalized[index].lower()
    return " ".join(normalized)


def normalize_email(value: str) -> str:
    return value.strip().lower()


def parse_date(value: str) -> date:
    """Parse ISO or numeric dates only when their order is clear."""
    value = value.strip()
    try:
        return date.fromisoformat(value)
    except ValueError:
        pass

    match = DATE_PATTERN.fullmatch(value)
    if not match:
        raise ValueError("unsupported date format")

    first, second, year = (int(part) for part in match.groups())
    if first > 12 and second <= 12:
        day, month = first, second
    elif second > 12 and first <= 12:
        month, day = first, second
    else:
        raise ValueError("ambiguous day/month order")

    try:
        return date(year, month, day)
    except ValueError as error:
        raise ValueError("invalid calendar date") from error


def parse_amount(value: str) -> Decimal:
    """Parse a simple amount; reject empty or malformed values."""
    cleaned = value.strip().upper()
    for mark in CURRENCY_MARKS:
        cleaned = cleaned.replace(mark, "")
    cleaned = re.sub(r"\s+", "", cleaned)
    if not cleaned:
        raise ValueError("missing amount")

    comma = cleaned.rfind(",")
    dot = cleaned.rfind(".")
    if comma >= 0 and dot >= 0:
        decimal_separator = "," if comma > dot else "."
        thousands_separator = "." if decimal_separator == "," else ","
        cleaned = cleaned.replace(thousands_separator, "")
        cleaned = cleaned.replace(decimal_separator, ".")
    elif comma >= 0 or dot >= 0:
        separator = "," if comma >= 0 else "."
        left, right = cleaned.rsplit(separator, 1)
        if len(right) in (1, 2):
            cleaned = left + "." + right
        elif len(right) == 3 and left:
            cleaned = left + right
        else:
            raise ValueError("unclear amount separator")

    try:
        amount = Decimal(cleaned)
    except InvalidOperation as error:
        raise ValueError("invalid amount") from error
    if not amount.is_finite() or amount < 0:
        raise ValueError("amount must be a non-negative number")
    return amount.quantize(Decimal("0.01"))


def normalize_row(row: dict[str, str], row_number: int, seen_ids: set[str]) -> tuple[dict[str, str] | None, list[str]]:
    errors: list[str] = []
    source = {key.strip().lower(): (value or "").strip() for key, value in row.items() if key}

    missing = [field for field in REQUIRED_FIELDS if not source.get(field)]
    if missing:
        errors.append("missing required field(s): " + ", ".join(missing))

    booking_id = source.get("booking_id", "")
    if booking_id and booking_id in seen_ids:
        errors.append("duplicate booking_id")
    elif booking_id:
        seen_ids.add(booking_id)

    name = normalize_name(source.get("customer_name", ""))
    email = normalize_email(source.get("email", ""))
    if email and not EMAIL_PATTERN.fullmatch(email):
        errors.append("invalid email format")

    booking_date = ""
    raw_date = source.get("booking_date", "")
    if raw_date:
        try:
            booking_date = parse_date(raw_date).isoformat()
        except ValueError as error:
            errors.append(f"booking_date: {error}")

    nights = ""
    raw_nights = source.get("nights", "")
    if raw_nights:
        try:
            parsed_nights = int(raw_nights)
            if parsed_nights <= 0:
                raise ValueError
            nights = str(parsed_nights)
        except ValueError:
            errors.append("nights must be a positive whole number")

    amount = ""
    raw_amount = source.get("amount", "")
    if raw_amount:
        try:
            amount = f"{parse_amount(raw_amount):.2f}"
        except ValueError as error:
            errors.append(f"amount: {error}")

    if errors:
        return None, errors
    return {
        "booking_id": booking_id,
        "customer_name": name,
        "email": email,
        "booking_date": booking_date,
        "nights": nights,
        "amount": amount,
    }, []


def clean_rows(rows: Iterable[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    cleaned: list[dict[str, str]] = []
    exceptions: list[dict[str, str]] = []
    seen_ids: set[str] = set()

    for row_number, row in enumerate(rows, start=2):
        result, errors = normalize_row(row, row_number, seen_ids)
        if result is not None:
            cleaned.append(result)
        else:
            exceptions.append({
                "source_row": str(row_number),
                "booking_id": (row.get("booking_id") or "").strip(),
                "reason": "; ".join(errors),
                "raw_row": json.dumps(row, ensure_ascii=False, sort_keys=True),
            })
    return cleaned, exceptions


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def run(input_path: Path, output_dir: Path) -> tuple[int, int]:
    output_dir.mkdir(parents=True, exist_ok=True)
    with input_path.open("r", newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames:
            raise ValueError("input CSV has no header row")
        cleaned, exceptions = clean_rows(reader)

    write_csv(output_dir / "clean_bookings.csv", OUTPUT_FIELDS, cleaned)
    exception_fields = ["source_row", "booking_id", "reason", "raw_row"]
    write_csv(output_dir / "exceptions.csv", exception_fields, exceptions)
    return len(cleaned), len(exceptions)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_csv", type=Path, help="path to the input CSV")
    parser.add_argument("--output-dir", type=Path, default=Path("output"))
    args = parser.parse_args()
    cleaned_count, exception_count = run(args.input_csv, args.output_dir)
    print(f"Clean rows: {cleaned_count}")
    print(f"Rows to review: {exception_count}")
    print(f"Output folder: {args.output_dir.resolve()}")


if __name__ == "__main__":
    main()

