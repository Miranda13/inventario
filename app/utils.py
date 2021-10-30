import sqlite3
from sqlite3 import Error

usuarios = [
    {
        "id": 1,
        "nombre_usuario": "Fulanito",
        "rol": "usuarioFinal",
        "correo": "fulanito@gmail.com"
    },
    {
        "id": 2,
        "nombre_usuario": "Fulanita",
        "rol": "usuarioFinal",
        "correo": "fulanita@gmail.com"
    }
]

proveedores = [
    {
        "id": 1,
        "nombre_proveedor": "General motors",
        "nit": "89127312-12",
        "correo": "general@gmail.com",
        "telefono": 3124556789,
        "productos": "Llantas, espejos"
    },
    {
        "id": 2,
        "nombre_proveedor": "Aero S.A.",
        "nit": "172763-1",
        "correo": "aero@gmail.com",
        "telefono": 3137889900,
        "productos": "Rines, sillas"
    },
    {
        "id": 3,
        "nombre_proveedor": "Michelin S.A.",
        "nit": "8917312-3",
        "correo": "michelin@gmail.com",
        "telefono": 3226775544,
        "productos": "Llantas, bujias"
    }
]

productos = [
    {
        "id": 1,
        "nombre_producto": "Llantas",
        "nombre_proveedor": "Michelin S.A.",
        "descripcion": "185/165 para auto",
        "cantidad_disponible": 15,
        "cantidad_minima": 10
    },
    {
        "id": 2,
        "nombre_producto": "Rin",
        "nombre_proveedor": "Aero S.A.",
        "descripcion": "13 pulgadas",
        "cantidad_disponible": 50,
        "cantidad_minima": 20
    },
    {
        "id": 3,
        "nombre_producto": "Espejos",
        "nombre_proveedor": "Aero S.A.",
        "descripcion": "Para carro renault 18",
        "cantidad_disponible": 35,
        "cantidad_minima": 40
    }
]

db = 'app\inventario.db'

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
    correo = form.correo.data
    rol = form.rol.data
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO usuarios(nombre, clave, correo, rol) VALUES (?,?,?,?)", (nombre, clave, correo, rol) )
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
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("UPDATE proveedores SET nombre=?, telefono=?, correo=? WHERE proveedor_id = ?", [nombre, telefono, correo] )
            con.commit()
            return con.total_changes > 0
    except Error:
        print(Error)
        return False

def insertar_proveedor(form):
    nombre = form.nombre_proveedor.data
    telefono = form.telefono.data
    correo = form.correo.data
    try:
        with sqlite3.connect(db) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO proveedor (nombre, telefono, correo) VALUES (?,?,?)", (nombre, telefono, correo) )
            con.commit()
            return True
    except Error:
        print(Error)
        return False