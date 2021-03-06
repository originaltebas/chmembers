"""empty message

Revision ID: d6606d00f9f5
Revises: f3c80e79066f
Create Date: 2019-06-05 20:47:50.213810

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd6606d00f9f5'
down_revision = 'f3c80e79066f'
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
    op.add_column('seguimientos', sa.Column('tipo_seg', sa.String(length=1), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('seguimientos', 'tipo_seg')
    op.alter_column('miembros', 'hoja_firmada',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.alter_column('asistencias', 'asistio',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    # ### end Alembic commands ###
