import csv
from pathlib import Path

from models import RequestEvent, JiraTicket


def ensure_csv_header(path: Path, header: list[str]) -> None:
    """Ensure the CSV file exists and has the expected header row."""
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)


def log_request_to_csv(
    csv_path: str,
    event: RequestEvent,
    ticket: JiraTicket,
    status: str = "CREATED",
) -> None:
    """Append a single request record to a CSV file."""
    path = Path(csv_path)
    header = ["timestamp", "user", "channel", "request_text", "ticket_id", "status"]

    ensure_csv_header(path, header)

    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                event.timestamp.isoformat(),
                event.user,
                event.channel,
                event.text,
                ticket.key,
                status,
            ]
        )
