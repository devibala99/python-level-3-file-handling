import json
from datetime import datetime

LOG_FILE = "events.log"

def log_event(user, action, data):
    event = {
        "ts": datetime.utcnow().isoformat(),
        "user" : user,
        "action" : action,
        "data" : data
    }

    with open(LOG_FILE, "a") as file:
        file.write(json.dumps(event)+ "\n")