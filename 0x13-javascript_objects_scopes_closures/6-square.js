#!/usr/bin/node
let i = 0;
let j;
let charact = 'X';
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return undefined;
    }
  }

  print () {
    i = 0;
    while (i < this.height) {
      console.log(charact.repeat(this.width));
      i++;
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    j = this.height;
    this.height = this.width;
    this.width = j;
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      charact = 'X';
      this.print();
    } else {
      charact = c;
      this.print();
    }
  }
};
