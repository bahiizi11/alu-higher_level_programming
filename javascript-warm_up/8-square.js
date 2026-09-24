#!/usr/bin/node
const args = process.argv.slice(2);
const size = parseInt(args[0], 10);

if (isNaN(size)) {
  console.log('Missing size');
}

for (let i = 0; i < size; i += 1) {
  let row = '';
  for (let j = 0; j < size; j += 1) {
    row += 'X';
  }
  console.log(row);
}
