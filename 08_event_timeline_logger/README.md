# Event Timeline Logger

## Description

A file-based event logging system that records user actions as immutable events.

## Features

- Append-only event logging
- Time-ordered history
- User-based filtering
- Crash-safe persistence

## Files

- main.py – CLI interface
- event_logger.py – event writer
- event_reader.py – event reader
- events.log – event storage

## Run

python main.py
