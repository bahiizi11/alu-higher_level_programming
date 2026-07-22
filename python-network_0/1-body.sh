#!/bin/bash
# displays the final body of a GET response, following redirects
curl -s -L -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s -L "$1"
