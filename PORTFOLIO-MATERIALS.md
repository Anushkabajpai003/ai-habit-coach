# AI Habit Coach — Portfolio Materials

_Ready-to-use descriptions, resume bullets, interview talking points, and a demo script for showcasing this project._

---

## Short Project Description (for portfolio site / LinkedIn featured section)

**AI Habit Coach** — a full-stack habit-tracking web app with a built-in AI coach that gives personalized motivation, detects behavioral patterns, and holds coaching conversations. Built solo in 10 days, from requirements through a live production deployment. Live demo: ai-habit-coach.onrender.com

---

## Medium Project Description (for portfolio project page)

AI Habit Coach is a habit-tracking web application that goes beyond simple checkboxes. Instead of just logging whether a habit was completed, it analyzes real check-in history to detect behavioral patterns (like a specific weekday where a habit tends to be skipped) and generates supportive, non-judgmental AI coaching messages in response. Users can also hold a full conversation with the AI coach about their progress.

The project was built end-to-end over a 10-day sprint following a complete software development lifecycle: requirements gathering and PRD writing, system architecture and database design, iterative implementation, a dedicated QA/security hardening pass, UI/UX polish, and a full production deployment with custom domain-ready hosting, environment-based configuration, and a real PostgreSQL database.

Notably, the AI coaching system runs entirely on a free-tier, zero-cost rule-based engine (with a fully-built real Claude API integration path ready to enable), making the entire product free to run and deploy — a deliberate architectural decision to keep the project accessible and sustainable.

**Tech stack:** Python, Flask, SQLAlchemy, PostgreSQL, Jinja2, vanilla CSS/JS, deployed on Render.

---

## Resume Bullet Points

Choose 2-4 depending on the role and resume format:

- Designed and shipped a full-stack Flask web application (AI Habit Coach) end-to-end in a 10-day sprint, from requirements and system architecture through a live production deployment on Render with a PostgreSQL database.
- Built a behavioral pattern-detection engine that analyzes user activity history and generates contextual, AI-driven coaching insights — architected to run entirely free by default while supporting a drop-in real LLM API integration.
- Identified and resolved a cross-site scripting (XSS) vulnerability and a database race condition through deliberate adversarial testing, hardening the application before public deployment.
- Diagnosed and fixed a mobile UI rendering bug using browser DevTools measurement rather than visual inspection, tracing the root cause to an HTML structural issue rather than a CSS-only symptom.
- Implemented a complete CRUD data model with SQLAlchemy ORM, including database-level integrity constraints (unique constraints, cascading deletes) to enforce data consistency beyond application-level validation alone.
- Wrote comprehensive project documentation (architecture, API reference, database schema, setup guides) covering the full development lifecycle of a production web application.

---

## Interview Talking Points

**"Tell me about a project you're proud of."**
Lead with: built a complete AI-powered product solo in 10 days — not just the happy path, but a genuinely production-hardened app. Mention the specific bugs found (XSS, race condition, mobile measurement bug) as evidence of real engineering rigor, not just "it works on my machine."

**"Describe a bug you found and how you fixed it."**
Use the mobile button-sizing bug: two buttons looked "close enough" visually, but instead of guessing, you used DevTools to measure actual computed widths (195px vs 66px), traced the real cause to an HTML structure issue (a wrapping `<form>` element wasn't a properly-sized flex child, not just a CSS tweak), and fixed the actual structural problem. This demonstrates measurement-driven debugging over assumption-driven debugging.

**"How do you handle scope and deadlines?"**
Discuss the mock-AI decision: rather than blocking the entire project on a paid Anthropic API key becoming available, you designed a clean abstraction (`USE_MOCK_AI` flag) that let development continue at full speed with zero cost, while preserving a real upgrade path. This is a genuine engineering tradeoff made under a real constraint, not a shortcut.

**"How do you approach security?"**
Discuss the XSS fix: found that habit names were being interpolated directly into inline JavaScript event handlers, which could allow injected code via a crafted habit name. Fixed by moving data through safe HTML data-attributes and JavaScript event listeners instead of string concatenation into executable code.

**"Walk me through your development process."**
Reference the full lifecycle: PRD → architecture/database/API design → implementation → dedicated QA/security review day → UI polish → deployment → release readiness review → v1.0.0 tag. Emphasize that documentation was generated at every stage, not bolted on at the end.

---

## Short Demo Script (2-3 minutes, for a live walkthrough or recorded video)

**[0:00-0:20] — Hook & Problem**
"Most habit trackers give you a blank checkbox and nothing else. I built AI Habit Coach to test something different — what if the tracker actually understood your patterns and coached you through them?"

**[0:20-0:50] — Core Loop**
[Screen: homepage] "Here's the app live — no login needed. I'll add a habit... and check in." [Click check-in] "Notice it immediately gives me a personalized message based on my actual streak, not a generic 'good job.'"

**[0:50-1:20] — Pattern Insight**
[Point to an existing habit with history] "Here's the more interesting part — this habit has enough history for the app to detect a real pattern. It noticed I tend to miss this habit on Mondays specifically, and gives me a supportive, non-judgmental insight instead of just showing a broken streak."

**[1:20-1:50] — Coach Chat**
[Navigate to Coach] "And if I want to talk it through, there's a full chat interface." [Type a message like "I skipped yesterday, feeling discouraged"] "The coach responds contextually, referencing my real streak data — this isn't scripted per-message, it's rule-based logic reading live data."

**[1:50-2:20] — Engineering Note**
"One thing I'm genuinely proud of: this entire AI layer runs for free. No paid API required by default — I built a rule-based engine that produces varied, contextual responses, with a real Claude API integration path ready to flip on with one line of code if needed."

**[2:20-2:40] — Close**
"Built solo over 10 days — full lifecycle, from requirements to a hardened, deployed production app, including finding and fixing a real security bug along the way. Code and full documentation are on GitHub — link in the description."

---

## Suggested Screenshots / Demo Media

For portfolio use, capture:
1. **Homepage with 2-3 habits**, at least one showing a streak and an AI motivational message
2. **A habit showing a pattern insight** (e.g. the seeded "Demo: Morning Run" habit)
3. **Coach Chat mid-conversation** (2-3 message exchange visible)
4. **Mobile view** of the homepage (proves responsive design was tested, not assumed)
5. **The delete confirmation modal** (shows attention to UX detail/data-safety)
6. Optional: a short (30-60 second) screen recording of the full check-in → AI message → pattern insight → coach chat flow, for a portfolio video reel

---

## Recommended GitHub Topics (already applied Day 9)

`flask` `python` `habit-tracker` `ai` `claude-ai` `sqlalchemy` `postgresql`

Consider adding: `full-stack` `web-app` `render` `capstone-project`
