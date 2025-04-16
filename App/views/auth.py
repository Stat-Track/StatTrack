from flask import (
    Blueprint, render_template, jsonify, request, flash,
    send_from_directory, redirect, url_for, Flask
)
from flask_jwt_extended import (
    jwt_required, current_user, unset_jwt_cookies,
    set_access_cookies, create_access_token
)
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose

from App.models.user import User
from App.views.index import index_views
from App.controllers import create_user, get_all_users, login
from App.database import db


auth_views = Blueprint('auth_views', __name__, template_folder='../templates')

def setup_admin(app):
    # Initialize Flask-Admin
    admin = Admin(app, name='Admin', template_mode='bootstrap3')

    # Add a view for the User model in the admin interface
    admin.add_view(ModelView(User, db.session))


'''
Page/Action Routes
'''    
@auth_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)


@auth_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_page():
    return render_template('message.html', title="Identify", message=f"You are logged in as {current_user.id} - {current_user.username}")


@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    token = login(data['username'], data['password'])

    if not token:
        flash('Bad username or password given', 'danger')
        return redirect(request.referrer)

    flash('Logged in successfully!', 'success')
    response = redirect(url_for('index_views.index_page'))
    return set_access_cookies(response, token)

"""
@auth_views.route('/signup', methods=['GET', 'POST'])
def signup_action():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("Passwords do not match", "danger")
            return render_template("signup.html")

        user = create_user(username, password)
        if user:
            flash("Account created successfully!", "success")
            return redirect(url_for('auth_views.get_user_page'))
        else:
            flash("Username already exists or something went wrong.", "danger")

    return render_template("signup.html")
"""

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    response = redirect(request.referrer)
    flash("Logged Out!", "info")
    unset_jwt_cookies(response)
    return response

'''
API Routes
'''

@auth_views.route('/api/login', methods=['POST'])
def user_login_api():
    data = request.json
    token = login(data['username'], data['password'])
    if not token:
        return jsonify(message='Bad username or password'), 401
    response = jsonify(access_token=token)
    set_access_cookies(response, token)
    return response


@auth_views.route('/api/signup', methods=['POST'])
def user_signup_api():
    data = request.json
    username = data['username']
    password = data['password']
    confirm_password = data['confirm_password']

    if password != confirm_password:
        return jsonify(message="Passwords do not match"), 400

    user = create_user(username, password)
    if user:
        return jsonify(message="Account created successfully!"), 201
    else:
        return jsonify(message="Username already exists or something went wrong."), 400


@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})


@auth_views.route('/api/logout', methods=['GET'])
def logout_api():
    response = jsonify(message="Logged Out!")
    unset_jwt_cookies(response)
    return response


'''
App Factory
'''
def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SECRET_KEY'] = 'MySecretKey'

    # JWT Config
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
    app.config['JWT_COOKIE_SECURE'] = False  # Set to True in production with HTTPS
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False  # Set to True if CSRF tokens are implemented

    db.init_app(app)

    app.register_blueprint(index_views, url_prefix='/')
    app.register_blueprint(auth_views, url_prefix='/auth')

    setup_admin(app)

    return app
