#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);
let result;
if (isNaN(arg1)) {
  console.log('NaN');
} else {
  result = add(arg1, arg2);
  console.log(result);
}
