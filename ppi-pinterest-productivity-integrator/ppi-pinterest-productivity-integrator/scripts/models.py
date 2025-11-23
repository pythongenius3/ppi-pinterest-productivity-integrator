from dataclasses import dataclass
from datetime import datetime


@dataclass
class RequestEvent:
    user: str
    channel: str
    text: str
    timestamp: datetime


@dataclass
class JiraTicket:
    key: str
    url: str
