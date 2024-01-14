from flask import Flask, render_template, request, redirect

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketsss.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.column(db.string(length=30), unique=True, nullable=False)
    email_address = db.column(db.string(length=50), unique=True, nullable=False)
    password_hash = db.column(db.string(length=60), nullable=False)
    budget = db.column(db.Integer(), nullable=False, default=1000)
    item = db.relationship('Item', backref='owned_user', lazy=True)

    def __repr__(self):
        return '<User{}>'.format(self.username)




class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    def __repr__(self):
        return f'Item {self.name}'


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)



if __name__ == '__main__':
    app.run()
