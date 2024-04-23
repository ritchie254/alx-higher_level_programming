#!/usr/bin/node

// fetching the number of movies
const request = require('request');
const url = process.argv[2].replace(/films/, '');

// actor with id 18
const actor = `${url}people/18`;

request(actor, (error, response, body) => {
  if (error) {
    console.error('no actor found');
    return;
  }
  try {
    const movies = JSON.parse(body);
    const actCount = movies.films;
    console.log(actCount.length);
  } catch (parseError) {
    console.error(parseError);
  }
});
