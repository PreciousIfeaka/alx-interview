const request = require('request');
const proc = process.argv[2];
let url = `https://swapi-api.alx-tools.com/api/films/${proc}`;

request.get(url, (error, response, body) => {
    if (error) {
        console.log(error);
    } else {
        const characters = JSON.parse(body).characters;
        printCharacters(characters, 0);
    }
})

function printCharacters(arr, idx) {
    request.get(arr[idx], (error, res, body) => {
        if(error) {
            console.log(error);
        } else {
            namee = JSON.parse(body).name;
            console.log(namee);
            if ((idx + 1) < arr.length) {
                printCharacters(arr, idx + 1)
            }
        }
    });
}