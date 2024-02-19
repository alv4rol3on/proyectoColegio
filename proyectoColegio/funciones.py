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

def habProfesor(id):
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        UPDATE `proyectocole`.`profesor`
        SET `estado` = 1
        WHERE `id` = '{id}';
        """        
    )    
    conexion.commit()
    cursor.close()
    conexion.close()
    
def profesoresHabilitados():
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        SELECT *
        FROM `proyectocole`.`profesor` where `estado`= 1 ;
        """)
    listaProfesores = cursor.fetchall()
    conexion.close()
    
    return listaProfesores      


#funciones admin
def listarAdmin():
    conexion, cursor = conectar()
    cursor.execute("""
        SELECT *
        FROM `proyectocole`.`admin`;
        """)

    listaAdministradores = cursor.fetchall()  
    conexion.close()
    
    return listaAdministradores

def habAdmin(id):
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        UPDATE `proyectocole`.`admin`
        SET `estado` = 1
        WHERE `id` = '{id}';
        """
    )
    conexion.commit()
    cursor.close()
    conexion.close()    
  
def deshAdmin(id):
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        UPDATE `proyectocole`.`admin`
        SET `estado` = 0
        WHERE `id` = '{id}';
        """
    )
    conexion.commit()
    cursor.close()
    conexion.close()


#funciones horarios
def horario_salon(salon, dia):
    conexion, cursor = conectar()    
    if salon and dia:
        cursor.execute(f"SELECT * FROM horario WHERE `horario`.`salon` = %s AND `horario`.`dia` = %s;", (salon, dia))
    elif salon:
        cursor.execute(f"SELECT * FROM horario WHERE `horario`.`salon` = %s;", (salon,))
    elif dia:    
        cursor.execute(f"SELECT * FROM horario WHERE `horario`.`dia` = %s;", (dia,))
    else:
        cursor.execute(f"SELECT * FROM horario;")     
        
    listaHorario = cursor.fetchall()  
    conexion.close()
        
    return listaHorario      
 
def eliminar_horario(id):
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        DELETE FROM `proyectocole`.`horario`
        WHERE `horario`.`id` = {id};
        """
    )
    conexion.commit()
    cursor.close()
    conexion.close() 
       
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
   