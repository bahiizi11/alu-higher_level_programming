#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i += 1) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
