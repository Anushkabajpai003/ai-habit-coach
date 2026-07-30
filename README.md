# AI Habit Coach

A habit-tracking web app with a built-in AI coach — get personalized motivation, spot behavioral patterns, and talk through your progress with a supportive AI, all in a clean, simple interface.

**Live demo:** https://ai-habit-coach.onrender.com
*(Free-tier hosting — the app may take 30-50 seconds to wake up if it hasn't been visited recently.)*

Built as a 10-day capstone project for the **AB Talks 60-Day Claude AI Challenge**, taking the product from a blank page through requirements, design, implementation, testing, and a production deployment — a complete software development lifecycle.

![Version](https://img.shields.io/badge/version-1.0.0-02545C)
![Python](https://img.shields.io/badge/python-3.10+-028090)
![Flask](https://img.shields.io/badge/flask-3.x-02C39A)
![License](https://img.shields.io/badge/license-MIT-00A896)

---

## Why This Project

Most habit trackers log data and stop there — a blank checkbox with no insight into *why* a streak breaks. AI Habit Coach was built to test a different idea: what if the tracker actually noticed your patterns and responded like a coach, not a spreadsheet? The result is a fully working product with real behavioral pattern detection, contextual AI coaching, and zero ongoing cost to run.

## What It Does

- **Track any habit** — add habits by name, no setup or configuration required
- **Daily check-ins** — simple one-tap yes/no tracking with automatic streak calculation, including correct "grace period" logic (a streak from yesterday still shows as alive until the day is over)
- **AI motivational messages** — a short, personalized message after every check-in, based on real streak data
- **Pattern insights** — detects behavioral patterns (e.g. "you tend to miss Mondays") from real check-in history and turns them into supportive, actionable insights
- **AI Coach Chat** — a conversational interface to talk through progress, motivation, or setbacks
- **No login required** — open the app and start immediately; data syncs via a shared cloud database

## Screenshots

| Home — Habit Tracking |
![Home](<docs/screenshots/Screenshot 2026-07-27 164519.png>) 

|Coach Chat |
![coach chat](<docs/screenshots/Screenshot 2026-07-27 165125.png>)

| Habit list with streaks, AI motivational messages, and pattern insights |
![habits](<docs/screenshots/Screenshot 2026-07-29 141838.png>)

| Contextual, conversational AI coaching |

![demo](<docs/screenshots/Screenshot 2026-07-28 132023.png>)


## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | PostgreSQL (production), SQLite (local development) |
| ORM | SQLAlchemy (Flask-SQLAlchemy) |
| AI | Rule-based mock AI system (free, zero-cost) with a fully-implemented real Claude API integration path |
| Frontend | Server-rendered Jinja2 templates, vanilla CSS/JS |
| Hosting | Render.com (free tier) |

**Why a mock AI system?** This project is built entirely on free-tier tools by design. Rather than requiring a paid Anthropic API key, the AI coaching features (motivational messages, pattern insights, chat replies) run on a rule-based system that produces varied, contextual responses using real user data (streaks, habit names, detected patterns) — with zero API cost. A fully-implemented real Claude API integration path already exists in `ai_coach.py` and can be enabled with a single flag change (`USE_MOCK_AI = False`) if API credits become available.

## Engineering Highlights

A few specific problems solved during the build, beyond just "making it work":

- **Fixed a real security vulnerability:** habit names were originally interpolated directly into inline JavaScript (`onclick="..."`), creating an XSS injection risk via crafted input (e.g. names containing quotes or backslashes). Resolved by moving data into safe HTML attributes and binding event listeners in JavaScript instead.
- **Fixed a database race condition:** rapid double-submission of the same habit name could bypass the application-level duplicate check and create two records before either finished saving. Resolved with a database-level `UNIQUE` constraint as the authoritative guarantee, with graceful `IntegrityError` handling at the application layer.
- **Diagnosed a mobile layout bug via measurement, not guesswork:** two buttons that looked "close enough" were measured via browser DevTools to be nearly 3x different in width. Root cause was an HTML structure issue (a wrapping `<form>` element wasn't sized correctly as a flex child) — fixed at the structural level, not patched with CSS overrides.
- **Corrected streak-calculation logic** so a habit's streak reflects reality the moment the app is opened (accounting for a same-day "grace period"), rather than incorrectly showing "0" until the user takes a new action.

Full day-by-day technical decisions and debugging logs are documented in [`docs/`](docs/) and [`challenge-retrospective.md`](challenge-retrospective.md).

## Getting Started Locally

### Prerequisites
- Python 3.10 or later
- Git

### Setup

```bash
git clone https://github.com/Anushkabajpai003/ai-habit-coach.git
cd ai-habit-coach

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

Copy `.env.example` to `.env` — the app runs fully in free mock-AI mode with no external API key required.

```bash
python app.py
```

Visit **http://127.0.0.1:5000** in your browser.

Full setup details, troubleshooting, and environment variable documentation: see [`docs/SETUP.md`](docs/SETUP.md) and [`docs/ENVIRONMENT.md`](docs/ENVIRONMENT.md).

## Project Documentation

This project was built following a full software development lifecycle, with documentation generated at each stage:

| Document | Description |
|---|---|
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | System architecture, component diagrams, request lifecycle |
| [`docs/SCHEMA.md`](docs/SCHEMA.md) | Database schema and design decisions |
| [`docs/API.md`](docs/API.md) | Full API endpoint reference |
| [`docs/UI-WIREFRAMES.md`](docs/UI-WIREFRAMES.md) | User flow and wireframes |
| [`docs/PROJECT-STRUCTURE.md`](docs/PROJECT-STRUCTURE.md) | Folder structure and file responsibilities |
| [`docs/SETUP.md`](docs/SETUP.md) | Local installation guide |
| [`docs/ENVIRONMENT.md`](docs/ENVIRONMENT.md) | Environment variables and configuration reference |
| [`docs/DAY3-SUMMARY.md`](docs/DAY3-SUMMARY.md) → [`docs/DAY9-SUMMARY.md`](docs/DAY9-SUMMARY.md) | Daily development logs: implementation, bugs found and fixed, testing performed |
| [`challenge-retrospective.md`](challenge-retrospective.md) | Full Day 1-10 journey, technical decisions, and lessons learned |
| [`future-scope.md`](future-scope.md) | 3/6/12-month product evolution roadmap |
| [`30-day-growth-plan.md`](30-day-growth-plan.md) | Day-by-day plan to grow this MVP into a more complete product |

## Project Structure

```
ai-habit-coach/
├── app.py                  # Flask routes and application entry point
├── models.py                # Database models (Habit, CheckIn)
├── utils.py                 # Streak calculation and pattern detection logic
├── ai_coach.py                # AI coaching logic (mock + real API paths)
├── templates/                # HTML templates
├── static/                   # CSS, favicon
├── scripts/                  # Utility scripts (demo data seeding, etc.)
├── docs/                     # Full project documentation
└── requirements.txt
```

See [`docs/PROJECT-STRUCTURE.md`](docs/PROJECT-STRUCTURE.md) for full details.

## Known Limitations (v1.0.0)

Documented and intentional, not oversights:

- **Single-user mode:** no login/accounts — all visitors share the same habit list. A deliberate scope decision to fit a 10-day build; multi-user accounts are planned (see [`future-scope.md`](future-scope.md)).
- **Free-tier hosting:** the live demo may take 30-50 seconds to respond after periods of inactivity (Render's free-tier "cold start" behavior).
- **Mock AI by default:** AI responses are rule-based rather than powered by a live LLM API call, to keep the project fully free to run.

## License

MIT License — see [`LICENSE`](LICENSE) for details.

## Acknowledgments

Built with Claude as part of the **AB Talks 60-Day Claude AI Challenge**.
