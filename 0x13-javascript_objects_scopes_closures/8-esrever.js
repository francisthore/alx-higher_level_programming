#!/usr/bin/node
// reveserses a list
exports.esrever = function (list) {
  if (!list) {
    return;
  }

  const reversed = [];
  for (let lastIdx = list.length - 1; lastIdx >= 0; lastIdx--) {
    reversed.push(list[lastIdx]);
  }
  return reversed;
};
