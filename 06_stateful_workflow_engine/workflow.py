
ALLOWED_TRANSACTIONS = {
    "OPEN" : ["IN_PROGRESS"],
    "IN_PROGRESS": ["RESOLVED"],
    "RESOLVED" : []
}

def is_valid_transaction(current, next_state):
    return next_state in ALLOWED_TRANSACTIONS.get(current, [])