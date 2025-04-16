import os
from flask import Flask, render_template
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage





from App.database import init_db
from App.config import load_config


from App.controllers import (
    setup_jwt,
    add_auth_context
)

from App.views.index import index_views
from App.views.auth import auth_views
from App.views.user import user_views

views = [index_views, auth_views, user_views]

def add_views(app):
        app.register_blueprint(auth_views, url_prefix='/auth')
        app.register_blueprint(index_views, url_prefix='/')
        app.register_blueprint(user_views, url_prefix='/user')
    

def create_app(overrides={}):
    app = Flask(__name__, static_url_path='/static')
    load_config(app, overrides)
    CORS(app)
    add_auth_context(app)
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app)
    init_db(app)
    jwt = setup_jwt(app)
    from App.views.admin import setup_admin
    setup_admin(app)
    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def custom_unauthorized_response(error):
        return render_template('401.html', error=error), 401
    app.app_context().push()
    return app

