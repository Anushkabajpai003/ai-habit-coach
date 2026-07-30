# Future Scope — AI Habit Coach

_How this specific project could evolve beyond v1.0.0, grounded in the actual architecture and decisions made during the 10-day build._

## Guiding Principle

Every item below builds directly on top of v1.0.0's existing architecture rather than requiring a rewrite. The single-responsibility file structure (`app.py` / `models.py` / `utils.py` / `ai_coach.py`) and the mock-AI abstraction were both deliberately designed on Day 2-3 to make this kind of incremental growth possible without a redesign.

---

## Next 3 Months

**Goal: Move from single-user to multi-user, and from mock AI to real AI, without breaking anything that currently works.**

1. **User accounts & authentication.** Add a `User` model, Flask-Login for session management, and scope every `Habit` query to the logged-in user. This was explicitly deferred in the Day 1 PRD specifically so it could be added later without redesigning the data model — the `Habit` table already has a clean structure for adding a `user_id` foreign key.
2. **Real Claude API integration, made default.** Flip `USE_MOCK_AI = False` in `ai_coach.py` once a funded Anthropic API budget is available, and add usage monitoring/rate limiting per user to control cost at scale. The real-API code paths already exist and were tested during Day 3-7 — this is enabling code, not writing it from scratch.
3. **Persistent chat history.** Currently chat history lives in the Flask session (intentionally, to save build time in the 10-day sprint). Move it to a `ChatMessage` table so coaching conversations persist across devices and sessions, matching how habit data already works.
4. **Habit categories and custom schedules.** Support "3x per week" style targets instead of only daily check-ins, which changes the streak-calculation logic in `utils.py` — a contained, well-isolated change given the current architecture.
5. **Seed the live production database** with a demo habit (extending `scripts/seed_demo_data.py` to run against Postgres) so every new visitor sees pattern insights immediately, not just after a week of real use.

## Next 6 Months

**Goal: Make it a habit tool people actually return to, not just try once.**

6. **Reminders and notifications.** Email or browser push reminders for habits at risk of breaking a streak, using the same `detect_pattern()` weekday data already being computed — the insight logic already knows which days are historically risky for each user.
7. **Weekly AI-generated summary emails.** A digest using the existing `get_pattern_insight()` and `get_motivational_message()` functions, run as a scheduled job (e.g. a Render Cron Job) rather than only on-demand at check-in time.
8. **Data export.** Let users download their check-in history as CSV — straightforward given the existing `CheckIn` model, and a common trust-building feature for any tracking app.
9. **Habit templates / suggested habits.** A curated starting list (exercise, reading, meditation, etc.) to reduce first-use friction, addressing the current "blank textbox" cold-start experience.
10. **A/B test mock vs. real AI messaging** to quantify whether real LLM-generated coaching measurably improves retention or streak length before fully committing to the ongoing API cost at scale.

## Next 12 Months

**Goal: A genuinely differentiated product, not just a polished clone of existing habit trackers.**

11. **AI-suggested goal adjustments (with user approval).** This was explicitly scoped out of v1.0 in the Day 1 PRD as "the AI should suggest, never auto-apply." At this stage, build the suggestion UI: the coach proposes a smaller/different version of a struggling habit, and the user explicitly accepts or declines — preserving user agency while finally delivering on the originally-envisioned fourth AI capability.
12. **Native mobile app or PWA.** Convert the responsive web app into an installable Progressive Web App (manifest + service worker) for a home-screen icon and offline check-in queuing, without needing a full native rewrite.
13. **Team/accountability-partner mode.** Optional shared visibility between two or three users on specific habits (not the current unrestricted shared-database model, but an intentional, opt-in sharing feature) — for people who want a real accountability partner, not just a solo AI coach.
14. **Insight richness beyond weekday patterns.** Extend `detect_pattern()` beyond single-weekday miss-rate detection to include time-of-day patterns (if check-in timestamps are captured), streak-recovery patterns, and multi-habit correlation (e.g. "you tend to also skip Habit B on days you skip Habit A").
15. **Public API.** Expose a documented, authenticated REST API (building on the existing clean route structure) so the habit data could power a companion mobile app, browser extension, or third-party integration in the future.

---

## What Won't Change

Regardless of which of the above gets built, the core architectural decisions from this capstone are expected to remain: Flask + SQLAlchemy as the backend foundation, a clean separation between data (`models.py`), logic (`utils.py`), and AI (`ai_coach.py`), and a commitment to the app remaining usable and testable without requiring a paid API key by default.
