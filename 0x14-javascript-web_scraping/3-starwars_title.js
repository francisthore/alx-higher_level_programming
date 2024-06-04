#!/usr/bin/node
// Sends a GET request to an api and logs results
const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
request({ url, json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(body.title);
  }
});
