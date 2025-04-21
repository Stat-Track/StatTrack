# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .admin import admin_views
from .admin import setup_admin
from.report import reports_views
from.report import generate_views

views = [user_views, index_views, auth_views,reports_views,admin_views,generate_views] #Added reports_views,admin_views and views list below-Jaidi Akii-Bua
# blueprints must be added to this list
views = [
    reports_views,
    user_views,
     auth_views,
    index_views,
    admin_views,
    generate_views
]