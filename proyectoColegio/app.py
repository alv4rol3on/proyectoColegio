import mysql.connector
from flask import *
from flask_wtf import *
from forms import agregarAlumno, agregarProfe, borrar

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mikeysecreta'

#conexion a base de datos
def conectar():
    conexion = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="proyectocole",
        port="3307")
    cursor = conexion.cursor()
    return conexion, cursor


#PAGINAS CON FORMULARIO ALUMNO
@app.route("/agregarAlumno", methods=["GET", "POST"])
def formularioAlumnos():
    aga = agregarAlumno(request.form)
    if request.method == "POST" and aga.validate:
        nombre = aga.nombres.data
        apellidoPa = aga.apellidoPaterno.data
        apellidoMa = aga.apellidoMaterno.data
        nroApo = aga.nroApoderado.data
        grado = aga.grado.data
        seccion = aga.seccion.data
        
        # registro en la base de datos
        try:
            conexion, cursor = conectar()
            cursor.execute(
                f"""
                INSERT INTO `alumnos`(`nombre`, `apellido`, `grado`, `seccion`) VALUES ('{aga.nombre.data}','{aga.apellido.data}','{aga.grado.data}','{aga.seccion.data}')
                """)
            conexion.commit()
            return redirect(url_for("inicio.html"))
        except:
            print("ERROR A: ERROR AL INSERTAR UN NUEVO ALUMNO")
        finally:
            conexion.close()
            return redirect("inicio")
        
    return render_template("agregarAlumno.html", aga=aga) 

@app.route("/borrarAlumno", methods=["GET", "POST"])
def borrarAlumnos():
    ba = borrar(request.form)
    if request.method == "POST" and ba.validate:
        id = ba.id.data
        
        #registro de base de datos
    
    return render_template("borrarAlumno.html", ba=ba)    
    
#PAGINAS CON FORMULARIO PROFESOR
@app.route("/agregarProfesor", methods=["GET", "POST"])
def formularioProfesor():
    agp = agregarProfe(request.form)
    if request.form == "POST" and agp.validate:
        nombre = agp.nombre.data
        apellido = agp.apellido.data
        telefono = agp.telefono.data
        email = agp.email.data
        salon = agp.salon.data
 
    return render_template("agregarProfesor.html", agp=agp)
        


#paginas enlace
@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/administrar")
def admin():
    return render_template("administracion.html") 
   
if __name__ == '__main__':
    app.run(debug=True)