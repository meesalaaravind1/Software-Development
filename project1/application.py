import os
from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from models import User,db
from imports import Book
import csv


app = Flask(__name__)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key="email"

db.init_app(app)
def main():
    db.create_all()

# Check for environment variable


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if (request.method == "POST"):
        mail = request.form['name']
        passw = request.form['pwd']

        count = User.query.filter_by(email=mail).count()
        print (count)
        try:
            register = User(email = mail, password = passw)
            db.session.add(register)
            db.session.commit()
            a=User.query.all()
            print(a)
            return render_template("login.html",name=mail)
        except:
            error="You have already registered with this email"
            return render_template("register.html",message=error)
    return render_template("register.html")

@app.route("/login.html",methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route("/admin")
def admin():
    users=User.query.all()
    return render_template ("admin.html",data=users)

@app.route("/auth", methods=["GET","POST"])
def auth():
    if request.method=="POST":
        mail = request.form.get("name") # i will get my email entered in the webpage
        passw = request.form.get("pwd")
        u = User.query.get(mail)
        #select * from user where email==mail  ===> email,password,timestamp
        if u != None:
            # print (u)
            # print (u.password)
            # print (passw,"====> entered password")

            if passw == u.password :
            #     print ("your mail id is found")
                session["email"]=mail
                return render_template("account.html")
            else:
                return "invalid password"
        else:
            return "No account associated with this password"

@app.route("/search",methods=["GET"])
def search():
    if session["email"] == None:
        return redirect(url_for("/logout"))
    else:
        return "Maintained successfully"

@app.route("/logout",methods=["GET","POST"])
def logout():
    session["email"]=None
    return redirect("/register")

if __name__ == "__main__":
    with app.app_context():
        main()