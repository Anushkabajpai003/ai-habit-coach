"""
Database models for AI Habit Coach.
Defines the Habit and CheckIn tables using SQLAlchemy.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    check_ins = db.relationship(
        'CheckIn', backref='habit', cascade='all, delete-orphan'
    )


class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    done = db.Column(db.Boolean, default=True)

    __table_args__ = (
        db.UniqueConstraint('habit_id', 'date', name='uq_habit_date'),
    )