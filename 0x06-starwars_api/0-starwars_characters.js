const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

const baseUrl = 'https://swapi.dev/api/';
const filmsEndpoint = 'films/';

request(baseUrl + filmsEndpoint + movieId, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('API request failed with status code:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  const characterPromises = characterUrls.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  });

  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(characterName => {
        console.log(characterName);
      });
    })
    .catch(error => {
      console.error('Error:', error);
      process.exit(1);
    });
});
