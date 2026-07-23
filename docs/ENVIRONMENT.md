# AI Habit Coach — Environment Configuration

_Day 3 Deliverable. All environment variables, tools, and configuration in one place._

## Environment Variables (`.env`)

| Variable | Purpose | Required? | Notes |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | Authenticates calls to the Claude API | Yes (for real AI mode) | Get from console.anthropic.com → API Keys. Never commit this file. |
| `DATABASE_URL` | Points to the production database | Only in production (Day 10) | Defaults to local SQLite if not set |

**`.env` file location:** project root. Already excluded from Git via `.gitignore`.

## Mock AI Mode (Current Status)

As of Day 3, the Anthropic account does not have API credits (the free "Evaluation access" tier allows creating a key but not making calls without credits). To keep development unblocked, `ai_coach.py` includes a **mock mode**:

```python
USE_MOCK_AI = True  # Flip to False once real Claude API credits are available
```

- When `True`: motivational messages are generated using simple, rule-based logic (varied by streak length) — no API calls made, no cost.
- When `False`: real Claude API calls are made via the `anthropic` SDK.
- If a real API call fails for any reason (including insufficient credits), the code automatically falls back to the mock response — the app never breaks.

**To switch to real AI once credits are added:** change `USE_MOCK_AI = False` in `ai_coach.py`. No other code changes needed — this was designed for a clean swap.

## Local Development Tools

| Tool | Version / Notes |
|---|---|
| Python | 3.10.7 |
| VS Code | With Microsoft Python extension |
| Virtual environment | `venv` (created via `python -m venv venv`) |
| Package manager | pip |

## Installed Python Packages (`requirements.txt`)

| Package | Purpose |
|---|---|
| Flask | Web framework — handles routes and rendering |
| Flask-SQLAlchemy | ORM — lets Python code define and query database tables |
| anthropic | Official Claude API SDK |
| python-dotenv | Loads `.env` variables into the running application |
| gunicorn | Production-grade server (used for deployment on Day 10) |

## Database Configuration

Currently configured in `app.py`:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'
```

This creates a local SQLite database file (Flask-SQLAlchemy places it inside an auto-generated `instance/` folder). This is intentional for local development — Day 10 will introduce a `DATABASE_URL` environment variable pointing to a hosted PostgreSQL database in production, without changing any model code.

`instance/` and `*.db` are excluded via `.gitignore` — database files are never committed.

## VS Code Execution Policy Note (Windows Only)

If PowerShell blocks running the virtual environment activation script, run once per machine:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
This only allows locally-created scripts to run — it does not lower security for downloaded/untrusted scripts.
