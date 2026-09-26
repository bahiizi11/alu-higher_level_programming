# javascript-web_scraping

Reading and writing files, and making HTTP requests with the
`request` module: status codes, JSON APIs, and scraping page content.

| File | Description |
|------|-------------|
| `0-readme.js` | Reads and prints a file's UTF-8 content |
| `1-writeme.js` | Writes a string to a file in UTF-8 |
| `2-statuscode.js` | Prints the HTTP status code of a GET request |
| `3-starwars_title.js` | Prints a Star Wars film's title by episode ID (SWAPI) |
| `4-starwars_count.js` | Counts films featuring a given character (Wedge Antilles, ID 18) |
| `5-request_store.js` | Fetches a URL and stores the response body to a file |
| `6-completed_tasks.js` | Counts completed to-dos per user from a JSON API |

## Usage

```bash
./0-readme.js somefile.txt
./2-statuscode.js https://example.com
```

## Requirements

- Node.js
- `request` npm package (`npm install request`)
- Scripts are executable (`chmod +x`) and start with `#!/usr/bin/node`
- Style-checked with `semistandard`
