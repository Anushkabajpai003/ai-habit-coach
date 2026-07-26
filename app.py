"""
AI Habit Coach — Flask application entry point.
"""

import os
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, session
from models import db, Habit, CheckIn
from utils import calculate_streak, already_checked_in_today, detect_pattern
from ai_coach import get_motivational_message, get_pattern_insight, get_coach_reply

app = Flask(__name__)

database_url = os.environ.get('DATABASE_URL', 'sqlite:///habits.db')
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

db.init_app(app)

with app.app_context():
    db.create_all()


def get_habits_summary():
    habits = Habit.query.order_by(Habit.created_at.asc()).all()
    return [{'name': h.name, 'streak': calculate_streak(h)} for h in habits]


@app.route('/')
def home():
    habits = Habit.query.order_by(Habit.created_at.asc()).all()
    habit_data = []
    for habit in habits:
        pattern = detect_pattern(habit)
        insight = get_pattern_insight(habit.name, pattern) if pattern else None
        habit_data.append({
            'id': habit.id,
            'name': habit.name,
            'streak': calculate_streak(habit),
            'checked_in_today': already_checked_in_today(habit),
            'insight': insight,
        })
    ai_message = request.args.get('ai_message')
    ai_habit_id = request.args.get('ai_habit_id')
    return render_template(
        'index.html',
        habits=habit_data,
        ai_message=ai_message,
        ai_habit_id=int(ai_habit_id) if ai_habit_id else None,
    )


@app.route('/habits/new', methods=['POST'])
def add_habit():
    name = request.form.get('name', '').strip()
    if name:
        new_habit = Habit(name=name)
        db.session.add(new_habit)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/habits/<int:habit_id>/delete', methods=['POST'])
def delete_habit(habit_id):
    habit = Habit.query.get(habit_id)
    if habit:
        db.session.delete(habit)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/habits/<int:habit_id>/checkin', methods=['POST'])
def checkin_habit(habit_id):
    habit = Habit.query.get(habit_id)
    if not habit:
        return redirect(url_for('home'))

    today = date.today()
    existing = CheckIn.query.filter_by(habit_id=habit.id, date=today).first()

    if not existing:
        new_checkin = CheckIn(habit_id=habit.id, date=today, done=True)
        db.session.add(new_checkin)
        db.session.commit()

    streak = calculate_streak(habit)
    message = get_motivational_message(habit.name, streak)

    return redirect(url_for('home', ai_message=message, ai_habit_id=habit.id))


@app.route('/habits/<int:habit_id>/uncheck', methods=['POST'])
def uncheck_habit(habit_id):
    today = date.today()
    existing = CheckIn.query.filter_by(habit_id=habit_id, date=today).first()
    if existing:
        db.session.delete(existing)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/coach')
def coach():
    chat_history = session.get('chat_history', [])
    return render_template('coach.html', chat_history=chat_history)


@app.route('/coach/send', methods=['POST'])
def coach_send():
    user_message = request.form.get('message', '').strip()[:500]

    if user_message:
        chat_history = session.get('chat_history', [])
        habits_summary = get_habits_summary()

        reply = get_coach_reply(habits_summary, chat_history, user_message)

        chat_history.append({'role': 'user', 'content': user_message})
        chat_history.append({'role': 'assistant', 'content': reply})

        session['chat_history'] = chat_history[-20:]

    return redirect(url_for('coach'))


@app.route('/coach/clear', methods=['POST'])
def coach_clear():
    session.pop('chat_history', None)
    return redirect(url_for('coach'))


if __name__ == '__main__':
    app.run(debug=True)