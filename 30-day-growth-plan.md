# 30-Day Growth Plan — AI Habit Coach

_A realistic, day-by-day roadmap transforming the v1.0.0 MVP into a significantly more complete product. Each day builds directly on the previous one and assumes the same 1-2 hour/day pace used during the original 10-day sprint. Adapted specifically to this project's actual stack (Flask, SQLAlchemy, PostgreSQL, Render) and its real, documented future-scope priorities._

**How to use this plan:** Use the accompanying `daily-build-prompt.md` each day, changing only the day number. Do not skip ahead — each day assumes the previous day's work is committed and working.

---

## Week 1 (Days 1-7): User Accounts Foundation

- **Day 1:** Add a `User` model to `models.py` (id, username, password_hash, created_at). Install Flask-Login. Do not wire up routes yet — just the model and a migration script to create the table.
- **Day 2:** Build signup and login routes/templates. Hash passwords with Werkzeug's `generate_password_hash`. Test creating and logging into an account locally.
- **Day 3:** Add a `user_id` foreign key to the `Habit` model. Update every habit query in `app.py` to filter by `current_user.id`. Test that two different accounts see two different habit lists.
- **Day 4:** Add logout functionality and route protection (`@login_required`) on all habit/coach routes. Test that a logged-out visitor is redirected to login.
- **Day 5:** Migrate existing shared demo data (if desired) to a specific "demo" account, so the live site's existing habits aren't orphaned when auth goes live.
- **Day 6:** Update `docs/SCHEMA.md`, `docs/API.md`, and the README to reflect the new authenticated architecture.
- **Day 7:** Deploy the authenticated version to Render (staging first if possible), test the full signup → login → habit → logout flow live, then merge to production.

## Week 2 (Days 8-14): Real AI + Persistent Chat

- **Day 8:** Add Anthropic API credits (small amount, e.g. $5) if budget allows. Flip `USE_MOCK_AI = False` in `ai_coach.py` and test real motivational messages locally.
- **Day 9:** Test real AI pattern insights and coach chat replies locally; compare quality/tone against the mock versions.
- **Day 10:** Add basic per-user rate limiting on AI calls (e.g. max N messages/hour) to control API cost at scale.
- **Day 11:** Create a `ChatMessage` model (id, user_id, role, content, created_at) to persist chat history instead of using Flask sessions.
- **Day 12:** Update `/coach` and `/coach/send` routes to read/write from the database instead of `session['chat_history']`.
- **Day 13:** Test that chat history now persists across logout/login and across devices for the same account.
- **Day 14:** Deploy real-AI + persistent-chat version to production. Update environment variables on Render (real `ANTHROPIC_API_KEY`). Test live.

## Week 3 (Days 15-21): Retention Features

- **Day 15:** Add a `reminder_time` optional field to the `Habit` model (nullable, for future use).
- **Day 16:** Set up a scheduled job (Render Cron Job or APScheduler) that runs once daily.
- **Day 17:** Build the logic for the daily job: for each user with habits at risk (based on existing `detect_pattern()` weekday data), prepare a reminder message.
- **Day 18:** Wire up email sending (e.g. via a free-tier transactional email service) for the daily reminder job.
- **Day 19:** Build a CSV export route (`/habits/export`) using the existing `CheckIn` model — straightforward given the current schema.
- **Day 20:** Add a simple "suggested habits" list (5-10 common habits) shown on the empty state instead of just a blank input, to reduce first-use friction.
- **Day 21:** Deploy and test all Week 3 features live: reminders, export, suggested habits.

## Week 4 (Days 22-30): Insight Depth + Polish + Public Launch Prep

- **Day 22:** Extend `CheckIn` model with an optional `time_of_day` field (captured at check-in time) to enable richer future insights.
- **Day 23:** Extend `detect_pattern()` in `utils.py` to also detect time-of-day patterns, not just weekday patterns, using the new field.
- **Day 24:** Add a "best streak ever" field/display per habit (separate from current streak), using existing `CheckIn` history — a small, high-value addition.
- **Day 25:** Add basic in-app onboarding (a one-time welcome message/tooltip for first-time users) explaining the three AI features.
- **Day 26:** Full accessibility re-audit (screen reader testing if possible, color contrast check) now that auth and new features have added new UI surfaces.
- **Day 27:** Full mobile re-test of every new feature added this month (auth screens, export, reminders settings) — using the same DevTools-measurement discipline from the original Day 8 review.
- **Day 28:** Update all documentation (`README.md`, `docs/`, `future-scope.md`) to reflect the new v1.1.0 feature set.
- **Day 29:** Full end-to-end regression walkthrough of the entire app — every feature from v1.0.0 plus everything added this month.
- **Day 30:** Tag and release **v1.1.0** on GitHub with a changelog summarizing the month's work (auth, real AI, persistent chat, reminders, export, richer insights). Write a "one month later" LinkedIn post reflecting on the growth from v1.0.0 to v1.1.0.

---

## Success Criteria for This 30-Day Plan

By Day 30, AI Habit Coach should have: real user accounts, real Claude API-powered coaching (not mock), persistent cross-device chat history, email reminders, data export, and richer AI insights — while remaining true to the same core identity established in the original 10-day sprint: simple, honest, and genuinely useful.
