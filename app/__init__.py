from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_rest_paginate import Pagination

app = Flask(__name__)
db = SQLAlchemy()

pagination = Pagination()


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    configure_app(app)
    pagination.init_app(app, db)
    init_db(app)

    from app.views.article import (
        ArticleCreateView,
        PaginationFlaskPaginateView,
        PaginationSQLAlchemyView,
    )

    api = Api(app)
    api.add_resource(ArticleCreateView, "/articles")
    api.add_resource(PaginationSQLAlchemyView, "/articles_alchemy")
    api.add_resource(PaginationFlaskPaginateView, "/articles_flask_paginate")

    return app


def configure_app(app):
    from app.config import Config

    app.config.from_object(Config)


def init_db(app):
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()
