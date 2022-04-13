#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + args[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const js = JSON.parse(body).characters;
  for (let i = 0; i < js.length; i++) {
    request(js[i], function (error, response, body) {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
}
);
