import os, csv
from flask import Flask, render_template, request

# Import table definitions.
from models import *

app = Flask(__name__)

# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)

def main():

    # Create tables based on each table definition in `models`
    db.create_all()

    # with open("books.csv", 'r') as f:
    #     reader = csv.reader(f)
    #     next(reader)

    #     for row in reader:
    #         new_book = Book(row[0], row[1], row[2], int(row[3]))
    #         db.session.add(new_book)
    # db.session.commit()

if __name__ == "__main__":
  # Allows for command line interaction with Flask application
  with app.app_context():
      main()