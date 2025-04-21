from App.models import Campus
from App.models import Report
from App.database import db

def create_campus(name):
    campus = Campus(name=name)
    db.session.add(campus)
    db.session.commit()
    return campus

def get_all_campuses():
    return Campus.query.all()

def get_campus_by_id(campus_id):
    return Campus.query.get(campus_id)

def update_campus(campus_id, name):
    campus = get_campus_by_id(campus_id)
    if campus:
        campus.name = name
        db.session.commit()
        return campus
    return None

def delete_campus(campus_id):
    campus = get_campus_by_id(campus_id)
    if campus:
        db.session.delete(campus)
        db.session.commit()
        return True
    return False


def get_campus_by_name(name):
    return Campus.query.filter_by(name=name).first()

def validate_campus(campus_id):
    return Campus.query.filter_by(id=campus_id).first() is not None

def get_reports_by_campus_and_filter(campus_id, **filters):
    query = Report.query.filter_by(campus_id=campus_id)
    for key, value in filters.items():
        query = query.filter(getattr(Report, key) == value)
    return query.all()

def get_campus_dropdown():
    return [{"id": campus.id, "name": campus.name} for campus in get_all_campuses()]

def get_campus_reports_with_faculty(campus_id, faculty_id=None):
    query = Report.query.filter_by(campus_id=campus_id)
    if faculty_id:
        query = query.filter_by(faculty_id=faculty_id)
    return query.all()

