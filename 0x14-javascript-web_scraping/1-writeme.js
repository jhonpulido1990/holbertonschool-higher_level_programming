#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
/***
 * implementation of writeFile
 */

fs.writeFile(args[2], args[3], 'utf8', function (err) {
  if (err) return console.error(err);
});
