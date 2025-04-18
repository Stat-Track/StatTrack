from App.models.report import Report
from App.database import db

def create_report(file):
    new_report = Report(file)
    db.session.add(new_report)
    db.session.commit()
    return new_report