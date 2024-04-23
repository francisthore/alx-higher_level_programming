#!/usr/bin/node
// Writes into a file
const fs = require('node:fs');
const { argv } = require('process');

fs.writeFile(argv[2], argv[3], 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
