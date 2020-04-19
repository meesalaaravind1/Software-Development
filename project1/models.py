from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()
class User(db.Model):
    __tablename__ = "user"
    time=db.Column(db.DateTime,nullable=False)
    email = db.Column(db.String(120),primary_key=True)
    password = db.Column(db.String(80),nullable=False)

    def __init__(self,email,password):
        self.email = email
        self.password=password
        self.time=dt.now()
