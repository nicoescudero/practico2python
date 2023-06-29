from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Preceptor(db.Model):
    __tablename__= 'preceptor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30),nullable=False)
    apellido = db.Column(db.String(30),nullable=False)
    correo = db.Column(db.String(40), unique = True,nullable=False)
    clave = db.Column(db.String(150),nullable=False)
    def __init__(self,nombre='',apellido='',correo='',clave=''):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.clave = clave

class Padre(db.Model):
    __tablename__= 'padre'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    correo = db.Column(db.String(40), unique = True)
    clave = db.Column(db.String(150))
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.id'),nullable=False)

class Estudiante(db.Model):
    __tablename__= 'estudiante'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30),nullable=False)
    apellido = db.Column(db.String(30),nullable=False)
    dni = db.Column(db.String(40), unique = True,nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'),nullable=False)

class Curso(db.Model):
    __tablename__= 'curso'
    id = db.Column(db.Integer, primary_key=True)
    año = db.Column(db.Integer,nullable=False)
    division = db.Column(db.Integer,nullable=False)
    preceptor_id = db.Column(db.Integer, db.ForeignKey('preceptor.id'),nullable=False)


class Asistencia(db.Model):
    __tablename__= 'asistencia'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime,nullable=False)
    codigoClase = db.Column(db.Integer,nullable=False)
    asistio = db.Column(db.String(10), default = 'Si')
    justificacion = db.Column(db.String(30),nullable=True)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.id'),nullable=False)
    def __init__(self,fecha='',codigoClase='',estudiante_id='',asistio='si',justificacion=''):
        self.fecha=fecha
        self.codigoClase=codigoClase
        self.asistio=asistio
        self.justificacion=justificacion
        self.estudiante_id=estudiante_id