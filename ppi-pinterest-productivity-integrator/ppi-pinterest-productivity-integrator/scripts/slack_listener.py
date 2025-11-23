import json
from datetime import datetime
from pathlib import Path

from models import RequestEvent


def load_mock_slack_event(mock_path: str) -> RequestEvent:
    """
    Load a mock Slack payload from JSON and convert it into a RequestEvent.
    """
    path = Path(mock_path)
    with path.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    # Convert ISO 8601 string (with Z) into datetime
    ts = datetime.fromisoformat(payload["timestamp"].replace("Z", "+00:00"))

    return RequestEvent(
        user=payload["user"],
        channel=payload["channel"],
        text=payload["text"],
        timestamp=ts,
    )


if __name__ == "__main__":
    event = load_mock_slack_event("../sample_data/mock_slack_payload.json")
    print(event)
