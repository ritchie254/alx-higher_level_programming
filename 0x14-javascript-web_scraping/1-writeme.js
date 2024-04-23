#!/usr/bin/node

// writing to a file
const fs = require('fs');
const fileName = process.argv[2];
const fileContent = process.argv[3];

try {
  fs.writeFileSync(fileName, fileContent);
} catch (err) {
  console.error(err);
}
