from werkzeug.security import check_password_hash, generate_password_hash
from .user import User
from App.database import db

class Admin(User):

    def __init__(self,username,password):
        self.username = username
        self.set_password = password
        self.user_type = "admin"
    
    def __repr__(self):
        return f'<Admin {self.id} {self.username}>'

    def toJson(self):
        return{
            'id': self.id,
            'username': self.username,
            'type':'staff'
        }

