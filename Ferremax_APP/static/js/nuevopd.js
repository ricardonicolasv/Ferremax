function validarFormulario() {
    let nuevopd = document.getElementById("nuevopd").value;
    let stock = document.getElementById("stock").value;
    let precio = document.getElementById("valor").value;

    if (nuevopd === "") {
        document.getElementById("msgprod").innerText = "Ingrese un nombre valido";
    } else {
        document.getElementById("msgprod").innerText = "";
    }
    if (stock === "") {
        document.getElementById("msgstock").innerText = "Ingrese una cantidad valido";
    } else {
        document.getElementById("msgstock").innerText = "";
    }
    if (precio === "") {
        document.getElementById("msgvalor").innerText = "Ingrese un precio valido";
    } else {
        document.getElementById("msgvalor").innerText = "";
    }
}