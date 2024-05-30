from flask_sqlalchemy import model
from app import db

# Defining the Book model
class User(db.Model):
    id  = db.Column(db.Integer(), primary_key=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100), nullable=False)