#!/usr/bin/node
// Displays status code of a GET request
const request = require('request');
const {argv} = request('process');

url = argv[2];
request($url, function (error, response, body) {
    if (error) {
        console.log(error);
    }
    else {
        console.log('code:', response && response.statusCode);
    }
});
