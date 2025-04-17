from werkzeug.security import check_password_hash, generate_password_hash
from .user import User
from App.database import db

class Admin(User):
    __tablename__ = 'admin'
    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    def __init__(self,username,password):
        super().__init__(username, password)
    
    def __repr__(self):
        return f'<Admin {self.id} - {self.username}>'
    

    def get_json(self):
        return{
            "id": self.id,
            "username": self.username,
            "type": self.type
        }

