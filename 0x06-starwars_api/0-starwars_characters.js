#!/usr/bin/node
const argv = process.argv;
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

const request = require('request');

request(urlMovie, function (error, response, body) {
  if (error == null) {
    const fbody = JSON.parse(body);
    const characters = fbody.characters;

    if (characters && characters.length > 0) {
      const limit = characters.length;
      CharRequest(0, characters[0], characters, limit);
    }
  } else {
    console.log(error);
  }
});

function CharRequest (index, url, characters, limit) {
  if (index === limit) {
    return;
  }
  request(url, function (error, response, body) {
    if (!error) {
      const rtnbody = JSON.parse(body);
      console.log(rtnbody.name);
      index++;
      CharRequest(index, characters[index], characters, limit);
    } else {
      console.error('error:', error);
    }
  });
}
