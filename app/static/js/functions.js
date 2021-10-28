let idUsuario;

function ponerId(id) {
    idUsuario = id;
}

function eliminarUsuario(){
    document.getElementById("eliminarUsuario").action="/usuario/delete"
}