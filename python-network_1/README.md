# python-network_1

This project covers HTTP requests in Python using both the low-level
`urllib` package and the higher-level `requests` package: fetching
resources, reading response headers, sending POST requests, handling
HTTP errors, and consuming JSON APIs (including the GitHub API).

## Learning Objectives

- What is the internet, IP, and network basics
- How to make an HTTP request with Python using `urllib`
- How to make an HTTP request with Python using `requests`
- How to send a POST request
- How to fetch JSON resources
- How to manipulate data from an external service
- How to handle `urllib.error.HTTPError` exceptions
- How to use Basic Authentication with `requests`

## Files

| File | Description |
|------|-------------|
| `0-hbtn_status.py` | Fetches the status endpoint with `urllib` |
| `1-hbtn_header.py` | Displays `X-Request-Id` header with `urllib` |
| `2-post_email.py` | POSTs an email with `urllib` |
| `3-error_code.py` | Handles `HTTPError` with `urllib` |
| `4-hbtn_status.py` | Fetches the status endpoint with `requests` |
| `5-hbtn_header.py` | Displays `X-Request-Id` header with `requests` |
| `6-post_email.py` | POSTs an email with `requests` |
| `7-error_code.py` | Handles status codes >= 400 with `requests` |
| `8-json_api.py` | Searches a user via a JSON POST API |
| `10-my_github.py` | Displays a GitHub user's id via Basic Auth |

## Author

bahiizi11
