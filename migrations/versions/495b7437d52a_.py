"""empty message

Revision ID: 495b7437d52a
Revises: 865228eedede
Create Date: 2019-06-06 14:56:16.561683

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '495b7437d52a'
down_revision = '865228eedede'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reuniones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha_culto', sa.Date(), nullable=False),
    sa.Column('nombre_culto', sa.String(length=20), nullable=False),
    sa.Column('comentarios', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('asistencias', sa.Column('id_reunion', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'asistencias', 'reuniones', ['id_reunion'], ['id'])
    op.drop_column('asistencias', 'id')
    op.drop_column('asistencias', 'asistio')
    op.drop_column('asistencias', 'fecha_culto')
    op.alter_column('miembros', 'hoja_firmada',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('miembros', 'hoja_firmada',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.add_column('asistencias', sa.Column('fecha_culto', mysql.DATETIME(), nullable=False))
    op.add_column('asistencias', sa.Column('asistio', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.add_column('asistencias', sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'asistencias', type_='foreignkey')
    op.drop_column('asistencias', 'id_reunion')
    op.drop_table('reuniones')
    # ### end Alembic commands ###
