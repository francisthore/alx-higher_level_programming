#!/usr/bin/node
// Reads the content of a file
const fs = require('node:fs');
const { argv } = require('process');

fs.readFile(argv[2], 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
