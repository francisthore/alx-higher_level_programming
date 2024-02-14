#!/usr/bin/node
// tracks numArgs printed
let numArgs = 0;
exports.logMe = function (item) {
  ++numArgs;
  console.log(`${numArgs - 1}: ${item}`);
};
