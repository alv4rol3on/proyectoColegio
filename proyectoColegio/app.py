import mysql.connector
from flask import *
from flask_wtf import *
from forms import *
from datetime import date
from funciones import *
from funcionesLogin import *
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mikeysecreta'

#necesario
salones = ["3 años", "4 años", "5 años", "1ro prim", "2do prim", "3ro prim",  "4to prim",  "5to prim", "6to prim", "1ro sec", "2do sec", "3ro sec", "4to sec", "5to sec"]
materias = ["Aritmetica", "Algebra", "Geometria", "Trigonometria", "Rz. Matemático", "Historia del Perú", "Historia Universal", "Geografía", "Cívica",
            "Biología", "Química", "Gramática", "Literatura", "Rz. Verbal", "Plan Lector", "Computo", "Arte", "Danza", "Ed. Física"]
dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

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

#modelo de usuario

            
#PAGINAS CON FORMULARIO ALUMNO
@app.route("/admin/agregarAlumno", methods=["GET", "POST"])
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
        
        idAlumnoGenerado = generadorID_Alumno(nombre, apellidoPa, apellidoMa)
        
        # registro en la base de datos
        try:
            conexion, cursor = conectar()
            cursor.execute(
                f"""
                INSERT INTO `proyectocole`.`alumno` (`nombreCompleto`,`usuario`, `tipoUsuario`, `dni`, `telf`, `grado`, `seccion`, `estado`)
                VALUES ('{aga.apellidoPaterno.data + " "+ aga.apellidoMaterno.data+ ", " + aga.nombres.data}', '{idAlumnoGenerado}', '{3}', '{aga.dni.data}', '{aga.nro.data}', '{aga.grado.data}', '{aga.seccion.data}', {1});
                """)
            conexion.commit()
        except Exception as e:
                    print(f"ERROR EN REGISTRAR UN ALUMNO: {str(e)}") 
        finally:
            conexion.close()
            return redirect(url_for("alumnos"))
        
    return render_template("alumnos/agregarAlumno.html", aga=aga) 

@app.route("/admin/alumnosX/<int:id>", methods=["GET", "POST"])
def deshabilitarAlumno(id):
    deshAlumno(id)
    return redirect(url_for("alumnos"))

@app.route("/admin/alumnosA/<int:id>", methods=["GET", "POST"])
def habilitarAlumno(id):
    habAlumno(id)
    return redirect(url_for("alumnos"))

@app.route("/admin/alumnos", methods=["GET", "POST"])     
def alumnos(): 
    if request.method=="POST":
        texto = request.form['buscar']
        conexion, cursor = conectar()
        cursor.execute("SELECT * FROM `proyectocole`.`alumno` WHERE `alumno`.`dni` = '%s'" % (texto,))
        resultadoBusqueda = cursor.fetchone()  
        cursor.close()
        conexion.close()
        return render_template("alumnos/resultadoBusqueda.html",resultados = resultadoBusqueda)
        
    
    if request.method=="GET":
        grado = request.args.get('grado', default=None, type=str)
        seccion = request.args.get('seccion', default=None, type=str)
        estado = request.args.get('estado', default=None, type=str)  
     
        listado = listarAlumnos(grado, seccion, estado) 
    return render_template("alumnos/listaAlumnos.html", listado = listado, salones=salones)
 
@app.route("/admin/actualizarAlumno/<int:id>", methods=["GET", "POST"])
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

                   
#PAGINAS CON FORMULARIO PROFESOR
@app.route("/admin/agregarProfesor", methods=["GET", "POST"])
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

@app.route("/admin/profesores", methods=["GET", "POST"])     
def profesores():
    listadoProfesores = listarProfesor()
    return render_template("profesores/listaProfesores.html", listadoProfesores = listadoProfesores)

@app.route("/admin/ProfesorX/<int:id>", methods=["GET", "POST"])
def deshabilitarProfesor(id):
    deshProfesor(id)
    return redirect(url_for("profesores"))

@app.route("/admin/actualizarProfesor/<int:id>", methods=["GET", "POST"])
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

@app.route("/admin/ProfesorA/<int:id>", methods=["GET", "POST"])
def habilitarProfesor(id):
    habProfesor(id)
    return redirect(url_for("profesores"))
  
    
  
#PAGINA EVENTOS
@app.route("/admin/eventos")
def eventosPagina():
    listaEventos = listarEventos()
    
    return render_template("eventos/eventos.html", listarEventos=listaEventos)

@app.route("/admin/eventos/crearEvento", methods=["GET", "POST"])
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
                `lugar`, `enlace`, `fechaCreacion`, `estado`)
                VALUES
                ('{titulo}', '{fecha}',
                '{hora}', '{tipoEvento}',
                '{descripcion}', '{lugar}',
                '{enlace}', '{date.today()}', '{1}');
                """
            )
            conexion.commit()
        except:
            print("ERROR C: ERROR AL INSERTAR UN NUEVO ALUMNO")
        finally:
            conexion.close()
            return redirect(url_for("eventosPagina"))
        
    return render_template("eventos/crearEvento.html", ev=ev)

@app.route("/admin/eventosX/<int:id>")
def deshabilitarEvento(id):
    deshEvento(id)
    return redirect(url_for("eventosPagina"))

@app.route("/admin/eventosA/<int:id>")
def habilitarEvento(id):
    habEvento(id)
    return redirect(url_for("eventosPagina"))

@app.route("/admin/eventosB/<int:id>")
def eliminarEvento(id):
    borrarEvento(id)
    return redirect(url_for("eventosPagina"))


#HORARIOS
@app.route("/admin/horarios", methods=["GET", "POST"])  
def horario():
    hr = horarios()
    listadoProfesores = profesoresHabilitados()
    hr.profesor.choices = [(profesor['nombreCompleto'], profesor['nombreCompleto']) for profesor in listadoProfesores]
    if request.method == "POST" and hr.validate:
        profesor = hr.profesor.data
        salon = hr.salon.data
        dia = hr.dia.data
        curso = hr.curso.data
        hora_inicio = hr.hora_inicio.data
        hora_fin = hr.hora_fin.data
        
        #BBDD
        try:
            # CONSULTA 1
            conexion, cursor = conectar()
            consulta = """
                SELECT * FROM `proyectocole`.`horario` WHERE `profesor` = %s
                AND `dia` = %s AND `inicio` = %s AND `fin` = %s;
            """
            valores = (hr.profesor.data, hr.dia.data, hr.hora_inicio.data, hr.hora_fin.data)
            cursor.execute(consulta, valores)
            resultado = cursor.fetchall()

            if len(resultado) == 0:
                # CONSULTA 2
                try:
                    consulta2 = """
                        SELECT * FROM `proyectocole`.`horario` WHERE `salon` = %s
                        AND `dia` = %s AND `inicio` = %s AND `fin` = %s;
                    """
                    valores2 = (hr.salon.data, hr.dia.data, hr.hora_inicio.data, hr.hora_fin.data)
                    cursor.execute(consulta2, valores2)
                    resultado = cursor.fetchall()

                    if len(resultado) == 0:
                        try:
                            # INSERTAR
                            consulta_form = """
                                INSERT INTO `proyectocole`.`horario`
                                (`profesor`, `salon`, `dia`, `curso`, `inicio`, `fin`)
                                VALUES
                                (%s, %s, %s, %s, %s, %s);
                            """
                            valores_form = (hr.profesor.data, hr.salon.data, hr.dia.data, hr.curso.data, hr.hora_inicio.data, hr.hora_fin.data)
                            cursor.execute(consulta_form, valores_form)
                            conexion.commit()

                        except Exception as e:
                            print(f"ERROR EN REGISTRAR UN HORARIO: {str(e)}")

                        finally:
                            print("CONSULTA 3 TERMINADA")
                            return redirect(url_for("horario"))

                    else:
                        print("Coincidencias encontradas en: salon, dia y horas")
                        flash("NO SE PUEDE REGISTRAR: Coincidencias encontradas en el salón y horas seleccionadas")

                except Exception as e:
                    print(f"ERROR EN REGISTRAR UN HORARIO: {str(e)}")

                finally:
                    print("CONSULTA 2 TERMINADA")

            else:
                print("Coincidencias encontradas en: profesor, dia y horas")
                flash("NO SE PUEDE REGISTRAR: Coincidencias encontradas en profesor, dia y horas")

        except Exception as e:
            print(f"ERROR EN REGISTRAR UN HORARIO: {str(e)}")

        finally:
            print("CONSULTA TERMINADA")
            conexion.close()
    
    if request.method == "GET":
        grado = request.args.get('grado', default=None, type=str)
        dia = request.args.get('dia', default=None, type=str)
        resultado = horario_salon(grado, dia)
   
    return render_template("/horarios/horariosSalon.html", resultado=resultado, salones=salones, dias=dias, listadoProfesores = listadoProfesores, hr=hr) 

@app.route("/admin/horarios/eliminar/<int:id>", methods=["GET", "POST"])
def eliminarTurno(id):
    eliminar_horario(id)
    return redirect(url_for("horario"))


#ADMIN
@app.route("/admin/crear", methods=["GET", "POST"])
def crearAdmin():
    adm = losforms(request.form)
    if request.method=="POST" and adm.validate:
        nombres = adm.nombres.data
        apellidoPa = adm.apellidoPaterno.data
        apellidoMa = adm.apellidoMaterno.data
        password = adm.password.data

        idGenerado = generadorID_Admin(nombres, apellidoPa, apellidoMa)
        
        try:
            conexion, cursor = conectar()
            cursor.execute(
                f"""
                INSERT INTO `proyectocole`.`admin`
                (`nombre`,`apellido`,`usuario`,`password`,`estado`)
                VALUES
                ('{adm.nombres.data}','{adm.apellidoPaterno.data + " " + adm.apellidoMaterno.data}','{idGenerado}','{adm.password.data}',{1});
                """
            )
            conexion.commit()  
        except Exception as e:
                    print(f"ERROR EN REGISTRAR UN ADMINISTRADOR: {str(e)}")  
                    return redirect(url_for("crearAdmin"))
        finally:
            conexion.close()
            return redirect(url_for("listadeAdmin"))  
        
    return render_template("adminpaginas/formAdmin.html", adm=adm)    
 
@app.route("/admin/lista", methods=["GET", "POST"])
def listadeAdmin():
    listaAdmin = listarAdmin()
    return render_template("adminpaginas/listaAdmin.html", listaAdmin=listaAdmin) 
 
@app.route("/adminX/<int:id>", methods=["GET", "POST"])
def deshabilitarAdmin(id):
    deshAdmin(id)
    return redirect(url_for("listadeAdmin"))

@app.route("/adminA/<int:id>", methods=["GET", "POST"])
def habilitarAdmin(id):
    habAdmin(id)
    return redirect(url_for("listadeAdmin"))
  
@app.route("/admin/editarUsuario/<int:id>", methods=["GET", "POST"])  
def actAdmin(id):
    adm = losforms(request.form)
    if request.method=="POST" and adm.validate:
        nombres = adm.nombres.data
        apellidoPa = adm.apellidoPaterno.data
        apellidoMa = adm.apellidoMaterno.data 
        password = adm.password.data

        idGenerado = generadorID_Alumno(nombres, apellidoPa, apellidoMa)

        try:
            conexion, cursor = conectar()
            cursor.execute(
                f"""
                UPDATE `proyectocole`.`admin`
                SET
                `nombre` = '{adm.nombres.data}',
                `apellido` = '{adm.apellidoPaterno.data + " " + adm.apellidoMaterno.data}',
                `password` = '{adm.password.data}'
                WHERE `id` = {id};
                """
            )
            conexion.commit()  
        except:
            print("ERROR AL ACTUALIZAR INFORMACION DEL ADMINISTRADOR")    
        finally:
            conexion.close()
            return redirect(url_for("listadeAdmin"))  
        
    return render_template("adminpaginas/actualizarAdmin.html", adm=adm)    
        
@app.route("/admin/inicio", methods=["GET", "POST"])
def inicio():
    le = eventosInicio()
    return render_template("inicio.html", le = le)    
    
#paginas enlace
@app.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for("paglogin"))
 
#ACCESO ALUMNOS
@app.route("/alumnos/inicio", methods=["GET", "POST"])
def inicioAlumno():
    listaEventos = eventosInicio()
    return render_template("AccesoAlumnos/inicioAlumno.html", listarEventos=listaEventos)

@app.route("/acceso-restringido")
def acceso_restringido_admin():
    return "Acceso restringido, solo accesible a usuarios de tipo administrador"



























#accesos
@app.route("/login", methods=["GET", "POST"])
def paglogin():
    if request.method == "POST":
        usuario = request.form['usuario']
        password = request.form['password']
        
        #BBDD
        try:
            conexion, cursor = conectar()
            consulta = (f"""SELECT * FROM `proyectocole`.`admin`
                         WHERE `usuario` = '{usuario}' AND `password` = '{password}';""")
            cursor.execute(consulta)
            resultadoAsc = cursor.fetchone()
                    
            if resultadoAsc:
                print("LOGUEO EXITOSO DE TIPO: ADMIN")
                return redirect(url_for("inicio"))
            else:
                print("Usuario o contraseña invalidas")  
                flash("Usuario o contraseña invalidas",'danger')   
                               
        except Exception as e:
            print(f"ERROR EN EL LOGUEO: {str(e)}")
        finally:  
            conexion.close()      
            print("INTENTO DE LOGUEO FINALIZADO")
    
    return render_template("login/login.html")
 
@app.route("/logout")
def logout():
    return redirect(url_for('paglogin')) 
 
@app.errorhandler(404)
def no_encontrado(error):
    return redirect(url_for('paglogin'))  

if __name__ == '__main__':
    app.run(debug=True)