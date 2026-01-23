# Authentication & Password Vault (File-Based)

## Overview

This project implements a basic authentication system using **file-based storage**.
It simulates how real backend systems handle user registration, login, and
user-scoped private data (vault) without using a database.

The focus is on **file handling, data persistence, and defensive backend logic**.

---

## Why This Project Exists

In real systems:

- User data lives longer than code
- Authentication is the gatekeeper for private data
- Storage logic must be isolated and reliable

This project teaches those ideas using **only Python and JSON files**.

---

## Application Flow

1. User registers with username and password
2. Password is **hashed** and stored in a JSON file
3. User logs in with credentials
4. After successful authentication:
   - User-specific vault data is unlocked
5. Admin user gets pre-initialized vault data

---

## File Structure

01_auth_password_vault/
│
├── main.py # Application flow & user interaction
├── storage.py # File handling, hashing, persistence logic
├── users.json # Persistent user data (acts like a database)
└── README.md

---

## File Responsibilities

### main.py

- Controls program flow
- Handles user input
- Calls authentication and storage logic
- Never touches files directly

### storage.py

- Reads and writes JSON files
- Hashes passwords
- Handles schema safety
- Initializes user vaults
- Simulates backend persistence layer

### users.json

- Stores all user data
- Must not be edited manually
- Automatically created and updated by the program

---

## Key Learnings

- File handling with JSON
- Persistent storage patterns
- Password hashing basics
- Defensive coding for old data
- Role-based data initialization
- Separation of concerns

---

## How to Run

```bash
python main.py
```
