#!/usr/bin/node
// prints x in a sqaure form
const { argv } = require('process');
if (argv.length === 2 || !Number(argv[2])) {
  console.log('Missing size');
} else if (Number(argv[2]) < 0 || Number(argv[2]) === 0) {
  // do nex
} else {
  let i;
  let j;
  for (i = 0; i < Number(argv[2]); i++) {
    let line = '';
    for (j = 0; j < Number(argv[2]); j++) {
      line += 'X';
    }
    console.log(line);
  }
}
