from flask_app import app
from flask_app.models.cookie_order import Cookie_order
from flask import redirect, render_template, request

@app.route('/')
@app.route('/cookies')
def index():
    orders= Cookie_order.get_all()
    return render_template("cookies.html", orders= orders)

@app.route('/cookies/new')
def new_order():
    return render_template("new_order.html")

@app.route('/cookies/', methods=["POST"])
def create_order():
    if not Cookie_order.validate_cookie_order(request.form):
        return redirect('/cookies/new')
    Cookie_order.save(request.form)
    return redirect('/')

@app.route('/cookies/edit/<int:cookie_id>',)
def edit_page(cookie_id):
    order = Cookie_order.get_by_id(cookie_id)
    return render_template("edit_order.html", order = order)

@app.route('/cookies/edit/<int:cookie_id>', methods = ['POST'])
def update_order(cookie_id):
    Cookie_order.update(request.form)
    return redirect('/')
