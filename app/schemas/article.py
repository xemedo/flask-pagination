from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.article import Article
from app.utils import FilteredSchema


class ArticleSchema(SQLAlchemyAutoSchema, FilteredSchema):
    class Meta:
        model = Article
        load_instance = True
        include_fk = True
