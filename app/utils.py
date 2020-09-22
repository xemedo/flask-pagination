from marshmallow_sqlalchemy import auto_field
from datetime import datetime

from . import db


class CreatedModifiedMixin:
    created = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    modified = db.Column(
        db.DateTime(), nullable=True, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class FilteredSchema:
    modified = auto_field(load_only=True)
    created = auto_field(load_only=True)
