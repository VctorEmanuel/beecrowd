var entrada = require("fs").readFileSync("/dev/stdin", "utf8");
informado = entrada.split(' ')
var A = parseInt(informado[0])
var B = parseInt(informado[1])
var C = parseInt(informado[2])
var D = parseInt(informado[3])

if (B > C && D > A && C + D > A + B && C > 0 && D > 0 && A % 2 === 0) {
    console.log("Valores aceitos");
} else {
    console.log("Valores nao aceitos");
}