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


##funciones para eventos
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
   
            
#funciones alumnos
def listarAlumnos():
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        SELECT `alumno`.`id`, `alumno`.`nombreCompleto`, `alumno`.`dni`, `alumno`.`telf`,
        `alumno`.`grado`, `alumno`.`seccion`, `alumno`.`estado` FROM `proyectocole`.`alumno`;
        """)
    lista = cursor.fetchall()  
    conexion.close()
        
    return lista    
  
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
   
   
#FILTRO
def filtroAlumnos(grado, seccion):   
    conexion, cursor = conectar()
    cursor.execute(
        f"""
        SELECT * FROM alumno WHERE 'grado' = '{grado}' and 'seccion' = '{seccion}';
        """)
    listaFiltrada = cursor.fetchall()   
    conexion.close()
    
    return listaFiltrada

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
   