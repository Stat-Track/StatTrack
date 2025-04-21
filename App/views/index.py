from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for, flash
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request, current_user
from App.controllers import create_user, initialize
from App.models import User
from App.controllers.campus import get_all_campuses, get_campus_by_id, get_campus_dropdown
from App.controllers.faculties import get_all_faculties, get_faculty_by_id, get_faculties_by_campus
from App.controllers.report import get_reports_by_campus_and_faculty

index_views = Blueprint('index_views', __name__, template_folder='../templates')

# Home page route
@index_views.route('/', methods=['GET'])
def index_page():
    try:
        # Try to verify JWT, but don't require it
        verify_jwt_in_request(optional=True)
        
        if current_user and current_user.is_authenticated:  # User is authenticated
            if current_user.role == 'admin':
                return redirect(url_for('admin.index'))
            else:
                return redirect(url_for('user_views.user_index'))
        else:
            # User is not authenticated, redirect to login
            return redirect(url_for('auth_views.login_page'))
    except:
        # If JWT verification fails, redirect to login
        return redirect(url_for('auth_views.login_page'))

 
@index_views.route('/filter-reports', methods=['GET'])
@jwt_required()
def filter_reports():
    campus_id = request.args.get('campus_id', type=int)
    faculty_id = request.args.get('faculty_id', type=int)

    # Get filtered reports
    reports = get_reports_by_campus_and_faculty(campus_id, faculty_id)

    return render_template(
        'index.html',
        campuses=get_all_campuses(),
        faculties=get_all_faculties(),
        reports=reports,
        selected_campus=campus_id,
        selected_faculty=faculty_id
    ) 


@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})