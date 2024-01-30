#!/usr/bin/node

const requs = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
requs.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const ded = data.characters;
  for (const i of ded) {
    req.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
