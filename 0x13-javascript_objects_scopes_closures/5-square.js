#!/usr/bin/node
let i = 0;
let j;
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
      console.log('X'.repeat(this.width));
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
};
