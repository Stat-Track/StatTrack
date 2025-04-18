from App.models import User
from App.models.regularuser import RegularUser
from App.database import db
from App.models.admin import Admin

def create_user(username, password, user_type='user'):
    # Check if user_type is 'admin' and create an Admin object; otherwise, create a RegularUser object
    if user_type == 'admin':
        new_user = Admin(username=username, password=password)
    else:
        new_user = RegularUser(username=username, password=password)

    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    