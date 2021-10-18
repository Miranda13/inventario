usuarios = [
    {
        "id": 1,
        "nombre": "Fulanito",
        "rol": "usuarioFinal",
        "correo": "fulanito@gmail.com"
    },
    {
        "id": 2,
        "nombre": "Fulanita",
        "rol": "usuarioFinal",
        "correo": "fulanita@gmail.com"
    }
]

proveedores = [
    {
        "id": 1,
        "nombre": "General motors",
        "nit": "89127312-12",
        "correo": "general@gmail.com",
        "telefono": 3124556789
    },
    {
        "id": 2,
        "nombre": "Aero S.A.",
        "nit": "172763-1",
        "correo": "aero@gmail.com",
        "telefono": 3137889900
    },
    {
        "id": 3,
        "nombre": "Michelin S.A.",
        "nit": "8917312-3",
        "correo": "michelin@gmail.com",
        "telefono": 3226775544
    }
]

productos = [
    {
        "id": 1,
        "nombre": "General motors",
        "nit": "89127312-12",
        "correo": "general@gmail.com",
        "telefono": 3124556789
    },
    {
        "id": 2,
        "nombre": "Aero S.A.",
        "nit": "172763-1",
        "correo": "aero@gmail.com",
        "telefono": 3137889900
    },
    {
        "id": 3,
        "nombre": "Michelin S.A.",
        "nit": "8917312-3",
        "correo": "michelin@gmail.com",
        "telefono": 3226775544
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