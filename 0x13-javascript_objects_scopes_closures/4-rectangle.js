#!/usr/bin/node
let i = 0;
let j;
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return Rectangle.removeClass;
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
    this.height = this.height *2 ;
  }

  rotate () {
    j = this.height;
    this.height = this.width;
    this.width = j;
  }
};
