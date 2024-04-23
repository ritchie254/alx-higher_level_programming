#!/usr/bin/node

// print status code of a request
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response.statusCode);
});
