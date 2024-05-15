function validarFormulario() {

    let email = document.getElementById("email").value;
    let passwd = document.getElementById("passwd").value;

    if (email === "") {
        document.getElementById("msgcorreo").innerText = "Ingrese un email valido";
    } else {
        document.getElementById("msgcorreo").innerText = "";
    }

    if (passwd ==="" ) {
        document.getElementById("msgcontraseña").innerText = "Por favor ingrese una contraseña";
    } else {
        document.getElementById("msgcontraseña").innerText = "";
    }

    if (email === "" || passwd === "") {
        btnsubmit.disabled = true; // Deshabilitar el botón de envío
    } else {
        btnsubmit.disabled = false; // Habilitar el botón de envío
    }
}