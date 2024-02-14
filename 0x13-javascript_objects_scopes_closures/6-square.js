#!/usr/bin/node
// defines sqaure class
const ParentSquare = require('./5-square');

module.exports = class Square extends ParentSquare {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let i;
      let j;
      for (i = 0; i < this.height; i++) {
        let row = '';
        for (j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
};
