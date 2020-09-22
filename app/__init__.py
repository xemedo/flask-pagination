from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api as restful_api
from flask_resty import Api as resty_api
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

    # Flask Restful
    api = restful_api(app)
    api.add_resource(ArticleCreateView, "/articles")
    api.add_resource(PaginationSQLAlchemyView, "/articles_alchemy")
    api.add_resource(PaginationFlaskPaginateView, "/articles_flask_paginate")

    # Flask Resty
    from app.views.article import PaginationFlaskResty

    api2 = resty_api(app)
    api2.add_resource("/articles_flask_resty", PaginationFlaskResty, PaginationFlaskResty)

    return app


def configure_app(app):
    from app.config import Config

    app.config.from_object(Config)


def init_db(app):
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()
