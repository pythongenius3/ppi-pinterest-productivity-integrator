# Testing Guide

Manual test scenarios:

1. **Baseline run**
   - Ensure you have installed dependencies with `pip install -r requirements.txt`
   - Run `python scripts/workflow_controller.py`
   - Confirm that:
     - `logs/ppi_activity_log.txt` contains new entries
     - `sample_data/request_log.csv` has an additional row
     - `sample_data/example_csv_report.csv` contains a summary line for the test user

2. **Change the Slack payload**
   - Edit `sample_data/mock_slack_payload.json` and change the `user`, `channel`, or `text`
   - Run `python scripts/workflow_controller.py` again
   - Verify that the log and summary CSVs reflect the new values

3. **Simulate a different Jira ticket**
   - Edit `sample_data/sample_jira_response.json` to use a different `key`
   - Run the workflow and confirm the new ticket ID appears in the logs
