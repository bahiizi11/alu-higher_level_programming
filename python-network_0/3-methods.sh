#!/bin/bash
# displays all HTTP methods the server accepts for a URL
curl -s -X OPTIONS -i "$1" | grep -i "Allow:" | cut -d ' ' -f2- | tr -d '\r'
