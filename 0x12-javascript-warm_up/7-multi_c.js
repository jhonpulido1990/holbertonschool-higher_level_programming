#!/usr/bin/node

let i = 0;
const args = process.argv;
if (args[2] === undefined || parseInt(args[2] != 'number')) {
  console.log('Missing number of occurrences');
}
a = parseInt(args[2]);
while (i < args[2]) {
  console.log('C is fun');
  i++;
}
