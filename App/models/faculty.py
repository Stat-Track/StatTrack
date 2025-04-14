from App.database import db

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    campus_id = db.Column(db.Integer, db.ForeignKey('campus.id'), nullable=False)
    reports = db.relationship('Report', backref='faculty', lazy=True, cascade="all, delete-orphan")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Campus - {self.campus.name}, Faculty {self.campusId} - {self.campusName}>'
    
    def get_json(self):
        "id" = self.id
        "name" = self.name
        "campus_id" = self.campus_id

