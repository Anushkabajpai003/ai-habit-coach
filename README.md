# AI Habit Coach

A habit-tracking web app with a built-in AI coach — get personalized motivation, spot behavioral patterns, and talk through your progress with a supportive AI, all in a clean, simple interface.

**Live demo:** https://ai-habit-coach.onrender.com
*(Free-tier hosting — the app may take 30-50 seconds to wake up if it hasn't been visited recently.)*

Built as a 10-day capstone project for the **AB Talks 60-Day Claude AI Challenge**.

---

## What It Does

- **Track any habit** — add habits by name, no setup or configuration required
- **Daily check-ins** — simple one-tap yes/no tracking with automatic streak calculation
- **AI motivational messages** — get a short, personalized message after every check-in
- **Pattern insights** — the app detects behavioral patterns (e.g. "you tend to miss Mondays") and turns them into supportive, actionable insights
- **AI Coach Chat** — talk through your progress, motivation, or setbacks with a conversational AI coach
- **No login required** — open the app and start immediately; works across devices via a shared cloud database

## Screenshots

| Home | Coach Chat |
|---|---|
| Habit list with streaks, AI messages, and pattern insights | Conversational AI coaching interface |

*(See `docs/` for detailed wireframes and design documentation.)*

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | PostgreSQL (production), SQLite (local development) |
| ORM | SQLAlchemy (Flask-SQLAlchemy) |
| AI | Rule-based mock AI system (free, zero-cost) with an optional real Claude API integration path |
| Frontend | Server-rendered Jinja2 templates, vanilla CSS/JS |
| Hosting | Render.com (free tier) |

**Why a mock AI system?** This project is built entirely on free-tier tools. Rather than requiring a paid Anthropic API key, the AI coaching features (motivational messages, pattern insights, chat replies) run on a rule-based system that produces varied, contextual responses using real user data (streaks, habit names, detected patterns) — with zero API cost. A fully-implemented real Claude API integration path exists in `ai_coach.py` and can be enabled with a single flag change (`USE_MOCK_AI = False`) if API credits become available.

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

Copy `.env.example` to `.env` and fill in values (see `.env.example` for what's needed — the app runs fully in free mock-AI mode with no external API key required).

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
| [`docs/DAY3-SUMMARY.md`](docs/DAY3-SUMMARY.md) through [`docs/DAY8-SUMMARY.md`](docs/DAY8-SUMMARY.md) | Daily development logs covering implementation, bugs found and fixed, and testing performed |

## Project Structure

ai-habit-coach/
├── app.py # Flask routes and application entry point
├── models.py # Database models (Habit, CheckIn)
├── utils.py # Streak calculation and pattern detection logic
├── ai_coach.py # AI coaching logic (mock + real API paths)
├── templates/ # HTML templates
├── static/ # CSS
├── scripts/ # Utility scripts (demo data seeding, etc.)
├── docs/ # Full project documentation
└── requirements.txt

See [`docs/PROJECT-STRUCTURE.md`](docs/PROJECT-STRUCTURE.md) for full details.

## Known Limitations (v1.0)

This is a v1.0 capstone project with intentionally scoped limitations, documented from the earliest planning stage:

- **Single-user mode:** no login/accounts — all visitors share the same habit list. This was a deliberate scope decision to fit a 10-day build; multi-user accounts are documented future scope.
- **Free-tier hosting:** the live demo may take 30-50 seconds to respond after periods of inactivity (Render's free-tier "cold start" behavior).
- **Mock AI by default:** AI responses are rule-based rather than powered by a live LLM API call, to keep the project fully free to run. See the Tech Stack section above for how to enable real Claude API integration.

## License

This project is licensed under the MIT License — see [`LICENSE`](LICENSE) for details.

## Acknowledgments

Built with Claude as part of the **AB Talks 60-Day Claude AI Challenge**.