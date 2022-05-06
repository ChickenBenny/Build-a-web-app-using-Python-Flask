from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Question
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/meeting', methods=['GET', 'POST'])
@login_required
def meeting():
    if request.method == 'POST':
        question = request.form.get('question')

        if len(question) < 1:
            flash('Question is too short!', category='error')
        else:
            new_question = Question(data=question, id = current_user.id)
            db.session.add(new_question)
            db.session.commit()
            flash('Question added!', category='success')

    return render_template("meeting.html", user=current_user)


@views.route('/delete-question', methods=['POST'])
def delete_question():
    question = json.loads(request.data)
    questionId = question['questionId']
    question = Question.query.get(questionId)
    if question:
        db.session.delete(question)
        db.session.commit()