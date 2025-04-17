from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for 
from App.controllers import create_user, initialize
from flask_jwt_extended import jwt_required, current_user, get_jwt_identity


index_views = Blueprint('index_views', __name__)

@index_views.route('/', methods=['GET'])
@jwt_required()
def index_page():
    user_id = get_jwt_identity()
    if not user_id:
        return redirect(url_for('auth_views.login_page'))
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

