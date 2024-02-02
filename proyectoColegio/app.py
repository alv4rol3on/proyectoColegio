import mysql.connector
from flask import *
from flask_wtf import *
from forms import losforms, busqueda, eventos
from datetime import date
from funciones import *

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

@app.route("/alumnos/<int:id>", methods=["GET", "POST"])
def deshabilitarAlumno(id):
    deshAlumno(id)
    return redirect(url_for("alumnos"))

@app.route("/alumnos", methods=["GET", "POST"])     
def alumnos():  
    listado = listarAlumnos()       
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
        estado = act.estado.data
        
        # registro en la base de datos
        try:
            conexion, cursor = conectar()
            cursor.execute(
                f"""
               UPDATE `proyectocole`.`alumno`
                SET `nombreCompleto` = '{act.apellidoPaterno.data + " "+ act.apellidoMaterno.data+ ", " + act.nombres.data}', `dni` = {act.dni.data},
                `telf` = {act.nro.data}, `grado` = '{act.grado.data}', `seccion` = '{act.seccion.data}', `estado` = {act.estado.data}
                WHERE `id` = {id};
                """)
            conexion.commit()
        except:
            print("ERROR A2: ERROR AL EDITAR UN ALUMNO")
        finally:
            conexion.close()
            return redirect(url_for("inicio"))
        
    return render_template("alumnos/actualizarAlumno.html", act=act)   

@app.route("/filtrado", methods=["GET", "POST"])
def filtrar():
    filtro = busqueda(request.form)
    if request.method == "POST":
        grado = filtro.grado.data
        seccion = filtro.seccion.data
        #estado = filtro.estado.data
        #listaFiltrada = filtroAlumnos(filtro.grado.data, filtro.seccion.data)
        #print(filtroAlumnos(filtro.grado.data, filtro.seccion.data))
        return redirect(url_for('resultados', grado=grado, seccion=seccion))
    
    return render_template('alumnos/filtrosAlumnos.html', filtro=filtro)
 
@app.route("/filtradoResultado/<grado>/<seccion>", methods=["GET", "POST"])
def resultados(grado, seccion):
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        SELECT * FROM alumno WHERE 'grado' = '{grado}' and 'seccion' = '{seccion}';
        """)
    listaFiltrada = cursor.fetchall() 
    print(listaFiltrada)
    
      
    return render_template("alumnos/filtroResultadoAlumnos.html", grado=grado, seccion=seccion, listaFiltrada=listaFiltrada)  
            
            
            
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
            print("ERROR B: ERROR AL INSERTAR UN NUEVO PROFESOR")   
        finally:
            conexion.close()
            return redirect(url_for("inicio"))      
 
    return render_template("profesores/agregarProfesor.html", agp=agp)

@app.route("/profesores", methods=["GET", "POST"])     
def profesores():
    listadoProfesores = listarProfesor()
    return render_template("profesores/listaProfesores.html", listadoProfesores = listadoProfesores)

@app.route("/Profesor/<int:id>", methods=["GET", "POST"])
def deshabilitarProfesor(id):
    deshProfesor(id)
    return redirect(url_for("profesores"))

@app.route("/actualizarProfesor/<int:id>", methods=["GET", "POST"])
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
                `dni` = {acp.dni.data}, `telefono` = {acp.nro.data},
                `tutoria` = '{acp.tutor.data}', `estado` = '{acp.estado.data}'
                WHERE `id` = {id};
                """)
            conexion.commit()  
        except:
            print("ERROR B2: ERROR AL EDITAR UN NUEVO PROFESOR")   
        finally:
            conexion.close()
            return redirect(url_for("profesores"))      
 
    return render_template("profesores/actualizarProfesor.html", acp=acp)
    
    
  
#PAGINA EVENTOS
@app.route("/eventos")
def eventosPagina():
    listaEventos = listarEventos()
    
    return render_template("eventos/eventos.html", listarEventos=listaEventos)

@app.route("/eventos/crearEvento", methods=["GET", "POST"])
def crearEventos():
    ev = eventos(request.form)
    if request.method == "POST" and ev.validate:
        titulo = ev.titulo.data
        tipoEvento = ev.tipoEvento.data
        fecha = ev.fecha.data
        hora = ev.hora.data
        descripcion = ev.descripcion.data
        lugar = ev.lugar.data
        enlace = ev.enlace.data
        
        #BBDD
        try:
            conexion, cursor = conectar()
            cursor.execute(
                f"""
                INSERT INTO `proyectocole`.`eventos`
                (`nombreEvento`, `fechaEvento`, `hora`, `tipoEvento`, `descripcion`,
                `lugar`, `enlace`, `fechaCreacion`)
                VALUES
                ('{titulo}', '{fecha}',
                '{hora}', '{tipoEvento}',
                '{descripcion}', '{lugar}',
                '{enlace}', '{date.today()}');
                """
            )
            conexion.commit()
        except:
            print("ERROR C: ERROR AL INSERTAR UN NUEVO ALUMNO")
        finally:
            conexion.close()
            return redirect(url_for("eventosPagina"))
        
    return render_template("eventos/crearEvento.html", ev=ev)

@app.route("/eventosX/<int:id>")
def deshabilitarEvento(id):
    deshEvento(id)
    return redirect(url_for("eventosPagina"))

@app.route("/eventosA/<int:id>")
def habilitarEvento(id):
    habEvento(id)
    return redirect(url_for("eventosPagina"))

    
#paginas enlace
@app.route("/", methods=["GET", "POST"])
def inicio():
    listaEventos = eventosInicio()
    return render_template("inicio.html", listarEventos=listaEventos)
  

if __name__ == '__main__':
    app.run(debug=True)