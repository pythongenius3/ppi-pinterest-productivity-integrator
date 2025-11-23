import csv
from collections import Counter
from pathlib import Path


def build_summary_report(
    request_log_csv: str,
    summary_csv: str,
) -> None:
    """Read the request log CSV and build a simple summary by user."""
    log_path = Path(request_log_csv)
    summary_path = Path(summary_csv)

    if not log_path.exists():
        print(f"No request log found at {log_path}, skipping summary generation")
        return

    with log_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        counts = Counter(row["user"] for row in reader)

    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with summary_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["user", "total_requests"])
        for user, total in counts.items():
            writer.writerow([user, total])
