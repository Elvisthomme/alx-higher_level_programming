#!/usr/bin/node
const myVar = Number(process.argv[2]);
if (!myVar) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myVar; i++) {
    console.log('C is fun');
  }
}
