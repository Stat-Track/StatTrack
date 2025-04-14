from App.database import db

class Report(db.Model):
    reportId = db.Column(db.Integer, primary_key=True)
    reportName = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)

