"""
AI Coach module — handles all AI-generated coaching content.

MOCK MODE: Currently using simulated/rule-based responses instead of
real Claude API calls, so this works with zero API cost and no API key
required. To switch to real Claude API later: set USE_MOCK_AI = False
below, and ensure ANTHROPIC_API_KEY is set in .env with available credits.
"""

import os
import random
from dotenv import load_dotenv

load_dotenv()

USE_MOCK_AI = True  # Flip to False only if you have Anthropic API credits available


def get_motivational_message(habit_name, streak):
    """Returns a short motivational message based on habit name and streak."""
    if USE_MOCK_AI:
        return _mock_motivational_message(habit_name, streak)
    else:
        return _real_motivational_message(habit_name, streak)


def get_pattern_insight(habit_name, pattern):
    """Returns a short, supportive insight message based on a detected pattern."""
    if USE_MOCK_AI:
        return _mock_pattern_insight(habit_name, pattern)
    else:
        return _real_pattern_insight(habit_name, pattern)


def _day_word(streak):
    return "day" if streak == 1 else "days"


def _mock_motivational_message(habit_name, streak):
    word = _day_word(streak)
    if streak == 0:
        messages = [
            f"Every '{habit_name}' journey starts with day one. You've got this!",
            f"Today is the perfect day to start '{habit_name}'. One step at a time.",
        ]
    elif streak < 5:
        messages = [
            f"{streak} {word} of '{habit_name}' — the momentum is building!",
            f"Nice work! {streak} {word} in on '{habit_name}'. Keep it going.",
        ]
    else:
        messages = [
            f"{streak} {word} strong on '{habit_name}' — that's real consistency!",
            f"Wow, {streak} {word} of '{habit_name}'. You're building something lasting.",
        ]
    return random.choice(messages)


def _mock_pattern_insight(habit_name, pattern):
    weekday = pattern["weekday"]
    missed = pattern["missed"]
    total = pattern["total"]

    templates = [
        f"You've missed '{habit_name}' on {weekday} {missed} out of {total} times recently. "
        f"{weekday}s might just need a smaller version of this habit, or a different time of day — no judgment, just data.",

        f"Here's something worth noticing: {weekday} seems to be the toughest day for '{habit_name}'. "
        f"That's really common — maybe plan something lighter for {weekday}s so the streak has a better shot.",

        f"Looks like {weekday} is where '{habit_name}' tends to slip ({missed}/{total} times). "
        f"That's not failure, that's useful information — you now know exactly where to focus.",
    ]
    return random.choice(templates)


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


def _real_pattern_insight(habit_name, pattern):
    """Placeholder for real Claude API call — implemented when credits are available."""
    from anthropic import Anthropic
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    prompt = (
        f"A user has been tracking the habit '{habit_name}'. Data shows they miss it "
        f"on {pattern['weekday']} {pattern['missed']} out of {pattern['total']} times. "
        f"Write one short (1-2 sentence), supportive, non-judgmental insight about this pattern, "
        f"and gently suggest a reframe."
    )
    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=120,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text
    except Exception:
        return _mock_pattern_insight(habit_name, pattern)