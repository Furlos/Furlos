import csv
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT))

from clean_csv import normalize_name, parse_amount, parse_date, run


class CleanCsvTests(unittest.TestCase):
    def test_normalizes_name_without_losing_accents(self):
        self.assertEqual(normalize_name("  ana   GARCÍA "), "Ana García")
        self.assertEqual(normalize_name("josé DE la cruz"), "José de la Cruz")

    def test_accepts_iso_and_unambiguous_numeric_dates(self):
        self.assertEqual(parse_date("2026-05-10"), date(2026, 5, 10))
        self.assertEqual(parse_date("17/05/2026"), date(2026, 5, 17))
        self.assertEqual(parse_date("05/17/2026"), date(2026, 5, 17))

    def test_flags_ambiguous_numeric_date(self):
        with self.assertRaisesRegex(ValueError, "ambiguous"):
            parse_date("05/06/2026")

    def test_parses_common_amount_formats(self):
        self.assertEqual(parse_amount("1.234,50 €"), parse_amount("1234.50"))
        self.assertEqual(parse_amount("1,234.50 USD"), parse_amount("1234.50"))

    def test_sample_writes_clean_rows_and_review_exceptions(self):
        sample = PROJECT / "sample" / "raw_bookings.csv"
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            clean_count, exception_count = run(sample, output)
            self.assertEqual((clean_count, exception_count), (3, 3))

            with (output / "clean_bookings.csv").open(encoding="utf-8-sig", newline="") as stream:
                clean = list(csv.DictReader(stream))
            self.assertEqual(clean[0]["customer_name"], "Ana García")
            self.assertEqual(clean[0]["email"], "ana@example.com")
            self.assertEqual(clean[0]["amount"], "80.00")

            with (output / "exceptions.csv").open(encoding="utf-8-sig", newline="") as stream:
                exceptions = list(csv.DictReader(stream))
            reasons = " ".join(row["reason"] for row in exceptions)
            self.assertIn("ambiguous day/month order", reasons)
            self.assertIn("duplicate booking_id", reasons)
            self.assertIn("positive whole number", reasons)


if __name__ == "__main__":
    unittest.main()

