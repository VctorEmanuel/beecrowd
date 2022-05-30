var palavra = require("fs").readFileSync("/dev/stdin", "utf8");
  
if ((palavra.length) >= 10)
    console.log("palavrao");
else
    console.log("palavrinha");

