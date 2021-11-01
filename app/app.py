from flask import Flask, render_template, request, redirect, url_for, session
from utils import *
from forms.forms import *
from werkzeug.security import check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods = ['GET', 'POST'])
def login():
    formulario = FormularioIngreso()
    if request.method == 'POST':
        if (formulario.validate_on_submit()):
            correo = formulario.correo.data
            usuario = obtener_usuario_correo(correo)
            if usuario is None:
                return "El usuario no existe"
            else:
                clave = formulario.clave.data
                if check_password_hash(usuario[2],clave):
                    session["usuario"] = usuario
                    session["rol"] = usuario[4]
                    return redirect("main")
                else:
                    return "Contraseña incorrecta"
    return render_template('login/login.html', form = formulario)

@app.route('/cerrar')
def cerrar():
    if "usuario" in session:
        session.clear()
        return redirect('/')
    else:
        return render_template('error/error.html')

@app.route('/main')
def main():
    if "usuario" in session:
        return render_template('home/home.html', rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/error')
def error():
    return render_template('error/error.html')

@app.route('/dashboard')
def dashboard():
    if "usuario" in session:
        return render_template('dashboard/dashboard.html',                             
                                productos = obtener_productos_dash(),
                                cant_user = cantidad_usuario(),
                                cant_produ = cantidad_productos(),
                                cant_prove = cantidad_proveedores(),
                                rol = session["rol"])
    else:
        return render_template('error/error.html')

####--------------CRUD PRODUCTOS-----------------------####

@app.route('/productos')
def productos():
    if "usuario" in session:
        return render_template('productos/productos.html', productos = obtener_productos(), rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/productos/crear', methods = ['GET','POST'])
def crear_producto():
    if "usuario" in session:
        formulario = FormularioProducto()
        if request.method == "POST":
            if (formulario.validate_on_submit()):
                if insertar_producto(formulario):
                    return redirect(url_for('productos'))
                else:
                    return "No se pudo guardar"
        return render_template('productos/crear-productos.html', form = formulario, rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/productos/editar/<id>', methods = ['GET','POST'])
def editar_producto(id = int):
    if "usuario" in session:
        formulario = FormularioProducto()
        try:
            producto = obtener_producto(int(id))
            if producto is None:
                return "El producto no existe"
        except ValueError:
            return "Formato inválido de id"
        if request.method == "POST":
            if (formulario.validate_on_submit()):
                if actualizar_producto(formulario,id):
                    return redirect(url_for('productos'))
                else:
                    return "El producto no se pudo actualizar"
        return render_template('productos/editar-productos.html', form = formulario, producto = producto, rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/productos/eliminar/<id>', methods = ['DELETE'])
def eliminar_producto(id = int):
    if "usuario" in session:
        try:
            if quitar_producto(int(id)):
                return redirect(url_for('productos'))
            else:
                return "El producto no existe"
        except ValueError:
            return "Formato inválido de id"
    else:
        return render_template('error/error.html')

####--------------CRUD USUARIOS-----------------------####

@app.route('/usuarios')
def usuarios():
    if "usuario" in session:
        return render_template('usuarios/usuarios.html', usuarios = obtener_usuarios(), rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/usuarios/crear', methods = ['GET','POST'])
def crear_usuario():
    if "usuario" in session:
        formulario = FormularioUsuario()
        if request.method == "POST":
            if (formulario.validate_on_submit()):
                if insertar_usuario(formulario):
                    return redirect(url_for('usuarios'))
                else:
                    return "No se pudo guardar"
        return render_template('usuarios/crear-usuarios.html', form = formulario, rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/usuarios/editar/<id>', methods = ['GET','POST'])
def editar_usuario(id):
    if "usuario" in session:
        formulario = FormularioUsuario()
        try:
            usuario = obtener_usuario(int(id))
            if usuario is None:
                return "El usuario no existe"
        except ValueError:
            return "Formato inválido de id"
        if request.method == "POST":
            if (formulario.validate_on_submit()):
                if actualizar_usuario(formulario,id):
                    return redirect(url_for('usuarios'))
                else:
                    return "El usuario no se pudo actualizar"
        return render_template('usuarios/editar-usuarios.html', form = formulario, usuario = usuario, rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/usuarios/eliminar/<id>')
def eliminar_usuario(id):
    if "usuario" in session:
        try:
            if quitar_usuario(int(id)):
                return redirect(url_for('usuarios'))
            else:
                return "El usuario no existe"
        except ValueError:
            return "Formato inválido de id"
    else:
        return render_template('error/error.html')

####--------------CRUD PROVEEDORES-----------------------####

@app.route('/proveedores')
def proveedores():
    if "usuario" in session:
        return render_template('proveedores/proveedores.html', proveedores = obtener_proveedores(), rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/proveedores/crear', methods = ['GET','POST'])
def crear_proveedor():
    if "usuario" in session:
        formulario = FormularioProveedor()
        if request.method == "POST":
            if (formulario.validate_on_submit()):
                if insertar_proveedor(formulario):
                    return redirect(url_for('proveedores'))
                else:
                    return "No se pudo guardar"
        return render_template('proveedores/crear-proveedores.html', form = formulario, rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/proveedores/editar/<id>', methods = ['GET','POST'])
def editar_proveedor(id = int):
    if "usuario" in session:
        formulario = FormularioProveedor()
        try:
            proveedor = obtener_proveedor(int(id))
            if proveedor is None:
                return "El proveedor no existe"
        except ValueError:
            return "Formato inválido de id"
        if request.method == "POST":
            if (formulario.validate_on_submit()):
                if actualizar_proveedor(formulario,id):
                    return redirect(url_for('proveedores'))
                else:
                    return "El proveedor no se pudo actualizar"
        return render_template('proveedores/editar-proveedores.html', form = formulario, proveedor = proveedor, rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/proveedores/eliminar/<id>')
def eliminar_proveedor(id = int):
    if "usuario" in session:
        try:
            if quitar_proveedor(int(id)):
                return redirect(url_for('proveedores'))
            else:
                return "El proveedor no existe"
        except ValueError:
            return "Formato inválido de id"
    else:
        return render_template('error/error.html')

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
