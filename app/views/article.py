from marshmallow import ValidationError
from flask_restful import Resource
from flask import request
from flask_resty import GenericModelView, PagePagination

from app.schemas.article import ArticleSchema
from app import db, pagination
from app.models.article import Article


class ArticleCreateView(Resource):
    def post(self):
        try:
            article_data = request.get_json(force=True)
            schema = ArticleSchema(many=True)
            new_articles = schema.load(article_data, session=db.session)
            db.session.add_all(new_articles)
            db.session.commit()
        except ValidationError as err:
            return err.messages, 400
        except Exception as e:
            return str(e), 400

        return 200


class PaginationSQLAlchemyView(Resource):
    def get(self):
        page = request.args.get("page", 1, type=int)
        articles = (
            db.session.query(Article)
            .order_by("created")
            .paginate(page=page, per_page=5)
        )
        schema = ArticleSchema(many=True)
        return schema.dump(articles.items), 200


class PaginationFlaskPaginateView(Resource):
    def get(self):
        res = pagination.paginate(Article, ArticleSchema(many=True), True)
        return res, 200

class PaginationFlaskResty(GenericModelView):
    model = Article
    schema = ArticleSchema(many=True)
    pagination = PagePagination(page_size=5)

    def get(self):
        return self.list()

