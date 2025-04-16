# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .admin import setup_admin
from flask import Flask

views = [user_views, index_views, auth_views]

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Register blueprints
    app.register_blueprint(auth_views, url_prefix='/auth')  # For login, signup
    app.register_blueprint(index_views, url_prefix='/')  # For the index/home page
    app.register_blueprint(user_views, url_prefix='/user')  # For user-related routes
    setup_admin(app)  # If you're using something like Flask-Admin for admin panel setup

    return app

 
# blueprints must be added to this list