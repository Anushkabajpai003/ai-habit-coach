# AI Habit Coach — Setup Guide

_Day 3 Deliverable. Follow these steps to get the project running locally from scratch._

## Prerequisites

- **Python 3.10+** installed (confirmed working: 3.10.7)
- **VS Code** with the Microsoft Python extension installed
- **Git** installed and a GitHub account

## 1. Clone the Repository

```
git clone https://github.com/Anushkabajpai003/ai-habit-coach.git
cd ai-habit-coach
```

## 2. Create and Activate a Virtual Environment

A virtual environment keeps this project's Python packages isolated from other projects on your machine.

**Windows (PowerShell):**
```
python -m venv venv
venv\Scripts\activate
```

If you see an error like `running scripts is disabled on this system`, run this once (only needs to be done one time per machine):
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then confirm with `Y` when prompted, and re-run the activate command.

You'll know it worked when your terminal prompt shows `(venv)` at the start.

## 3. Install Dependencies

```
pip install flask flask-sqlalchemy anthropic python-dotenv gunicorn
pip freeze > requirements.txt
```

Or, if `requirements.txt` already exists (e.g. after cloning):
```
pip install -r requirements.txt
```

## 4. Set Up Environment Variables

Create a `.env` file in the project root (if it doesn't exist) and add:

```
ANTHROPIC_API_KEY=your-key-here
```

Get a key from **console.anthropic.com → API Keys → Create Key**. See `ENVIRONMENT.md` for full details, including what to do if you don't have API credits yet (mock mode).

**Important:** Never commit `.env` to GitHub. It's already excluded via `.gitignore`.

## 5. Run the Application

```
python app.py
```

You should see output like:
```
* Running on http://127.0.0.1:5000
```

Open your browser to **http://127.0.0.1:5000** — you should see the AI Habit Coach homepage confirming the foundation is working.

## 6. Common Setup Issues

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Virtual environment not activated — run `venv\Scripts\activate` first |
| `running scripts is disabled` (PowerShell) | Run the `Set-ExecutionPolicy` command in Step 2 |
| `anthropic.AuthenticationError: invalid x-api-key` | API key was corrupted during copy/paste — delete the old key on console.anthropic.com and create + paste a fresh one carefully |
| `Your credit balance is too low` | No API credits available — the project currently runs in **mock AI mode** (see ENVIRONMENT.md) until credits are added |
| `ModuleNotFoundError: No module named 'ai_coach'` (when running scripts inside `scripts/`) | Run from the project root using `python -m scripts.your_script_name` instead of `python scripts/your_script_name.py`, and ensure `scripts/__init__.py` exists |

## 7. Project Documentation

- `docs/ARCHITECTURE.md` — system architecture and diagrams
- `docs/SCHEMA.md` — database schema
- `docs/API.md` — API endpoint design
- `docs/UI-WIREFRAMES.md` — UI/UX flow and wireframes
- `docs/PROJECT-STRUCTURE.md` — folder structure explanation
- `ENVIRONMENT.md` — environment variables and configuration reference
- `PROJECT_LOG.md` — running log of daily progress
