"""User schema module."""

from marshmallow import fields as ma_fields

from api import ma

from ..models import user_model


class UserSchema(ma.SQLAlchemySchema):
    """User schema class."""

    class Meta:
        """User schema meta definitions."""

        model = user_model.User
        fields = ("id", "name", "email", "password", "is_admin")
        load_model = True

    name = ma_fields.String(required=True)
    email = ma_fields.String(required=True)
    password = ma_fields.String(required=True)
    is_admin = ma_fields.Boolean(required=True)
