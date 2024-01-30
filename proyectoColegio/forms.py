from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length

salones = [("3 años", "3 años"), ("4 años", "4 años"), ("5 años", "5 años"), ("1ro prim", "1ro prim"), ("2do prim", "2do prim"), 
            ("3ro prim", "3ro prim"), ("4to prim", "4to prim"), ("5to prim", "5to prim"), ("6to prim", "6to prim"),
            ("1ro sec", "1ro sec"), ("2do sec", "2do sec"), ("3ro sec", "3ro sec"), ("4to sec", "4to sec"), ("5to sec", "5to sec")]

tutoria = [("libre", "libre"), ("3 años", "3 años"), ("4 años", "4 años"), ("5 años", "5 años"), ("1ro prim", "1ro prim"), ("2do prim", "2do prim"), 
            ("3ro prim", "3ro prim"), ("4to prim", "4to prim"), ("5to prim", "5to prim"), ("6to prim", "6to prim"),
            ("1ro sec", "1ro sec"), ("2do sec", "2do sec"), ("3ro sec", "3ro sec"), ("4to sec", "4to sec"), ("5to sec", "5to sec")]

materias = [("aritmetica", "aritmetica"), ("algebra", "algebra"), ("geometria", "geometria"), ("trigonometria", "trigonometria")]
       
class losforms(FlaskForm):
    
    #global
    id = IntegerField(validators=[DataRequired()], render_kw={"placeholder": "Ingrese el id"}) 
    nombres = StringField(validators=[DataRequired()], render_kw={"placeholder": "Ingrese los nombres", "size":30})
    apellidoPaterno = StringField(validators=[DataRequired()], render_kw={"placeholder": "Ingrese el apellido paterno"})
    apellidoMaterno = StringField(validators=[DataRequired()], render_kw={"placeholder": "Ingrese el apellido materno"})
    nro = IntegerField(validators=[DataRequired()], render_kw={"placeholder": "Telefono"})
    estado = SelectField("Estado: ", choices=[(0, "Deshabilitar"), (1, "Habilitar")])
    dni = IntegerField(validators=[DataRequired(), Length(min=9, max=9)], render_kw={"placeholder": "Ingrese el dni"})
    
    #alumno
    grado = SelectField("Grado del alumno: ", choices=salones)   
    seccion = SelectField("Seccion: ", choices=[("A", "A"), ("B", "B")])
       
    #profesores
    tutor = SelectField("Tutoria: ", choices=tutoria)
    
    #acciones
    boton = SubmitField("Registrar")
    deshabilitar = SubmitField("X")
    actualizar = SubmitField("F5")
    
    
    
class borrar(FlaskForm):
    id = IntegerField("Id de la persona: ", validators=[DataRequired()])  
    boton = SubmitField("Borrar de los registros")     
    
class filtro(FlaskForm):
    grado = SelectField("Grado del alumno: ", choices=salones)    
    buscar = SubmitField("Buscar")
    
   