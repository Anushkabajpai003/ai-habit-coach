# AI Habit Coach — Database Schema

_Day 2 Deliverable. Implements the data layer for models.py, built on Day 3._

## Tables

### `habit`

| Field | Type | Constraints |
|---|---|---|
| id | Integer | Primary Key, autoincrement |
| name | String(100) | Not null |
| created_at | DateTime | Default: current UTC time |

### `check_in`

| Field | Type | Constraints |
|---|---|---|
| id | Integer | Primary Key, autoincrement |
| habit_id | Integer | Foreign Key → habit.id, Not null |
| date | Date | Not null |
| done | Boolean | Default: True |

**Added constraint (Day 2 improvement):** `UNIQUE(habit_id, date)` — enforces one check-in per habit per day at the database level, not just in application logic. This directly supports Day 4's duplicate-check-in prevention and Day 9's rapid-click edge case testing.

## Relationships

- One `Habit` → Many `CheckIn` (one-to-many via `habit_id` foreign key)
- Deleting a `Habit` cascades to delete all its associated `CheckIn` records (`cascade="all, delete-orphan"` in SQLAlchemy relationship definition)

## Example SQLAlchemy Model Sketch (for Day 3, not implemented yet)

```python
class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    check_ins = db.relationship('CheckIn', backref='habit', cascade="all, delete-orphan")

class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    done = db.Column(db.Boolean, default=True)
    __table_args__ = (db.UniqueConstraint('habit_id', 'date', name='uq_habit_date'),)
```

## Schema Validation Against PRD User Stories

| User Story | Supported By |
|---|---|
| US-1: Add a habit by name | `habit.name` |
| US-2: Daily yes/no check-in | One `check_in` row per (habit_id, date) |
| US-3: See current streak | Computed from consecutive `check_in` rows — no extra field needed |
| US-4: Motivational message after check-in | Uses `habit` + `check_in` data as prompt context; response is ephemeral (not stored) |
| US-5: Pattern insight (e.g. weekday misses) | Computed by grouping `check_in.date` by weekday |
| US-6: Coach chat | Handled via Flask session (Blueprint Day 7 decision) — intentionally not a database table, to save build time in v1.0 |
| US-7: Cross-device persistence | Shared PostgreSQL database, no per-device or per-user partitioning |
| US-8: No signup required | No `user` table exists — correct for single-user v1.0 scope |

**Conclusion:** schema fully supports every in-scope user story with no gaps. No additional tables needed for v1.0.

## Future Scope (Not Built Now)

- A `user` table with authentication, once accounts are introduced (post-v1.0).
- A `chat_message` table if persistent (not session-only) chat history becomes a requirement later.
- Fields for habit categories/schedules if that future-scope feature is picked up.
