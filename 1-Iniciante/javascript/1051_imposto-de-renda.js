let entry = require("fs").readFileSync("/dev/stdin", "utf8");
let total;

if (entry > 0 && entry <= 2000) {
    total = entry;
} else if (entry > 2000.1 && entry <= 3000.0) {
    entry -= 2000
    total = (entry*0.02).toFixed(2);
} else if (entry > 3000.1 && entry <= 4500.0) {
    entry -= 3000;
    total = ((1000*0.08)+(entry*0.18)).toFixed(2);
} else {
    entry -= 4500;
    total = ((1000*0.08)+(1500*0.18)+(entry*0.28)).toFixed(2);
}

console.log(total == entry ? 'Isento' : `R$ ${total}`);