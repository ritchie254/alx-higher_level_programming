#!/usr/bin/node

// write the content of webpage to afile

const fs = require('fs');
const request = require('request');
const siteUrl = process.argv[2];
const fileSave = process.argv[3];

if (process.argv.length < 4) {
  console.error('incorrect number of args');
  process.exit(1);
}

request(siteUrl, (error, response, body) => {
  if (error) {
    console.error('failed');
    return;
  }
  try {
    const fileContent = body;
    fs.writeFileSync(fileSave, fileContent);
  } catch (err) {
    console.error(err);
  }
});
