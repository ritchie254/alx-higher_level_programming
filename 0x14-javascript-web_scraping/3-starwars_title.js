#!/usr/bin/node

// scraping the star wars api

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

if (process.argv.length < 3) {
  console.error('provide a movie id');
  process.exit(1);
}
const movieId = url + process.argv[2];

request(movieId, (error, reponse, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
