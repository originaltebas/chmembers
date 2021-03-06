"""empty message

Revision ID: f3c80e79066f
Revises: f7f3dbae07bb
Create Date: 2019-06-05 20:12:49.715771

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f3c80e79066f'
down_revision = 'f7f3dbae07bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('asistencias', 'asistio',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=False)
    op.alter_column('miembros', 'hoja_firmada',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.alter_column('seguimientos', 'fecha_seg',
               existing_type=mysql.DATETIME(),
               type_=sa.Date(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('seguimientos', 'fecha_seg',
               existing_type=sa.Date(),
               type_=mysql.DATETIME(),
               existing_nullable=False)
    op.alter_column('miembros', 'hoja_firmada',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('asistencias', 'asistio',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    # ### end Alembic commands ###
