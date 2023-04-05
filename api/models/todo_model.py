"""Todo model module."""
from api import db


class Todo(db.Model):
    """Todo model."""

    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    expiration_date = db.Column(db.Date, nullable=True)
