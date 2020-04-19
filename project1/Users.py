import os
from flask import Flask, session,request,render_template,flash,logging,redirect,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://kkkshorvycaxqz:9888b3a6098fdd052f03433ae560f49b6bbab0e1ed99fb526c2f3197177cc512@ec2-54-147-209-121.compute-1.amazonaws.com:5432/dc4viourhlk7fq'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Users(db.Model):
    time=db.Column(db.DateTime,nullable=False)
    email = db.Column(db.String(120),primary_key=True)
    password = db.Column(db.String(80),nullable=False)

    def __init__(self,email,password):
        self.email = email
        self.password=password
        self.time=dt.now()

db.create_all()
db.session.commit()
