#!/usr/bin/node

// a js script that reads a file
const fs = require('fs');
const fileName = process.argv[2];

try {
  const data = fs.readFileSync(fileName, 'utf8');
  console.log(data);
} catch (err) {
  console.error(err);
}
