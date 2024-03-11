#!/usr/bin/node
const arg = parseInt(process.argv[2]);
let size = '';
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    for (let j = 0; j < arg; j++) {
      size += 'X';
    }
    console.log(size);
    size = '';
  }
}
