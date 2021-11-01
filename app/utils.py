import sqlite3
from sqlite3 import Error
import hashlib 
from werkzeug.security import generate_password_hash

db = 'inventario.db'

def obtener_productos_dash():
    try:
        with sqlite3.connect(db) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute(
                "SELECT * FROM  productos WHERE cant_minima > cant_disponible ")
            row = cur.fetchall()
            return row
    except Error:
        print(Error)
        return Error


def cantidad_usuario():
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("SELECT COUNT(*) as conteo FROM usuarios")
            conteo = cur.fetchone()
            return conteo[0]
    except Error:
        print(Error)
        return False


def cantidad_productos():
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("SELECT COUNT(*) as conteo FROM productos")
            conteo = cur.fetchone()
            return conteo[0]
    except Error:
        print(Error)
        return False


def cantidad_proveedores():
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("SELECT COUNT(*) as conteo FROM proveedores")
            conteo = cur.fetchone()
            return conteo[0]
    except Error:
        print(Error)
        return False

def obtener_usuarios():
    try:
        with sqlite3.connect(db) as con:
            con.row_factory = sqlite3.Row 
            cur = con.cursor()
            cur.execute("SELECT * FROM  usuarios")
            row = cur.fetchall()
            return row
    except  Error:
        print(Error)
        return Error

def obtener_usuario(id):
    try:
        with sqlite3.connect(db) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM usuarios WHERE usuario_id = ?", [id])
            row = cur.fetchone()
            return row
    except Error:
        print(Error)
        return Error

def obtener_usuario_correo(correo):
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM usuarios WHERE correo = ?", [correo])
            row = cur.fetchone()
            return row
    except Error:
        print(Error)
        return Error

def quitar_usuario(id):
    try:
        with sqlite3.connect(db) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("DELETE FROM usuarios WHERE usuario_id = ?", [id])
            return con.total_changes > 0
    except Error:
        print(Error)
        return False

def actualizar_usuario(form, id):
    nombre = form.nombre_usuario.data
    clave = form.clave.data
    correo = form.correo.data
    rol = form.rol.data
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("UPDATE usuarios SET nombre=?, clave=?, correo=?, rol=? WHERE usuario_id = ?", [nombre, clave, correo, rol, id] )
            con.commit()
            return con.total_changes > 0
    except Error:
        print(Error)
        return False

def insertar_usuario(form):
    nombre = form.nombre_usuario.data
    clave = form.clave.data
    hashclave = generate_password_hash(clave)
    correo = form.correo.data
    rol = form.rol.data
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO usuarios(nombre, clave, correo, rol) VALUES (?,?,?,?)", (nombre, hashclave, correo, rol) )
            con.commit()
            return True
    except Error:
        print(Error)
        return False

def obtener_proveedores():
    try:
        with sqlite3.connect(db) as con:
            con.row_factory = sqlite3.Row 
            cur = con.cursor()
            cur.execute("SELECT * FROM  proveedores")
            row = cur.fetchall()
            return row
    except  Error:
        print(Error)
        return Error

def obtener_proveedor(id):
    try:
        with sqlite3.connect(db) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM proveedores WHERE proveedor_id = ?", [id])
            row = cur.fetchone()
            print(row)
            return row
    except Error:
        print(Error)
        return Error

def quitar_proveedor(id):
    try:
        with sqlite3.connect(db) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("DELETE FROM proveedores WHERE proveedor_id = ?", [id])
            return con.total_changes > 0
    except Error:
        print(Error)
        return False

def actualizar_proveedor(form, id):
    nombre = form.nombre_proveedor.data
    telefono = form.telefono.data
    correo = form.correo.data
    nit = form.nit.data
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("UPDATE proveedores SET nombre=?, telefono=?, correo=?, nit=? WHERE proveedor_id = ?", [nombre, telefono, correo, nit, id] )
            con.commit()
            return con.total_changes > 0
    except Error:
        print(Error)
        return False

def insertar_proveedor(form):
    nombre = form.nombre_proveedor.data
    telefono = form.telefono.data
    correo = form.correo.data
    nit = form.nit.data
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO proveedores (nombre, telefono, correo, nit) VALUES (?,?,?,?)", (nombre, telefono, correo, nit) )
            con.commit()
            return True
    except Error:
        print(Error)
        return False

#################### CRUD de Productos #######################

def obtener_productos():
    try:
        with sqlite3.connect(db) as con:
            con.row_factory = sqlite3.Row 
            cur = con.cursor()
            cur.execute("SELECT * FROM  productos")
            row = cur.fetchall()
            return row
    except  Error:
        print(Error)
        return Error

def obtener_producto(id):
    try:
        with sqlite3.connect(db) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM productos WHERE producto_id = ?", [id])
            row = cur.fetchone()
            return row
    except Error:
        print(Error)
        return Error

def quitar_producto(id):
    try:
        with sqlite3.connect(db) as con:
            con.row_factory = sqlite3.Row
            cur = con.cursor()
            cur.execute("DELETE FROM productos WHERE producto_id = ?", [id])
            return con.total_changes > 0
    except Error:
        print(Error)
        return False

def actualizar_producto(form, id):
    nombre = form.nombre_producto.data
    cant_minim = form.cantidad_minima.data
    cant_disp = form.cantidad_disponible.data
    descripcion = form.descripcion.data
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("UPDATE productos SET nombre=?, cant_minima=?, cant_disponible=?, descripcion=? WHERE producto_id = ?", [nombre, cant_minim, cant_disp, descripcion  ,id] )
            con.commit()
            return con.total_changes > 0
    except Error:
        print(Error)
        return False

def insertar_producto(form):
    nombre = form.nombre_producto.data
    cant_minim = form.cantidad_minima.data
    cant_disp = form.cantidad_disponible.data
    descripcion = form.descripcion.data
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO productos(nombre, cantidad_minima, cantidad_disponible, descripcion) VALUES (?,?,?,?)", (nombre, cant_minim, cant_disp, descripcion) )
            con.commit()
            return True
    except Error:
        print(Error)
        return False