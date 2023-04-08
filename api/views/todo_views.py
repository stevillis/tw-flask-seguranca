"""Todo views module."""

from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api

from ..entities import todo_entity
from ..models.todo_model import Todo
from ..pagination import paginate
from ..schemas import todo_schema
from ..services import todo_service


def get_todo_fields(req):
    """Get todo fields from request."""
    title = req.json["title"]
    description = req.json["description"]
    expiration_date = req.json["expiration_date"]

    return title, description, expiration_date


class TodoList(Resource):
    """Todo class based views without parameter."""

    @jwt_required()
    def get(self):
        """
        List all Todos.
        ---
        responses:
          200:
            description: List of all Todos.
            schema:
              id: Todo
              properties:
                id:
                  type: integer
                title:
                  type: string
                description:
                  type: string
                expiration_date:
                  type: string
        """
        # todos = todo_service.get_todos()
        ts = todo_schema.TodoSchema(many=True)

        # return make_response(ts.jsonify(todos), 200)
        return paginate(Todo, ts)

    @jwt_required()
    def post(self):
        """
        Create Todo.
        ---
        parameters:
          - in: body
            name: Todo
            description: Create a Todo.
            schema:
              type: object
              required:
                - title
                - description
                - expiration_date
              properties:
                title:
                  type: string
                description:
                  type: string
                expiration_date:
                  type: string
        responses:
          201:
            description: Todo created successfully.
            schema:
              id: Todo
              properties:
                title:
                  type: string
                description:
                  type: string
                expiration_date:
                  type: string
          400:
            description: Bad request. Loading Todos failed.
          404:
            description: Todo not found.
        """
        ts = todo_schema.TodoSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        title, description, expiration_date = get_todo_fields(request)

        new_todo = todo_entity.Todo(
            title=title,
            description=description,
            expiration_date=expiration_date,
        )

        todo_db = todo_service.create_todo(new_todo)

        return make_response(ts.jsonify(todo_db), 201)


class TodoDetail(Resource):
    """Todo class based views with parameter."""

    @jwt_required()
    def get(self, pk):
        """
        Get a Todo by its pk.
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
        responses:
          200:
            description: The Todo if found.
            schema:
              id: Todo
              properties:
                id:
                  type: integer
                title:
                  type: string
                description:
                  type: string
                expiration_date:
                  type: string
          404:
            description: Todo not found.
        """
        todo = todo_service.get_todo_by_pk(pk)
        if not todo:
            return make_response(jsonify("Todo not found!"), 404)

        ts = todo_schema.TodoSchema()
        return make_response(ts.jsonify(todo), 200)

    @jwt_required()
    def put(self, pk):
        """
        Update Todo.
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
          - in: body
            description: Update a Todo
            schema:
              type: object
              required:
                - title
                - description
                - expiration_date
              properties:
                title:
                  type: string
                description:
                  type: string
                expiration_date:
                  type: string
        responses:
          200:
            description: Todo successfully updated.
            schema:
              id: Todo
              properties:
                title:
                  type: string
                description:
                  type: string
                expiration_date:
                  type: string
          400:
            description: Bad request. Malformed data.
          404:
            description: Todo not found.
        """
        todo_db = todo_service.get_todo_by_pk(pk)
        if not todo_db:
            return make_response(jsonify("Todo not found!"), 404)

        ts = todo_schema.TodoSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)

        title, description, expiration_date = get_todo_fields(request)

        new_todo = todo_entity.Todo(
            title=title,
            description=description,
            expiration_date=expiration_date,
        )

        todo_service.update_todo(todo_db, new_todo)
        updated_todo = todo_service.get_todo_by_pk(pk)

        return make_response(ts.jsonify(updated_todo), 200)

    @jwt_required()
    def delete(self, pk):
        """
        Delete a Todo.
        ---
        parameters:
          - in: path
            name: id
            type: integer
            required: true
        responses:
          204:
            description: Todo successfully deleted.
          404:
            description: Todo not found.
        """
        todo = todo_service.get_todo_by_pk(pk)
        if not todo:
            return make_response(jsonify("Todo not found!"), 404)

        todo_service.delete_todo(todo)
        return make_response("", 204)


api.add_resource(TodoList, "/todos")
api.add_resource(TodoDetail, "/todos/<int:pk>")
