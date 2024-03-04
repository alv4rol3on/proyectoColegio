from random import randint

#Generador ID unico
def generadorID_Admin(nombre, apellidoPa, apellidoMa):
    c1 = nombre[0:2].upper()
    c2 = apellidoPa[0:2].upper()
    c3 = apellidoMa[0:3].upper()
    aleatorio = randint(0,9999)
    
    resultado = f"ASC_{c1}{c2}{c3}{aleatorio}"
    print(f" el ID generado es: {resultado}")
    
    return resultado 

def generadorID_Alumno(nombre, apellidoPa, apellidoMa):
    c1 = nombre[0:2].upper()
    c2 = apellidoPa[0:2].upper()
    c3 = apellidoMa[0:3].upper()
    aleatorio = randint(10000,99999)
    
    resultado = f"STU_{c1}{c2}{c3}{aleatorio}"
    print(f" el ID generado es: {resultado}")
    
    return resultado 
