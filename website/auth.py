from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db #from __init__

auth = Blueprint('auth',__name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #check if email in database (querying)
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password,password):
                flash("Logged in successfully!", category='success')
                return redirect(url_for('views.home'))
            else:
                flash("Invalid password! Try again.",category='error')
        else:
            flash("User not found!",category='error')

    return render_template('login.html')

@auth.route('/sign_up', methods =['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('User already exists!', category='error')
        elif len(email) < 4:
            flash("Email is too short!", category='error')
        elif len(first_name) < 2 or len(last_name) < 2:
            flash("The first or last name is invalid!", category='error')
        elif password1 != password2:
            flash("Passwords do not match!", category='error')
        elif len(password1) < 4:
            flash("Password should be longer than 4 characters!")
        #can later make symbols, numbers and caps required
        else:
            #create a new user
            new_user = User(email=email, first_name = first_name, last_name = last_name, password = generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit() #commit after updating db

            flash("Account created!", category='success')

            return redirect(url_for('views.home')) #home of the views.py --> same as '/'
         
    return render_template('sign_up.html')

@auth.route('/logout')
def logout():
    return '<h1>Logout<h1>'