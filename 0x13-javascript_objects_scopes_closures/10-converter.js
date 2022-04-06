#!/usr/bin/node

exports.converter = function (j) {
  return function add (f) {
    return (f).toString(j);
  };
};
