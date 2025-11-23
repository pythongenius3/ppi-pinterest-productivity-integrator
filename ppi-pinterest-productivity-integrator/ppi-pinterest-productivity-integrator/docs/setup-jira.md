# Jira Setup (Optional)

By default, the project uses a mock Jira response defined in
`sample_data/sample_jira_response.json` so it can run without network access.

To connect to a real Jira Cloud instance:
- Create or use an existing Jira Cloud site
- Generate an API token for your Atlassian account
- Update `config/config-example.json` with your base URL, email, and API token
- Set `use_mock=False` when calling `create_jira_ticket_from_event()` in `workflow_controller.py`
