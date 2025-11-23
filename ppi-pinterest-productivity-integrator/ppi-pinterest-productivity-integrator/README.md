# Pinterest Productivity Integrator (PPI)

The Pinterest Productivity Integrator (PPI) is a simulated internal IT systems project
that automates a typical enterprise workflow across Slack, Jira, and a Google
Workspace–style request log.

It demonstrates:
- SaaS integrations
- Configuration management
- Process mapping
- Automation workflows
- Systems analysis
- Collaboration tooling

---

## 🔁 High-Level Workflow

1. A request is submitted from Slack (mock payload)
2. The system parses the Slack request
3. A Jira ticket is created (mock or real)
4. The request is logged to a sheet-like CSV request log
5. A CSV activity summary report is generated
6. All actions are written to an activity log

---

## 📂 Repository Structure

- `architecture/` – architecture, sequence, and process diagrams (text form)
- `config/` – example configuration
- `scripts/` – core Python modules for the workflow
- `docs/` – setup notes, system flow, and testing guide
- `sample_data/` – mock Slack payload, mock Jira response, CSV logs
- `logs/` – activity log output

---

## 🏗 Architecture Overview

Core components:

- `slack_listener.py` – reads Slack-style request payloads
- `workflow_controller.py` – orchestrates the workflow
- `jira_ticket_creator.py` – creates or simulates Jira issues
- `gworkspace_logger.py` – logs activity to a CSV request log
- `generate_csv_report.py` – compiles a summary activity report

See the `architecture/` folder for diagrams.

---

## ⚙ Setup

1. Clone this repository
2. (Optional) Create and activate a virtual environment
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run a sample workflow:

   ```bash
   python scripts/workflow_controller.py
   ```

The script will:
- Load a mock Slack payload
- Simulate creating a Jira ticket
- Log the request
- Generate or update a summary CSV
- Append entries to `logs/ppi_activity_log.txt`

---

## 🧪 Testing

See `docs/testing-guide.md` for manual test scenarios.

---

## ✨ Author

Built by Dirhut Shafik as a systems integration and productivity engineering lab
inspired by internal IT work at modern SaaS companies.
