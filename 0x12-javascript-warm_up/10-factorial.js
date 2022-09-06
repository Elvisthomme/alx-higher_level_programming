#!/usr/bin/node
const myVar = Number(process.argv[2]);
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(myVar));
