# AI Habit Coach — Project Structure

_Day 2 Deliverable. This is the folder layout every future day builds into._

```
ai-habit-coach/
│
├── app.py                 # Flask app entry point; all routes defined/imported here
├── models.py               # SQLAlchemy models: Habit, CheckIn
├── utils.py                # Streak calculation + pattern detection logic
├── ai_coach.py              # All Claude API calls (motivation, insight, chat)
├── requirements.txt        # Python dependencies
├── .env                     # Local secrets (API key, DB URL) — never committed
├── .gitignore               # Excludes .env, venv/, __pycache__, *.db
├── Procfile                 # Production start command (added Day 10)
│
├── templates/               # Jinja2 HTML templates
│   ├── index.html           # Homepage (habit list, check-in, AI messages)
│   ├── coach.html           # Coach chat page
│   └── error.html           # Friendly fallback error page (added Day 9)
│
├── static/                  # CSS, JS, any static assets
│   └── style.css            # All app styling (polished Day 8)
│
├── scripts/                 # One-off utility scripts, not part of the running app
│   ├── test_claude.py       # Day 2 — verifies Claude API connection
│   └── seed_demo_data.py    # Day 6 — inserts demo habit history for testing/demo
│
├── docs/                    # Design deliverables (this folder)
│   ├── ARCHITECTURE.md
│   ├── SCHEMA.md
│   ├── API.md
│   ├── UI-WIREFRAMES.md
│   └── PROJECT-STRUCTURE.md
│
└── README.md
```

## Responsibility of Each Major Folder/File

- **`app.py`** — the only place Flask routes live. Keeps request handling centralized and easy to scan.
- **`models.py`** — the only place database schema/models live. Anything touching the DB shape goes here.
- **`utils.py`** — pure logic functions (streak calculation, pattern detection) that don't touch Flask or the AI API directly — easy to test in isolation.
- **`ai_coach.py`** — the only place that talks to the Claude API. Keeps all prompt-engineering and API-error-handling in one file, so debugging AI behavior never requires searching through route code.
- **`templates/`** — all user-facing HTML. Kept separate from Python logic per Flask convention.
- **`static/`** — CSS and any future JS/images. No logic lives here.
- **`scripts/`** — anything run manually/independently of the live app (API test, demo data seeding). Never imported by `app.py`.
- **`docs/`** — living design documentation, version-controlled with the code so it's always in sync with what's actually built.

## Why This Structure

- **One file, one responsibility** — when adding a feature, there's never ambiguity about which file to open.
- **No premature framework/folder complexity** — no `/blueprints`, `/services`, `/controllers` layers that a solo 1–2 hr/day build doesn't need yet.
- **Future-proof without over-building** — if the project grows post-v1.0 (e.g. real accounts), this structure can evolve (e.g. `models.py` splits into a `models/` package) without a rewrite.

## Where Future Code Will Live

| Day | What Gets Added | Where |
|---|---|---|
| Day 3 | Habit CRUD routes + models | `app.py`, `models.py`, `templates/index.html` |
| Day 4 | Check-in + streak logic | `utils.py`, `app.py` |
| Day 5 | Motivational messages | `ai_coach.py`, `app.py` |
| Day 6 | Pattern detection + insights | `utils.py`, `ai_coach.py`, `scripts/seed_demo_data.py` |
| Day 7 | Coach chat | `ai_coach.py`, `app.py`, `templates/coach.html` |
| Day 8 | UI polish | `static/style.css`, both templates |
| Day 9 | Testing/hardening | All files as needed, `templates/error.html` |
| Day 10 | Deployment | `Procfile`, `requirements.txt`, environment config |
