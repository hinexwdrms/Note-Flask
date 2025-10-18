from flask import Flask

def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ujjarp'

    #importing blueprint variables
    from .views import views
    from .auth import auth

    #registering blueprints
    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app