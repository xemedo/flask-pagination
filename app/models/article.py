from app.utils import CreatedModifiedMixin
from app import db


class Article(db.Model, CreatedModifiedMixin):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
