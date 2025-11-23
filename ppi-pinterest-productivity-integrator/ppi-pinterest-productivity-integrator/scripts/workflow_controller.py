import json
from pathlib import Path
from datetime import datetime

from slack_listener import load_mock_slack_event
from jira_ticket_creator import create_jira_ticket_from_event
from gworkspace_logger import log_request_to_csv
from generate_csv_report import build_summary_report


def load_config(config_path: str = "../config/config-example.json") -> dict:
    path = Path(config_path)
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def log_activity(activity_log_path: str, message: str) -> None:
    path = Path(activity_log_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.utcnow().isoformat()
    with path.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def run_workflow() -> None:
    """
    Orchestrate the full workflow:

    1. Load a mock Slack event
    2. Create a Jira ticket (mock or real)
    3. Log the request to a CSV log
    4. Update the summary report
    5. Write activity entries
    """
    config = load_config()

    paths = config["paths"]
    logging_conf = config["logging"]
    jira_conf = config["jira"]

    activity_log_path = logging_conf["activity_log_path"]

    log_activity(activity_log_path, "Starting workflow run")

    # 1. Load Slack event
    event = load_mock_slack_event(paths["mock_slack_payload"])
    log_activity(activity_log_path, f"Loaded Slack event from {event.user}")

    # 2. Create Jira ticket (mock by default)
    ticket = create_jira_ticket_from_event(
        event,
        base_url=jira_conf["base_url"],
        project_key=jira_conf["project_key"],
        email=jira_conf.get("email"),
        api_token=jira_conf.get("api_token"),
        use_mock=True,
        mock_response_path=paths["mock_jira_response"],
    )
    log_activity(activity_log_path, f"Created Jira ticket {ticket.key}")

    # 3. Log request
    log_request_to_csv(paths["request_log_csv"], event, ticket)
    log_activity(activity_log_path, "Logged request to CSV")

    # 4. Build summary
    build_summary_report(
        request_log_csv=paths["request_log_csv"],
        summary_csv=paths["summary_csv"],
    )
    log_activity(activity_log_path, "Updated summary report")

    log_activity(activity_log_path, "Workflow completed successfully")


if __name__ == "__main__":
    run_workflow()
    print("Workflow run complete. Check logs and CSV outputs.")
