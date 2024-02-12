#!/usr/bin/node
// prints first arg passed
const { argv } = require('process');
if (argv.length === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
