// var entrada = require("fs").readFileSync("/dev/stdin", "utf8");
entrada = prompt()
entrada = entrada.split(' ')
var n1 = parseFloat(entrada[0])
var n2 = parseFloat(entrada[1])
var n3 = parseFloat(entrada[2])
var n4 = parseFloat(entrada[3])

media = (n1*2+n2*3+n3*4+n4*1)/10
console.log(`Media: ${media.toFixed(1)}`)
if (media < 5){
    console.log(`Aluno reprovado.`)
} else if (media >= 7) {
    console.log(`Aluno aprovado.`)
} else if (5 <= media && media < 7) {
    console.log(`Aluno em exame.`)
    // var exame = require("fs").readFileSync("/dev/stdin", "utf8");
    exame = parseFloat(prompt())
    console.log(`Nota do exame: ${parseFloat(exame).toFixed(1)}`)
    var mediaf = (media+exame)/2
    if (mediaf >= 5) {
        console.log(`Aluno aprovado.`)
    } else {
        console.log(`Aluno reprovado.`)
    }
    console.log(`Media final: ${mediaf.toFixed(1)}`)
}