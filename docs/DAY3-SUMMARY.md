# Day 3 Summary — Project Setup & Foundation

## What Was Completed Today

- ✅ Development environment fully configured: Python 3.10.7 confirmed, virtual environment created and activated, PowerShell execution policy fixed
- ✅ Dependencies installed: Flask, Flask-SQLAlchemy, anthropic, python-dotenv, gunicorn — recorded in `requirements.txt`
- ✅ Anthropic API key obtained (Evaluation access tier) — account currently has no usage credits
- ✅ **Mock AI Coach built** (`ai_coach.py`) as a working stand-in for the real Claude API, so development is unblocked regardless of billing status. Includes a clean, single-flag switch (`USE_MOCK_AI`) to enable real API calls later with zero other code changes.
- ✅ Database models defined (`Habit`, `CheckIn`) in `models.py`, matching the Day 2 schema design exactly, including the unique constraint on `(habit_id, date)`
- ✅ Flask application (`app.py`) created, connected to a local SQLite database, with a working homepage route (`GET /`)
- ✅ "Hello World" milestone achieved — app runs locally, database connects and auto-creates tables, homepage renders successfully in browser
- ✅ `.gitignore` updated to exclude `instance/` and `*.db`, keeping the database out of version control

## Issues Encountered & Resolved

1. **PowerShell execution policy blocked venv activation** — fixed via `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.
2. **`venv` initially created in the wrong parent folder** — recreated inside `ai-habit-coach` correctly.
3. **API key corruption during copy-paste** — multiple attempts resulted in a corrupted key (extra/wrong characters). Root cause traced to manual copy/paste rather than using the platform's "Copy key" button, and possibly clipboard/encoding issues from terminal-based `.env` file creation.
4. **`.env` file encoding issue** — a terminal `echo > .env` command produced a file encoding that `python-dotenv` couldn't parse. Resolved by creating the file directly in the VS Code editor instead.
5. **Anthropic account has no usage credits** — the free "Evaluation access" tier allows key creation but returned a `400: Your credit balance is too low` error on actual API calls. Per project rules (no paid tools without explicit approval), a **mock AI coach** was built instead, preserving full development velocity. Real Claude integration remains a one-line flag change away.
6. **`ModuleNotFoundError` when running scripts from inside `scripts/`** — resolved by adding `scripts/__init__.py` and running scripts as modules from the project root (`python -m scripts.script_name`).

## What's Ready to Build Tomorrow (Day 4)

- Database and models are live and tested — ready for full Habit CRUD (create, list, delete) and daily check-in logic.
- Flask app structure is in place — new routes can be added directly to `app.py`.
- Mock AI Coach is ready to be called from check-in routes immediately (no blocking on API credits).
- Folder structure, `.env`, and `.gitignore` are all correctly configured — no more environment setup needed for the rest of the capstone.

## Tomorrow's Objective (Day 4, per Blueprint)

Implement full habit management: add habit form, habit list display, delete functionality, daily check-in button, and streak calculation logic — the first real user-facing feature of the product.

## Blueprint Update

No structural changes to the remaining Blueprint days. One addition: Day 4 should begin by confirming `USE_MOCK_AI` status before wiring up the check-in → AI motivational message flow (originally planned for Day 5, but the mock version can realistically be connected as early as Day 4's check-in work, since it requires no API credits).
