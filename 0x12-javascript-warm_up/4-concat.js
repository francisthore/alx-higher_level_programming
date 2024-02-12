#!/usr/bin/node
// concats strings
const { argv } = require('process');
if (argv.length === 2) {
  console.log('No argument');
} else {
  console.log(argv[2] + ' is ' + argv[3]);
}
