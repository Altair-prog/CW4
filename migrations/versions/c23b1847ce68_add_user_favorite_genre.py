"""add user.favorite_genre

Revision ID: c23b1847ce68
Revises: 5ca77737ce80
Create Date: 2022-10-29 11:07:26.037692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c23b1847ce68'
down_revision = '5ca77737ce80'
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
