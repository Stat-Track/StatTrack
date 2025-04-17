from App.database import db

class Report(db.Model):
    reportId = db.Column(db.Integer, primary_key=True)
    reportName = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    

