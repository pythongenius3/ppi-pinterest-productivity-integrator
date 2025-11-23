# ppi-pinterest-productivity-integrator
Slack → Jira → Workspace automation lab for IT Systems Engineering. Integrates SaaS tools, logs workflows, and demonstrates internal productivity automation.
# Pinterest Productivity Integrator (PPI)

The Pinterest Productivity Integrator (PPI) is a simulated internal IT systems project that automates a typical enterprise workflow across Slack, Jira, and Google Workspace

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
4. The request is logged to a Google Workspace style log (CSV as a stand-in)
5. A CSV activity report is generated
6. All actions are written to an activity log

---

## 📂 Repository Structure

See the `/scripts`, `/docs`, `/architecture`, and `/sample_data` folders for implementation, documentation, diagrams, and sample payloads

---

## 🏗 Architecture Overview

The core components are:

- `slack_listener.py` – reads Slack-style request payloads
- `workflow_controller.py` – orchestrates the whole workflow
- `jira_ticket_creator.py` – creates or simulates Jira issues
- `gworkspace_logger.py` – logs activity to a sheet-like CSV store
- `generate_csv_report.py` – compiles a summary activity report

Diagrams are in `/architecture`

---

## ⚙ Setup

1. Clone this repository
2. Create and activate a virtual environment
3. Install dependencies

```bash
pip install -r requirements.txt
