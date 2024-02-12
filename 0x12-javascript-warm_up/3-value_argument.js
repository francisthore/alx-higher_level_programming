#!/usr/bin/node
// prints first arg passed
const { argv } = require('process');
let i = 0;
argv.forEach((val) => {
  i = i + 1;
});
if (i === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
