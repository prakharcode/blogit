"""empty message

Revision ID: d753e8af2755
Revises: None
Create Date: 2016-07-19 16:49:24.776874

"""

# revision identifiers, used by Alembic.
revision = 'd753e8af2755'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'entry', 'user', ['author_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'entry', type_='foreignkey')
    ### end Alembic commands ###
