from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.forms import LoginForm, RegistrationForm, DynamicQuestionForm
from app.models import User, Awnser


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
@login_required
def index():
    if current_user.awnsers.first() is not None:
        flash("Du har allerede svaret.")
        return redirect(url_for('completed')) 

    form = DynamicQuestionForm()()
    questions = [getattr(form, i) for i in dir(form) if i.startswith('feild_')]

    if form.validate_on_submit():
        for i in questions:
            q_id = i.name.split("_")[2]
            data = i.data

            a = Awnser(user_id=current_user.id, question_id=q_id, body=data)
            db.session.add(a)
        
        db.session.commit()
        return redirect(url_for('completed')) 

    return render_template('index.html', title='Form', form=form, questions=questions)


@app.route('/completed')
def completed():
    return render_template('complete.html', title='Tak for hjælpen!')

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user is None or not user.check_password(form.password.data):
            flash("Forkert email eller adgangskode.")
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
