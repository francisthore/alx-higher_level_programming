#!/usr/bin/node
// Displays characters of a movie
const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
request({ url, json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = body.characters;
    for (let i = 0; i < characters.length; i++) {
      const url = characters[i];
      request({ url, json: true }, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          console.log(body.name);
        }
      });
    }
  }
});
