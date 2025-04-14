from werkzeug.security import check_password_hash, generate_password_hash
from .user import User
from App.database import db

class RegularUser(User):
  __tablename__ = 'regular_user'
  __mapper_args__ = {
      'polymorphic_identity': 'regular user',
  }

  def __repr__(self):
    return f'<RegularUser {self.id} - {self.username}>'