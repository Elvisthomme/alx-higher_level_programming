#!/usr/bin/node
const myArgs = process.argv;
function add (a, b) {
  console.log(a + b);
}
add(Number(myArgs[2]), Number(myArgs[3]));
