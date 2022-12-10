from flask import render_template, redirect, flash, url_for, request, jsonify, make_response
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
import io
import csv

from app import db
from app.admin import bp
from app.admin.forms import AdminEditStringForm, AdminEditSelectForm, AdminAddForm
from app.models import User, Awnser, Question, Choice


@bp.route('/dashbord')
@login_required
def admin():
    if not current_user.is_admin():
        return redirect(url_for("main.index"))

    return render_template('admin/admin.html', title="Admin", awnsers=Question.count_awnsers(), round=round) 


@bp.route('/add', methods=["GET", "POST"])
@login_required
def add_question():
    if not current_user.is_admin():
        return redirect(url_for("main.index"))

    form = AdminAddForm()

    if form.validate_on_submit():
        q = Question(body=form.title.data, type=form.type.data)
        db.session.add(q)
        db.session.commit()
        return redirect(url_for("admin.admin"))

    return render_template('admin/add_question.html', title="Admin", form=form) 


@bp.route('/remove')
@login_required
def remove():
    if not current_user.is_admin():
        return redirect(url_for("main.index"))

    args = request.args
    q = Question.query.filter_by(id=args.get("question")).delete()

    db.session.commit()

    return redirect(url_for("admin.admin"))


@bp.route('/modify', methods=["GET", "POST"])
@login_required
def modify():
    if not current_user.is_admin():
        return redirect(url_for("main.index"))

    args = request.args
    q = Question.query.filter_by(id=args["question"]).first_or_404()
    print(q, q.type)
    if q.type == "SelectField":
        form = AdminEditSelectForm()
        c = [i.body for i in q.choices.all()]

        if form.validate_on_submit():
            q.body = form.title.data
            for i, old_item in zip(range(1,5,1), c+[""]*(4-len(c))):
                print(old_item)
                item = Choice.query.filter_by(question_id=q.id, body=old_item) if old_item != "" else ""
                new = getattr(form, f"feild{i}").data
                # A feild has been updated
                if new != "" and item != "":
                    item.body = new
                # A feild has been removed
                elif new == "" and item != "":
                    q.awnsers.filter_by(body=old_item).delete()
                    item.delete()
                # A feild has been created
                elif new != "" and item == "":
                    new_item = Choice(body=new, question_id=q.id)
                    db.session.add(new_item)

            db.session.commit()
            return redirect(url_for("admin.admin"))

        form.title.data = q.body
        for i, item in zip(range(1,5,1), c+[""]*(4-len(c))):
            getattr(form, f"feild{i}").data = item

        return render_template('admin/edit_question.html', title="Admin", form=form, q=q) 

    elif q.type == "StringField":
        form = AdminEditStringForm()

        if form.validate_on_submit():
            q.body = form.title.data
            db.session.commit()
            return redirect(url_for("admin.admin"))

        form.title.data = q.body
        return render_template('admin/edit_question.html', title="Admin", form=form, q=q) 


    return redirect(url_for("admin.admin"))


@bp.route('/download')
def download():
    if not current_user.is_admin():
        return redirect(url_for("main.index"))

    args = request.args
    q = Question.query.filter_by(id=args.get("question")).first_or_404()
    a = q.awnsers.all()
    u = [( 
            User.query.filter_by(id=i.user_id).first().email, 
            i.body 
        ) for i in a]

    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)
    [writer.writerow(csvrow) for csvrow in u]

    out = output.getvalue()
    print(out)
    response = make_response(out, 200)
    response.mimetype = "text/plain"
    return response
