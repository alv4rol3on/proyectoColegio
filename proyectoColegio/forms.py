from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, EmailField, SelectField
from wtforms.validators import DataRequired, Email

salones = [("3 años", "3 años"), ("4 años", "4 años"), ("5 años", "5 años"), ("1ro prim", "1ro prim"), ("2do prim", "2do prim"), 
            ("3ro prim", "3ro prim"), ("4to prim", "4to prim"), ("5to prim", "5to prim"), ("6to prim", "6to prim"),
            ("1ro sec", "1ro sec"), ("2do sec", "2do sec"), ("3ro sec", "3ro sec"), ("4to sec", "4to sec"), ("5to sec", "5to sec")]

tutoria = [("libre", "libre"), ("3 años", "3 años"), ("4 años", "4 años"), ("5 años", "5 años"), ("1ro prim", "1ro prim"), ("2do prim", "2do prim"), 
            ("3ro prim", "3ro prim"), ("4to prim", "4to prim"), ("5to prim", "5to prim"), ("6to prim", "6to prim"),
            ("1ro sec", "1ro sec"), ("2do sec", "2do sec"), ("3ro sec", "3ro sec"), ("4to sec", "4to sec"), ("5to sec", "5to sec")]

class agregarProfe(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()], render_kw={"placeholder": "Ingrese el nombre"})
    apellido = StringField("Apellido: ", validators=[DataRequired()], render_kw={"placeholder": "Ingrese el apellido"})
    telefono = IntegerField("Telefono: ", validators=[DataRequired()], render_kw={"placeholder": "Ingrese el telefono"})
    email = EmailField("Correo electronico: ", validators=[DataRequired(), Email()], render_kw={"placeholder": "Ingrese el correo electronico"})
    salon = SelectField("Salón de tutoria: ", choices=tutoria)   
    boton = SubmitField("Registrar nuevo docente")
    
class agregarAlumno(FlaskForm):
    nombre = StringField("Nombre: ", validators=[DataRequired()])
    apellido = StringField("Apellido: ", validators=[DataRequired()])
    grado = SelectField("Grado del alumno: ", choices=salones)   
    seccion = SelectField("Seccion: ", choices=[("A", "A"), ("B", "B"),
                                               ("C", "C"), ("D", "D"),
                                               ("E", "E"), ("F", "F")])   
    boton = SubmitField("Registrar nuevo alumno")