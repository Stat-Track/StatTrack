from App.models import Campus
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
