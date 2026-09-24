#!/usr/bin/node
const args = process.argv.slice(2);
const count = parseInt(args[0], 10);

if (isNaN(count)) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < count; i += 1) {
  console.log('C is fun');
}
