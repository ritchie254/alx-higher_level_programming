#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

# check if arguement is provided
if [ $# -ne 1 ]; then
	echo "Usage: $0 url"
	exit 1
else
	URL=$1
	response=$(curl -s "$URL" -o /tmp/file1)
	size=$(stat --format=%s /tmp/file1)
	echo "$size"
fi
rm -f /tmp/file1

