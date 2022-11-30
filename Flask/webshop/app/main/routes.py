from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import db
from app.main import bp
from app.main.forms import DynamicForm, BuyItemForm, UpdateItemForm
from app.models import User, Item, CartItem


@bp.route('/', methods=["GET", "POST"])
@bp.route('/index', methods=["GET", "POST"])
@login_required
def index():
    items = Item.query.all()

    form = BuyItemForm()

    if form.validate_on_submit():
        args = request.args
        c = CartItem.query.filter_by(item_id=args.get("item"), user_id=current_user.id).first()
        if c is not None:
            c.amount += int(form.amount.data)
        else:
            i = Item.query.filter_by(id=args.get("item")).first_or_404()
            amount = form.amount.data
            c = CartItem(user_id=current_user.id, item_id=i.id, amount=amount)
            db.session.add(c)
        db.session.commit()

        return redirect(url_for("main.index"))

    print(items)
    return render_template("index.html", items=items, form=form)


@bp.route('/cart', methods=["GET", "POST"])
def cart():
    cart = current_user.cart.all()
    # kwargs = {f"feild_quant_{i.item_id}": 3 for i in cart}
    form = DynamicForm(cart)()


    if form.validate_on_submit():
        return redirect(url_for("main.cart"))

    for i in cart:
        getattr(form,f"feild_quant_{i.item_id}").data = str(i.amount)

    selects = [getattr(form, i) for i in dir(form) if i.startswith('feild_quant_')]
    print(cart, form)

    sub = sum(map(lambda x: x.get_item().price*int(x.amount), cart))
    delivery = 25
    tax = 0.26 * sub
    tot = sum((sub, tax, delivery))
    return render_template(
                           "cart.html", 
                           title="Cart", 
                           form=form, 
                           items=zip(cart, selects), 
                           total=sub,
                           delivery=delivery,
                           taxes=tax
                          )

@bp.route('/favorite')
def favorite():
    return "Hello world!"


@bp.route('/remove')
def remove():
    return "Hello world!"


@bp.route('/completed')
def completed():
    return render_template('complete.html', title='Tak for hjælpen!')

