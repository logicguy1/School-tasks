from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import db
from app.main import bp
from app.main.forms import DynamicQuestionForm
from app.models import User, Awnser, Question, Choice


@bp.route('/', methods=["GET", "POST"])
@bp.route('/index', methods=["GET", "POST"])
@login_required
def index():
    if current_user.awnsers.first() is not None and current_user.admin == 0:
        flash("Du har allerede svaret.")
        return redirect(url_for('main.completed')) 

    form = DynamicQuestionForm()()
    questions = [getattr(form, i) for i in sorted(dir(form), key=lambda x: x.split("_")[-1]) if i.startswith('feild_')]

    if form.validate_on_submit():
        for i in questions:
            q_id = i.name.split("_")[2]
            data = i.data

            if data != "":
                a = Awnser(user_id=current_user.id, question_id=q_id, body=data)
                db.session.add(a)
        
        db.session.commit()
        return redirect(url_for('main.completed')) 

    return render_template('index.html', title='Form', form=form, questions=questions)


@bp.route('/completed')
def completed():
    return render_template('complete.html', title='Tak for hjælpen!')

