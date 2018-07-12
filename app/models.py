# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


miembros_roles = db.Table('miembros_roles',
    db.Column('id_miembro', db.Integer, db.ForeignKey('miembros.id'),nullable=False),
    db.Column('id_rol', db.Integer, db.ForeignKey('roles.id'),nullable=False)
)

miembros_parientes = db.Table('miembros_parientes',
    db.Column('id_miembro_origen', db.Integer, db.ForeignKey('miembros.id'),nullable=False),
    db.Column('id_miembro_destino', db.Integer, db.ForeignKey('miembros.id'),nullable=False),
    db.Column('id_parentezco', db.Integer, db.ForeignKey('parentezcos.id'),nullable=False)
)



class Miembro(db.Model):
    """
    Crear una tabla de miembros
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'miembros'

    id = db.Column(db.Integer, primary_key=True)
    id_familia = db.Column(db.Integer, db.ForeignKey('familias.id'),nullable=False)
    nombres = db.Column(db.String(100), index=True)
    apellidos = db.Column(db.String(100), index=True)
    dni_doc = db.Column(db.String(20))
    email = db.Column(db.String(60), index=True, unique=True)
    id_estado_civil = db.Column(db.Integer, db.ForeignKey('estadosciviles.id'),nullable=False)
    direccion = db.Column(db.String(200))
    telefono_1 = db.Column(db.String(15))
    telefono_2 = db.Column(db.String(15))
    fecha_nac = db.Column(db.DateTime)
    fecha_inicio_icecha = db.Column(db.DateTime)
    fecha_miembro = db.Column(db.DateTime)
    fecha_bautismo = db.Column(db.DateTime)
    lugar_bautismo = db.Column(db.String(50))
    id_tipo_miembro = db.Column(db.Integer, db.ForeignKey('tiposmiembros.id'),nullable=False)
    id_grupo_casero = db.Column(db.Integer, db.ForeignKey('gruposcaseros.id'))
    observaciones = db.Column(db.String(500))

    pariente_origen = db.relationship(
        'Miembro', secondary=miembros_parientes,
        primaryjoin=(miembros_parientes.c.id_miembro_destino == id),
        secondaryjoin=(miembros_parientes.c.id_miembro_origen == id),
        backref=db.backref('pariente_destino', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<Miembro: %s ' ' %s>' %(self.nombres,self.apellidos)

class GrupoCasero(db.Model):
    """
    Crear una tabla de grupos caseros
    """

    __tablename__ = 'gruposcaseros'

    id = db.Column(db.Integer, primary_key=True)
    nombre_grupo = db.Column(db.String(60),nullable=False)
    descripcion_grupo = db.Column(db.String(200),nullable=False)
    direccion_grupo = db.Column(db.String(200),nullable=False)
    miembros = db.relationship('Miembro', backref='grupocasero', lazy='dynamic')

    def __repr__(self):
        return '<Grupo Casero: {}>'.format(self.nombre_grupo)


class Rol(db.Model):
    """
    Crea una tabla de funciones y roles
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    descripcion = db.Column(db.String(200))
    miembros = db.relationship('Miembro', secondary=miembros_roles, backref=db.backref('roles', lazy='dynamic'))


    def __repr__(self):
        return '<Rol: {}>'.format(self.nombre)

class Parentezco(db.Model):
    """
    Crea una tabla de parentezcos (padre, madre, hermano, nieto, abuelo)
    se carga todas las relaciones que tenga cada persona con otros de la iglesia
    """

    __tablename__ = 'parentezcos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    descripcion = db.Column(db.String(200))

    def __repr__(self):
        return '<Parentezco: {}>'.format(self.nombre)

class EstadoCivil(db.Model):
    """
    Crea una tabla de estados civiles
    """

    __tablename__ = 'estadosciviles'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    descripcion = db.Column(db.String(200))
    miembros = db.relationship('Miembro', backref='estado',lazy='dynamic')


    def __repr__(self):
        return '<Estado Civil: {}>'.format(self.nombre)

class TipoMiembro(db.Model):
    """
    Crea una tabla de tipos de miembros ( miembro, asistente regular, no viene, etc)
    """

    __tablename__ = 'tiposmiembros'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    descripcion = db.Column(db.String(200))
    miembros = db.relationship('Miembro', backref='tipomiembro',lazy='dynamic')


    def __repr__(self):
        return '<Tipo de Miembro: {}>'.format(self.nombre)

class Familia(db.Model):
    """
    Crea una tabla familias
    """

    __tablename__ = 'familias'

    id = db.Column(db.Integer, primary_key=True)
    apellidos_familia = db.Column(db.String(60))
    comentarios = db.Column(db.String(200))
    id_tipofamilia = db.Column(db.Integer, db.ForeignKey('tiposfamilias.id'))
    miembros = db.relationship('Miembro', backref='familia',lazy='dynamic')

    def __repr__(self):
        return '<Familia: {}>'.format(self.apellidos_familia)

class TipoFamilia(db.Model):
    """
    Crea una tabla tipo familia- nucleares (padre,madre,hijos), monoparentales, extendidas(nuclear+parientes), otras
    """
    __tablename__ = 'tiposfamilias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    descripcion = db.Column(db.String(200))
    familias = db.relationship('Familia', backref='tipofamilia',lazy='dynamic')

    def __repr__(self):
        return '<Tipo de Familia: {}>'.format(self.nombre)


class Usuario(UserMixin, db.Model):
    """
    Crear una tabla de usuarios de la aplicacion
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'usuarios'


    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))
