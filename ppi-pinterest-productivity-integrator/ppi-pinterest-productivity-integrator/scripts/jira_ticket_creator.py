import json
from pathlib import Path
from typing import Optional

import requests

from models import JiraTicket, RequestEvent


def create_jira_ticket_from_event(
    event: RequestEvent,
    base_url: str,
    project_key: str,
    email: Optional[str] = None,
    api_token: Optional[str] = None,
    use_mock: bool = True,
    mock_response_path: str = "../sample_data/sample_jira_response.json",
) -> JiraTicket:
    """
    Create or simulate a Jira ticket from a RequestEvent.

    If use_mock=True, load a mock Jira response from JSON instead of making
    a network call.
    """

    if use_mock:
        data = json.loads(Path(mock_response_path).read_text(encoding="utf-8"))
        return JiraTicket(key=data["key"], url=data["self"])

    # Real Jira call (optional)
    url = f"{base_url}/rest/api/3/issue"
    headers = {"Content-Type": "application/json"}
    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": event.text[:255],
            "description": f"Slack request from {event.user} in {event.channel}",
            "issuetype": {"name": "Task"},
        }
    }

    auth = (email, api_token) if email and api_token else None
    response = requests.post(url, headers=headers, json=payload, auth=auth)
    response.raise_for_status()
    data = response.json()

    return JiraTicket(key=data["key"], url=data["self"])
