var entrada = require("fs").readFileSync("/dev/stdin", "utf8");
var n = parseInt(entrada)
var horas = 0
var minutos = 0
var segundos = 0
while (n > 0) {
    if (n > 3600) {
        horas++
        n -= 3600
    } else if (n > 60) {
        minutos++
        n -= 60
    } else {
        segundos = n
        n = 0
    }
}
console.log(`${horas}:${minutos}:${segundos}`)