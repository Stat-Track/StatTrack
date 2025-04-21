from App.models import Faculty
from App.database import db

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