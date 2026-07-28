"""
AI Habit Coach — Flask application entry point.
"""

import os
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, session, flash
from sqlalchemy.exc import IntegrityError
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
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024

db.init_app(app)

with app.app_context():
    db.create_all()

MAX_CHAT_TURNS = 12


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
    if not name:
        flash("Habit name can't be empty.")
        return redirect(url_for('home'))
    if len(name) > 100:
        flash("Habit name is too long (max 100 characters).")
        return redirect(url_for('home'))

    existing = Habit.query.filter(db.func.lower(Habit.name) == name.lower()).first()
    if existing:
        flash(f"You already have a habit called '{name}'.")
        return redirect(url_for('home'))

    try:
        new_habit = Habit(name=name)
        db.session.add(new_habit)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        flash("That habit couldn't be added — please try again.")

    return redirect(url_for('home'))


@app.route('/habits/<int:habit_id>/delete', methods=['POST'])
def delete_habit(habit_id):
    habit = Habit.query.get(habit_id)
    if habit:
        habit_name = habit.name
        db.session.delete(habit)
        db.session.commit()
        flash(f"Deleted '{habit_name}'.")
    else:
        flash("That habit no longer exists.")
    return redirect(url_for('home'))


@app.route('/habits/<int:habit_id>/checkin', methods=['POST'])
def checkin_habit(habit_id):
    habit = Habit.query.get(habit_id)
    if not habit:
        flash("That habit no longer exists.")
        return redirect(url_for('home'))

    today = date.today()
    existing = CheckIn.query.filter_by(habit_id=habit.id, date=today).first()

    if not existing:
        try:
            new_checkin = CheckIn(habit_id=habit.id, date=today, done=True)
            db.session.add(new_checkin)
            db.session.commit()
        except IntegrityError:
            # Another request already created today's check-in
            # (e.g. rapid double-click) — safe to ignore, not an error.
            db.session.rollback()

    streak = calculate_streak(habit)
    message = get_motivational_message(habit.name, streak)

    return redirect(url_for('home', ai_message=message, ai_habit_id=habit.id))


@app.route('/habits/<int:habit_id>/uncheck', methods=['POST'])
def uncheck_habit(habit_id):
    habit = Habit.query.get(habit_id)
    if not habit:
        flash("That habit no longer exists.")
        return redirect(url_for('home'))

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

        try:
            reply = get_coach_reply(habits_summary, chat_history, user_message)
        except Exception:
            reply = "Sorry, I had trouble responding just now — could you try saying that again?"

        chat_history.append({'role': 'user', 'content': user_message})
        chat_history.append({'role': 'assistant', 'content': reply})

        session['chat_history'] = chat_history[-(MAX_CHAT_TURNS * 2):]

    return redirect(url_for('coach'))


@app.route('/coach/clear', methods=['POST'])
def coach_clear():
    session.pop('chat_history', None)
    return redirect(url_for('coach'))


@app.errorhandler(404)
def not_found(e):
    return render_template('error.html', message="That page doesn't exist."), 404


@app.errorhandler(500)
def server_error(e):
    db.session.rollback()
    return render_template('error.html', message="Something went wrong on our end. Please try again."), 500


@app.errorhandler(413)
def payload_too_large(e):
    flash("That input was too large.")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)