import os
from flask import Flask,request,render_template,redirect
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['URI_DB']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db,Asistencia,Curso,Estudiante,Padre,Preceptor

@app.route('/',methods = ['GET'])
def index(): return render_template('index.html',message='')

@app.route('/home', methods = ['GET'])
def home():return render_template('main.html',message='')

@app.route('/login',methods = ['POST'])
def login():
	try:
		correo = request.form.get('correo')
		clave = request.form.get('clave')
		user = Preceptor.query.filter_by(correo=correo).first()
		if (user == None):
			return render_template('index.html',message = 'Usuario no encontrado')
		if (user.clave == clave):
			return redirect('/home')
		return render_template('index.html',message = 'Contraseña incorrecta')
	except:
		return render_template('index.html',message = 'Email o Contraseña Incorrectos')

@app.route('/asistencia', methods = ['POST'])
def registar():
	try:
		fecha = request.form.get('fecha')
		codigo = request.form.get('codigo')
		asistio = request.form.get('asistio')
		justificacion = request.form.get('justificacion')
		estudianteID = request.form.get('estudianteID')
		data = Asistencia(fecha,codigo,estudianteID,asistio,justificacion)
		db.session.add(data)
		db.session.commit()
		return render_template('main.html',message='Asistencia registrada')
	except:
		return render_template('error.html')
	
@app.route('/listado', methods = ['GET'])
def listado():
	try:
		data = Asistencia.query.all()
		return render_template('listado.html',inasistencias = data)
	except:
		return render_template('error.html')

with app.app_context():
	    db.create_all()

if __name__ == '__main__':
	app.run(debug = True)