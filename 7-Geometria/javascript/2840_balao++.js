var entrada = (require("fs").readFileSync("/dev/stdin", "utf8")).split(' ');
var n = parseInt(entrada[0]);
var r = parseInt(entrada[1]);
var pi = 3.1415;
var v = (4/3) * (pi * (n ** 3));
console.log(`${Math.floor(r/v)}`);
