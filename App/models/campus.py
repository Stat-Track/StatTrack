from App.database import db

class Campus(db.Model):
    campusID = db.Column(db.Integer, primary_key=True)
    campusName = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120))
    faculties = db.relationship('Faculty')


    def __repr__(self):
        return f'<Campus {self.campusId} - {self.campusName}>'
    
    def toJson(self):
        return{
            'campusId':self.campusID,
            'campusName':self.campusName,
            'location':self.location,
            'faculties':self.faculties
        }