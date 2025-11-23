# Google Workspace Style Logging

In a production environment, this kind of workflow would typically log into a
Google Sheet or database for reporting and auditing.

For simplicity and portability, this project uses CSV files to represent a
sheet-like request log and summary report:

- `sample_data/request_log.csv` – detailed per-request log
- `sample_data/example_csv_report.csv` – aggregated summary by user

The structure makes it easy to swap CSV-based logging for the Google Sheets API
in the future.
