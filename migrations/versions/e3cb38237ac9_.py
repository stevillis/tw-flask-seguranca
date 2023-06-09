"""empty message

Revision ID: e3cb38237ac9
Revises: 79ff331f3211
Create Date: 2023-04-08 11:29:51.581115

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e3cb38237ac9"
down_revision = "79ff331f3211"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # Manual updated to set nullable=True
    op.add_column("user", sa.Column("is_admin", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###

    # Manual commands
    op.execute("UPDATE public.user SET is_admin = FALSE")
    op.alter_column("user", "is_admin", nullable=False)
    # End Manual commands


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "is_admin")
    # ### end Alembic commands ###
