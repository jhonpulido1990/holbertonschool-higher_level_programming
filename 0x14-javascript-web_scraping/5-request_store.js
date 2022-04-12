#!/usr/bin/node

const request = require('request');
const args = process.argv;
const url = args[2];
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  fs.writeFile(args[3], body, 'utf8', function (error) {
    console.error(error);
  });
});
