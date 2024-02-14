#!/usr/bin/node
// defines sqaure class
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (w) {
    super(w, w);
  }
};
