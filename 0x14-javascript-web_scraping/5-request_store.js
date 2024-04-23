#!/usr/bin/node
// Writes web content into a file
const request = require('request');
const { argv } = require('process');
const fs = require('node:fs');
const url = argv[2];
const filePath = argv[3];

request({ url, json: false }, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});
