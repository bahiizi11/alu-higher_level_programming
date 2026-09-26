#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const counts = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        counts[todo.userId] = (counts[todo.userId] || 0) + 1;
      }
    });
    console.log(counts);
  }
});
