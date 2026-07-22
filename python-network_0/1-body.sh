#!/bin/bash
# sends a GET request and displays the body, only if status is 200
response=$(curl -s -w "\n%{http_code}" "$1")
status=$(echo "$response" | tail -n1)
body=$(echo "$response" | sed '$d')
if [ "$status" -eq 200 ]; then
    echo -n "$body"
fi
