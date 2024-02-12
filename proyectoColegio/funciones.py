import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        user="root",
        password="ajlz_74840106",
        host="localhost",
        database="proyectocole",
        port="3306")
    cursor = conexion.cursor(dictionary=True)
    return conexion, cursor


#funciones para eventos
def listarEventos():
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        SELECT *
        FROM `proyectocole`.`eventos`;   
        """)
    listaEventos = cursor.fetchall()
    conexion.close()
    
    return listaEventos

def habEvento(id):
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        UPDATE `proyectocole`.`eventos`
        SET `estado` = 1
        WHERE `id` = {id};
        """
    )    
    conexion.commit()
    cursor.close()
    conexion.close()
     
def deshEvento(id):
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        UPDATE `proyectocole`.`eventos`
        SET `estado` = 0
        WHERE `id` = {id};
        """
    )
    conexion.commit()
    cursor.close()
    conexion.close()
 
def borrarEvento(id):
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        DELETE FROM `proyectocole`.`eventos`
        WHERE id = {id};
        """
    )
    conexion.commit()
    cursor.close()
    conexion.close()       



#alumnos
def listarAlumnos(grado=None, seccion=None, estado=None):
    conexion, cursor = conectar()

    if grado and seccion and estado:
        cursor.execute(
            f"""
            SELECT `alumno`.`id`, `alumno`.`nombreCompleto`, `alumno`.`dni`, `alumno`.`telf`,
            `alumno`.`grado`, `alumno`.`seccion`, `alumno`.`estado` FROM `proyectocole`.`alumno`
            WHERE `alumno`.`grado` = %s AND `alumno`.`seccion` = %s and `alumno`.`estado` = %s;
            """, (grado, seccion, estado))
    elif grado:
        cursor.execute(
            f"""
            SELECT `alumno`.`id`, `alumno`.`nombreCompleto`, `alumno`.`dni`, `alumno`.`telf`,
            `alumno`.`grado`, `alumno`.`seccion`, `alumno`.`estado` FROM `proyectocole`.`alumno`
            WHERE `alumno`.`grado` = %s;
            """, (grado,))
    elif seccion:
        cursor.execute(
            f"""
            SELECT `alumno`.`id`, `alumno`.`nombreCompleto`, `alumno`.`dni`, `alumno`.`telf`,
            `alumno`.`grado`, `alumno`.`seccion`, `alumno`.`estado` FROM `proyectocole`.`alumno`
            WHERE `alumno`.`seccion` = %s;
            """, (seccion,))
    elif estado:
        cursor.execute(
            f"""
            SELECT `alumno`.`id`, `alumno`.`nombreCompleto`, `alumno`.`dni`, `alumno`.`telf`,
            `alumno`.`grado`, `alumno`.`seccion`, `alumno`.`estado` FROM `proyectocole`.`alumno`
            WHERE `alumno`.`estado` = %s;
            """, (estado,))
    else:
        cursor.execute(
            f"""
            SELECT `alumno`.`id`, `alumno`.`nombreCompleto`, `alumno`.`dni`, `alumno`.`telf`,
            `alumno`.`grado`, `alumno`.`seccion`, `alumno`.`estado` FROM `proyectocole`.`alumno`;
            """)

    lista = cursor.fetchall()  
    conexion.close()
        
    return lista       

def habAlumno(id):
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        UPDATE `proyectocole`.`alumno`
        SET `estado` = 1
        WHERE `id` = '{id}';
        """
    )
    conexion.commit()
    cursor.close()
    conexion.close()    
  
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

#funciones profesor
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



#funciones admin
def listarAdmin():
    conexion, cursor = conectar()
    cursor.execute("""
        SELECT `admin`.`id`,
        `admin`.`nombre`, `admin`.`apellido`, `admin`.`usuario`
        FROM `proyectocole`.`admin`;
        """)

    listaAdministradores = cursor.fetchall()  
    conexion.close()
    
    return listaAdministradores

#inicio  
def eventosInicio():
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        SELECT * FROM `proyectocole`.`eventos` 
        where `eventos`.`estado` = 1;;   
        """)
    listaEventos = cursor.fetchall()
    conexion.close()
    
    return listaEventos
   