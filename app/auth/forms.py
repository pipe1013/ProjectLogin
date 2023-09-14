from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField ,SubmitField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField(
                label = 'nombre de usuario:' ,
                validators=[InputRequired(
                    message="Nombre requerido")])
    
    password = PasswordField(
        label = 'password' ,
        validators=[InputRequired(
            message = "password requerido")
        ])
    
    submimt = SubmitField("Iniciar Sesión")
    
    
    
    
    
 