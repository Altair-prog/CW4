"""add user.favorite_genre

Revision ID: 5ccfa978888d
Revises: 9ddf61e43014
Create Date: 2022-10-29 11:02:13.964331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ccfa978888d'
down_revision = '9ddf61e43014'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user', 'genre', ['favorite_genre'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    # ### end Alembic commands ###
