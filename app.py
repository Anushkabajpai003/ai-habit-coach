"""
AI Habit Coach — Flask application entry point.
"""

from datetime import date
from flask import Flask, render_template, request, redirect, url_for
from models import db, Habit, CheckIn
from utils import calculate_streak, already_checked_in_today
from ai_coach import get_motivational_message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    habits = Habit.query.order_by(Habit.created_at.asc()).all()
    habit_data = []
    for habit in habits:
        habit_data.append({
            'id': habit.id,
            'name': habit.name,
            'streak': calculate_streak(habit),
            'checked_in_today': already_checked_in_today(habit),
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


if __name__ == '__main__':
    app.run(debug=True)