import json
import os

DATA_FILE = "tickets.json"

def load_tickets():
    if not os.path.exists(DATA_FILE):
        return {}
    
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}
        
def save_tickets(tickets):
    with open(DATA_FILE, "w") as file:
        json.dump(tickets, file, indent=4)