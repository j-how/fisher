from flask import Flask
from flask_cache import Cache

from app.models.book import db

cache = Cache()


def create_app():
    app = Flask(__name__, static_folder='frontend/static', static_url_path='/static',
                template_folder='frontend\\templates')
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    cache.init_app(app)
    db.init_app(app)
    db.create_all(app=app)
    register_blueprint(app)

    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
