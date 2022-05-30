var entry = require("fs").readFileSync("/dev/stdin", "utf8");
var entrada = entry.split(' ')
var hi = parseInt(entrada[0])
var mi = parseInt(entrada[1])
var hf = parseInt(entrada[2])
var mf = parseInt(entrada[3])
var hora = hf - hi
var minuto = mf - mi
if (hi == hf) {
    if (mi == mf) {
        hora = 24
        minuto = 0
    } else if (mi > mf) {
        hora = 24
        hora -= 1
        minuto += 60
    } else {}
} else if (hi > hf) {
    hora += 24;
    if (mi > mf) {
        minuto += 60
        hora -= 1
    } else {}
} else {
    if (mi >= mf) {
        hora -= 1
        minuto += 60
    } else {}
}

console.log(`O JOGO DUROU ${hora} HORA(S) E ${minuto} MINUTO(S)`);
