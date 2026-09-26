# javascript-web_jquery

DOM manipulation with plain JavaScript and with jQuery: selecting
elements, event handling, class toggling, and AJAX requests.

| File | Description |
|------|-------------|
| `0-script.js` | Sets `<header>` text color to red, using `document.querySelector` (no jQuery) |
| `1-script.js` | Same, using jQuery instead of `document.querySelector` |
| `2-script.js` | Turns `<header>` red on click of `DIV#red_header` |
| `3-script.js` | Adds the `red` class to `<header>` on click |
| `4-script.js` | Toggles `<header>` between `red` and `green` on click |
| `5-script.js` | Appends a new `<li>Item</li>` to `UL.my_list` on click |
| `6-script.js` | Updates `<header>` text to "New Header!!!" on click |
| `7-script.js` | Fetches a Star Wars character's name and displays it in `DIV#character` |
| `8-script.js` | Fetches all Star Wars film titles and lists them in `UL#list_movies` |
| `9-script.js` | Fetches a translated "hello" and displays it in `DIV#hello`, on DOM ready |

Each task's matching `<n>-main.html` demonstrates the required page
structure for testing in a browser.

## Requirements

- A browser (open the `*-main.html` files directly)
- jQuery 3.2.1, loaded via CDN in the HTML files (already included)
- Style-checked with `semistandard` (see `package.json`'s
  `semistandard.globals` for the jQuery `$` global)
