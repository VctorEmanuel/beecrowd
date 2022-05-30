var entrada = require("fs").readFileSync("/dev/stdin", "utf8");
entrada = entrada.split('\n')
A = parseFloat(entrada[0])
B = parseFloat(entrada[1])

console.log(`MEDIA = ${((A*3.5+B*7.5)/11).toFixed(5)}`);