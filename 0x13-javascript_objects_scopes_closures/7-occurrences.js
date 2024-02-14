#!/usr/bin/node
// checks number of occurances in a list

exports.nbOccurences = function (list, searchElement) {
  let numOccurances = 0;
  if (!list || !searchElement) {
    return;
  }
  for (const item of list) {
    if (item === searchElement) {
      numOccurances++;
    }
  }
  return numOccurances;
};
