function validarRut(rut) {
    // Formato válido: 12345678-9
    if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rut)) {
        return false;
    }

    var split = rut.split('-');
    var num = split[0];
    var dv = split[1];

    // Cálculo del dígito verificador
    var suma = 0;
    var multiplo = 2;

    // Se suman los productos de cada dígito del RUT por la secuencia 2, 3, 4, 5, 6, 7
    for (var i = 1; i <= num.length; i++) {
        var index = multiplo * parseInt(num.charAt(num.length - i));
        suma += index;
        if (multiplo < 7) {
            multiplo += 1;
        } else {
            multiplo = 2;
        }
    }

    // Se calcula el dígito verificador esperado
    var dvEsperado = 11 - (suma % 11);
    dvEsperado = (dvEsperado === 11) ? 0 : (dvEsperado === 10) ? 'K' : dvEsperado;

    // Se compara el dígito verificador esperado con el ingresado
    if (dvEsperado != dv.toUpperCase()) {
        return false;
    }

    return true;
}
function validarFormulario() {
    let rut = document.getElementById("regRut").value;
    let nombre = document.getElementById("regNombre").value;
    let apellido = document.getElementById("regApellido").value;
    let email = document.getElementById("regEmail").value;
    let telefono = document.getElementById("regTelefono").value;
    let passwd = document.getElementById("passwd").value;
    let passwd2 = document.getElementById("passwd2").value;

    if (!validarRut(rut)) {
        document.getElementById("msgRut").innerText = "Ingrese un rut valido";
    } else {
        document.getElementById("msgRut").innerText = "";
    }


    if(nombre === "") {
        document.getElementById("msgNombre").innerText = "Ingrese un nombre valido";
    } else {
        document.getElementById("msgNombre").innerText = "";
    }

    if(apellido === "") {
        document.getElementById("msgApellido").innerText = "Ingrese un apellido valido";
    } else {
        document.getElementById("msgApellido").innerText = "";
    }

    if (email ==="" ) {
        document.getElementById("msgEmail").innerText = "Ingrese un email valido";
    } else {
        document.getElementById("msgEmail").innerText = "";
    }

    if (telefono ==="" ) {
        document.getElementById("msgTel").innerText = "Ingrese un telefono valido";
    } else {
        document.getElementById("msgTel").innerText = "";
    }

    if (passwd ==="" ) {
        document.getElementById("msgpass1").innerText = "Por favor ingrese una contraseña";
    } else {
        document.getElementById("msgpass1").innerText = "";
    }

    if (passwd2 === ""){
        document.getElementById("msgpass2").innerText = "Por favor confirme la contraseña";
      
    }
    if(passwd2 !== passwd){
        document.getElementById("msgpass2").innerText = "Las contraseñas deben ser iguales";
    } else{
        document.getElementById("msgpass2").innerText = "";
    }

    if (nombre === "" || apellido === "" || rut === "" || email === "" || telefono === "" || passwd === "" || passwd2 === "") {
        btnsubmit.disabled = true; // Deshabilitar el botón de envío
    } else {
        btnsubmit.disabled = false; // Habilitar el botón de envío
    }
}



