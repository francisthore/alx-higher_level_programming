#!/usr/bin/node
// Displays characters of a movie
const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
request({ url, json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let characters = body.characters;
    characters.sort((a, b) => {
      const idA = parseInt(a.match(/people\/(\d+)\//)[1], 10);
      const idB = parseInt(b.match(/people\/(\d+)\//)[1], 10);
      return idA - idB;
    });
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
