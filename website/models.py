from . import db #relative import from the package (__init__)
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(15000))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #identify each note by storing unique user_id 
    #(foreign key) & the user.id --> user from the User class with id field(how it works)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #one user with many note (user --> parent object, note --> child object)
    #keeps record of the note.id everytime user creates note