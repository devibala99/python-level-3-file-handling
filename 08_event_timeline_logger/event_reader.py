import json

LOG_FILE = "events.log"

def read_all_events():
    events = []
    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                events.append(json.loads(line))
    except FileNotFoundError:
        pass
    return events

def read_events_by_user(username):
    return [e for e in read_all_events() if e["user"] == username]