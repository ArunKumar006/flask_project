from market import app
from flask import render_template,url_for,redirect,flash
from market.models import Item
from market.forms import RegistrationForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password_hash=form.password2.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for error in form.errors.values():
            flash(f'Error: {error}')

    return render_template('register.html', form=form)
