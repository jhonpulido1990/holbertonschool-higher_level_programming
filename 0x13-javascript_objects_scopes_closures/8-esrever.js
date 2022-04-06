#!/usr/bin/node

exports.esrever = function (j) {
  let i = j.length - 1;
  let a = 0;
  let tmp;
  while (a < i) {
    tmp = j[a];
    j[a] = j[i];
    j[i] = tmp;
    a++;
    i--;
  }
  return j;
};
