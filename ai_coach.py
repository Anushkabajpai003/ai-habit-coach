"""
AI Coach module — handles all Claude API interactions.

MOCK MODE: Currently using simulated/rule-based responses instead of
real Claude API calls, since API credits are not yet set up.
To switch to real Claude API later: set USE_MOCK_AI = False below,
and ensure ANTHROPIC_API_KEY is set in .env with available credits.
"""

import os
import random
from dotenv import load_dotenv

load_dotenv()

USE_MOCK_AI = True  # Flip to False once real Claude API credits are available


def get_motivational_message(habit_name, streak):
    """Returns a short motivational message based on habit name and streak."""
    if USE_MOCK_AI:
        return _mock_motivational_message(habit_name, streak)
    else:
        return _real_motivational_message(habit_name, streak)


def _mock_motivational_message(habit_name, streak):
    if streak == 0:
        messages = [
            f"Every '{habit_name}' journey starts with day one. You've got this!",
            f"Today is the perfect day to start '{habit_name}'. One step at a time.",
        ]
    elif streak < 5:
        messages = [
            f"{streak} days of '{habit_name}' — the momentum is building!",
            f"Nice work! {streak} days in on '{habit_name}'. Keep it going.",
        ]
    else:
        messages = [
            f"{streak} days strong on '{habit_name}' — that's real consistency!",
            f"Wow, {streak} days of '{habit_name}'. You're building something lasting.",
        ]
    return random.choice(messages)


def _real_motivational_message(habit_name, streak):
    """Placeholder for real Claude API call — implemented when credits are available."""
    from anthropic import Anthropic
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    prompt = (
        f"The user just checked in on their habit '{habit_name}'. "
        f"Their current streak is {streak} days. Write one short (1-2 sentence), "
        f"warm, specific, non-cheesy motivational message."
    )
    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=100,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except Exception:
        return _mock_motivational_message(habit_name, streak)