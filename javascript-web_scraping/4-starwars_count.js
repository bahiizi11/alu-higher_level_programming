#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const films = JSON.parse(body).results;
    const count = films.filter(
      (film) => film.characters.some((character) => character.includes('/people/18/'))
    ).length;
    console.log(count);
  }
});
