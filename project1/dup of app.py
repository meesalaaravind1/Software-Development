import os
import datetime
from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from models import db,Persons


app = Flask(__name__)

# Tell Flask what SQLAlchemy databas to use.

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://kkkshorvycaxqz:9888b3a6098fdd052f03433ae560f49b6bbab0e1ed99fb526c2f3197177cc512@ec2-54-147-209-121.compute-1.amazonaws.com:5432/dc4viourhlk7fq'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
# db.create_all()
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if (request.method == "POST"):
        mail = request.form['name']
        passw = request.form['pwd']

#  Flight.query.filter_by(origin="Paris").count()

        count = Users.query.filter_by(email=mail)
        print (count)
        try:
            register = Users(email = mail, password = passw)
            db.session.add(register)
            db.session.commit()
            a=Users.query.all()
            print(a)
            return render_template("login.html",name=mail)
        except:
            error="You have already registered with this email"
            return render_template("register.html",message=error)
    return render_template("register.html")

@app.route("/login.html",methods=["GET","POST"])
def login():
    return render_template("login.html")