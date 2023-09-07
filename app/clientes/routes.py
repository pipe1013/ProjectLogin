from . import clientes
from flask import render_template, redirect,flash
from .forms import NewClientForm, EditClientForm
import app
import os 


 
# Crear las rutas del blueprint
@clientes.route('/crear', methods=["GET", "POST"])
def crear():
    c = app.models.Cliente()  # Usa el modelo Cliente
    form = NewClientForm()  # Usa el formulario ClienteForm
    if form.validate_on_submit():
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()
        flash("Registro Existoso!!")
        return redirect('/clientes/listar')
    return render_template('newclientes.html', form=form)

@clientes.route('/listar')
def listar():
    clientes = app.models.Cliente.query.all()  # Usa el modelo Cliente
    return render_template('listarclientes.html', clientes=clientes)

@clientes.route('/editar/<int:cliente_id>', methods=['GET', 'POST'])  # Agregamos <int:cliente_id> para capturar el ID
def editar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)  # Usa el modelo Cliente

    form_edit = EditClientForm(obj=p)  # Usa el formulario EditClienteForm
    if form_edit.validate_on_submit():
        form_edit.populate_obj(p)
        app.db.session.commit()
        flash("Cliente editado exitosamente!!")
        return redirect("/clientes/listar")
        
    return render_template('newclientes.html', form=form_edit)

@clientes.route('/eliminar/<int:cliente_id>', methods=['GET', 'POST'])  # Agregamos <int:cliente_id> para capturar el ID
def eliminar(cliente_id):
    c = app.models.Cliente.query.get(cliente_id)  # Usa el modelo Cliente
    
    app.db.session.delete(c)
    app.db.session.commit()
    flash("Cliente eliminado!!")
    return redirect("/clientes/listar")
