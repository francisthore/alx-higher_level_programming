#!/usr/bin/node
// Prints number of movies where a character ID is matched
const request = require('request');
const { argv } = require('process');
const charId = 18;
const charUrl = 'https://swapi-api.alx-tools.com/api/people/' + charId + '/';
const url = argv[2];

request({ url:url, json: true }, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const results = body.results;
    let i = 0;
    for (const idx1 in results) {
      const characters = results[idx1].characters;
      for (const idx2 in characters) {
        if (charUrl === characters[idx2]) {
          i = i + 1;
        }
      }
    }
    console.log(i);
  }
});
