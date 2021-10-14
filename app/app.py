from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main/main.html')

@app.route('/productos')
def productos():
    return render_template('productos/productos.html')

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores/proveedores.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios/usuarios.html')

@app.route('/usuarios/editar')
def editarUsuarios():
    return render_template('usuarios/editar-usuarios.html')

@app.route('/usuarios/crear')
def crearUsuarios():
    return render_template('usuarios/crear-usuarios.html')

@app.route('/proveedores/editar')
def editarProveedores():
    return render_template('proveedores/editar-proveedores.html')

@app.route('/proveedores/crear')
def crearProveedores():
    return render_template('proveedores/crear-proveedores.html')

if __name__ == '__main__':
    app.run(debug = True, port = 8000)