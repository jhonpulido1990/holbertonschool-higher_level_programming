#!/usr/bin/node
exports.nbOccurences = function (j, n) {
  let i = 0;
  let count = 0;
  while (j[i]) {
    if (j[i] === n) {
      count++;
    }
    i++;
  }
  return count;
};
