#!/usr/bin/node

const dict = require('./101-data');

const diction = dict.dict;
const arr = [];
const arr1 = [];
const arr2 = [];
const newdict = {};
for (const key in diction) {
  const value = diction[key];
  if (value === 1) {
    arr.push(key);
    newdict[value] = arr;
  } else if (value === 2) {
    arr1.push(key);
    newdict[value] = arr1;
  } else {
    arr2.push(key);
    newdict[value] = arr2;
  }
}

console.log(newdict);
