#!/usr/bin/node
// typecasting
const { argv } = require('process');
if (!Number(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(argv[2]));
}
