from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager #flask login manager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ujjarp'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) #initializing database for our app with the path above

    #importing blueprint variables
    from .views import views
    from .auth import auth

    #registering blueprints
    app.register_blueprint(views)
    app.register_blueprint(auth)

    from .models import User, Note

    create_database(app)

    #login function
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #where to redirect if not logged in
    login_manager.init_app(app) #specifying app

    @login_manager.user_loader #describes how to load user
    def load_user(id):
        return User.query.get(int(id)) #looks for primary key (id) --> get()

    return app

#create database if none
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')