#!/usr/bin/node
// Script that prints all characters of a Star Wars movie in order
const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const URL = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(URL, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);
  if (!data.characters) {
    console.error('No characters found.');
    return;
  }

  // Fonction pour récupérer les noms des personnages en série
  const getCharacter = url =>
    new Promise((resolve, reject) => {
      request.get(url, (err, res, body) => {
        if (err) reject(err);
        else resolve(JSON.parse(body).name);
      });
    });

  // Exécuter les requêtes en série pour respecter l'ordre
  (async () => {
    for (const charUrl of data.characters) {
      try {
        const name = await getCharacter(charUrl);
        console.log(name);
      } catch (error) {
        console.error(`Error fetching character: ${error}`);
      }
    }
  })();
});
