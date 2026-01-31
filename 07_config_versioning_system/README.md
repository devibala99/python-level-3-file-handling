# Config Versioning System

## Description
A file-based configuration management system that maintains versioned configs
and allows safe switching between versions.

## Features
- Create versioned configuration files
- Maintain immutable history
- Switch active configuration
- Simple rollback support

## Files
- main.py – CLI interface
- config_manager.py – core logic
- versions/ – stored config versions
- active_config.json – currently active config

## How to Run
```bash
python main.py
