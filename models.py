from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Preceptor(db.Model):
    __tablename__= 'Preceptor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30),nullable=False)
    apellido = db.Column(db.String(30),nullable=False)
    correo = db.Column(db.String(40), unique = True,nullable=False)
    clave = db.Column(db.String(150),nullable=False)
    curso = db.relationship('Curso', backref='Preceptor', cascade="all, delete-orphan")
    def __init__(self,nombre='',apellido='',correo='',clave=''):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.clave = clave

class Curso(db.Model):
    __tablename__= 'Curso'
    id = db.Column(db.Integer, primary_key=True)
    año = db.Column(db.Integer,nullable=False)
    division = db.Column(db.Integer,nullable=False)
    preceptor_id = db.Column(db.Integer, db.ForeignKey('Preceptor.id'),nullable=False)
    estudiante = db.relationship('Estudiante', backref='Curso', cascade="all, delete-orphan")

class Estudiante(db.Model):
    __tablename__= 'Estudiante'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30),nullable=False)
    apellido = db.Column(db.String(30),nullable=False)
    dni = db.Column(db.String(40), unique = True,nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('Curso.id'),nullable=False)
    padre = db.relationship('Padre', backref='Estudiante', cascade="all, delete-orphan")
    asistencia = db.relationship('Asistencia', backref='Estudiante', cascade="all, delete-orphan")

class Padre(db.Model):
    __tablename__= 'Padre'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    correo = db.Column(db.String(40), unique = True)
    clave = db.Column(db.String(150))
    estudiante_id = db.Column(db.Integer, db.ForeignKey('Estudiante.id'),nullable=False)


class Asistencia(db.Model):
    __tablename__= 'Asistencia'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime,nullable=False)
    codigoClase = db.Column(db.Integer,nullable=False)
    asistio = db.Column(db.String(10), default = 'Si')
    justificacion = db.Column(db.String(30),nullable=True)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('Estudiante.id'),nullable=False)
    def __init__(self,fecha='',codigoClase='',estudiante_id='',asistio='si',justificacion=''):
        self.fecha=fecha
        self.codigoClase=codigoClase
        self.asistio=asistio
        self.justificacion=justificacion
        self.estudiante_id=estudiante_id