"""empty message

Revision ID: 17784e0726e9
Revises: 65bdfa20b574
Create Date: 2019-03-22 00:47:51.992067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17784e0726e9'
down_revision = '65bdfa20b574'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuarios', sa.Column('is_editor', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuarios', 'is_editor')
    # ### end Alembic commands ###
