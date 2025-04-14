from App.database import db

class Faculty(db.Model):
    facultyId = db.Column(db.Integer, primary_key=True)
    facultyName = db.Column(db.String(80), nullable=False)
    campusId = db.Column(db.Integer, db.ForeignKey('campus.id'))

