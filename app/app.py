from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login/login.html')
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
    return render_template('productos/productos.html')

@app.route('/productos/crear', methods = ['GET','POST'])
def crear_producto():
    return render_template('productos/crear-productos.html')

@app.route('/productos/editar/<id>', methods = ['GET','POST'])
def editar_producto(id = int):
    return render_template('productos/editar-productos.html')

@app.route('/productos/<id>', methods = ['DELETE'])
def eliminar_producto(id = int):
    return 1

####--------------CRUD USUARIOS-----------------------####

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios/usuarios.html')

@app.route('/usuarios/crear', methods = ['GET','POST'])
def crear_usuario():
    return render_template('usuarios/crear-usuarios.html')

@app.route('/usuarios/editar/<id>', methods = ['GET','POST'])
def editar_usuario(id = int):
    return render_template('usuarios/editar-usuarios.html')

@app.route('/usuarios/<id>', methods = ['DELETE'])
def eliminar_usuario(id = int):
    return 1

####--------------CRUD PROVEEDORES-----------------------####

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores/proveedores.html')

@app.route('/proveedores/crear', methods = ['GET','POST'])
def crear_proveedor():
    return render_template('proveedores/crear-proveedores.html')

@app.route('/proveedores/editar/<id>', methods = ['GET','POST'])
def editar_proveedor(id = int):
    return render_template('proveedores/editar-proveedores.html')

@app.route('/proveedores/<id>', methods = ['DELETE'])
def eliminar_proveedor(id = int):
    return 1

if __name__ == '__main__':
    app.run(debug = True, port = 8000)
