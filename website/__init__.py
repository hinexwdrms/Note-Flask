from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

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

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')