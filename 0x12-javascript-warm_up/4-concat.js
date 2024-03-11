#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (arg1 === undefined) {
  console.log('undefined is undefined');
} else if (arg2 === undefined) {
  console.log(arg1 + ' is undefined');
} else {
  console.log(arg1 + ' is ' + arg2);
}
