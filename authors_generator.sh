#!/usr/bin/env bash
# Generates an authors file

OUTPUT_FILE="AUTHORS"

if [ ! -d ".git" ]; then
    echo "This script must be run inside a git repository"
    exit 1
fi 
{
    echo "# Authors"
    echo 
    echo "This project is maintained by the following contributors"
    echo 

    git log --format='%aN <%aE>' | sort -u
} > "$OUTPUT_FILE"

echo "AUTHORS file created."
cat "$OUTPUT_FILE"
