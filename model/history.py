import json
import os

HISTORY_FILE = "history.json"

def get_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r") as f:
            content = f.read().strip()

            if not content:
                return []

            return json.loads(content)

    except  json.JSONDecodeError:
        return []