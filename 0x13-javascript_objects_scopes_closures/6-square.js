#!/usr/bin/node
const Rectangle = require('./4-rectangle')

let i = 0;
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      i = 0;
      while (i < this.height) {
      console.log(c.repeat(this.width));
      i++;
    }
    }
  }
};
