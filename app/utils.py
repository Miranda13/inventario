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


def buscar_usuario(id):
    return "Usuario no encontrado"

def listar_usuarios():
    return usuarios

def listar_proveedores():
    return proveedores

def listar_productos():
    return productos