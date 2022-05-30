var entry = parseInt(require("fs").readFileSync("/dev/stdin", "utf8"));
var meses = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
console.log(meses[entry-1])