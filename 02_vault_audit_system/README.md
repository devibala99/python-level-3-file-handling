# Project 2: Vault + Audit System

## Description

This project extends the authentication system by adding:

- A user vault to store sensitive data
- An audit log to track all vault modifications

The focus is on **file handling**, **data persistence**, and **separating state from logs**.

---

## Features

- User registration and login
- Vault data stored per user
- Default vault data for admin user
- Audit log for every vault update
- Data stored using JSON and text files

---

## Files and Purpose

### main.py

- Handles user interaction
- Controls program flow (menus, inputs, outputs)
- Calls functions from `storage.py`
- Does not directly read/write files

### storage.py

- Handles all file operations
- Manages users.json and audit.log
- Contains business logic for:
  - User creation
  - Authentication
  - Vault updates
  - Audit logging

### users.json

- Stores user data persistently
- Structure:
  - username
  - hashed password
  - vault list

### audit.log

- Append-only log file
- Records:
  - username
  - action performed
  - item added
  - timestamp

---

## Concepts Practiced

- File handling (read, write, append)
- JSON data persistence
- Password hashing
- Data validation
- Separating responsibilities across files
- Maintaining data consistency

---

## How to Run

```bash
python main.py
```
