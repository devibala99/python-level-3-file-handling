import json
import os
from datetime import datetime

VERSIONS_DIR = "versions"
ACTIVE_FILE = "active_config.json"

os.makedirs(VERSIONS_DIR, exist_ok=True)

def _get_next_version():
    existing = os.listdir(VERSIONS_DIR)
    versions = [int(f[1:-5]) for f in existing if f.startswith("v")]
    return max(versions, default=0) + 1

def create_new_config(config_data: dict):
    version = _get_next_version()
    path = f"{VERSIONS_DIR}/v{version}.json"

    payload = {
        "version" : version,
        "created_at": datetime.utcnow().isoformat(),
        "config": config_data
    }

    with open(path, "w") as f:
        json.dump(payload, f, indent=4)

    set_active_version(version)
    return version

def set_active_version(version: int):
    path = f"{VERSIONS_DIR}/v{version}.json"

    if not os.path.exists(path):
        return False, "Version not found"
    
    with open(path, "r") as f:
        data = json.load(f)

    with open(ACTIVE_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return True, "Active config updated"

def list_versions():
    return sorted(os.listdir(VERSIONS_DIR))

def read_active_config():
    if not os.path.exists(ACTIVE_FILE):
        return None
    
    with open(ACTIVE_FILE, "r") as f:
        return json.load(f)