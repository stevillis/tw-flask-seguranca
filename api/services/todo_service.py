"""Todo service module."""

from typing import List

from api import db

from ..entities.todo_entity import Todo as TodoEntity
from ..models.todo_model import Todo as TodoModel


def create_todo(todo: TodoEntity) -> TodoModel:
    """Create todo service."""
    todo_db = TodoModel(title=todo.title, description=todo.description, expiration_date=todo.expiration_date)

    db.session.add(todo_db)
    db.session.commit()

    return todo_db


def get_todos() -> List[TodoModel]:
    """Get todos service."""
    return TodoModel.query.all()


def get_todo_by_pk(pk):
    """Get todo by pk service."""
    return TodoModel.query.filter_by(id=pk).first()


def update_todo(todo_db, new_todo):
    """Update todo service."""
    todo_db.title = new_todo.title
    todo_db.description = new_todo.description
    todo_db.expiration_date = new_todo.expiration_date
    db.session.commit()


def delete_todo(todo):
    """Delete todo service."""
    db.session.delete(todo)
    db.session.commit()
