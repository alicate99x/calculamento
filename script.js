function calcular() {

    let numero1 = Number(document.getElementById("numero1").value);
    let numero2 = Number(document.getElementById("numero2").value);
    let operacao = document.getElementById("operacao").value;
    let resultado;


    if (operacao === "soma") {
        resultado = numero1 + numero2;

    } else if (operacao === "subtracao") {
        resultado = numero1 - numero2;

    } else if (operacao === "multiplicacao") {
        resultado = numero1 * numero2;

    } else if (operacao === "divisao") {
        resultado = numero1 / numero2;
    }

    localStorage.setItem("resultado", resultado);
    window.location.href = "/resultado";
}
