# javascript_objects_scopes_closures

ES6 classes, inheritance, scope, and closures in JavaScript, run
directly with Node.js.

| File | Description |
|------|-------------|
| `0-rectangle.js` | An empty `Rectangle` class |
| `1-rectangle.js` | `Rectangle` with a `width`/`height` constructor |
| `2-rectangle.js` | Same, but invalid dimensions produce an empty object |
| `3-rectangle.js` | Adds an instance `print()` method |
| `4-rectangle.js` | Adds `rotate()` and `double()` instance methods |
| `5-square.js` | `Square`, extending `Rectangle` via `super()` |
| `6-square.js` | `Square`, extending `5-square.js`, adds `charPrint(c)` |
| `7-occurrences.js` | Counts occurrences of a value in a list |
| `8-esrever.js` | Reverses a list without using `Array.prototype.reverse` |
| `9-logme.js` | Logs each call with a running count, using closure state |
| `10-converter.js` | Returns a function converting base-10 numbers to another base |

Each task also has a matching `<n>-main.js` test script demonstrating
its expected behavior.

## Usage

```bash
./0-main.js
```

## Requirements

- Node.js
- Scripts are executable (`chmod +x`) and start with `#!/usr/bin/node`
- Style-checked with `semistandard`
