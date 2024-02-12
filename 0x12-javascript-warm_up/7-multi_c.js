#!/usr/bin/node
// prints x times
const { argv } = require('process');
if (argv.length === 2 || !Number(argv[2])) {
  console.log('Missing number of occurences');
} else if (Number(argv[2]) < 0 || Number(argv[2]) === 0) {
  // do nex
} else {
  let i;
  for (i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
}
