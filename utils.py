"""
Utility functions: streak calculation and pattern detection.
"""

from datetime import date, timedelta


def calculate_streak(habit):
    """
    Calculates the current consecutive-day streak for a habit.
    Counts backward from today through CheckIn records where done=True,
    stopping at the first missed day.
    """
    check_in_dates = {c.date for c in habit.check_ins if c.done}

    if not check_in_dates:
        return 0

    streak = 0
    current_day = date.today()

    while current_day in check_in_dates:
        streak += 1
        current_day -= timedelta(days=1)

    return streak


def already_checked_in_today(habit):
    """Returns True if the habit has a CheckIn record for today."""
    today = date.today()
    return any(c.date == today for c in habit.check_ins)