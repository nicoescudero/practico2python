import os
import pymysql
from sqlalchemy import exc
from flask import Flask,request,render_template,redirect
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['URI_DB']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db,Asistencia,Curso,Estudiante,Padre,Preceptor

@app.route('/',methods = ['GET'])
def index(): return render_template('index.html')

@app.route('/home', methods = ['GET'])
def home():return render_template('main.html')

@app.route('/login',methods = ['POST'])
def login():
	try:
		correo = request.form.get('correo')
		clave = request.form.get('clave')
		user = Preceptor.query.filter_by(correo=correo).first()
		if (user == None): return 'Not Found',404
		if (user.clave == clave):
			return redirect('/home')
	except:
		return render_template('error.html')

@app.route('/asistencia', methods = ['POST'])
def registar():
	try:
		fecha = request.form.get('fecha')
		codigo = request.form.get('codigo')
		asistio = request.form.get('asistio')
		justificacion = request.form.get('justificacion')
		estudianteID = request.form.get('estudianteID')
		print(fecha)
		data = Asistencia(fecha,codigo,estudianteID,asistio,justificacion)
		db.session.add(data)
		db.session.commit()
		return render_template('success.html')
	except:
		return 'error',404
	
@app.route('/listado', methods = ['GET'])
def listado():
	try:
		data = Asistencia.query.all()
		print(data)
		return render_template('listado.html',inasistencias = data)
	except:
		return 'SOME ERROR',404
with app.app_context():
	    db.create_all()
if __name__ == '__main__':
	app.run(debug = True)