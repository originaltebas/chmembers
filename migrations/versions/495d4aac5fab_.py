"""empty message

Revision ID: 495d4aac5fab
Revises: a8f231ea597e
Create Date: 2019-04-06 00:17:15.229799

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '495d4aac5fab'
down_revision = 'a8f231ea597e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('asistencias', 'asistio',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.create_foreign_key(None, 'miembros', 'estadosciviles', ['id_estadocivil'], ['id'])
    op.alter_column('seguimientos', 'comentarios_seg',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('seguimientos', 'comentarios_seg',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    op.drop_constraint(None, 'miembros', type_='foreignkey')
    op.drop_column('miembros', 'id_estadocivil')
    op.alter_column('asistencias', 'asistio',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    # ### end Alembic commands ###
