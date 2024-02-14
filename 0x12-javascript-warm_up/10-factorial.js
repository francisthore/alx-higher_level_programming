#!/usr/bin/node
// factorial
const { argv } = require('process');
function factorial (num) {
  if (num < 0) {
    return;
  }
  if (!num || num === 0) {
    return 1;
  }
  return (num * factorial(num - 1));
}

const num = Number(argv[2]);
console.log(factorial(num));
