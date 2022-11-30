from flask import render_template, redirect, flash, url_for, request, Response
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import db
from app.main import bp
from app.main.forms import DynamicForm, BuyItemForm, UpdateItemForm, CuponForm
from app.models import User, Item, CartItem, Cupon, UserCupon


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
    form = DynamicForm(cart)()
    cupon_form = CuponForm()

    if f1 := form.validate_on_submit():
        selects = [getattr(form, i).data for i in dir(form) if i.startswith('feild_quant_')]

    if f2 := cupon_form.validate_on_submit():
        code = cupon_form.code.data
        cupons = current_user.cupons.filter_by(status=1).all()
        if len(cupons) >= 1:
            flash("You already have an active cupon!")
            return redirect(url_for("main.cart"))

        found_cupon = Cupon.query.filter_by(name=code).first()
        if found_cupon is None or found_cupon.cupons.count() >= found_cupon.max_uses:
            flash("Invalid cupon code.")
            return redirect(url_for("main.cart"))
        
        c = UserCupon(user_id=current_user.id, cupon_id=found_cupon.id, status=1)
        db.session.add(c)
        db.session.commit()
        flash("Your cupon has been activated and will be applied at your next purchase!")

    if f1 or f2:
        return redirect(url_for("main.cart"))

    for i in cart:
        getattr(form,f"feild_quant_{i.item_id}").data = str(i.amount)
        getattr(form,f"feild_hidden_{i.item_id}").data = str(i.id)

    selects = [getattr(form, i) for i in dir(form) if i.startswith('feild_quant_')]
    hidden  = [getattr(form, i) for i in dir(form) if i.startswith('feild_hidden_')]
    cupon = current_user.cupons.filter_by(status=1).first()

    sub = sum(map(lambda x: x.get_item().price*int(x.amount), cart))
    delivery = 25
    if cupon is not None:
        # The amount that the cupon is worth in this instance
        cpn_amt = (sub+delivery)*(cupon.cupon.procent/100)
    else:
        cpn_amt = sub + delivery

    tax = 0.26 * cpn_amt
    tot = cpn_amt + tax
    return render_template(
        "cart.html", 
        title="Cart", 
        form=form, 
        cupon_form=cupon_form,
        items=zip(cart, zip(selects, hidden)), 
        total=sub,
        delivery=delivery,
        taxes=tax,
        cupon=cupon,
        tot=tot,
        cpn_amt=cpn_amt,
        round=round,
    )

@bp.route('/favorite')
def favorite():
    return "Hello world!"


@bp.route('/remove')
def remove():
    CartItem.query.filter_by(user_id=current_user.id, item_id=request.args.get("item")).delete()
    db.session.commit()
    return redirect(url_for("main.cart"))


@bp.route('/updateCart', methods=["POST"])
def update_cart():
    content = request.json
    for id, amount in content.items():
        CartItem.query.filter_by(user_id=current_user.id, id=id).first_or_404().amount = amount
    db.session.commit()
    return Response("{}", status=200, mimetype='application/json') 


@bp.route('/completed')
def completed():
    return render_template('complete.html', title='Tak for hjælpen!')

