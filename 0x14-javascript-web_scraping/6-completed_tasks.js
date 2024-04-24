#!/usr/bin/node
// Counts the number of tasks completed by userid
const request = require('request');
const { argv } = require('process');

function filterIds (obj) {
  const outputArr = Array.from(new Set(obj));
  return outputArr;
}

function getIds (obj) {
  const outputArr = [];
  for (const idx in obj) {
    outputArr.push(obj[idx].userId);
  }
  return filterIds(outputArr);
}

const url = argv[2];

request({ url, json: true }, function (error, response, results) {
  if (error) {
    console.error(error);
  } else {
    const users = getIds(results);
    const completedDict = {};
    for (const idx in users) {
      const currentUser = users[idx];
      let completed = 0;
      for (const idx in results) {
        if (currentUser === results[idx].userId) {
          if (results[idx].completed === true) {
            completed = completed + 1;
          }
        }
        if (completed > 0) {
          completedDict[currentUser] = completed;
        }
      }
    }
    console.log(completedDict);
  }
});
