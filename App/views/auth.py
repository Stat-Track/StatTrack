from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies


from.index import index_views

from App.controllers import (
    login,
    create_user
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')




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
        return redirect(url_for('auth_views.login_page'))
    
    flash('Login Successful', 'success')
        
    from App.models import User
    user = User.query.filter_by(username=data['username']).first()
    
    if user is None:
        flash('User not found after login?', 'danger')
        return redirect(url_for('auth_views.login_page'))
    
    # Debug: Print user role to console
    print(f"User {user.username} logged in with role: {user.role}")
    
    # Role-based redirect
    if user.role == 'admin':
        redirect_url = url_for('admin.index')
    else:
        redirect_url = url_for('user_views.user_index')

    
    print(f"Redirecting to: {redirect_url}")
    response = redirect(redirect_url)
    set_access_cookies(response, token)
    return response

@auth_views.route('/signup', methods=['POST'])
def signup_action():
    data = request.form

    if not data.get('username') or not data.get('password'):
        flash('Username and password are required', 'danger')
        return redirect(url_for('auth_views.signup_page'))
    
    # Check if username already exists
    from App.models import User
    existing_user = User.query.filter_by(username=data['username']).first()
    
    if existing_user:
        flash('Username already exists', 'danger')
        return redirect(url_for('auth_views.signup_page'))
    
    # Create the user
    user = create_user(
        username=data['username'],
        password=data['password'],
        role='user'  
    )
    
    if user:
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('auth_views.login_page'))
    else:
        flash('Error creating account', 'danger')
        return redirect(url_for('auth_views.signup_page'))


@auth_views.route('/login', methods=['GET'])
def login_page():
    return render_template('index.html')

@auth_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    response = redirect(url_for('auth_views.login_page')) 
    flash("Logged Out!")
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
    return jsonify(message='bad username or password given'), 401
  response = jsonify(access_token=token) 
  set_access_cookies(response, token)
  return response


@auth_views.route('/api/signup', methods=['POST'])
def signup_api():
    data = request.json
    
    if not data.get('username') or not data.get('password'):
        return jsonify(message='Username and password are required'), 400
    
    from App.models import User
    existing_user = User.query.filter_by(username=data['username']).first()
    
    if existing_user:
        return jsonify(message='Username already exists'), 409
    
    user = create_user(
        username=data['username'],
        password=data['password'],
        role='user'
    )
    
    if user:
        return jsonify(message='Account created successfully'), 201
    else:
        return jsonify(message='Error creating account'), 500
    

@auth_views.route('/api/identify', methods=['GET'])
@jwt_required()
def identify_user():
    return jsonify({'message': f"username: {current_user.username}, id : {current_user.id}"})

@auth_views.route('/api/logout', methods=['GET'])
def logout_api():
    response = jsonify(message="Logged Out!")
    unset_jwt_cookies(response)
    return response