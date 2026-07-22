#!/bin/bash
# displays the body of a GET response only if the status is 200
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
