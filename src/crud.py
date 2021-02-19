from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dotenv import load_dotenv 
from src.models import User, db


load_dotenv()


app = Flask(__name__)

db.init_app(app)
db.app = app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

now = datetime.now()


@app.route('/')
@app.route('/home')
def home():
    users = User.query.all()
    return render_template("home.html", users=users)


@app.route('/<int:id>/del')
def post_delete(id):
	user_del = User.query.get(id)
	
	try:
		db.session.delete(user_del)
		db.session.commit()


		return redirect(url_for('home'))
	except:
		return "Foydalanuvchini o'chirishda xatolik yuzaga keldi!"


@app.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
    users = User.query.get(id)
    if request.method == "POST":
        users.name = request.form['name']
        users.email = request.form['email']
        users.phone = request.form['phone']

        try:
            db.session.commit()

            return redirect(url_for('home'))
        except:
            return "Error!"
    return render_template("edit.html", users=users)


@app.route('/add_user', methods=['POST', 'GET'])
def add_user():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        user = User(name=name, email=email, phone=phone)

        try: 
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('home'))
        except:
            return "Error!"

    return render_template("create_user.html")


