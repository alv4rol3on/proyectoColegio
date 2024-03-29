from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, DateField, TimeField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length

salones = [("3 años", "3 años"), ("4 años", "4 años"), ("5 años", "5 años"), ("1ro prim", "1ro prim"), ("2do prim", "2do prim"), 
            ("3ro prim", "3ro prim"), ("4to prim", "4to prim"), ("5to prim", "5to prim"), ("6to prim", "6to prim"),
            ("1ro sec", "1ro sec"), ("2do sec", "2do sec"), ("3ro sec", "3ro sec"), ("4to sec", "4to sec"), ("5to sec", "5to sec")]

tutoria = [("libre", "libre"), ("3 anhos", "3 años"), ("4 anhos", "4 años"), ("5 anhos", "5 años"), ("1ro prim", "1ro prim"), ("2do prim", "2do prim"), 
            ("3ro prim", "3ro prim"), ("4to prim", "4to prim"), ("5to prim", "5to prim"), ("6to prim", "6to prim"),
            ("1ro sec", "1ro sec"), ("2do sec", "2do sec"), ("3ro sec", "3ro sec"), ("4to sec", "4to sec"), ("5to sec", "5to sec")]

dia = [("Lunes", "Lunes"), ("Martes", "Martes"), ("Miercoles", "Miercoles"), ("Jueves", "Jueves"), ("Viernes", "Viernes")]

materias = [("Aritmetica", "Aritmetica"), ("Algebra", "Algebra"), ("Geometria", "Geometria"), ("Trigonometria", "Trigonometria"), ("Biologia", "Biología"), ("Quimica", "Quimica"), ("Ed. física", "Ed. física")]
       
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
    
    #admin
    user = StringField(validators=[DataRequired()], render_kw={"placeholder": "Ingrese el nombre de usuario", "size":30})
    password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Ingrese la contraseña", "size":30})


#filtro   
class busqueda(FlaskForm):
    grado = SelectField("Grado del alumno: ", choices=salones)
    seccion = SelectField("Seccion: ", choices=[("A", "A"), ("B", "B")])
    estado = IntegerField(render_kw={"placeholder": "Estado"})
    boton = SubmitField("Buscar")
       
#eventos 
class eventos(FlaskForm):
    titulo = StringField(validators=[DataRequired()], render_kw={"placeholder": "Ingrese el título del evento"})  
    tipoEvento = SelectField("Tipo de evento: ", choices=[("Anuncio", "Anuncio"), ("Invitacion", "Invitacion")])
    fecha = DateField('Fecha del evento:', validators=[DataRequired()]) 
    hora = TimeField("Hora: ")
    descripcion = TextAreaField(validators=[DataRequired()], render_kw={"placeholder": "Ingrese la descripcion del evento"})
    lugar = StringField("Lugar del evento: ", render_kw={"placeholder": "Lugar del evento(opcional)"})
    enlace = StringField(render_kw={"placeholder": "Ingrese un enlace(opcional)"})
    boton = SubmitField("Crear evento")
    
#horarios
class horarios(FlaskForm):
    profesor = SelectField('Profesor', coerce=str)
    salon = SelectField("Salón ", choices=salones)  
    dia = SelectField("Dia ", choices=dia)
    curso = SelectField("Curso ", choices=materias)
    hora_inicio = TimeField('Hora de inicio', validators=[DataRequired()])
    hora_fin = TimeField('Hora de fin', validators=[DataRequired()])
    boton = SubmitField("Crear turno")
    
class login(FlaskForm):    
    usuario = StringField(validators=[DataRequired()], render_kw={"placeholder": "Ingrese el usuario"})
    password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Ingrese la contraseña"})
    boton = SubmitField("Iniciar sesión")