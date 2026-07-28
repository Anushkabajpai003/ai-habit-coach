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


def get_coach_reply(habits_summary, chat_history, user_message):
    """Returns a coach reply to a chat message, given habit context and history."""
    if USE_MOCK_AI:
        return _mock_coach_reply(habits_summary, chat_history, user_message)
    else:
        return _real_coach_reply(habits_summary, chat_history, user_message)


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
    weekday = pattern.get("weekday", "that day")
    missed = pattern.get("missed", 0)
    total = pattern.get("total", 0)

    templates = [
        f"You've missed '{habit_name}' on {weekday} {missed} out of {total} times recently. "
        f"{weekday}s might just need a smaller version of this habit, or a different time of day — no judgment, just data.",

        f"Here's something worth noticing: {weekday} seems to be the toughest day for '{habit_name}'. "
        f"That's really common — maybe plan something lighter for {weekday}s so the streak has a better shot.",

        f"Looks like {weekday} is where '{habit_name}' tends to slip ({missed}/{total} times). "
        f"That's not failure, that's useful information — you now know exactly where to focus.",
    ]
    return random.choice(templates)


def _mock_coach_reply(habits_summary, chat_history, user_message):
    """
    Rule-based, keyword-aware coach reply. Looks at the user's message
    for emotional/topical cues and responds accordingly, referencing
    real habit data when relevant. Defensive against missing/malformed
    habit summary data.
    """
    text = (user_message or "").lower()

    habit_line = ""
    if habits_summary and isinstance(habits_summary, list) and len(habits_summary) > 0:
        top = habits_summary[0]
        name = top.get('name', 'your habit')
        streak = top.get('streak', 0)
        habit_line = f" I can see you're at a {streak}-{_day_word(streak)} streak on '{name}' right now."

    if any(word in text for word in ["skip", "miss", "fail", "didn't", "couldn't", "bad"]):
        replies = [
            f"That's okay — one missed day doesn't erase your progress.{habit_line} What made today harder than usual?",
            f"Missing a day happens to everyone building a habit.{habit_line} The important part is coming back, which you're doing right now by checking in here.",
        ]
    elif any(word in text for word in ["tired", "hard", "difficult", "struggl", "overwhelmed", "stress"]):
        replies = [
            f"It sounds like things are genuinely tough right now.{habit_line} Sometimes the goal isn't to do more — it's to just not lose the thread completely. Even a tiny version of the habit counts.",
            "That's a real feeling, not a character flaw. What would make tomorrow 10% easier than today?",
        ]
    elif any(word in text for word in ["good", "great", "proud", "happy", "excited", "did it", "done"]):
        replies = [
            f"That's genuinely great to hear!{habit_line} Momentum like this is worth noticing — what's been working for you?",
            "Love that. Consistency is built exactly from days like this one.",
        ]
    elif any(word in text for word in ["why", "how", "help", "advice", "suggest"]):
        replies = [
            f"Happy to help think it through.{habit_line} What's the specific part that feels stuck right now?",
            "Good question — habits usually break down at a specific moment in the day. When does yours tend to slip?",
        ]
    elif any(word in text for word in ["habit", "sport", "exercise", "run", "walk", "read", "meditat", "gym", "workout", "added", "new"]):
        replies = [
            f"Nice — building that into your routine takes real intention.{habit_line} What's your plan for staying consistent with it?",
            f"Great choice of habit.{habit_line} What time of day feels most realistic for you to actually do it?",
            f"That's a solid one to build.{habit_line} What's usually the biggest thing that gets in the way when you try?",
        ]
    else:
        replies = [
            f"Thanks for sharing that.{habit_line} How are you feeling about your progress overall?",
            "I hear you. Tell me a bit more about what's on your mind with your habits right now.",
            f"Got it.{habit_line} Is there anything specific you'd like help thinking through today?",
            "Appreciate you checking in here. What's on your mind about your habits today?",
        ]

    return random.choice(replies)


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


def _real_coach_reply(habits_summary, chat_history, user_message):
    """Placeholder for real Claude API call — implemented when credits are available."""
    from anthropic import Anthropic
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    habits_text = ", ".join(
        f"{h['name']} ({h['streak']} day streak)" for h in habits_summary
    ) or "no habits tracked yet"

    system_prompt = (
        f"You are a warm, supportive habit-building coach. The user's current habits: {habits_text}. "
        f"Keep replies short (1-3 sentences), specific, and non-judgmental."
    )

    messages = []
    for turn in chat_history[-10:]:
        messages.append({"role": turn["role"], "content": turn["content"]})
    messages.append({"role": "user", "content": user_message})

    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=150,
            system=system_prompt,
            messages=messages,
        )
        return response.content[0].text
    except Exception:
        return _mock_coach_reply(habits_summary, chat_history, user_message)