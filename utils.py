"""
Utility functions: streak calculation and pattern detection.
"""

from datetime import date, timedelta
from collections import defaultdict

WEEKDAY_NAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

MIN_CHECKINS_FOR_PATTERN = 7


def calculate_streak(habit):
    """
    Calculates the current streak for a habit.

    The streak is considered "alive" as long as the most recent
    completed check-in was today OR yesterday (the user still has
    until the end of today to keep it going). If the last check-in
    was 2+ days ago, the streak is broken and returns 0.

    Counts backward from the most recent valid day through consecutive
    completed CheckIn records, stopping at the first gap.
    """
    check_in_dates = {c.date for c in habit.check_ins if c.done}

    if not check_in_dates:
        return 0

    today = date.today()
    yesterday = today - timedelta(days=1)

    if today in check_in_dates:
        start_day = today
    elif yesterday in check_in_dates:
        start_day = yesterday
    else:
        return 0

    streak = 0
    current_day = start_day

    while current_day in check_in_dates:
        streak += 1
        current_day -= timedelta(days=1)

    return streak


def already_checked_in_today(habit):
    """Returns True if the habit has a CheckIn record for today."""
    today = date.today()
    return any(c.date == today for c in habit.check_ins)


def detect_pattern(habit):
    """
    Analyzes a habit's check-in history to find the weekday with the
    highest miss rate. Requires at least MIN_CHECKINS_FOR_PATTERN
    total check-in days (done or not) before returning a pattern.

    Returns a dict like:
        {"weekday": "Monday", "missed": 3, "total": 4}
    or None if there isn't enough data yet.
    """
    check_ins = habit.check_ins

    if len(check_ins) < MIN_CHECKINS_FOR_PATTERN:
        return None

    weekday_stats = defaultdict(lambda: {"missed": 0, "total": 0})

    for c in check_ins:
        weekday = WEEKDAY_NAMES[c.date.weekday()]
        weekday_stats[weekday]["total"] += 1
        if not c.done:
            weekday_stats[weekday]["missed"] += 1

    worst_weekday = None
    worst_miss_rate = -1

    for weekday, stats in weekday_stats.items():
        if stats["total"] == 0:
            continue
        miss_rate = stats["missed"] / stats["total"]
        if stats["missed"] > 0 and miss_rate > worst_miss_rate:
            worst_miss_rate = miss_rate
            worst_weekday = weekday

    if worst_weekday is None:
        return None

    stats = weekday_stats[worst_weekday]
    return {
        "weekday": worst_weekday,
        "missed": stats["missed"],
        "total": stats["total"],
    }