import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    with app.app_context():
        app.template_folder = os.path.join(os.path.dirname(__file__), 'templates')
        from . import routes
        app.register_blueprint(routes.bp)

    return app