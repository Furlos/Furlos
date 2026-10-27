# CSV cleanup example

Small, dependency-free Python example using invented booking data. It normalizes names and email addresses, parses unambiguous dates, removes duplicate booking IDs and writes uncertain rows to a separate exceptions file. It never guesses an ambiguous day/month date.

This is a portfolio sample, **not a client project**. The sample data is fictional and contains no real customer information.

## Run

```powershell
python clean_csv.py sample/raw_bookings.csv --output-dir output
```

The command creates:

- `output/clean_bookings.csv` — rows that passed validation.
- `output/exceptions.csv` — rows needing human review and the reason.

Only Python's standard library is required. Run checks with:

```powershell
python -m unittest discover -s tests -v
```

## Rules

- ISO dates (`YYYY-MM-DD`) are accepted.
- Numeric dates are accepted only when one component is greater than 12 and the order is therefore unambiguous.
- Dates such as `05/06/2026` are flagged; no day/month convention is assumed.
- Amounts support common currency marks/codes and decimal/thousands separators.
- Rows with missing required fields, malformed values, or repeated booking IDs go to the exceptions file.

Real client data should be reviewed and its rules agreed with the client before processing.

