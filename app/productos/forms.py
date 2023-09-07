from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField ,SubmitField
from wtforms.validators import InputRequired,NumberRange
from  flask_wtf.file import FileField, FileRequired, FileRequired, FileAllowed

class ProductForm():
    nombre = StringField('Ingrese el nombre del cliente :',
                         validators=[InputRequired(message="Nombre del cliente")])
    email = StringField('Ingrese el correo :', validators=[
                                                    InputRequired(message="Perecio fuera de rango"),
                                                    NumberRange(message="Precio fuera de rango",
                                                                        min =1000,
                                                                        max = 100000)
                                                     ])

class NewProductForm(FlaskForm, ProductForm):
    imagen =FileField(validators=[FileRequired(
                                        message="debe ingresar un archivo"
                                        ),
                                  FileAllowed(["jpg", "png"],
                                                message="solo se admiten imagenes"
                                                ) ] ,
                      label="Ingrese imagen del producto:")
    submit = SubmitField("Registrar")

class EditProductForm(FlaskForm, ProductForm):
    submit = SubmitField("Editar")