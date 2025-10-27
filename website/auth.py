from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

    return render_template('login.html')

@auth.route('/sign_up', methods =['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

    return render_template('sign_up.html')

@auth.route('/logout')
def logout():
    return '<h1>Logout<h1>'