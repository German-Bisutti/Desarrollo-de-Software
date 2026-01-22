function calcularPromedio(a, b, c, d) {
    const suma = (a + b + c + d);
    const promedio = suma / 4;
    return promedio;
}

function testCalcularPromedio() {
    const resultado = calcularPromedio(5, 10, 15, 20);
    if (resultado === 12.5) {
        console.log("Prueba pasada con éxito");
    } else {
        console.log("Error en la prueba. Resultado: " + resultado);
    }
}

testCalcularPromedio();