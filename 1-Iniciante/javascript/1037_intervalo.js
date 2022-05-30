var entrada = require("fs").readFileSync("/dev/stdin", "utf8");
informado = parseFloat(entrada)

if (0 <= informado && informado <= 25) {
    console.log("Intervalo [0,25]")
} else if (25 < informado && informado <= 50) {
    console.log("Intervalo (25,50]")
} else if (50 < informado && informado <= 75) {
    console.log("Intervalo (50,75]")
} else if (75 < informado && informado <= 100) {
    console.log("Intervalo (75,100]")
} else {
    console.log("Fora de intervalo")
}
