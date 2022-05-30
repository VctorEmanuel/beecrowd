var entrada = require("fs").readFileSync("/dev/stdin", "utf8");
var a = entrada.split(" ");
var x = parseFloat(a[0]);
var y = parseFloat(a[1]);
if (x > 0 && y > 0)
    console.log("Q1");
else if (x < 0 && y > 0)
    console.log("Q2");
else if (x < 0 && y < 0)
    console.log("Q3");
else if (x > 0 && y < 0)
    console.log("Q4");
else if (x === 0 && y === 0)
    console.log("Origem");
else if (x === 0)
    console.log("Eixo Y");
else if (y === 0)
    console.log("Eixo X");