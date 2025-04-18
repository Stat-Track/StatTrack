from App.database import db

class Campus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    faculties = db.relationship('Faculty', backref='campus', lazy=True, cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Campus {self.campusId} - {self.campusName}>'
    
    def get_json(self):
        return{
            "id": self.campusID,
            "name": self.campusName,
            "faculties": self.faculties
        }