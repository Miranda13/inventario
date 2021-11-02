from flask import Flask, render_template, request, redirect, url_for, session, flash
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
                flash('El usuario no existe', 'error')
            else:
                clave = formulario.clave.data
                if check_password_hash(usuario[2],clave):
                    session["usuario"] = usuario
                    session["rol"] = usuario[4]
                    session["nombre"] = usuario[1]
                    return redirect("main")
                else:
                    flash('Contraseña inválida', 'error')
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
        return render_template('home/home.html', rol = session["rol"], nombre = session["nombre"])
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

@app.route('/productos/reporte')
def reporte_productos():
    if "usuario" in session:
        return render_template('productos/reporte.html', productos = obtener_productos_dash(), rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/productos/crear', methods = ['GET','POST'])
def crear_producto():
    if "usuario" in session:
        formulario = FormularioProducto()
        proveedores = [(prov["proveedor_id"],prov["nombre"]) for prov in obtener_proveedores()]
        formulario.nombre_proveedor.choices = proveedores
        if request.method == "POST":
            if (formulario.validate_on_submit()):
                if insertar_producto(formulario):
                    flash('El producto se guardó con éxito', 'info')
                    return redirect(url_for('productos'))
                else:
                    flash('No se pudo guardar','error')
        return render_template('productos/crear-productos.html', form = formulario, rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/productos/<id>')
def detalle_producto(id):
    if "usuario" in session:
        formulario = FormularioProducto()
        producto = obtener_producto(id)
        proveedores = obtener_productos_proveedores(id)
        return render_template('productos/detalles-producto.html', form = formulario, producto = producto, proveedores = proveedores, rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/productos/editar/<id>', methods = ['GET','POST'])
def editar_producto(id = int):
    if "usuario" in session:
        formulario = FormularioProducto()
        proveedores = [(prov["proveedor_id"],prov["nombre"]) for prov in obtener_proveedores()]
        formulario.nombre_proveedor.choices = proveedores
        try:
            producto = obtener_producto(int(id))
            if producto is None:
                flash('El producto no existe','error')
        except ValueError:
            return "Formato inválido de id"
        if request.method == "POST":
            if (formulario.validate_on_submit()):
                if actualizar_producto(formulario,id):
                    flash('El producto se editó con éxito', 'info')
                    return redirect(url_for('productos'))
                else:
                    flash('El producto no se pudo actualizar')
        return render_template('productos/editar-productos.html', form = formulario, producto = producto, rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/productos/eliminar/<id>')
def eliminar_producto(id = int):
    if "usuario" in session:
        try:
            if quitar_producto(int(id)):
                quitar_relacion_producto(id)
                flash('El producto se eliminó con éxito', 'info')
                return redirect(url_for('productos'))
            else:
                flash('El producto no existe','error')
        except ValueError:
            flash('Formato inválido de id','error')
        return redirect(url_for('productos'))
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
                    flash('Usuario guardado con éxito', 'info')
                    return redirect(url_for('usuarios'))
                else:
                    flash('No se pudo guardar', 'error')
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
                flash('El usuario no existe','error')
        except ValueError:
            flash('Formato inválido de id','error')
        if request.method == "POST":
            if (formulario.validate_on_submit()):
                if actualizar_usuario(formulario,id):
                    flash('El usuario se editó con éxito', 'info')
                    return redirect(url_for('usuarios'))
                else:
                    flash('El usuario no se pudo actualizar','error')
        return render_template('usuarios/editar-usuarios.html', form = formulario, usuario = usuario, rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/usuarios/eliminar/<id>')
def eliminar_usuario(id):
    if "usuario" in session:
        try:
            if quitar_usuario(int(id)):
                flash('El usuario se eliminó con éxito', 'info')
                return redirect(url_for('usuarios'))
            else:
                flash('El usuario no existe','error')
        except ValueError:
            flash('Formato inálido de id','error')
        return redirect(url_for('usuarios'))
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
                    flash('El proveedor se creó con éxito', 'info')
                    return redirect(url_for('proveedores'))
                else:
                    flash('No se pudo guardar el proveedor', 'error')
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
                flash('El proveedor no existe', 'error')
        except ValueError:
            flash('Formato inválido de id', 'error')
        if request.method == "POST":
            if (formulario.validate_on_submit()):
                if actualizar_proveedor(formulario,id):
                    flash('El proveedor se editó con éxito', 'info')
                    return redirect(url_for('proveedores'))
                else:
                    flash('El proveedor no se pudo actualizar', 'error')
        return render_template('proveedores/editar-proveedores.html', form = formulario, proveedor = proveedor, rol = session["rol"])
    else:
        return render_template('error/error.html')

@app.route('/proveedores/eliminar/<id>')
def eliminar_proveedor(id = int):
    if "usuario" in session:
        try:
            if quitar_proveedor(int(id)):
                quitar_relacion_proveedor(id)
                flash('El proveedor se eliminó con éxito', 'info')
                return redirect(url_for('proveedores'))
            else:
                flash('El proveedor no existe', 'error')
        except ValueError:
            flash('Formato inválido de id', 'error')
        return redirect(url_for('proveedores'))
    else:
        return render_template('error/error.html')

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
