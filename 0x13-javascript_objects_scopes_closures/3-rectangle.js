#!/usr/bin/node
// defines rectangle class
module.exports = class Rectangle {
  constructor (w = 0, h = 0) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let i;
    let j;
    for (i = 0; i < this.height; i++) {
      let row = '';
      for (j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
};
