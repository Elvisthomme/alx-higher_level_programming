#!/usr/bin/node
const myVar = Number(process.argv[2]);
let x = 'x';
if (!myVar) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVar - 1; i++) {
    x += 'x';
  }
  for (let i = 0; i < myVar; i++) {
    console.log(x);
  }
}
