#!/usr/bin/node
let i = 0;
exports.logMe = function (args) {
  console.log(i++ + ': ' + args);
};
