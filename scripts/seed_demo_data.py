"""
Seeds a demo habit with 3 weeks of realistic check-in history,
including a deliberate pattern (frequently missed Mondays),
so the pattern detection and AI insight features can be tested
without waiting real weeks.

Run from the project root:
    python -m scripts.seed_demo_data
"""

import random
from datetime import date, timedelta

from app import app
from models import db, Habit, CheckIn

DEMO_HABIT_NAME = "Demo: Morning Run"
DAYS_OF_HISTORY = 21


def seed():
    with app.app_context():
        existing = Habit.query.filter_by(name=DEMO_HABIT_NAME).first()
        if existing:
            db.session.delete(existing)
            db.session.commit()
            print(f"Removed old '{DEMO_HABIT_NAME}' habit before reseeding.")

        habit = Habit(name=DEMO_HABIT_NAME)
        db.session.add(habit)
        db.session.commit()

        today = date.today()

        for days_ago in range(DAYS_OF_HISTORY, 0, -1):
            check_date = today - timedelta(days=days_ago)
            weekday = check_date.weekday()  # 0 = Monday

            if weekday == 0:
                # Monday: mostly missed (deliberate pattern for demo)
                done = random.random() < 0.2
            else:
                # Other days: mostly completed
                done = random.random() < 0.85

            check_in = CheckIn(habit_id=habit.id, date=check_date, done=done)
            db.session.add(check_in)

        db.session.commit()
        print(f"Seeded '{DEMO_HABIT_NAME}' with {DAYS_OF_HISTORY} days of history.")
        print("Restart the app (if not already running) and refresh the homepage to see it.")


if __name__ == "__main__":
    seed()