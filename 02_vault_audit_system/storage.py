import json
import os
import hashlib
from datetime import datetime

DATA_FILE = "users.json"
AUDIT_FILE = "audit.log"

def load_users():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_users(users):
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, password):
    users = load_users()

    if username in users:
        return False, "User already exists"

    if username == "admin":
        vault_data = [
            "SYSTEM_SECRET_KEY",
            "DATABASE_PASSWORD",
            "SERVER_CONFIG"
        ]
    else:
        vault_data = []

    users[username] = {
        "password": hash_password(password),
        "vault": vault_data
    }

    save_users(users)
    return True, "User registered successfully"

def authenticate_user(username, password):
    users = load_users()

    if username not in users:
        return False, "User does not exist"

    user = users[username]

    # Backward compatibility
    if "vault" not in user:
        user["vault"] = []
        users[username] = user
        save_users(users)

    if user["password"] != hash_password(password):
        return False, "Wrong password"

    return True, user

def log_audit_event(username, action, item):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp} | user={username} | action={action} | item={item}\n"

    with open(AUDIT_FILE, "a") as file:
        file.write(log_line)

def add_vault_item(username, item):
    users = load_users()

    if username not in users:
        return False, "User not found"

    users[username]["vault"].append(item)
    save_users(users)

    log_audit_event(username, "ADD_VAULT_ITEM", item)

    return True, "Vault item added successfully"
