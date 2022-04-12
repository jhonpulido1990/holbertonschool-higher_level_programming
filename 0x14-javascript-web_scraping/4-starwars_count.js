#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request(url, function (error, response, body) {
    let i = 0;
  if (error) {
    console.log(error);
  } else {
    const characterID = JSON.parse(body).results;
    const a = Object.values(characterID['0'].characters)
    while (a[i]){
        if (a[i].includes('18') === true){
            request(a[i], function(error, response, body) {
                if (error) {
                    console.error(error);
                }
                console.log(JSON.parse(body).films.length)
            } )
            break;
        }
        i++;
    }
  }
});
