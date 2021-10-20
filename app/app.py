from flask import Flask, render_template, request, redirect
from utils import *
from forms.forms import *
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        formulario = FormularioIngreso()
        return render_template('login/login.html', form = formulario)
    if request.method == 'POST':
        return redirect("main")

@app.route('/main')
def main():
    return render_template('main/main.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html')

####--------------CRUD PRODUCTOS-----------------------####

@app.route('/productos')
def productos():
    return render_template('productos/productos.html', productos = listar_productos())

@app.route('/productos/crear', methods = ['GET','POST'])
def crear_producto():
    formulario = FormularioProducto()
    if request.method == "POST":
        if (formulario.validate_on_submit()):
            print("valido") 
    return render_template('productos/crear-productos.html', form = formulario)

@app.route('/productos/editar/<id>', methods = ['GET','POST'])
def editar_producto(id = int):
    formulario = FormularioProducto()
    producto = [product for product in listar_productos() if product['id'] == int(id)]
    if request.method == "POST":
        if (formulario.validate_on_submit()):
            print("valido")
    return render_template('productos/editar-productos.html', producto = producto, form = formulario, id = id)

@app.route('/productos/<id>', methods = ['DELETE'])
def eliminar_producto(id = int):
    return 1

####--------------CRUD USUARIOS-----------------------####

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios/usuarios.html', usuarios = listar_usuarios())

@app.route('/usuarios/crear', methods = ['GET','POST'])
def crear_usuario():
    formulario = FormularioUsuario()
    if request.method == "POST":
        if (formulario.validate_on_submit()):
            print("valido") 
    return render_template('usuarios/crear-usuarios.html', form = formulario)

@app.route('/usuarios/editar/<id>', methods = ['GET','POST'])
def editar_usuario(id = int):
    formulario = FormularioUsuario()
    usuario = [user for user in listar_usuarios() if user['id'] == id]
    if request.method == "POST":
        if (formulario.validate_on_submit()):
            print("valido")
    return render_template('usuarios/editar-usuarios.html', form = formulario, usuario = usuario)

@app.route('/usuarios/<id>', methods = ['DELETE'])
def eliminar_usuario(id = int):
    return 1

####--------------CRUD PROVEEDORES-----------------------####

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores/proveedores.html', proveedores = listar_proveedores())

@app.route('/proveedores/crear', methods = ['GET','POST'])
def crear_proveedor():
    formulario = FormularioProveedor()
    if request.method == "POST":
        if (formulario.validate_on_submit()):
            print("valido") 
    return render_template('proveedores/crear-proveedores.html', form = formulario)

@app.route('/proveedores/editar/<id>', methods = ['GET','POST'])
def editar_proveedor(id = int):
    formulario = FormularioProveedor()
    proveedor = [provider for provider in listar_proveedores() if provider['id'] == id]
    if request.method == "POST":
        if (formulario.validate_on_submit()):
            print("valido")
    return render_template('proveedores/editar-proveedores.html', form = formulario, proveedor = proveedor)

@app.route('/proveedores/<id>', methods = ['DELETE'])
def eliminar_proveedor(id = int):
    return 1

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
