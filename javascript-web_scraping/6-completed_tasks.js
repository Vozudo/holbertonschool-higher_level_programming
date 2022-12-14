#!/usr/bin/node
const request = require('request');
const url = process.argv[2] || '';
const storage = {};

request(url, (err, response, body) => {
  if (err) {
    return console.log(err);
  }

  const result = JSON.parse(body);

  for (let i = 0; i < result.length; i++) {
    const tmp = result[i].userId;
    if (result[i].completed) {
      storage[tmp] = (storage[tmp] || 0) + 1;
    }
  }

  console.log(storage);
});
