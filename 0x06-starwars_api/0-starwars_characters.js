#!/usr/bin/node

const axios = require('axios');

async function fetchMovieCharacters(movieId) {
    const baseUrl = "https://swapi.dev/api/films/";

    try {
        // Fetch movie details
        const movieResponse = await axios.get(`${baseUrl}${movieId}/`);
        const movieData = movieResponse.data;

        // Get the list of character URLs
        const characters = movieData.characters;

        // Fetch and print each character name
        for (const characterUrl of characters) {
            const charResponse = await axios.get(characterUrl);
            console.log(charResponse.data.name);
        }
    } catch (error) {
        console.error(`Error fetching data: ${error.message}`);
        process.exit(1);
    }
}

if (process.argv.length !== 3) {
    console.error("Usage: node star_wars_characters.js <Movie ID>");
    process.exit(1);
}

const movieId = process.argv[2];
fetchMovieCharacters(movieId);

