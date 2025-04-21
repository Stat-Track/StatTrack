from App.models import Faculty
from App.database import db
from App.models import Report

def create_faculty(name, campus_id):
    faculty = Faculty(name=name, campus_id=campus_id)
    db.session.add(faculty)
    db.session.commit()
    return faculty

def get_all_faculties():
    return Faculty.query.all()

def get_faculties_by_campus(campus_id):
    return Faculty.query.filter_by(campus_id=campus_id).all()

def get_faculty_by_id(faculty_id):
    return Faculty.query.get(faculty_id)

def update_faculty(faculty_id, name, campus_id):
    faculty = get_faculty_by_id(faculty_id)
    if faculty:
        faculty.name = name
        faculty.campus_id = campus_id
        db.session.commit()
        return faculty
    return None

def delete_faculty(faculty_id):
    faculty = get_faculty_by_id(faculty_id)
    if faculty:
        db.session.delete(faculty)
        db.session.commit()
        return True
    return False

def get_faculty_reports(faculty_id):
    faculty = get_faculty_by_id(faculty_id)
    if faculty:
        return faculty.reports.all()
    return None

def validate_faculty(faculty_id):
    return Faculty.query.get(faculty_id) is not None

def get_reports_by_campus_and_faculty(campus_id, faculty_id):
    return Report.query.filter_by(campus_id=campus_id, faculty_id=faculty_id).all()