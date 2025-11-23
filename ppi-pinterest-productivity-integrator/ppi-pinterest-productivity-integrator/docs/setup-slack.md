# Slack Setup (Mock Mode)

This project uses a mock Slack payload defined in `sample_data/mock_slack_payload.json`
to simulate an incoming IT request from a Slack channel.

To adapt this to a real Slack app:
- Create a Slack app and enable the Events API
- Configure a request URL that points to a small web service
- Translate the real Slack event into the `RequestEvent` structure used by this project
