from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired
from wtforms.validators import InputRequired, Email
from wtforms.validators import InputRequired, Length

class NewClientForm(FlaskForm):
    username = StringField('nombre:', validators=[InputRequired(message="nombre requerido")])
   
    email = StringField('correo:', validators=[
        InputRequired(message="correo requerido"),
        Email(message="El correo electrónico no es válido")
    ])
   
    password = StringField('contraseña:', validators=[
        InputRequired(message="contraseña requerida"),
        Length(min=6, message="La contraseña debe tener al menos 6 caracteres")
    ])
   
    submit = SubmitField("ingresar")

class EditClientForm(FlaskForm):
    username = StringField('nombre:', validators=[InputRequired(message="nombre requerido")])
   
    email = StringField('correo:', validators=[
        InputRequired(message="correo requerido"),
        Email(message="El correo electrónico no es válido")
    ])
   
    password = StringField('contraseña:', validators=[
        InputRequired(message="contraseña requerida"),
        Length(min=6, message="La contraseña debe tener al menos 6 caracteres")
    ])
    submit = SubmitField("registrar")