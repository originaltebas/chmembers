"""empty message

Revision ID: 6314ce890090
Revises: 396698708af2
Create Date: 2017-11-27 22:02:18.977970

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6314ce890090'
down_revision = '396698708af2'
branch_labels = None
depends_on = None


def upgrade():

    op.create_foreign_key('fk_tf','familias', 'tiposfamilias', ['id_tipofamilia'], ['id'])
    op.add_column(u'miembros', sa.Column('dni_doc', sa.String(length=20), nullable=True))
    op.add_column(u'miembros', sa.Column('fecha_inicio_icecha', sa.DateTime(), nullable=True))
    op.add_column(u'miembros', sa.Column('lugar_bautismo', sa.String(length=50), nullable=True))
    op.alter_column(u'miembros', 'id_grupo_casero',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.drop_column(u'miembros', 'asiste_regular')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'miembros', sa.Column('asiste_regular', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.alter_column(u'miembros', 'id_grupo_casero',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.drop_column(u'miembros', 'lugar_bautismo')
    op.drop_column(u'miembros', 'fecha_inicio_icecha')
    op.drop_column(u'miembros', 'dni_doc')
    op.drop_constraint(None, 'familias', type_='foreignkey')
    op.drop_column(u'familias', 'id_tipofamilia')
    op.drop_table('tiposfamilias')
    # ### end Alembic commands ###