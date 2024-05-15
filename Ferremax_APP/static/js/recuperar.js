function validarFormulario() {

    let email = document.getElementById("email").value;
    if (email === "") {
        document.getElementById("msgcorreo").innerText = "Ingrese un email valido";
    } else {
        document.getElementById("msgcorreo").innerText = "";
    }
}