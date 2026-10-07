import json
import urllib.request

STATUS_URL = "https://status.internal.example/api/v1/health"


def fetch_status() -> str:
    """Return the health status reported by the internal status service."""
    with urllib.request.urlopen(STATUS_URL, timeout=5) as resp:
        return json.load(resp)["status"]
