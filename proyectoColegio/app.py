import mysql.connector
from flask import *
from flask_wtf import *
from forms import losforms, borrar

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mikeysecreta'

#conexion a base de datos
def conectar():
    conexion = mysql.connector.connect(
        user="root",
        password="ajlz_74840106",
        host="localhost",
        database="proyectocole",
        port="3306")
    cursor = conexion.cursor(dictionary=True)
    return conexion, cursor

#PAGINAS CON FORMULARIO ALUMNO
@app.route("/agregarAlumno", methods=["GET", "POST"])
def formularioAlumnos():
    aga = losforms(request.form)
    if request.method == "POST" and aga.validate:
        nombre = aga.nombres.data
        apellidoPa = aga.apellidoPaterno.data
        apellidoMa = aga.apellidoMaterno.data
        dni = aga.dni.data
        nroApo = aga.nro.data
        grado = aga.grado.data
        seccion = aga.seccion.data
        
        # registro en la base de datos
        try:
            conexion, cursor = conectar()
            cursor.execute(
                f"""
                INSERT INTO `proyectocole`.`alumno` (`nombreCompleto`, `tipoUsuario`, `dni`, `telf`, `grado`, `seccion`, `estado`)
                VALUES ('{aga.apellidoPaterno.data + " "+ aga.apellidoMaterno.data+ ", " + aga.nombres.data}', '{3}', '{aga.dni.data}', '{aga.nro.data}', '{aga.grado.data}', '{aga.seccion.data}', {1});
                """)
            conexion.commit()
        except:
            print("ERROR A: ERROR AL INSERTAR UN NUEVO ALUMNO")
        finally:
            conexion.close()
            return redirect(url_for("alumnos"))
        
    return render_template("alumnos/agregarAlumno.html", aga=aga) 

@app.route("/xAlumno/<int:id>", methods=["GET", "POST"])
def deshabilitarAlumno(id):
    deshAlumno(id)
    return redirect(url_for("alumnos"))

@app.route("/alumnos", methods=["GET", "POST"])     
def alumnos():            
    listado = listar()
    return render_template("alumnos/listaAlumnos.html", listado = listado)
 
@app.route("/actualizarAlumno/<int:id>", methods=["GET", "POST"])
def actAlumnos(id):
    act = losforms(request.form)
    if request.method == "POST" and act.validate:
        dni = act.dni.data  
        nombre = act.nombres.data
        apellidoPa = act.apellidoPaterno.data
        apellidoMa = act.apellidoMaterno.data
        nroApo = act.nro.data
        grado = act.grado.data
        seccion = act.seccion.data
        estado = act.seccion.data
        
        # registro en la base de datos
        try:
            conexion, cursor = conectar()
            cursor.execute(
                f"""
               UPDATE `proyectocole`.`alumno`
                SET `nombreCompleto` = '{act.apellidoPaterno.data + " "+ act.apellidoMaterno.data+ ", " + act.nombres.data}', `dni` = {act.dni.data},
                `telf` = {act.nro.data}, `grado` = '{act.grado.data}', `seccion` = '{act.seccion.data}', `estado` = '{act.estado.data}'
                WHERE `id` = {id};
                """)
            conexion.commit()
        except:
            print("ERROR D: ERROR AL EDITAR UN ALUMNO")
        finally:
            conexion.close()
            return redirect(url_for("inicio"))
        
    return render_template("alumnos/actualizarAlumno.html", act=act)
         
#PAGINAS CON FORMULARIO PROFESOR
@app.route("/agregarProfesor", methods=["GET", "POST"])
def formularioProfesor():
    agp = losforms(request.form)
    if request.method == "POST" and agp.validate:
        nombre = agp.nombres.data
        apellidoPa = agp.apellidoPaterno.data
        apellidoMa = agp.apellidoMaterno.data
        dni = agp.dni.data
        nro = agp.nro.data
        tutoria = agp.tutor.data
        
        #conexion a base de datos
        try:
            conexion, cursor = conectar()
            cursor.execute(
                f"""
                INSERT INTO `proyectocole`.`profesor`
                (`nombreCompleto`, `tipoUsuario`, `dni`, `telefono`, `tutoria`, `estado`)
                VALUES
                ('{agp.apellidoPaterno.data + " "+ agp.apellidoMaterno.data+ ", " + agp.nombres.data}', '{2}', '{agp.dni.data}', '{agp.nro.data}',
                '{agp.tutor.data}', '{1}');
                """
            )
            conexion.commit()  
        except:
            print("ERROR A02: ERROR AL INSERTAR UN NUEVO PROFESOR")   
        finally:
            conexion.close()
            return redirect(url_for("inicio"))      
 
    return render_template("profesores/agregarProfesor.html", agp=agp)

@app.route("/profesores", methods=["GET", "POST"])     
def profesores():
    listadoProfesores = listarProfesor()
    return render_template("profesores/listaProfesores.html", listadoProfesores = listadoProfesores)

@app.route("/xProfesor/<int:id>", methods=["GET", "POST"])
def deshabilitarProfesor(id):
    deshProfesor(id)
    return redirect(url_for("profesores"))

@app.route("/actualizarAlumno/<int:id>", methods=["GET", "POST"])
def actProfesor(id):
    acp = losforms(request.form)
    if request.method == "POST" and acp.validate:
        nombre = acp.nombres.data
        apellidoPa = acp.apellidoPaterno.data
        apellidoMa = acp.apellidoMaterno.data
        dni = acp.dni.data
        nro = acp.nro.data
        tutoria = acp.tutor.data
        estado = acp.estado.data
        
        #conexion a base de datos
        try:
            conexion, cursor = conectar()
            cursor.execute(
                f"""
                UPDATE `proyectocole`.`profesor`
                SET `nombreCompleto` = '{acp.apellidoPaterno.data + " "+ acp.apellidoMaterno.data+ ", " + acp.nombres.data}',
                `dni` = '{acp.dni.data}', `telefono` = '{acp.nro.data}',
                `tutoria` = '{acp.tutor.data}', `estado` = '{acp.estado.data}'>
                WHERE `id` = {id};
                """
            )
            conexion.commit()  
        except:
            print("ERROR A02: ERROR AL ACTUALIZAR UN NUEVO PROFESOR")   
        finally:
            conexion.close()
            return redirect(url_for("profesores"))      
 
    return render_template("profesores/agregarProfesor.html", acp=acp)
    

#PAGINAS DE HORARIO
@app.route("/horarios")
def paginaHorario():
    return render_template("horarios/pagHorarios.html")

#paginas enlace
@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/administrar")
def admin():
    return render_template("administracion.html") 
   
  
#otras funciones  
def listar():
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        SELECT `alumno`.`id`, `alumno`.`nombreCompleto`, `alumno`.`dni`, `alumno`.`telf`,
        `alumno`.`grado`, `alumno`.`seccion`, `alumno`.`estado` FROM `proyectocole`.`alumno`;
        """)
    lista = cursor.fetchall()  
    conexion.close()
        
    return lista    
  
def listarProfesor():
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        SELECT `profesor`.`id`, `profesor`.`nombreCompleto`,
        `profesor`.`dni`, `profesor`.`telefono`, `profesor`.`tutoria`, `profesor`.`estado`
        FROM `proyectocole`.`profesor`;
        """)
    listaProfesores = cursor.fetchall()
    conexion.close()
    
    return listaProfesores         

def deshAlumno(id):
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        UPDATE `proyectocole`.`alumno`
        SET `estado` = 0
        WHERE `id` = '{id}';
        """
    )
    conexion.commit()
    cursor.close()
    conexion.close()

def deshProfesor(id):
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        UPDATE `proyectocole`.`profesor`
        SET `estado` = 0
        WHERE `id` = '{id}';
        """        
    )    
    conexion.commit()
    cursor.close()
    conexion.close()
                
if __name__ == '__main__':
    app.run(debug=True)