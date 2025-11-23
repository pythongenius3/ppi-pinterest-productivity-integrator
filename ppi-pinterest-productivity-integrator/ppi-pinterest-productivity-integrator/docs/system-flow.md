# System Flow

1. A Slack-style request is defined in `sample_data/mock_slack_payload.json`
2. `workflow_controller.py` loads this payload using `slack_listener.py`
3. A `RequestEvent` object is created
4. `jira_ticket_creator.py` simulates creation of a Jira ticket and returns a ticket key and URL
5. `gworkspace_logger.py` logs the request into `sample_data/request_log.csv`
6. `generate_csv_report.py` produces a simple summary by user in `sample_data/example_csv_report.csv`
7. `logs/ppi_activity_log.txt` contains a timestamped log of key actions
