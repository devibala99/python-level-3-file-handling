from storage import load_tickets, save_tickets
from workflow import is_valid_transaction

def create_ticket(ticket_id, description):
    tickets = load_tickets()

    if ticket_id in tickets:
        return False, "Ticket already exists"
    
    tickets[ticket_id] = {
        "description" : description,
        "state" : "OPEN"
    }

    save_tickets(tickets)
    return True, "Ticket created"

def update_ticket_state(ticket_id, new_state):
    tickets = load_tickets()

    if ticket_id not in tickets:
        return False, "Ticket not found"
    
    current_state = tickets[ticket_id]["state"]

    if not is_valid_transaction(current_state, new_state):
        return False, f"Invalid transition from {current_state} to {new_state}"

    tickets[ticket_id]["state"] = new_state
    save_tickets(tickets)
    return True, "Ticket updated"