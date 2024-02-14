#!/usr/bin/node
// returns 2nd largest
const { argv } = require('process');
if (argv.length < 4) {
  console.log(0);
} else {
  const list = [];
  for (const item of argv) {
    if (Number(item)) {
      list.push(Number(item));
    }
  }
  list.sort((a, b) => b - a);
  console.log(list[1]);
}
