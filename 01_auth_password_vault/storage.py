import json
import os
import hashlib

DATA_FILE = "users.json"


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

    # 🔐 Role-based default vault
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
    return True, "User registered successfully."


def authenticate_user(username, password):
    users = load_users()

    if username not in users:
        return False, "User does not exist"

    user = users[username]

    # 🛡️ Schema safety (handles old users)
    if "vault" not in user:
        user["vault"] = []
        users[username] = user
        save_users(users)

    hashed_input = hash_password(password)

    if user["password"] != hashed_input:
        return False, "Wrong password"

    return True, user
