# Daily Build Prompt — 30-Day Growth Plan

_Copy this prompt exactly, changing only the day number, and use it once per day throughout the 30-day growth plan. Paste it into a fresh conversation with Claude each day._

---

```
Today is Day [X] of my 30-Day Growth Plan for AI Habit Coach, continuing from my AB Talks 60-Day Claude AI Challenge capstone.

Context: My project's GitHub repo is at https://github.com/Anushkabajpai003/ai-habit-coach and the live app is at https://ai-habit-coach.onrender.com. The full history of how this project was built (Days 1-10 of the original capstone) is documented in challenge-retrospective.md, and the complete 30-day roadmap is in 30-day-growth-plan.md — both are in the repo root. Please read 30-day-growth-plan.md and find the section for "Day [X]" — that is today's scope, and today's scope ONLY. Do not redesign the project or jump ahead to future days.

If you need any project files (models.py, app.py, ai_coach.py, utils.py, templates, docs/, etc.) to see the current state of the code, ask me to upload them before proceeding — do not assume file contents you haven't seen.

Standing rules for today:
- Assume I have limited development experience. Explain concepts briefly before using them.
- Whenever I need to do something outside this chat (installing a package, configuring a service, running a terminal command, deploying, etc.), stop and give me exact, step-by-step instructions with real button/menu names and exact commands. Wait for my confirmation before continuing.
- Prioritize implementation over explanation — most of your response should be complete, production-ready code, not lengthy descriptions.
- Generate complete file contents only — never snippets, placeholders, or "...existing code..." comments. Tell me exactly which file each block belongs in, and whether it's new or replaces an existing file.
- Use only free tools, libraries, and services unless I explicitly say otherwise. Never introduce a paid dependency without asking me first.
- Build one milestone at a time. Pause after each meaningful milestone, deployment step, or whenever something needs my testing/confirmation/screenshot before we continue.
- If something breaks, debug it completely with me before moving forward — don't build on top of broken code.
- Do not scope-creep into tomorrow's work, even if it feels like a natural continuation.

At the end of today's session:
- Confirm everything built today actually works (ask me to test and confirm).
- Help me write a clear, specific git commit message and push today's work to GitHub.
- Note briefly what tomorrow (Day [X+1]) will cover, based on 30-day-growth-plan.md, so I know what to expect.

Let's begin Day [X].
```

---

## Usage Notes

- Replace `[X]` with the actual day number (1 through 30) each time you use this prompt.
- Keep this prompt text itself unchanged across all 30 days — consistency here is what makes each day's session start with the same expectations and guardrails, matching how the original 10-day capstone was run.
- If a day's work naturally needs to reference specific files, upload them at the start of that day's session rather than assuming Claude remembers them from a previous, separate conversation.
