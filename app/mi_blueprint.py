from flask import Blueprint

#Crear y configurar el blueprint
mi_blueprint = Blueprint('mi_blueprint', 
                         __name__,
                         url_prefix = '/ejemplo'  )

#Crear ruta para el blueprint
@mi_blueprint.route('/saludo')
def saludo():
    return 'chamba'